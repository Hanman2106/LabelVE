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
        Widget = QWidget()
        layout = QVBoxLayout()
        self.vt = QLineEdit("Anzahl der Vereiler hier eintragen")
        self.button1 = QPushButton("Bestätigen1")
        layout.addWidget(self.vt)
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.click1)
        Widget.setLayout(layout)
        return Widget
        
    def panele(self):
        i = 1
        Widget = QWidget()
        layout = QVBoxLayout()
        self.pan = QLineEdit("Anzahl der Panele für VT%i hier eintragen" %i)
        self.button2 = QPushButton("Bestätigen2")
        layout.addWidget(self.pan)
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.click2)
        Widget.setLayout(layout)
        return Widget
#        while i <= int(self.vt.text()):
#            self.pan = QLineEdit("Anzahl der Panele für VT%i hier eintragen" %i)
#            self.button = QPushButton("Bestätigen")
#            layout = QVBoxLayout()
#            layout.addWidget(self.pan)
#            layout.addWidget(self.button)
#            self.setLayout(layout)
#            self.button.clicked.connect(self.ports)
#            i = i + 1

    def ports(self):
        j = 0
        Widget = QWidget()
        layout = QVBoxLayout()
        self.ports = QLineEdit("24")
        self.dosen = QLineEdit("J")
        self.button3 = QPushButton("Bestätigen3")
        layout.addWidget(self.ports)
        layout.addWidget(self.dosen)
        layout.addWidget(self.button3)
        self.button3.clicked.connect(self.click3)
        Widget.setLayout(layout)
        return Widget
#        while j < self.pan.text():
#            k = 1
#            self.ports = QLineEdit("24")
#            self.dosen = QLineEdit("J")
#            self.button = QPushButton("Bestätigen")
#            layout = QVBoxLayout()
#            layout.addWidget(self.ports)
#            layout.addWidget(self.dosen)
#            layout.addWidget(self.button)
#            self.setLayout(layout)
#            self.button.clicked.connect(self.schleifen)
#            j = j + 1

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
