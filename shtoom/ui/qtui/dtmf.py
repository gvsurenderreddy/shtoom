# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dtmf.ui'
#
# Created: Wed Jan 19 01:12:26 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DTMF(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("DTMF")


        DTMFLayout = QVBoxLayout(self,11,6,"DTMFLayout")

        layout11 = QGridLayout(None,1,1,0,6,"layout11")

        self.dtmfButton8 = QPushButton(self,"dtmfButton8")
        self.dtmfButton8.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton8.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton8,2,1)

        self.dtmfButton2 = QPushButton(self,"dtmfButton2")
        self.dtmfButton2.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton2.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton2,0,1)

        self.dtmfButtonStar = QPushButton(self,"dtmfButtonStar")
        self.dtmfButtonStar.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButtonStar.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButtonStar,3,0)

        self.dtmfButtonHash = QPushButton(self,"dtmfButtonHash")
        self.dtmfButtonHash.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButtonHash.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButtonHash,3,2)

        self.dtmfButton3 = QPushButton(self,"dtmfButton3")
        self.dtmfButton3.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton3.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton3,0,2)

        self.dtmfButton6 = QPushButton(self,"dtmfButton6")
        self.dtmfButton6.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton6.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton6,1,2)

        self.dtmfButton5 = QPushButton(self,"dtmfButton5")
        self.dtmfButton5.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton5.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton5,1,1)

        self.dtmfButton4 = QPushButton(self,"dtmfButton4")
        self.dtmfButton4.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton4.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton4,1,0)

        self.dtmfButton7 = QPushButton(self,"dtmfButton7")
        self.dtmfButton7.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton7.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton7,2,0)

        self.dtmfButton9 = QPushButton(self,"dtmfButton9")
        self.dtmfButton9.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton9.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton9,2,2)

        self.dtmfButton1 = QPushButton(self,"dtmfButton1")
        self.dtmfButton1.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton1.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton1,0,0)

        self.dtmfButton0 = QPushButton(self,"dtmfButton0")
        self.dtmfButton0.setSizePolicy(QSizePolicy(7,7,0,0,self.dtmfButton0.sizePolicy().hasHeightForWidth()))

        layout11.addWidget(self.dtmfButton0,3,1)
        DTMFLayout.addLayout(layout11)

        layout9 = QHBoxLayout(None,0,6,"layout9")
        spacer2 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addItem(spacer2)

        self.dtmfClose = QPushButton(self,"dtmfClose")
        layout9.addWidget(self.dtmfClose)
        spacer3 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addItem(spacer3)
        DTMFLayout.addLayout(layout9)

        self.languageChange()

        self.resize(QSize(177,207).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.dtmfButton1,SIGNAL("released()"),self.dtmfButton1_released)
        self.connect(self.dtmfButton1,SIGNAL("pressed()"),self.dtmfButton1_pressed)
        self.connect(self.dtmfClose,SIGNAL("clicked()"),self.dtmfClose_clicked)
        self.connect(self.dtmfButton2,SIGNAL("released()"),self.dtmfButton2_released)
        self.connect(self.dtmfButton2,SIGNAL("pressed()"),self.dtmfButton2_pressed)
        self.connect(self.dtmfButton3,SIGNAL("released()"),self.dtmfButton3_released)
        self.connect(self.dtmfButton3,SIGNAL("pressed()"),self.dtmfButton3_pressed)
        self.connect(self.dtmfButton4,SIGNAL("released()"),self.dtmfButton4_released)
        self.connect(self.dtmfButton4,SIGNAL("pressed()"),self.dtmfButton4_pressed)
        self.connect(self.dtmfButton5,SIGNAL("released()"),self.dtmfButton5_released)
        self.connect(self.dtmfButton5,SIGNAL("pressed()"),self.dtmfButton5_pressed)
        self.connect(self.dtmfButton6,SIGNAL("released()"),self.dtmfButton6_released)
        self.connect(self.dtmfButton6,SIGNAL("pressed()"),self.dtmfButton6_pressed)
        self.connect(self.dtmfButton7,SIGNAL("released()"),self.dtmfButton7_released)
        self.connect(self.dtmfButton7,SIGNAL("pressed()"),self.dtmfButton7_pressed)
        self.connect(self.dtmfButton8,SIGNAL("released()"),self.dtmfButton8_released)
        self.connect(self.dtmfButton8,SIGNAL("pressed()"),self.dtmfButton8_pressed)
        self.connect(self.dtmfButton9,SIGNAL("released()"),self.dtmfButton9_released)
        self.connect(self.dtmfButton9,SIGNAL("pressed()"),self.dtmfButton9_pressed)
        self.connect(self.dtmfButtonStar,SIGNAL("released()"),self.dtmfButtonStar_released)
        self.connect(self.dtmfButtonStar,SIGNAL("pressed()"),self.dtmfButtonStar_pressed)
        self.connect(self.dtmfButton0,SIGNAL("released()"),self.dtmfButton0_released)
        self.connect(self.dtmfButton0,SIGNAL("pressed()"),self.dtmfButton0_pressed)
        self.connect(self.dtmfButtonHash,SIGNAL("released()"),self.dtmfButtonHash_released)
        self.connect(self.dtmfButtonHash,SIGNAL("pressed()"),self.dtmfButtonHash_pressed)


    def languageChange(self):
        self.setCaption(self.__tr("DTMF"))
        self.dtmfButton8.setText(self.__tr("8"))
        self.dtmfButton2.setText(self.__tr("2"))
        self.dtmfButtonStar.setText(self.__tr("*"))
        self.dtmfButtonHash.setText(self.__tr("#"))
        self.dtmfButton3.setText(self.__tr("3"))
        self.dtmfButton6.setText(self.__tr("6"))
        self.dtmfButton5.setText(self.__tr("5"))
        self.dtmfButton4.setText(self.__tr("4"))
        self.dtmfButton7.setText(self.__tr("7"))
        self.dtmfButton9.setText(self.__tr("9"))
        self.dtmfButton1.setText(self.__tr("1"))
        self.dtmfButton0.setText(self.__tr("0"))
        self.dtmfClose.setText(self.__tr("Close"))


    def pushButton35_released(self):
        print "DTMF.pushButton35_released(): Not implemented yet"

    def pushButton35_pressed(self):
        print "DTMF.pushButton35_pressed(): Not implemented yet"

    def dtmfButton1_released(self):
        print "DTMF.dtmfButton1_released(): Not implemented yet"

    def dtmfButton1_pressed(self):
        print "DTMF.dtmfButton1_pressed(): Not implemented yet"

    def dtmfClose_clicked(self):
        print "DTMF.dtmfClose_clicked(): Not implemented yet"

    def dtmfButton1_2_released(self):
        print "DTMF.dtmfButton1_2_released(): Not implemented yet"

    def dtmfButton1_2_pressed(self):
        print "DTMF.dtmfButton1_2_pressed(): Not implemented yet"

    def dtmfButton2_released(self):
        print "DTMF.dtmfButton2_released(): Not implemented yet"

    def dtmfButton2_pressed(self):
        print "DTMF.dtmfButton2_pressed(): Not implemented yet"

    def dtmfButton3_released(self):
        print "DTMF.dtmfButton3_released(): Not implemented yet"

    def dtmfButton3_pressed(self):
        print "DTMF.dtmfButton3_pressed(): Not implemented yet"

    def dtmfButton4_released(self):
        print "DTMF.dtmfButton4_released(): Not implemented yet"

    def dtmfButton4_pressed(self):
        print "DTMF.dtmfButton4_pressed(): Not implemented yet"

    def dtmfButton5_released(self):
        print "DTMF.dtmfButton5_released(): Not implemented yet"

    def dtmfButton5_pressed(self):
        print "DTMF.dtmfButton5_pressed(): Not implemented yet"

    def dtmfButton6_released(self):
        print "DTMF.dtmfButton6_released(): Not implemented yet"

    def dtmfButton6_pressed(self):
        print "DTMF.dtmfButton6_pressed(): Not implemented yet"

    def dtmfButton7_released(self):
        print "DTMF.dtmfButton7_released(): Not implemented yet"

    def dtmfButton7_pressed(self):
        print "DTMF.dtmfButton7_pressed(): Not implemented yet"

    def dtmfButton8_released(self):
        print "DTMF.dtmfButton8_released(): Not implemented yet"

    def dtmfButton8_pressed(self):
        print "DTMF.dtmfButton8_pressed(): Not implemented yet"

    def dtmfButton9_released(self):
        print "DTMF.dtmfButton9_released(): Not implemented yet"

    def dtmfButton9_pressed(self):
        print "DTMF.dtmfButton9_pressed(): Not implemented yet"

    def dtmfButtonStar_released(self):
        print "DTMF.dtmfButtonStar_released(): Not implemented yet"

    def dtmfButtonStar_pressed(self):
        print "DTMF.dtmfButtonStar_pressed(): Not implemented yet"

    def dtmfButton0_released(self):
        print "DTMF.dtmfButton0_released(): Not implemented yet"

    def dtmfButton0_pressed(self):
        print "DTMF.dtmfButton0_pressed(): Not implemented yet"

    def dtmfButtonHash_released(self):
        print "DTMF.dtmfButtonHash_released(): Not implemented yet"

    def dtmfButtonHash_pressed(self):
        print "DTMF.dtmfButtonHash_pressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DTMF",s,c)
