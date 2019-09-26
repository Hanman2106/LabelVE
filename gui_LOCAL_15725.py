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
        layout3.addWidget(self.buttonNext)
        layout3.addWidget(self.buttonStart)
        self.setLayout(layoutV)
        self.buttonNext.clicked.connect(self.nextVT)
        self.buttonStart.clicked.connect(self.endVT)

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
        QApplication.quit()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    app.exec_()
