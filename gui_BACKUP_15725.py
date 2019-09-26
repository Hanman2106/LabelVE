import csv
from PyQt5.QtWidgets import *
from datetime import datetime
from functools import partial
import string
import sys

ts = datetime.fromtimestamp(datetime.now().timestamp()).isoformat()

gcsv = open('/home/pointlogic/Desktop/Glabel-CSV-%s.csv' %ts, "w+")
fnames = ['A']
writer = csv.DictWriter(gcsv,fieldnames=fnames)
writer.writeheader

a = string.ascii_uppercase

<<<<<<< HEAD
panList = []
portList = []
ddList = []
edList = []
gdList = []
einList = []
class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        global panList
        global portList
        global ddList
        global edList
        global gdList
        global einList
=======
class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__()
>>>>>>> 8b23ca3b6cd77ce011fccbde2c0d2e68398ab6dc
        top = QWidget()
        top.setFixedHeight(50)
        bottom = QWidget()
        bottom.setFixedHeight(50)
        layoutV = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QGridLayout()
        layout3 = QHBoxLayout()
        top.setLayout(layout1)
        bottom.setLayout(layout3)
        layoutV.addWidget(top)
        layoutV.addLayout(layout2)
        layoutV.addWidget(bottom)
        vtLab = QLabel("Verteiler Name:")
        self.vt = QLineEdit("")
        self.vt.setFixedWidth(100)
        layout1.addWidget(vtLab)
        layout1.addWidget(self.vt)
        layout1.addStretch(1)
        panLab = QLabel("Panelname")
        portLab = QLabel("Portanzahl")
        ddLab = QLabel("Doppel- oder")
        edLab = QLabel("Einzeldosen")
        gdLab = QLabel("Gemischt")
        einLab = QLabel("Wenn Gemischt, Einzeldosen eintragen (z.B. 3,6,9...)")
        layout2.addWidget(panLab,0,1)
        layout2.addWidget(portLab,0,2)
        layout2.addWidget(ddLab,0,3)
        layout2.addWidget(edLab,0,4)
        layout2.addWidget(gdLab,0,5)
        layout2.addWidget(einLab,0,6)
<<<<<<< HEAD
        for x in range(9):
            panList.append(QLineEdit(""))
            panList[x].setFixedWidth(50)
            portList.append(QLineEdit(""))
            portList[x].setFixedWidth(25)
            ddList.append(QCheckBox())
            edList.append(QCheckBox())
            gdList.append(QCheckBox())
            einList.append(QLineEdit(""))
            layout2.addWidget(panList[x],x+1,1)
            layout2.addWidget(portList[x],x+1,2)
            layout2.addWidget(ddList[x],x+1,3)
            layout2.addWidget(edList[x],x+1,4)
            layout2.addWidget(gdList[x],x+1,5)
            layout2.addWidget(einList[x],x+1,6)
            panList[x].textEdited.connect(partial(self.edit_port, x))
            ddList[x].stateChanged.connect(partial(self.checkstatedd, x))
            edList[x].stateChanged.connect(partial(self.checkstateed, x))
            gdList[x].stateChanged.connect(partial(self.checkstategd, x))
        self.buttonNext = QPushButton("Nächster Verteiler")
        self.buttonStart = QPushButton("Beenden")
=======
        self.pan1 = QLineEdit("")
        self.pan1.setFixedWidth(50)
        self.port1 = QLineEdit("")
        self.port1.setFixedWidth(25)
        self.dd1 = QCheckBox()
        self.ed1 = QCheckBox()
        self.gd1 = QCheckBox()
        self.ein1 = QLineEdit("")
        layout2.addWidget(self.pan1,1,1)
        layout2.addWidget(self.port1,1,2)
        layout2.addWidget(self.dd1,1,3)
        layout2.addWidget(self.ed1,1,4)
        layout2.addWidget(self.gd1,1,5)
        layout2.addWidget(self.ein1,1,6)
        self.pan1.textEdited.connect(self.edit_port1)
        self.pan2 = QLineEdit("")
        self.pan2.setFixedWidth(50)
        self.port2 = QLineEdit("")
        self.port2.setFixedWidth(25)
        self.dd2 = QCheckBox()
        self.ed2 = QCheckBox()
        self.gd2 = QCheckBox()
        self.ein2 = QLineEdit("")
        layout2.addWidget(self.pan2,2,1)
        layout2.addWidget(self.port2,2,2)
        layout2.addWidget(self.dd2,2,3)
        layout2.addWidget(self.ed2,2,4)
        layout2.addWidget(self.gd2,2,5)
        layout2.addWidget(self.ein2,2,6)
        self.pan2.textEdited.connect(self.edit_port2)
        self.pan3 = QLineEdit("")
        self.pan3.setFixedWidth(50)
        self.port3 = QLineEdit("")
        self.port3.setFixedWidth(25)
        self.dd3 = QCheckBox()
        self.ed3 = QCheckBox()
        self.gd3 = QCheckBox()
        self.ein3 = QLineEdit("")
        layout2.addWidget(self.pan3,3,1)
        layout2.addWidget(self.port3,3,2)
        layout2.addWidget(self.dd3,3,3)
        layout2.addWidget(self.ed3,3,4)
        layout2.addWidget(self.gd3,3,5)
        layout2.addWidget(self.ein3,3,6)
        self.pan3.textEdited.connect(self.edit_port3)
        self.pan4 = QLineEdit("")
        self.pan4.setFixedWidth(50)
        self.port4 = QLineEdit("")
        self.port4.setFixedWidth(25)
        self.dd4 = QCheckBox()
        self.ed4 = QCheckBox()
        self.gd4 = QCheckBox()
        self.ein4 = QLineEdit("")
        layout2.addWidget(self.pan4,4,1)
        layout2.addWidget(self.port4,4,2)
        layout2.addWidget(self.dd4,4,3)
        layout2.addWidget(self.ed4,4,4)
        layout2.addWidget(self.gd4,4,5)
        layout2.addWidget(self.ein4,4,6)
        self.pan4.textEdited.connect(self.edit_port4)
        self.pan5 = QLineEdit("")
        self.pan5.setFixedWidth(50)
        self.port5 = QLineEdit("")
        self.port5.setFixedWidth(25)
        self.dd5 = QCheckBox()
        self.ed5 = QCheckBox()
        self.gd5 = QCheckBox()
        self.ein5 = QLineEdit("")
        layout2.addWidget(self.pan5,5,1)
        layout2.addWidget(self.port5,5,2)
        layout2.addWidget(self.dd5,5,3)
        layout2.addWidget(self.ed5,5,4)
        layout2.addWidget(self.gd5,5,5)
        layout2.addWidget(self.ein5,5,6)
        self.pan5.textEdited.connect(self.edit_port5)
        self.pan6 = QLineEdit("")
        self.pan6.setFixedWidth(50)
        self.port6 = QLineEdit("")
        self.port6.setFixedWidth(25)
        self.dd6 = QCheckBox()
        self.ed6 = QCheckBox()
        self.gd6 = QCheckBox()
        self.ein6 = QLineEdit("")
        layout2.addWidget(self.pan6,6,1)
        layout2.addWidget(self.port6,6,2)
        layout2.addWidget(self.dd6,6,3)
        layout2.addWidget(self.ed6,6,4)
        layout2.addWidget(self.gd6,6,5)
        layout2.addWidget(self.ein6,6,6)
        self.pan6.textEdited.connect(self.edit_port6)
        self.pan7 = QLineEdit("")
        self.pan7.setFixedWidth(50)
        self.port7 = QLineEdit("")
        self.port7.setFixedWidth(25)
        self.dd7 = QCheckBox()
        self.ed7 = QCheckBox()
        self.gd7 = QCheckBox()
        self.ein7 = QLineEdit("")
        layout2.addWidget(self.pan7,7,1)
        layout2.addWidget(self.port7,7,2)
        layout2.addWidget(self.dd7,7,3)
        layout2.addWidget(self.ed7,7,4)
        layout2.addWidget(self.gd7,7,5)
        layout2.addWidget(self.ein7,7,6)
        self.pan7.textEdited.connect(self.edit_port7)
        self.pan8 = QLineEdit("")
        self.pan8.setFixedWidth(50)
        self.port8 = QLineEdit("")
        self.port8.setFixedWidth(25)
        self.dd8 = QCheckBox()
        self.ed8 = QCheckBox()
        self.gd8 = QCheckBox()
        self.ein8 = QLineEdit("")
        layout2.addWidget(self.pan8,8,1)
        layout2.addWidget(self.port8,8,2)
        layout2.addWidget(self.dd8,8,3)
        layout2.addWidget(self.ed8,8,4)
        layout2.addWidget(self.gd8,8,5)
        layout2.addWidget(self.ein8,8,6)
        self.pan8.textEdited.connect(self.edit_port8)
        self.pan9 = QLineEdit("")
        self.pan9.setFixedWidth(50)
        self.port9 = QLineEdit("")
        self.port9.setFixedWidth(25)
        self.dd9 = QCheckBox()
        self.ed9 = QCheckBox()
        self.gd9 = QCheckBox()
        self.ein9 = QLineEdit("")
        layout2.addWidget(self.pan9,9,1)
        layout2.addWidget(self.port9,9,2)
        layout2.addWidget(self.dd9,9,3)
        layout2.addWidget(self.ed9,9,4)
        layout2.addWidget(self.gd9,9,5)
        layout2.addWidget(self.ein9,9,6)
        self.pan9.textEdited.connect(self.edit_port9)
        self.pan10 = QLineEdit("")
        self.pan10.setFixedWidth(50)
        self.port10 = QLineEdit("")
        self.port10.setFixedWidth(25)
        self.dd10 = QCheckBox()
        self.ed10 = QCheckBox()
        self.gd10 = QCheckBox()
        self.ein10 = QLineEdit("")
        layout2.addWidget(self.pan10,10,1)
        layout2.addWidget(self.port10,10,2)
        layout2.addWidget(self.dd10,10,3)
        layout2.addWidget(self.ed10,10,4)
        layout2.addWidget(self.gd10,10,5)
        layout2.addWidget(self.ein10,10,6)
        self.pan10.textEdited.connect(self.edit_port10)
        self.buttonNext = QPushButton("Nächster Verteiler")
        self.buttonStart = QPushButton("Beenden")
        self.dd1.stateChanged.connect(self.checkstatedd1)
        self.dd2.stateChanged.connect(self.checkstatedd2)
        self.dd3.stateChanged.connect(self.checkstatedd3)
        self.dd4.stateChanged.connect(self.checkstatedd4)
        self.dd5.stateChanged.connect(self.checkstatedd5)
        self.dd6.stateChanged.connect(self.checkstatedd6)
        self.dd7.stateChanged.connect(self.checkstatedd7)
        self.dd8.stateChanged.connect(self.checkstatedd8)
        self.dd9.stateChanged.connect(self.checkstatedd9)
        self.dd10.stateChanged.connect(self.checkstatedd10)
        self.ed1.stateChanged.connect(self.checkstateed1)
        self.ed2.stateChanged.connect(self.checkstateed2)
        self.ed3.stateChanged.connect(self.checkstateed3)
        self.ed4.stateChanged.connect(self.checkstateed4)
        self.ed5.stateChanged.connect(self.checkstateed5)
        self.ed6.stateChanged.connect(self.checkstateed6)
        self.ed7.stateChanged.connect(self.checkstateed7)
        self.ed8.stateChanged.connect(self.checkstateed8)
        self.ed9.stateChanged.connect(self.checkstateed9)
        self.ed10.stateChanged.connect(self.checkstateed10)
        self.gd1.stateChanged.connect(self.checkstategd1)
        self.gd2.stateChanged.connect(self.checkstategd2)
        self.gd3.stateChanged.connect(self.checkstategd3)
        self.gd4.stateChanged.connect(self.checkstategd4)
        self.gd5.stateChanged.connect(self.checkstategd5)
        self.gd6.stateChanged.connect(self.checkstategd6)
        self.gd7.stateChanged.connect(self.checkstategd7)
        self.gd8.stateChanged.connect(self.checkstategd8)
        self.gd9.stateChanged.connect(self.checkstategd9)
        self.gd10.stateChanged.connect(self.checkstategd10)
>>>>>>> 8b23ca3b6cd77ce011fccbde2c0d2e68398ab6dc
        layout3.addWidget(self.buttonNext)
        layout3.addWidget(self.buttonStart)
        self.setLayout(layoutV)
        self.buttonNext.clicked.connect(self.nextVT)
        self.buttonStart.clicked.connect(self.endVT)

<<<<<<< HEAD
    def edit_port(self, x):
        print (x)
        global portList
        global ddList
        global edList
        global gdList
        portList[x].setText("24")
        ddList[x].setChecked(True)
        edList[x].setChecked(False)
        gdList[x].setChecked(False)

    def checkstatedd(self, x):
        if ddList[x].isChecked() == True:
            edList[x].setChecked(False)
            gdList[x].setChecked(False)

    def checkstateed(self, x):
        if edList[x].isChecked() == True:
            ddList[x].setChecked(False)
            gdList[x].setChecked(False)

    def checkstategd(self, x):
        if gdList[x].isChecked() == True:
            ddList[x].setChecked(False)
            edList[x].setChecked(False)

    def nextVT(self):
        for x in range(9):
            if panList[0].text() != "":
                k = 1
                if ddList[x].isChecked() == True:
                    while k <= int(portList[x].text()):
                        string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif edList[x].isChecked() == True:
                    while k <= int(portList[x].text()):
                        string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                        k = k + 1
                        print (string)
                        writer.writerow({'A' : string})
                elif gdList[x].isChecked() == True:
                    str = einList[x].text()
                    l = [int(s) for s in str.split(",")]
                    while k < l[0]:
                        string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = 0
                    z = len(l)
                    while i < z-1:
                        while k < l[i+1]:
                            string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                            k = k + 2
                            print (string)
                            writer.writerow({'A' : string})
                        string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                        k = k + 1
                        print (string)
                        writer.writerow({'A' : string})
                        i = i + 1
                    if l[i] < int(portList[x].text()) and (int(portList[x].text())-l[i]) % 2 == 0:
                        while k <= int(portList[x].text()):
                            string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                            k = k + 2
                            print (string)
                            writer.writerow({'A' : string})
                    elif l[i] < int(portList[x].text()) and (int(portList[x].text())-l[i]) % 2 != 0:
                        while k <= int(portList[x].text())-1:
                            string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                            k = k + 2
                            print (string)
                            writer.writerow({'A' : string})
                        string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                        k = k + 1
                        print (string)
                        writer.writerow({'A' : string})
        self.vt.clear()
        for x in range(9):
            panList[x].clear()
            portList[x].clear()
            einList[x].clear()
            ddList[x].setChecked(False)
            edList[x].setChecked(False)
            gdList[x].setChecked(False)

    def endVT(self):
        for x in range(9):
            if panList[0].text() != "":
                k = 1
                if ddList[x].isChecked() == True:
                    while k <= int(portList[x].text()):
                        string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif edList[x].isChecked() == True:
                    while k <= int(portList[x].text()):
                        string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                        k = k + 1
                        print (string)
                        writer.writerow({'A' : string})
                elif gdList[x].isChecked() == True:
                    str = einList[x].text()
                    l = [int(s) for s in str.split(",")]
                    while k < l[0]:
                        string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = 0
                    z = len(l)
                    while i < z-1:
                        while k < l[i+1]:
                            string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                            k = k + 2
                            print (string)
                            writer.writerow({'A' : string})
                        string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                        k = k + 1
                        print (string)
                        writer.writerow({'A' : string})
                        i = i + 1
                    if l[i] < int(portList[x].text()) and (int(portList[x].text())-l[i]) % 2 == 0:
                        while k <= int(portList[x].text()):
                            string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                            k = k + 2
                            print (string)
                            writer.writerow({'A' : string})
                    elif l[i] < int(portList[x].text()) and (int(portList[x].text())-l[i]) % 2 != 0:
                        while k <= int(portList[x].text())-1:
                            string = '%s%i %s %s%i'% (panList[x].text(), k, self.vt.text(), panList[x].text(), k+1)
                            k = k + 2
                            print (string)
                            writer.writerow({'A' : string})
                        string = '%s %s%i'% (self.vt.text(), panList[x].text(), k)
                        k = k + 1
                        print (string)
                        writer.writerow({'A' : string})
        gcsv.close()
=======
    def edit_port1(self):
        self.port1.setText("24")
        self.dd1.setChecked(True)
        self.ed1.setChecked(False)
        self.gd1.setChecked(False)

    def edit_port2(self):
        self.port2.setText("24")
        self.dd2.setChecked(True)
        self.ed2.setChecked(False)
        self.gd2.setChecked(False)

    def edit_port3(self):
        self.port3.setText("24")
        self.dd3.setChecked(True)
        self.ed3.setChecked(False)
        self.gd3.setChecked(False)

    def edit_port4(self):
        self.port4.setText("24")
        self.dd4.setChecked(True)
        self.ed4.setChecked(False)
        self.gd4.setChecked(False)

    def edit_port5(self):
        self.port5.setText("24")
        self.dd5.setChecked(True)
        self.ed5.setChecked(False)
        self.gd5.setChecked(False)

    def edit_port6(self):
        self.port6.setText("24")
        self.dd6.setChecked(True)
        self.ed6.setChecked(False)
        self.gd6.setChecked(False)

    def edit_port7(self):
        self.port7.setText("24")
        self.dd7.setChecked(True)
        self.ed7.setChecked(False)
        self.gd7.setChecked(False)

    def edit_port8(self):
        self.port8.setText("24")
        self.dd8.setChecked(True)
        self.ed8.setChecked(False)
        self.gd8.setChecked(False)

    def edit_port9(self):
        self.port9.setText("24")
        self.dd9.setChecked(True)
        self.ed9.setChecked(False)
        self.gd9.setChecked(False)

    def edit_port10(self):
        self.port10.setText("24")
        self.dd10.setChecked(True)
        self.ed10.setChecked(False)
        self.gd10.setChecked(False)

    def checkstatedd1(self):
        if self.dd1.isChecked() == True:
            self.ed1.setChecked(False)
            self.gd1.setChecked(False)

    def checkstateed1(self):
        if self.ed1.isChecked() == True:
            self.dd1.setChecked(False)
            self.gd1.setChecked(False)

    def checkstategd1(self):
        if self.gd1.isChecked() == True:
            self.dd1.setChecked(False)
            self.ed1.setChecked(False)

    def checkstatedd2(self):
        if self.dd2.isChecked() == True:
            self.ed2.setChecked(False)
            self.gd2.setChecked(False)

    def checkstateed2(self):
        if self.ed2.isChecked() == True:
            self.dd2.setChecked(False)
            self.gd2.setChecked(False)

    def checkstategd2(self):
        if self.gd2.isChecked() == True:
            self.dd2.setChecked(False)
            self.ed2.setChecked(False)

    def checkstatedd3(self):
        if self.dd3.isChecked() == True:
            self.ed3.setChecked(False)
            self.gd3.setChecked(False)

    def checkstateed3(self):
        if self.ed3.isChecked() == True:
            self.dd3.setChecked(False)
            self.gd3.setChecked(False)

    def checkstategd3(self):
        if self.gd3.isChecked() == True:
            self.dd3.setChecked(False)
            self.ed3.setChecked(False)

    def checkstatedd4(self):
        if self.dd4.isChecked() == True:
            self.ed4.setChecked(False)
            self.gd4.setChecked(False)

    def checkstateed4(self):
        if self.ed4.isChecked() == True:
            self.dd4.setChecked(False)
            self.gd4.setChecked(False)

    def checkstategd4(self):
        if self.gd4.isChecked() == True:
            self.dd4.setChecked(False)
            self.ed4.setChecked(False)

    def checkstatedd5(self):
        if self.dd5.isChecked() == True:
            self.ed5.setChecked(False)
            self.gd5.setChecked(False)

    def checkstateed5(self):
        if self.ed5.isChecked() == True:
            self.dd5.setChecked(False)
            self.gd5.setChecked(False)

    def checkstategd5(self):
        if self.gd5.isChecked() == True:
            self.dd5.setChecked(False)
            self.ed5.setChecked(False)

    def checkstatedd6(self):
        if self.dd6.isChecked() == True:
            self.ed6.setChecked(False)
            self.gd6.setChecked(False)

    def checkstateed6(self):
        if self.ed6.isChecked() == True:
            self.dd6.setChecked(False)
            self.gd6.setChecked(False)

    def checkstategd6(self):
        if self.gd6.isChecked() == True:
            self.dd6.setChecked(False)
            self.ed6.setChecked(False)

    def checkstatedd7(self):
        if self.dd7.isChecked() == True:
            self.ed7.setChecked(False)
            self.gd7.setChecked(False)

    def checkstateed7(self):
        if self.ed7.isChecked() == True:
            self.dd7.setChecked(False)
            self.gd7.setChecked(False)

    def checkstategd7(self):
        if self.gd7.isChecked() == True:
            self.dd7.setChecked(False)
            self.ed7.setChecked(False)

    def checkstatedd8(self):
        if self.dd8.isChecked() == True:
            self.ed8.setChecked(False)
            self.gd8.setChecked(False)

    def checkstateed8(self):
        if self.ed8.isChecked() == True:
            self.dd8.setChecked(False)
            self.gd8.setChecked(False)

    def checkstategd8(self):
        if self.gd8.isChecked() == True:
            self.dd8.setChecked(False)
            self.ed8.setChecked(False)

    def checkstatedd9(self):
        if self.dd9.isChecked() == True:
            self.ed9.setChecked(False)
            self.gd9.setChecked(False)

    def checkstateed9(self):
        if self.ed9.isChecked() == True:
            self.dd9.setChecked(False)
            self.gd9.setChecked(False)

    def checkstategd9(self):
        if self.gd9.isChecked() == True:
            self.dd9.setChecked(False)
            self.ed9.setChecked(False)

    def checkstatedd10(self):
        if self.dd10.isChecked() == True:
            self.ed10.setChecked(False)
            self.gd10.setChecked(False)

    def checkstateed10(self):
        if self.ed10.isChecked() == True:
            self.dd10.setChecked(False)
            self.gd10.setChecked(False)

    def checkstategd10(self):
        if self.gd10.isChecked() == True:
            self.dd10.setChecked(False)
            self.ed10.setChecked(False)

    def nextVT(self):
        if self.pan1.text() != "":
            k = 1
            if self.dd1.isChecked() == True:
                while k <= int(self.port1.text()):
                    string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed1.isChecked() == True:
                while k <= int(self.port1.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd1.isChecked() == True:
                str = self.ein1.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port1.text()) and (int(self.port1.text())-l[i]) % 2 == 0:
                    while k <= int(self.port1.text()):
                        string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port1.text()) and (int(self.port1.text())-l[i]) % 2 != 0:
                    while k <= int(self.port1.text())-1:
                        string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan2.text() != "":
            k = 1
            if self.dd2.isChecked() == True:
                while k <= int(self.port2.text()):
                    string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed2.isChecked() == True:
                while k <= int(self.port2.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd2.isChecked() == True:
                str = self.ein2.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port2.text()) and (int(self.port2.text())-l[i]) % 2 == 0:
                    while k <= int(self.port2.text()):
                        string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port2.text()) and (int(self.port2.text())-l[i]) % 2 != 0:
                    while k <= int(self.port2.text())-1:
                        string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan3.text() != "":
            k = 1
            if self.dd3.isChecked() == True:
                while k <= int(self.port3.text()):
                    string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed3.isChecked() == True:
                while k <= int(self.port3.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd3.isChecked() == True:
                str = self.ein3.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port3.text()) and (int(self.port3.text())-l[i]) % 2 == 0:
                    while k <= int(self.port3.text()):
                        string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port3.text()) and (int(self.port3.text())-l[i]) % 2 != 0:
                    while k <= int(self.port3.text())-1:
                        string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan4.text() != "":
            k = 1
            if self.dd4.isChecked() == True:
                while k <= int(self.port4.text()):
                    string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed4.isChecked() == True:
                while k <= int(self.port4.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd4.isChecked() == True:
                str = self.ein4.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port4.text()) and (int(self.port4.text())-l[i]) % 2 == 0:
                    while k <= int(self.port4.text()):
                        string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port4.text()) and (int(self.port4.text())-l[i]) % 2 != 0:
                    while k <= int(self.port4.text())-1:
                        string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan5.text() != "":
            k = 1
            if self.dd5.isChecked() == True:
                while k <= int(self.port5.text()):
                    string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed5.isChecked() == True:
                while k <= int(self.port5.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd5.isChecked() == True:
                str = self.ein5.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port5.text()) and (int(self.port5.text())-l[i]) % 2 == 0:
                    while k <= int(self.port5.text()):
                        string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port5.text()) and (int(self.port5.text())-l[i]) % 2 != 0:
                    while k <= int(self.port5.text())-1:
                        string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan6.text() != "":
            k = 1
            if self.dd6.isChecked() == True:
                while k <= int(self.port6.text()):
                    string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed6.isChecked() == True:
                while k <= int(self.port6.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd6.isChecked() == True:
                str = self.ein6.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port6.text()) and (int(self.port6.text())-l[i]) % 2 == 0:
                    while k <= int(self.port6.text()):
                        string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port6.text()) and (int(self.port6.text())-l[i]) % 2 != 0:
                    while k <= int(self.port6.text())-1:
                        string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan7.text() != "":
            k = 1
            if self.dd7.isChecked() == True:
                while k <= int(self.port7.text()):
                    string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed7.isChecked() == True:
                while k <= int(self.port7.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd7.isChecked() == True:
                str = self.ein7.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port7.text()) and (int(self.port7.text())-l[i]) % 2 == 0:
                    while k <= int(self.port7.text()):
                        string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port7.text()) and (int(self.port7.text())-l[i]) % 2 != 0:
                    while k <= int(self.port7.text())-1:
                        string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan8.text() != "":
            k = 1
            if self.dd8.isChecked() == True:
                while k <= int(self.port8.text()):
                    string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed8.isChecked() == True:
                while k <= int(self.port8.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd8.isChecked() == True:
                str = self.ein8.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port8.text()) and (int(self.port8.text())-l[i]) % 2 == 0:
                    while k <= int(self.port8.text()):
                        string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port8.text()) and (int(self.port8.text())-l[i]) % 2 != 0:
                    while k <= int(self.port8.text())-1:
                        string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan9.text() != "":
            k = 1
            if self.dd9.isChecked() == True:
                while k <= int(self.port9.text()):
                    string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed9.isChecked() == True:
                while k <= int(self.port9.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd9.isChecked() == True:
                str = self.ein9.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port9.text()) and (int(self.port9.text())-l[i]) % 2 == 0:
                    while k <= int(self.port9.text()):
                        string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port9.text()) and (int(self.port9.text())-l[i]) % 2 != 0:
                    while k <= int(self.port9.text())-1:
                        string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan10.text() != "":
            k = 1
            if self.dd10.isChecked() == True:
                while k <= int(self.port10.text()):
                    string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed10.isChecked() == True:
                while k <= int(self.port10.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd10.isChecked() == True:
                str = self.ein10.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port10.text()) and (int(self.port10.text())-l[i]) % 2 == 0:
                    while k <= int(self.port10.text()):
                        string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port10.text()) and (int(self.port10.text())-l[i]) % 2 != 0:
                    while k <= int(self.port10.text())-1:
                        string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        self.vt.clear()
        self.pan1.clear()
        self.port1.clear()
        self.ein1.clear()
        self.dd1.setChecked(False)
        self.ed1.setChecked(False)
        self.gd1.setChecked(False)
        self.pan2.clear()
        self.port2.clear()
        self.ein2.clear()
        self.dd2.setChecked(False)
        self.ed2.setChecked(False)
        self.gd2.setChecked(False)
        self.pan3.clear()
        self.port3.clear()
        self.ein3.clear()
        self.dd3.setChecked(False)
        self.ed3.setChecked(False)
        self.gd3.setChecked(False)
        self.pan4.clear()
        self.port4.clear()
        self.ein4.clear()
        self.dd4.setChecked(False)
        self.ed4.setChecked(False)
        self.gd4.setChecked(False)
        self.pan5.clear()
        self.port5.clear()
        self.ein5.clear()
        self.dd5.setChecked(False)
        self.ed5.setChecked(False)
        self.gd5.setChecked(False)
        self.pan6.clear()
        self.port6.clear()
        self.ein6.clear()
        self.dd6.setChecked(False)
        self.ed6.setChecked(False)
        self.gd6.setChecked(False)
        self.pan7.clear()
        self.port7.clear()
        self.ein7.clear()
        self.dd7.setChecked(False)
        self.ed7.setChecked(False)
        self.gd7.setChecked(False)
        self.pan8.clear()
        self.port8.clear()
        self.ein8.clear()
        self.dd8.setChecked(False)
        self.ed8.setChecked(False)
        self.gd8.setChecked(False)
        self.pan9.clear()
        self.port9.clear()
        self.ein9.clear()
        self.dd9.setChecked(False)
        self.ed9.setChecked(False)
        self.gd9.setChecked(False)
        self.pan10.clear()
        self.port10.clear()
        self.ein10.clear()
        self.dd10.setChecked(False)
        self.ed10.setChecked(False)
        self.gd10.setChecked(False)

    def endVT(self):
        if self.pan1.text() != "":
            k = 1
            if self.dd1.isChecked() == True:
                while k <= int(self.port1.text()):
                    string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed1.isChecked() == True:
                while k <= int(self.port1.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd1.isChecked() == True:
                str = self.ein1.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port1.text()) and (int(self.port1.text())-l[i]) % 2 == 0:
                    while k <= int(self.port1.text()):
                        string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port1.text()) and (int(self.port1.text())-l[i]) % 2 != 0:
                    while k <= int(self.port1.text())-1:
                        string = '%s%i %s %s%i'% (self.pan1.text(), k, self.vt.text(), self.pan1.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan1.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan2.text() != "":
            k = 1
            if self.dd2.isChecked() == True:
                while k <= int(self.port2.text()):
                    string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed2.isChecked() == True:
                while k <= int(self.port2.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd2.isChecked() == True:
                str = self.ein2.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port2.text()) and (int(self.port2.text())-l[i]) % 2 == 0:
                    while k <= int(self.port2.text()):
                        string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port2.text()) and (int(self.port2.text())-l[i]) % 2 != 0:
                    while k <= int(self.port2.text())-1:
                        string = '%s%i %s %s%i'% (self.pan2.text(), k, self.vt.text(), self.pan2.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan2.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan3.text() != "":
            k = 1
            if self.dd3.isChecked() == True:
                while k <= int(self.port3.text()):
                    string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed3.isChecked() == True:
                while k <= int(self.port3.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd3.isChecked() == True:
                str = self.ein3.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port3.text()) and (int(self.port3.text())-l[i]) % 2 == 0:
                    while k <= int(self.port3.text()):
                        string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port3.text()) and (int(self.port3.text())-l[i]) % 2 != 0:
                    while k <= int(self.port3.text())-1:
                        string = '%s%i %s %s%i'% (self.pan3.text(), k, self.vt.text(), self.pan3.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan3.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan4.text() != "":
            k = 1
            if self.dd4.isChecked() == True:
                while k <= int(self.port4.text()):
                    string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed4.isChecked() == True:
                while k <= int(self.port4.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd4.isChecked() == True:
                str = self.ein4.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port4.text()) and (int(self.port4.text())-l[i]) % 2 == 0:
                    while k <= int(self.port4.text()):
                        string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port4.text()) and (int(self.port4.text())-l[i]) % 2 != 0:
                    while k <= int(self.port4.text())-1:
                        string = '%s%i %s %s%i'% (self.pan4.text(), k, self.vt.text(), self.pan4.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan4.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan5.text() != "":
            k = 1
            if self.dd5.isChecked() == True:
                while k <= int(self.port5.text()):
                    string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed5.isChecked() == True:
                while k <= int(self.port5.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd5.isChecked() == True:
                str = self.ein5.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port5.text()) and (int(self.port5.text())-l[i]) % 2 == 0:
                    while k <= int(self.port5.text()):
                        string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port5.text()) and (int(self.port5.text())-l[i]) % 2 != 0:
                    while k <= int(self.port5.text())-1:
                        string = '%s%i %s %s%i'% (self.pan5.text(), k, self.vt.text(), self.pan5.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan5.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan6.text() != "":
            k = 1
            if self.dd6.isChecked() == True:
                while k <= int(self.port6.text()):
                    string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed6.isChecked() == True:
                while k <= int(self.port6.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd6.isChecked() == True:
                str = self.ein6.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port6.text()) and (int(self.port6.text())-l[i]) % 2 == 0:
                    while k <= int(self.port6.text()):
                        string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port6.text()) and (int(self.port6.text())-l[i]) % 2 != 0:
                    while k <= int(self.port6.text())-1:
                        string = '%s%i %s %s%i'% (self.pan6.text(), k, self.vt.text(), self.pan6.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan6.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan7.text() != "":
            k = 1
            if self.dd7.isChecked() == True:
                while k <= int(self.port7.text()):
                    string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed7.isChecked() == True:
                while k <= int(self.port7.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd7.isChecked() == True:
                str = self.ein7.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port7.text()) and (int(self.port7.text())-l[i]) % 2 == 0:
                    while k <= int(self.port7.text()):
                        string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port7.text()) and (int(self.port7.text())-l[i]) % 2 != 0:
                    while k <= int(self.port7.text())-1:
                        string = '%s%i %s %s%i'% (self.pan7.text(), k, self.vt.text(), self.pan7.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan7.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan8.text() != "":
            k = 1
            if self.dd8.isChecked() == True:
                while k <= int(self.port8.text()):
                    string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed8.isChecked() == True:
                while k <= int(self.port8.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd8.isChecked() == True:
                str = self.ein8.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port8.text()) and (int(self.port8.text())-l[i]) % 2 == 0:
                    while k <= int(self.port8.text()):
                        string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port8.text()) and (int(self.port8.text())-l[i]) % 2 != 0:
                    while k <= int(self.port8.text())-1:
                        string = '%s%i %s %s%i'% (self.pan8.text(), k, self.vt.text(), self.pan8.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan8.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan9.text() != "":
            k = 1
            if self.dd9.isChecked() == True:
                while k <= int(self.port9.text()):
                    string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed9.isChecked() == True:
                while k <= int(self.port9.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd9.isChecked() == True:
                str = self.ein9.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port9.text()) and (int(self.port9.text())-l[i]) % 2 == 0:
                    while k <= int(self.port9.text()):
                        string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port9.text()) and (int(self.port9.text())-l[i]) % 2 != 0:
                    while k <= int(self.port9.text())-1:
                        string = '%s%i %s %s%i'% (self.pan9.text(), k, self.vt.text(), self.pan9.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan9.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
        if self.pan10.text() != "":
            k = 1
            if self.dd10.isChecked() == True:
                while k <= int(self.port10.text()):
                    string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
            elif self.ed10.isChecked() == True:
                while k <= int(self.port10.text()):
                    string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
            elif self.gd10.isChecked() == True:
                str = self.ein10.text()
                l = [int(s) for s in str.split(",")]
                while k < l[0]:
                    string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                    k = k + 2
                    print (string)
                    writer.writerow({'A' : string})
                string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                k = k + 1
                print (string)
                writer.writerow({'A' : string})
                i = 0
                z = len(l)
                while i < z-1:
                    while k < l[i+1]:
                        string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
                    i = i + 1
                if l[i] < int(self.port10.text()) and (int(self.port10.text())-l[i]) % 2 == 0:
                    while k <= int(self.port10.text()):
                        string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                elif l[i] < int(self.port10.text()) and (int(self.port10.text())-l[i]) % 2 != 0:
                    while k <= int(self.port10.text())-1:
                        string = '%s%i %s %s%i'% (self.pan10.text(), k, self.vt.text(), self.pan10.text(), k+1)
                        k = k + 2
                        print (string)
                        writer.writerow({'A' : string})
                    string = '%s %s%i'% (self.vt.text(), self.pan10.text(), k)
                    k = k + 1
                    print (string)
                    writer.writerow({'A' : string})
>>>>>>> 8b23ca3b6cd77ce011fccbde2c0d2e68398ab6dc
        QApplication.quit()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    app.exec_()
