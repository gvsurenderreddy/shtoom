# Copyright (C) 2004 Anthony Baxter

""" A leg """


class Leg(object):

    def __init__(self, ):
        """ Create a new leg
        """
        self.app = None

    def getVoiceApp(self):
        "Get the VoiceApp currently connected to this leg"
        return self.app

    def hijackLeg(self, voiceapp):
        """ Remove the currently running VoiceApp from the leg, and
            slot in a new one. Returns the hijacked app.
        """

    
