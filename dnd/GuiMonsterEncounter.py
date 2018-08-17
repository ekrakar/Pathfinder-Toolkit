from dnd import BackMonsterEncounter
from PyQt5.QtWidgets import QWidget,  QDoubleSpinBox, QPushButton, QGridLayout, QCheckBox, QSpinBox, QLabel, \
    QVBoxLayout, QTextEdit
from PyQt5.QtCore import pyqtSlot


class MonsterEncounter(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.inputLayout = QGridLayout()

        self.output = QTextEdit()

        self.numberEnemiesLabel = QLabel("Enter the Number of enemies in the encounter: ")
        self.consistentCRLabel = QLabel("Will the enemies have the same CR: ")
        self.generalLabel = QLabel("Will the encounter have a General: ")
        self.generalRatioLabel = QLabel("If there is a general what portion of the exp is it (.33-.66): ")
        self.partySizeLabel = QLabel("How many party members: ")
        self.partyLevelLabel = QLabel("What is the average party level: ")
        self.difficultyLabel = QLabel("Enter difficulty (0:easy 1:average 2:challenging 3:hard 4:epic): ")

        self.numberEnemies = QSpinBox()
        self.consistentCR = QCheckBox()
        self.general = QCheckBox()
        self.generalRatio = QDoubleSpinBox()
        self.partySize = QSpinBox()
        self.partyLevel = QSpinBox()
        self.difficulty = QSpinBox()

        self.numberEnemies.setRange(1, 200)
        self.generalRatio.setRange(.33, .66)
        self.generalRatio.setDecimals(2)
        self.partySize.setRange(1, 10)
        self.partyLevel.setRange(1, 25)
        self.difficulty.setRange(0, 4)

        self.pushButton1 = QPushButton("Create Encounter")

        self.inputLayout.addWidget(self.numberEnemiesLabel, 0, 0)
        self.inputLayout.addWidget(self.numberEnemies, 0, 1)
        self.inputLayout.addWidget(self.consistentCRLabel, 1, 0)
        self.inputLayout.addWidget(self.consistentCR, 1, 1)
        self.inputLayout.addWidget(self.generalLabel, 2, 0)
        self.inputLayout.addWidget(self.general, 2, 1)
        self.inputLayout.addWidget(self.generalRatioLabel, 3, 0)
        self.inputLayout.addWidget(self.generalRatio, 3, 1)
        self.inputLayout.addWidget(self.partySizeLabel, 4, 0)
        self.inputLayout.addWidget(self.partySize, 4, 1)
        self.inputLayout.addWidget(self.partyLevelLabel, 5, 0)
        self.inputLayout.addWidget(self.partyLevel, 5, 1)
        self.inputLayout.addWidget(self.difficultyLabel, 6, 0)
        self.inputLayout.addWidget(self.difficulty, 6, 1)

        self.pushButton1.clicked.connect(self.createEncounter_slot)
        self.layout.addLayout(self.inputLayout)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.pushButton1)
        self.setLayout(self.layout)

    @pyqtSlot()
    def createEncounter_slot(self):
        self.output.setPlainText(BackMonsterEncounter.CreateEncounter(enemies=self.numberEnemies.value(),
                                                                      consistant_cr=self.consistentCR.isChecked(),
                                                                      general=self.general.isChecked(),
                                                                      general_ratio=self.generalRatio.value(),
                                                                      party_size=self.partySize.value(),
                                                                      party_level=self.partyLevel.value(),
                                                                      difficulty=self.difficulty.value()))


