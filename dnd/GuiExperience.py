from dnd import BackParty, BackExperience
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSpinBox, QLabel, \
    QVBoxLayout, QTextEdit, QLineEdit, QComboBox
from PyQt5.QtCore import pyqtSlot


class GuiExp(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.inputLayout = QGridLayout()
        self.inputLayout.setColumnMinimumWidth(5, 200)

        self.party = BackParty.Party()

        self.output = QTextEdit()

        self.mainLabel = QLabel("Enter the amount of each CR ")
        self.labels = [QLabel("CR 1/8: "), QLabel("CR 1/6: "), QLabel("CR 1/4: "), QLabel("CR 1/3: "),
                       QLabel("CR 1/2: ")]
        for i in range(1, 31):
            self.labels.append(QLabel("CR " + str(i) + ": "))
        self.boxes = []
        for i in range(0, 35):
            self.boxes.append(QSpinBox())
        for i in self.boxes:
            i.setRange(0, 100)

        self.pushButton1 = QPushButton("View Party")
        self.pushButton2 = QPushButton("Add Experience")
        self.pushButton3 = QPushButton("Save All Characters(Includes Not In Party)")
        self.pushButton4 = QPushButton("Load Save")
        self.pushButton5 = QPushButton("Add Average Party Level Worth Of Experience")

        self.pushButton1.clicked.connect(self.viewParty_slot)
        self.pushButton2.clicked.connect(self.addExperience_slot)
        self.pushButton3.clicked.connect(self.saveChars_slot)
        self.pushButton4.clicked.connect(self.loadSave_slot)
        self.pushButton5.clicked.connect(self.grantAPL_slot)
        x = 0
        y = 1
        for i in self.labels:
            self.inputLayout.addWidget(i, y, x)
            x += 1
            if x > 9:
                y += 2
                x = 0
        x = 0
        y = 2
        for i in self.boxes:
            self.inputLayout.addWidget(i, y, x)
            x += 1
            if x > 9:
                y += 2
                x = 0
        self.inputLayout.addWidget(self.mainLabel, 0, 0)

        self.layout.addLayout(self.inputLayout)
        self.buttonLayout = QGridLayout()
        self.buttonLayout.addWidget(self.pushButton1, 0, 0)
        self.buttonLayout.addWidget(self.pushButton2, 0, 1)
        self.buttonLayout.addWidget(self.pushButton3, 1, 1)
        self.buttonLayout.addWidget(self.pushButton4, 1, 0)
        self.buttonLayout.addWidget(self.pushButton5, 2, 0)
        self.layout.addLayout(self.buttonLayout)
        self.layout.addWidget(self.output)

        self.setLayout(self.layout)

    @pyqtSlot()
    def viewParty_slot(self):
        self.output.setPlainText(self.party.printChars())

    @pyqtSlot()
    def addExperience_slot(self):
        CR = []
        for i in self.boxes:
            CR.append(i.value())
        out = BackExperience.calculateExperience(CR, self.party)
        self.party.autoSave()
        self.output.setPlainText("The updated experience has been saved to autosave.\n" + out)

    @pyqtSlot()
    def saveChars_slot(self):
        self.party.saveChars()
        self.output.setPlainText("Characters have been saved.")

    @pyqtSlot()
    def loadSave_slot(self):
        self.party.loadChars()
        self.output.setPlainText("Characters have been loaded from main save.")

    @pyqtSlot()
    def grantAPL_slot(self):
        APL = self.party.getAPL()
        CR = []
        for i in range(0, 35):
            if APL != 0 and APL == i - 4:
                CR.append(1)
            else:
                CR.append(0)
        out = BackExperience.calculateExperience(CR, self.party)
        self.party.autoSave()
        self.output.setPlainText("The updated experience has been saved to autosave.\n" +
                                 "The party's average party level is " + str(APL) + ".\n" + out)
