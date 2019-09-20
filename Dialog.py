import csv
from PyQt5.QtWidgets import *
from datetime import datetime
import string
import sys

ts = datetime.fromtimestamp(datetime.now().timestamp()).isoformat()

gcsv = open('Glabel-CSV-%s.csv' %ts, "w+")
fnames = ['A']
writer = csv.DictWriter(gcsv,fieldnames=fnames)
writer.writeheader

a = string.ascii_uppercase

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__()
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
        layout3.addWidget(self.buttonNext)
        layout3.addWidget(self.buttonStart)
        self.setLayout(layoutV)
#        self.buttonStart.clicked.connect(self.anzpanele)

    def edit_port1(self):
        self.port1.setText("24")
        self.dd1.setChecked(True)

    def edit_port2(self):
        self.port2.setText("24")
        self.dd2.setChecked(True)

    def edit_port3(self):
        self.port3.setText("24")
        self.dd3.setChecked(True)

    def edit_port4(self):
        self.port4.setText("24")
        self.dd4.setChecked(True)

    def edit_port5(self):
        self.port5.setText("24")
        self.dd5.setChecked(True)

    def edit_port6(self):
        self.port6.setText("24")
        self.dd6.setChecked(True)

    def edit_port7(self):
        self.port7.setText("24")
        self.dd7.setChecked(True)

    def edit_port8(self):
        self.port8.setText("24")
        self.dd8.setChecked(True)

    def edit_port9(self):
        self.port9.setText("24")
        self.dd9.setChecked(True)

    def edit_port10(self):
        self.port10.setText("24")
        self.dd10.setChecked(True)

#class Form(QMainWindow):

#    def __init__(self, parent=None):
#        global x
#        super().__init__(parent)
#        # Create widgets
#        self.SL = QStackedLayout()
#        self.SL.addWidget(self.startLayout())
#        self.SL.addWidget(self.panele())
#        self.SL.addWidget(self.ports())
#        self.SL.addWidget(self.schleifen())
#        self.SL.setCurrentIndex(0)
#        self.MW = QWidget()
#        self.MW.setLayout(self.SL)
#        self.setCentralWidget(self.MW)
#    
#    def click1(self):
#        self.SL.removeWidget(self.panele())
#        self.panele().destroy()
#        self.SL.setCurrentIndex(1)
#        
#    def click2(self):
#        self.SL.setCurrentIndex(2)
#        
#    def click3(self):
#        self.SL.setCurrentIndex(3)
#        
#    def click4(self):
#        self.SL.setCurrentIndex(0)
#        
#    def startLayout(self):
#        global ivt
#        Widget = QWidget()
#        layout1 = QVBoxLayout()
#        layout2 = QHBoxLayout()
#        layout1.addLayout(layout2)
#        vtLab = QLabel("Anzahl Verteiler:")
#        self.vt = QLineEdit("4")
#        layout2.addWidget(vtLab)
#        layout2.addWidget(self.vt)
#        self.button1 = QPushButton("Bestätigen1")
#        layout1.addWidget(self.button1)
#        self.button1.clicked.connect(self.click1)
#        ivt = int(self.vt.text())
#        Widget.setLayout(layout1)
#        return Widget
#        
#    def panele(self):
#        global ivt
#        global panList
#        panList = [0]
#        i = 1
#        Widget = QWidget()
#        layout1 = QVBoxLayout()
#        layout2 = QHBoxLayout()
#        layout1.addLayout(layout2)
#        pan1lab = QLabel("Anzahl Panele für VT%i:" %i)
#        self.pan1 = QLineEdit("4")
#        self.button2 = QPushButton("Bestätigen2")
#        layout2.addWidget(pan1lab)
#        layout2.addWidget(self.pan1)
#        panList[0] = int(self.pan1.text())
#        while i < ivt:
#            i=i+1
#            layout = QHBoxLayout()
#            pan2lab = QLabel("Anzahl Panele für VT%i:" %i)
#            self.pan2 = QLineEdit("4")
#            layout.addWidget(pan2lab)
#            layout.addWidget(self.pan2)
#            layout1.addLayout(layout)
#            panList.append(int(self.pan2.text()))
#        layout1.addWidget(self.button2)
#        self.button2.clicked.connect(self.click2)
#        Widget.setLayout(layout1)
#        return Widget

#    def ports(self):
#        global ivt
#        global panList
#        j = 1
#        i = 0
#        Widget = QWidget()
#        layout = QVBoxLayout()
#        while i < ivt:
#            i=i+1
#            portlab = QLabel("Anzahl der Ports für VT%i Panel %i:" % (i, j))
#            self.ports = QLineEdit("24")
#            dosenlab = QLabel("Handelt es sich bei den Dosen um Doppeldosen (J/n):")
#            self.dosen = QLineEdit("J")
#            layout.addWidget(portlab)
#            layout.addWidget(self.ports)
#            layout.addWidget(dosenlab)
#            layout.addWidget(self.dosen)
#            while j < panList[j]-1:
#                portlab = QLabel("Anzahl der Ports für VT%i Panel %i:" % (i+1, j+1))
#                self.ports = QLineEdit("24")
#                dosenlab = QLabel("Handelt es sich bei den Dosen um Doppeldosen (J/n):")
#                self.dosen = QLineEdit("J")
#                layout.addWidget(portlab)
#                layout.addWidget(self.ports)
#                layout.addWidget(dosenlab)
#                layout.addWidget(self.dosen)
#                j =j +1
#            j = 1
#        self.button3 = QPushButton("Bestätigen3")
#        layout.addWidget(self.button3)
#        self.button3.clicked.connect(self.click3)
#        Widget.setLayout(layout)
#        return Widget

#    def schleifen(self):
#        Widget = QWidget()
#        layout = QVBoxLayout()
#        self.button = QPushButton("Bestätigen4")
#        layout.addWidget(self.button)
#        self.button.clicked.connect(self.click4)
#        Widget.setLayout(layout)
#        return Widget
##        while k <= self.ports.text():
##            if self.dosen.text() == 'J':
##                string = '%s%i VT%i %s%i'% (a[j], k, i, a[j], k+1)
##                k = k + 2
##            elif self.dosen.text() == 'n':
##                string = 'VT%i %s%i'% (i, a[j], k)
##                k = k + 1
##            print(string)
##            writer.writerow({'A' : string})

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    app.exec_()
