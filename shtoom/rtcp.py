# Copyright (C) 2004 Anthony Baxter

from twisted.internet.protocol import DatagramProtocol
from twisted.python import log

# Placeholder until I get time to integrate old rtcp code into new
# codebase

# got RTCP from ('192.168.41.250', 18867) (72 bytes): 
#    81c90007 261a29fa
#    03cfe121 06000018
#    000018b7 00000000
#    00000000 00000000
#    81ca0007 261a29fa
#    0114302e 302e3040
#    3139322e 3136382e
#    34312e32 35300000
#    81cb0001 261a29fa
#    00000000 00000000

RTCP_PT_SR = 200
RTCP_PT_RR = 201
RTCP_PT_SDES = 202
RTCP_PT_BYE = 203
RTCP_PT_APP = 204
rtcpPTdict = {RTCP_PT_SR: 'SR', RTCP_PT_RR: 'RR', RTCP_PT_SDES:'SDES', RTCP_PT_BYE:'BYE'}
for k,v in rtcpPTdict.items(): 
    rtcpPTdict[v] = k

RTCP_SDES_CNAME = 1
RTCP_SDES_NAME = 2
RTCP_SDES_EMAIL = 3
RTCP_SDES_PHONE = 4
RTCP_SDES_LOC = 5
RTCP_SDES_TOOL = 6
RTCP_SDES_NOTE = 7
RTCP_SDES_PRIV = 8
rtcpSDESdict = {RTCP_SDES_CNAME: 'CNAME', 
                RTCP_SDES_NAME: 'NAME', 
                RTCP_SDES_EMAIL: 'EMAIL', 
                RTCP_SDES_PHONE: 'PHONE', 
                RTCP_SDES_LOC: 'LOC', 
                RTCP_SDES_TOOL: 'TOOL', 
                RTCP_SDES_NOTE: 'NOTE', 
                RTCP_SDES_PRIV: 'PRIV', 
               }
for k,v in rtcpSDESdict.items(): 
    rtcpSDESdict[v] = k



import struct

def hexrepr(bytes):
    out = ''
    bytes = bytes + '\0'* ( 8 - len(bytes)%8 )
    for i in range(0,len(bytes), 8):
        out = out +  "    %02x%02x%02x%02x %02x%02x%02x%02x\n"%tuple(
                                                    [ord(bytes[i+x]) for x in range(8)])
    return out

class RTCPPacket:
    def __init__(self, pt, contents=None):
        self._pt = pt
        self._body = ''
        if contents: 
            self._contents = contents
        else:
            self._contents = None

    def getPT(self):
        return self._pt

    def getContents(self):
        return self._content

    def getCount(self):
        return self._count

    def decode(self, count, body):
        self._count = count
        self._body = body
        getattr(self, 'decode_%s'%self._pt)()

    def encode(self):
        getattr(self, 'encode_%s'%self._pt)()
        raise NotImplementedError

    def decode_SDES(self):
        for i in range(self._count):
            self._contents = []
            print len(self._body)
            ssrc, = struct.unpack('!I', self._body[:4])
            self._contents.append((ssrc,[]))
            self._body = self._body[4:]
            while True:
                type, length = ord(self._body[0]), ord(self._body[1])
                off = length+2
                maybepadlen = 4-((length+2)%4)
                body, maybepad = self._body[2:off], self._body[off:off+maybepadlen]
                self._body = self._body[length+2:]
                self._contents[-1][1].append((rtcpSDESdict[type], body))
                if ord(maybepad[0]) == 0:
                    # end of list. eat the padding.
                    self._body = self._body[maybepadlen:]
                    break

    def decode_BYE(self):
        self._contents = [[],'']
        for i in range(self._count):
            ssrc, = struct.unpack('!I', self._body[:4])
            self._contents[0].append(ssrc)
            self._body = self._body[4:]
        if self._body:
            # A reason!
            length = ord(self._body[0]) 
            reason = self._body[1:length+1]
            self._contents[1] = reason
            self._body = ''

    def decode_SR(self):
        self._contents = []
        ssrc, = struct.unpack('!I', self._body[:4])
        bits = struct.unpack('!IIIII', self._body[4:24])
        names = 'ntpHi', 'ntpLo', 'rtpTS', 'packets', 'octets'
        sender = dict(zip(names, bits))
        sender['ntpTS'] = (sender['ntpHi'] * 2**32) + sender['ntpLo']
        del sender['ntpHi'], sender['ntpLo'] 
        blocks = self._decodeRRSRReportBlocks()
        self._contents = [ssrc,sender,blocks]

    def decode_RR(self):
        ssrc, = struct.unpack('!I', self._body[:4])
        self._body = self._body[4:]
        blocks = self._decodeRRSRReportBlocks()
        self._contents = [ssrc,blocks]

    def _decodeRRSRReportBlocks(self):
        blocks = []
        for i in range(self._count):
            bits = struct.unpack('!IIIIII', self._body[:24])
            names = 'ssrc', 'lost', 'highest', 'jitter', 'lsr', 'dlsr'
            c = dict(zip(names,bits))
            c['fraclost'] = ((c['lost'] & 0xFF000000) >> 24)/256.0
            c['packlost'] = (c['lost'] & 0x00FFFFFF) 
            del c['lost']
            blocks.append(c)
            self._body = self._body[24:]
        return blocks

    def decode_APP(self):
        self._contents = []
        subtype = self._count
        ssrc, = struct.unpack('!I', self._body[:4])
        name = self._body[4:8]
        value = self._body[8:]
        self._contents = [subtype,ssrc,name,value]

    def decode_UNKNOWN(self):
        self._contents = 'UNKNOWN'

    def encode_SDES(self):
        pass

    def encode_BYE(self):
        pass

    def encode_SR(self):
        pass

    def encode_RR(self):
        pass

    def encode_APP(self):
        pass

    def __repr__(self):
        if self._body:
            leftover = ' '+repr(self._body)
        else:
            leftover = ''
        return '<RTCP %s %r %s>'%(self._pt, self._contents, leftover)

class RTCPCompound:
    "A single RTCP packet can contain multiple RTCP items"
    def __init__(self, bytes=None):
        self._rtcp = []
        if bytes:
            self.decode(bytes)

    def addPacket(self, packet):
        self._rtcp.append(packet)

    def decode(self, bytes):
        while bytes:
            count = ord(bytes[0]) & 31
            PT = rtcpPTdict.get(ord(bytes[1]), 'UKNOWN')
            length, = struct.unpack('!H', bytes[2:4])
            offset = 4*(length+1)
            body, bytes = bytes[4:offset], bytes[offset:]
            p = RTCPPacket(PT)
            p.decode(count, body)
            self._rtcp.append(p)

    def __len__(self):
        return len(self._rtcp)

    def __getitem__(self, i):
        return self._rtcp[i]
            

class RTCPProtocol(DatagramProtocol):
    def datagramReceived(self, datagram, addr):
        print "got RTCP from %r (%d bytes): \n%s"%(addr, len(datagram), hexrepr(datagram))
        

    def sendDatagram(self, packet):
        self.transport.write(packet)
