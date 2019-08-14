import csv
from PyQt5.QtWidgets import *


import sys

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Label Vorlagen Ersteller")
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Anzahl Verteiler:"), QLineEdit())
        layout.addRow(QLabel("Panele:"), QLineEdit())
        layout.addRow(QLabel("Ports:"), QLineEdit('24'))
        self.formGroupBox.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dialog = Dialog()	
	sys.exit(dialog.exec_())

