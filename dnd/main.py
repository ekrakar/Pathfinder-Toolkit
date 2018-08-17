import sys
from dnd import GuiMonsterEncounter, GuiParty, GuiExperience
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'D&D Tools'
        self.left = 0
        self.top = 30
        self.width = 1920
        self.height = 1010
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()

        # Add tab1
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Monster Encounter")
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(GuiMonsterEncounter.MonsterEncounter(self))
        self.tab1.setLayout(self.tab1.layout)

        # Add tab2
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Party Manager")
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(GuiParty.GuiParty(self))
        self.tab2.setLayout(self.tab2.layout)

        # Add tab3
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Experience Manager")
        self.tab3.layout = QVBoxLayout(self)
        self.tab3.layout.addWidget(GuiExperience.GuiExp(self))
        self.tab3.setLayout(self.tab3.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
