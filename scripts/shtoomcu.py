#!/usr/bin/env python

# Hack hack hack.
import sys, os
f = sys.path.pop(0)
if f.endswith('scripts') and os.path.isdir(os.path.join(os.path.dirname(f),
                                                        'shtoom')):
    sys.path.insert(0, os.path.dirname(f))
else:
    sys.path.append(f)



from shtoom.doug import VoiceApp
from shtoom.doug.events import *

from shtoom.exceptions import CallRejected

from twisted.python import log
log.FileLogObserver.timeFormat = "%Y/%m/%d %H:%M:%S"

class ConferencingApp(VoiceApp):

    announceFile = 'tmp/conf_welcome.raw'

    def __init__(self, *args, **kwargs):
        self.conf = None
        self.__dict__.update(kwargs)
        if not self.announceFile:
            raise ValueError, "must supply announceFile"        
        super(ConferencingApp, self).__init__(*args, **kwargs)

    def __start__(self):
        print "voiceapp.__start__"
        return ( (CallStartedEvent, self.answerCall),
                 #(Event,            self.unknownEvent), 
               )

    def unknownEvent(self, event):
        print "Got unhandled event %s"%event
        return ()

    def answerCall(self, event):
        self.leg = event.getLeg()

        roomname = self.leg.getDialog().getLocalTag().getURI().username
        print "voiceapp.__start__ to user %s"%(roomname)
        if roomname == 'nope':
            self.leg.rejectCall(CallRejected('go away'))
            del self.leg
        else:
            self.roomname = roomname
            self.leg.answerCall(self)
        return ( (CallAnsweredEvent, self.playAnnounce),
               )

    def playAnnounce(self, event):
        # Begin the call

        # We want to receive the DTMF one keystroke at a time.
        self.dtmfMode(single=True)
        self.mediaPlay(self.announceFile)
        return ( (MediaDoneEvent, self.startConference), 
                 (CallEndedEvent,  self.allDone),
                 (DTMFReceivedEvent,      self.startConference),
                 #(Event,          self.unknownEvent), 
               )

    def startConference(self, event):
        from shtoom.doug.conferencing import newConferenceMember
        self.mediaStop()
        self.conf = newConferenceMember(self.roomname, self.leg)
        self.mediaPlay([self.conf])
        return ( (MediaDoneEvent, self.startConference), 
                 (CallEndedEvent,  self.allDone),
                 (DTMFReceivedEvent,      IGNORE_EVENT),
                 #(Event,          self.unknownEvent), 
               )


    def allDone(self, event):
        self.mediaStop()
        del self.leg, self.conf
        self.mediaStop()
        self.returnResult('other end closed')



from shtoom.doug.service import DougService
global app
srv = DougService(ConferencingApp)
srv.startService()
app = srv.app
#app.boot()
#app.start()


