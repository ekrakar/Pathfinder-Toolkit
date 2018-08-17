from dnd import BackParty, GuiExpTable
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSpinBox, QLabel, \
    QVBoxLayout, QTextEdit, QLineEdit, QComboBox
from PyQt5.QtCore import pyqtSlot


class GuiParty(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.inputLayout = QGridLayout()
        self.inputLayout.setColumnMinimumWidth(5, 200)

        self.party = BackParty.Party()

        self.output = QTextEdit()
        self.charNameLabel = QLabel("Enter The Character's Name: ")
        self.charClassLabel = QLabel("Enter The Character's Class: ")
        self.charRaceLabel = QLabel("Enter The Character's Race: ")
        self.charExpLabel = QLabel("Enter The Character's Current Experience: ")
        self.charExpRateLabel = QLabel("How Fast Will The Character level: ")
        self.deleteCharLabel = QLabel("Pick The Character To Delete: ")
        self.addCharLabel = QLabel("Pick The Character To Add To The Party: ")
        self.viewCharLabel = QLabel("Pick The Character To View: ")
        self.updateCharLabel = QLabel("Pick The Character To Update: ")
        self.removeCharLabel = QLabel("Pick The Character To Remove From The Party: ")

        self.charName = QLineEdit()
        self.charClass = QLineEdit()
        self.charRace = QLineEdit()
        self.charExp = QSpinBox()
        self.charExpRate = QComboBox()
        self.deleteChar = QComboBox()
        self.addChar = QComboBox()
        self.viewChar = QComboBox()
        self.updateChar = QComboBox()
        self.removeChar = QComboBox()

        self.updateComboBoxes()
        self.charExp.setRange(0, 10000000)
        self.charExpRate.addItem("Slow")
        self.charExpRate.addItem("Medium")
        self.charExpRate.addItem("Fast")

        self.pushButton1 = QPushButton("Create a Character")
        self.pushButton2 = QPushButton("Save All Characters(Includes Not In Party)")
        self.pushButton3 = QPushButton("Delete")
        self.pushButton4 = QPushButton("Add")
        self.pushButton5 = QPushButton("Experience Table")
        self.pushButton6 = QPushButton("Remove")
        self.pushButton7 = QPushButton("Update")
        self.pushButton8 = QPushButton("View")
        self.pushButton9 = QPushButton("Load AutoSave")
        self.pushButton10 = QPushButton("Load Save")
        self.pushButton11 = QPushButton("Average party Level")

        self.pushButton1.clicked.connect(self.createChar_slot)
        self.pushButton2.clicked.connect(self.saveChars_slot)
        self.pushButton3.clicked.connect(self.deleteChar_slot)
        self.pushButton4.clicked.connect(self.addChar_slot)
        self.pushButton5.clicked.connect(self.expTable_slot)
        self.pushButton6.clicked.connect(self.removeChar_slot)
        self.pushButton7.clicked.connect(self.updateChar_slot)
        self.pushButton8.clicked.connect(self.viewChar_slot)
        self.pushButton9.clicked.connect(self.loadAutoSave_slot)
        self.pushButton10.clicked.connect(self.loadSave_slot)
        self.pushButton11.clicked.connect(self.APL_slot)

        self.inputLayout.addWidget(self.charNameLabel, 0, 0)
        self.inputLayout.addWidget(self.charName, 0, 1)
        self.inputLayout.addWidget(self.charClassLabel, 0, 2)
        self.inputLayout.addWidget(self.charClass, 0, 3)
        self.inputLayout.addWidget(self.charRaceLabel, 1, 0)
        self.inputLayout.addWidget(self.charRace, 1, 1)
        self.inputLayout.addWidget(self.charExpLabel, 1, 2)
        self.inputLayout.addWidget(self.charExp, 1, 3)
        self.inputLayout.addWidget(self.charExpRateLabel, 2, 0)
        self.inputLayout.addWidget(self.charExpRate, 2, 1)

        self.inputLayout.addWidget(self.deleteCharLabel, 0, 4)
        self.inputLayout.addWidget(self.deleteChar, 0, 5)
        self.inputLayout.addWidget(self.pushButton3, 0, 6)
        self.inputLayout.addWidget(self.addCharLabel, 1, 4)
        self.inputLayout.addWidget(self.addChar, 1, 5)
        self.inputLayout.addWidget(self.pushButton4, 1, 6)
        self.inputLayout.addWidget(self.viewCharLabel, 2, 4)
        self.inputLayout.addWidget(self.viewChar, 2, 5)
        self.inputLayout.addWidget(self.pushButton8, 2, 6)
        self.inputLayout.addWidget(self.updateCharLabel, 3, 4)
        self.inputLayout.addWidget(self.updateChar, 3, 5)
        self.inputLayout.addWidget(self.pushButton7, 3, 6)
        self.inputLayout.addWidget(self.removeCharLabel, 4, 4)
        self.inputLayout.addWidget(self.removeChar, 4, 5)
        self.inputLayout.addWidget(self.pushButton6, 4, 6)

        self.layout.addLayout(self.inputLayout)
        self.layout.addWidget(self.output)

        self.buttonLayout = QGridLayout()
        self.buttonLayout.addWidget(self.pushButton1, 0, 0)
        self.buttonLayout.addWidget(self.pushButton2, 0, 1)
        self.buttonLayout.addWidget(self.pushButton9, 1, 0)
        self.buttonLayout.addWidget(self.pushButton10, 1, 1)
        self.buttonLayout.addWidget(self.pushButton5, 2, 0)
        self.buttonLayout.addWidget(self.pushButton11, 2, 1)
        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

    @pyqtSlot()
    def saveChars_slot(self):
        self.party.saveChars()
        self.output.setPlainText("Characters have been saved.")

    @pyqtSlot()
    def loadAutoSave_slot(self):
        self.party.loadAutoSave()
        self.updateComboBoxes()
        self.output.setPlainText("Characters have been loaded from the autosave.")

    @pyqtSlot()
    def loadSave_slot(self):
        self.party.loadChars()
        self.updateComboBoxes()
        self.output.setPlainText("Characters have been loaded from main save.")

    @pyqtSlot()
    def createChar_slot(self):
        self.party.createChar(charName=self.charName.displayText(), charClass=self.charClass.displayText(),
                              charRace=self.charRace.displayText(), charExp=self.charExp.value(),
                              charExpRate=self.charExpRate.currentText())
        char = self.party.viewChar(self.charName.displayText())
        self.output.setPlainText("The characters have been saved to autosave.\n" + "Character has been created.\n" + char)
        self.updateComboBoxes()
        self.party.autoSave()


    @pyqtSlot()
    def updateChar_slot(self):
        if self.updateChar.currentText() != "":
            self.party.updateChar(charName=self.charName.displayText(), charClass=self.charClass.displayText(),
                                  charRace=self.charRace.displayText(), charExp=self.charExp.value(),
                                  charExpRate=self.charExpRate.currentText(), name=self.updateChar.currentText())
        char = self.party.viewChar(self.charName.displayText())
        self.output.setPlainText("The characters have been saved to autosave.\n" + "Character has been updated.\n" + char)
        self.updateComboBoxes()
        self.party.autoSave()


    @pyqtSlot()
    def deleteChar_slot(self):
        if self.deleteChar.currentText() != "":
            self.party.deleteChar(self.deleteChar.currentText())
        self.output.setPlainText("The characters have been saved to autosave.\n" + self.deleteChar.currentText() + " has been deleted.\n" + self.party.printChars())
        self.updateComboBoxes()
        self.party.autoSave()


    @pyqtSlot()
    def addChar_slot(self):
        if self.addChar.currentText() != "":
            self.party.switchLoad(self.addChar.currentText())
        self.output.setPlainText("The characters have been saved to autosave.\n" + self.addChar.currentText() + " has been added to the party.\n" + self.party.printChars())
        self.updateComboBoxes()
        self.party.autoSave()


    @pyqtSlot()
    def removeChar_slot(self):
        if self.removeChar.currentText() != "":
            self.party.switchLoad(self.removeChar.currentText())
        self.output.setPlainText("The characters have been saved to autosave.\n" + self.removeChar.currentText() + " has been removed from the party.\n" + self.party.printChars())
        self.updateComboBoxes()
        self.party.autoSave()


    @pyqtSlot()
    def viewChar_slot(self):
        if self.viewChar.currentText() != "":
            char = self.party.viewChar(self.viewChar.currentText())
            self.output.setPlainText(char)

    @pyqtSlot()
    def expTable_slot(self):
        self.expTable = GuiExpTable.ExpTable()

    @pyqtSlot()
    def APL_slot(self):
        APL = self.party.getAPL()
        self.output.setPlainText("The party's average party level is " + str(APL) + ".")

    def updateComboBoxes(self):
        allChars, loadedChars, unloadedChars = self.party.getAllChars()

        self.viewChar.clear()
        self.updateChar.clear()
        self.deleteChar.clear()
        self.addChar.clear()
        self.removeChar.clear()

        for i in allChars:
            self.viewChar.addItem(i)
            self.updateChar.addItem(i)
            self.deleteChar.addItem(i)
        for i in unloadedChars:
            self.addChar.addItem(i)
        for i in loadedChars:
            self.removeChar.addItem(i)


