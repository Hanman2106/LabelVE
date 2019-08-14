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
        super(Form, self).__init__(parent)
        # Create widgets
        self.vt = QLineEdit("Anzahl der Vereiler hier eintragen")
        self.button = QPushButton("Bestätigen")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.vt)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.panele)
	
    def panele(self):
        i = 1
        while i <= int(self.vt.text()):
            self.pan = QLineEdit("Anzahl der Panele für VT%i hier eintragen" %i)
            self.button = QPushButton("Bestätigen")
            layout = QVBoxLayout()
            layout.addWidget(self.pan)
            layout.addWidget(self.button)
            self.setLayout(layout)
            self.button.clicked.connect(self.ports)
            i = i + 1

    def ports(self):
	    j = 0
	    while j < self.pan.text():
		    k = 1
		    self.ports = QLineEdit("24")
		    self.dosen = QLineEdit("J")
		    self.button = QPushButton("Bestätigen")
		    layout = QVBoxLayout()
		    layout.addWidget(self.ports)
		    layout.addWidget(self.dosen)
		    layout.addWidget(self.button)
		    # Set dialog layout
		    self.setLayout(layout)
		    # Add button signal to greetings slot
		    self.button.clicked.connect(self.schleifen)
		    j = j + 1

    def schleifen(self):
        while k <= self.ports.text():
            if self.dosen.text() == 'J':
                string = '%s%i VT%i %s%i'% (a[j], k, i, a[j], k+1)
                k = k + 2
            elif self.dosen.text() == 'n':
                string = 'VT%i %s%i'% (i, a[j], k)
                k = k + 1
            print(string)
            writer.writerow({'A' : string})

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
