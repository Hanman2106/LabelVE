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


class Form(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create widgets
        self.SL = QStackedLayout()
        self.SL.addWidget(self.startLayout())
        self.SL.addWidget(self.panele())
        self.SL.addWidget(self.ports())
        self.SL.addWidget(self.schleifen())
        self.SL.setCurrentIndex(0)
        self.MW = QWidget()
        self.MW.setLayout(self.SL)
        self.setCentralWidget(self.MW)
    
    def click1(self):
        self.SL.setCurrentIndex(1)
        
    def click2(self):
        self.SL.setCurrentIndex(2)
        
    def click3(self):
        self.SL.setCurrentIndex(3)
        
    def click4(self):
        self.SL.setCurrentIndex(0)
        
    def startLayout(self):
        global ivt
        Widget = QWidget()
        layout = QVBoxLayout()
        vtLab = QLabel("Anzahl Verteiler:")
        self.vt = QLineEdit("4")
        self.button1 = QPushButton("Bestätigen1")
        layout.addWidget(vtLab)
        layout.addWidget(self.vt)
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.click1)
        ivt = int(self.vt.text())
        Widget.setLayout(layout)
        return Widget
        
    def panele(self):
        global ivt
        global panList
        panList = [0]
        i = 1
        Widget = QWidget()
        layout = QVBoxLayout()
        pan1lab = QLabel("Anzahl Panele für VT%i:" %i)
        self.pan1 = QLineEdit("4")
        self.button2 = QPushButton("Bestätigen2")
        layout.addWidget(pan1lab)
        layout.addWidget(self.pan1)
        panList[0] = int(self.pan1.text())
        while i < ivt:
            i=i+1
            pan2lab = QLabel("Anzahl Panele für VT%i:" %i)
            self.pan2 = QLineEdit("4")
            layout.addWidget(pan2lab)
            layout.addWidget(self.pan2)
            panList.append(int(self.pan2.text()))
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.click2)
        Widget.setLayout(layout)
        return Widget

    def ports(self):
        global ivt
        global panList
        j = 0
        i = 0
        Widget = QWidget()
        layout = QVBoxLayout()
        while i < ivt:
            i=i+1
            while j < panList[j]:
                j =j +1
                portlab = QLabel("Anzahl der Ports für VT%i Panel %i:" % (i, j))
                self.ports = QLineEdit("24")
                dosenlab = QLabel("Handelt es sich bei den Dosen um Doppeldosen (J/n):")
                self.dosen = QLineEdit("J")
                layout.addWidget(portlab)
                layout.addWidget(self.ports)
                layout.addWidget(dosenlab)
                layout.addWidget(self.dosen)
        self.button3 = QPushButton("Bestätigen3")
        layout.addWidget(self.button3)
        self.button3.clicked.connect(self.click3)
        Widget.setLayout(layout)
        return Widget

    def schleifen(self):
        Widget = QWidget()
        layout = QVBoxLayout()
        self.button = QPushButton("Bestätigen4")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.click4)
        Widget.setLayout(layout)
        return Widget
#        while k <= self.ports.text():
#            if self.dosen.text() == 'J':
#                string = '%s%i VT%i %s%i'% (a[j], k, i, a[j], k+1)
#                k = k + 2
#            elif self.dosen.text() == 'n':
#                string = 'VT%i %s%i'% (i, a[j], k)
#                k = k + 1
#            print(string)
#            writer.writerow({'A' : string})

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
