# Copyright (C) 2004 Anthony Baxter
"""Tests for shtoom.app.
"""

from twisted.trial import unittest

class TestUI:
    pass

class TestAudio:
    pass

class AppStartup(unittest.TestCase):

    def buildPhone(self):
        ui = TestUI()
        audio = TestAudio()
        from shtoom.app.phone import Phone
        return Phone(ui, audio)

    def getMinimalOptions(self):
        from shtoom.Options import AllOptions, OptionGroup, \
                StringOption, NumberOption
        o = AllOptions()
        g = OptionGroup('whatever', 'some settings')
        g.addOption(StringOption('ui', 'whatever', 'tk'))
        g.addOption(StringOption('no_config_file', 'whatever', True))
        g.addOption(NumberOption('listenport', 'port', 5060))
        o.addGroup(g)
        return o

    def test_phoneBootWithOptions(self):
        opts = self.getMinimalOptions()
        ae = self.assertEqual
        p = self.buildPhone()
        p.boot(options=opts)
        p.stopSIP()
        ae(p.getOptions(), opts)
        ae(p.getPref('ui'), 'tk')

    def test_phoneBootOpenSIP(self):
        import random
        opts = self.getMinimalOptions()
        l=random.randint(20000,30000)
        opts.updateOptions(listenport=l)
        ae = self.assertEqual
        ae(opts.getValue('listenport'), l)
        ae = self.assertEqual
        p = self.buildPhone()
        p.boot(options=opts)
        ae(p.sipListener.port, p.getPref('listenport'))
        p.stopSIP()

