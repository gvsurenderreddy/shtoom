# Copyright (C) 2004 Anthony Baxter
if __name__ == "__main__":
    import qt
    from twisted.internet import qtreactor
    app=qt.QApplication([])
    qtreactor.install(app)

from shtoommainwindow import ShtoomMainWindow as ShtoomBaseWindow
from dtmf import DTMF
from debugging import Debugging

from shtoom.ui.base import ShtoomBaseUI

import sys
from twisted.python import log
from qt import *




import sys
from twisted.python import log

class DTMF(DTMF):
    main = None

    def dtmfClose_clicked(self):
        self.hide()

    def dtmfButtonHash_pressed(self):
        self.main.startDTMF('#')

    def dtmfButtonHash_released(self):
        self.main.stopDTMF('#')

    def dtmfButtonStar_pressed(self):
        self.main.startDTMF('*')

    def dtmfButtonStar_released(self):
        self.main.stopDTMF('*')

    def dtmfButton1_pressed(self):
        self.main.startDTMF('1')

    def dtmfButton1_released(self):
        self.main.stopDTMF('1')

    def dtmfButton2_pressed(self):
        self.main.startDTMF('2')

    def dtmfButton2_released(self):
        self.main.stopDTMF('2')

    def dtmfButton3_pressed(self):
        self.main.startDTMF('3')

    def dtmfButton3_released(self):
        self.main.stopDTMF('3')

    def dtmfButton4_pressed(self):
        self.main.startDTMF('4')

    def dtmfButton4_released(self):
        self.main.stopDTMF('4')

    def dtmfButton5_pressed(self):
        self.main.startDTMF('5')

    def dtmfButton5_released(self):
        self.main.stopDTMF('5')

    def dtmfButton6_pressed(self):
        self.main.startDTMF('6')

    def dtmfButton6_released(self):
        self.main.stopDTMF('6')

    def dtmfButton7_pressed(self):
        self.main.startDTMF('7')

    def dtmfButton7_released(self):
        self.main.stopDTMF('7')

    def dtmfButton8_pressed(self):
        self.main.startDTMF('8')

    def dtmfButton8_released(self):
        self.main.stopDTMF('8')

    def dtmfButton9_pressed(self):
        self.main.startDTMF('9')

    def dtmfButton9_released(self):
        self.main.stopDTMF('9')

    def dtmfButton0_pressed(self):
        self.main.startDTMF('0')

    def dtmfButton0_released(self):
        self.main.stopDTMF('0')


class Debugging(Debugging):
    def debuggingCloseButton_clicked(self):
        self.hide()

    def debuggingClearButton_clicked(self):
        self.debuggingTextEdit.clear()

class ShtoomMainWindow(ShtoomBaseWindow, ShtoomBaseUI):

    sending = False
    audiosource = None
    cookie = None
    _muted = False

    def __init__(self, *args, **kwargs):
        from shtoom.ui.logo import logoGif
        self._newCallURL = None
        self.dtmf = DTMF()
        self.dtmf.main = self
        self.debugging = Debugging()
        ShtoomBaseWindow.__init__(self, *args, **kwargs)
        print "init done", self.dtmf, self.debugging

    def debugMessage(self, message):
        print message
        log.msg(message, system='ui')

    def statusMessage(self, message):
        self.statusLabel.setText(message)

    def errorMessage(self, message, exception=None):
        log.msg("ERROR: %s"%message, system='ui')

    def hangupButton_clicked(self):
        self.app.dropCall(self.cookie)
        self.callButton.setEnabled(True)
        self.hangupButton.setEnabled(False)
        self.cookie = None

    def register_clicked(self):
        self.app.register()

    def callButton_clicked(self):
        sipURL = str(self.addressComboBox.currentText()).strip()
        if not sipURL:
            return
        self.addressComboBox.setCurrentText(sipURL)
        self.addressComboBox.insertItem(QString(sipURL))
        self._newCallURL = sipURL
        self.callButton.setEnabled(False)
        defer = self.app.placeCall(sipURL)
        defer.addCallbacks(self.callConnected, self.callFailed).addErrback(log.err)

    def callStarted(self, cookie):
        print "started", cookie
        self.cookie = cookie
        self.hangupButton.setEnabled(True)
        self.statusMessage('Calling...')

    def callFailed(self, e, message=None):
        self.errorMessage("call failed", e.getErrorMessage())
        self.hangupButton.setEnabled(False)
        self.callButton.setEnabled(True)
        self.cookie = None

    def callConnected(self, cookie):
        self.hangupButton.setEnabled(True)
        self.statusMessage('Call Connected')
        if self._muted:
            self.app.muteCall(self.cookie)

    def callDisconnected(self, cookie, message):
        self.statusMessage('Call disconnected: %s'%message)
        self.hangupButton.setEnabled(False)
        self.callButton.setEnabled(True)
        self.cookie = None

    def getLogger(self):
        l = Logger(self.debugging.debuggingTextEdit)
        return l

    def editPreferences(self):
        from prefs import PreferencesDialog
        self.prefs =PreferencesDialog(self, self.app.getOptions())
        self.prefs.show()

    def preferences_save(self, options):
        print "save prefs", options
        self.app.updateOptions(options)
        self.prefs.hide()

    def preferences_discard(self):
        self.prefs.hide()

    def incomingCall(self, description, cookie):
        # XXX not good. Blockage. Argh.
        from twisted.internet import defer
        from shtoom.exceptions import CallRejected
        accept = QMessageBox.information(self, 'Shtoom',
                'Incoming Call: %s\nAnswer?'%description,
                'Yes', 'No', '', 0, 1)
        print "accept is", accept
        if accept == 0:
            self.cookie = cookie
            self.callButton.setEnabled(False)
            self.addressComboBox.setEnabled(False)
            return defer.succeed(cookie)
        else:
            return defer.fail(CallRejected(cookie))

    def muteCheck_stateChanged(self,val):
        if val:
            self._muted = True
        else:
            self._muted = False
        if self.cookie is not None:
            if val:
                self.app.muteCall(self.cookie)
            else:
                self.app.unmuteCall(self.cookie)

    def startDTMF(self, key):
        if self.cookie:
            self.app.startDTMF(self.cookie, key)

    def stopDTMF(self, key):
        if self.cookie:
            self.app.stopDTMF(self.cookie, key)

    def fileDTMF(self, *args):
        self.dtmf.show()

    def fileDebugging(self, *args):
        self.debugging.show()

class Logger:
    def __init__(self, textwidget):
        self._t = textwidget
    def flush(self):
        pass
    def write(self, text):
        self._t.append(text)

if __name__ == "__main__":
    from twisted.internet import reactor
    UI = ShtoomMainWindow()
    UI.show()
    reactor.run()
