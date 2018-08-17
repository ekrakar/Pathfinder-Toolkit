from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout


class ExpTable(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Experience Table'
        self.left = 0
        self.top = 30
        self.width = 365
        self.height = 650
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Slow Experience"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Medium Experience"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Fast Experience"))
        self.tableWidget.setVerticalHeaderItem(0, QTableWidgetItem("1st"))
        self.tableWidget.setVerticalHeaderItem(1, QTableWidgetItem("2nd"))
        self.tableWidget.setVerticalHeaderItem(2, QTableWidgetItem("3rd"))
        for i in range(3, 20):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(str(i + 1) + "th"))

        self.tableWidget.setItem(0, 0, QTableWidgetItem("0"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("0"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("0"))

        self.tableWidget.setItem(1, 0, QTableWidgetItem("3,000"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("2,000"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("1,000"))

        self.tableWidget.setItem(2, 0, QTableWidgetItem("7,500"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("5,000"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("3,300"))

        self.tableWidget.setItem(3, 0, QTableWidgetItem("14,000"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("9,000"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("6,000"))

        self.tableWidget.setItem(4, 0, QTableWidgetItem("23,000"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem("15,000"))
        self.tableWidget.setItem(4, 2, QTableWidgetItem("10,000"))

        self.tableWidget.setItem(5, 0, QTableWidgetItem("35,000"))
        self.tableWidget.setItem(5, 1, QTableWidgetItem("23,000"))
        self.tableWidget.setItem(5, 2, QTableWidgetItem("15,000"))

        self.tableWidget.setItem(6, 0, QTableWidgetItem("53,000"))
        self.tableWidget.setItem(6, 1, QTableWidgetItem("35,000"))
        self.tableWidget.setItem(6, 2, QTableWidgetItem("23,000"))

        self.tableWidget.setItem(7, 0, QTableWidgetItem("77,000"))
        self.tableWidget.setItem(7, 1, QTableWidgetItem("51,000"))
        self.tableWidget.setItem(7, 2, QTableWidgetItem("34,000"))

        self.tableWidget.setItem(8, 0, QTableWidgetItem("115,000"))
        self.tableWidget.setItem(8, 1, QTableWidgetItem("75,000"))
        self.tableWidget.setItem(8, 2, QTableWidgetItem("50,000"))

        self.tableWidget.setItem(9, 0, QTableWidgetItem("160,000"))
        self.tableWidget.setItem(9, 1, QTableWidgetItem("105,000"))
        self.tableWidget.setItem(9, 2, QTableWidgetItem("71,000"))

        self.tableWidget.setItem(10, 0, QTableWidgetItem("235,000"))
        self.tableWidget.setItem(10, 1, QTableWidgetItem("155,000"))
        self.tableWidget.setItem(10, 2, QTableWidgetItem("105,000"))

        self.tableWidget.setItem(11, 0, QTableWidgetItem("330,000"))
        self.tableWidget.setItem(11, 1, QTableWidgetItem("220,000"))
        self.tableWidget.setItem(11, 2, QTableWidgetItem("145,000"))

        self.tableWidget.setItem(12, 0, QTableWidgetItem("475,000"))
        self.tableWidget.setItem(12, 1, QTableWidgetItem("315,000"))
        self.tableWidget.setItem(12, 2, QTableWidgetItem("210,000"))

        self.tableWidget.setItem(13, 0, QTableWidgetItem("665,000"))
        self.tableWidget.setItem(13, 1, QTableWidgetItem("445,000"))
        self.tableWidget.setItem(13, 2, QTableWidgetItem("295,000"))

        self.tableWidget.setItem(14, 0, QTableWidgetItem("955,000"))
        self.tableWidget.setItem(14, 1, QTableWidgetItem("635,000"))
        self.tableWidget.setItem(14, 2, QTableWidgetItem("425,000"))

        self.tableWidget.setItem(15, 0, QTableWidgetItem("1,350,000"))
        self.tableWidget.setItem(15, 1, QTableWidgetItem("890,000"))
        self.tableWidget.setItem(15, 2, QTableWidgetItem("600,000"))

        self.tableWidget.setItem(16, 0, QTableWidgetItem("1,900,000"))
        self.tableWidget.setItem(16, 1, QTableWidgetItem("1,300,000"))
        self.tableWidget.setItem(16, 2, QTableWidgetItem("850,000"))

        self.tableWidget.setItem(17, 0, QTableWidgetItem("2,700,000"))
        self.tableWidget.setItem(17, 1, QTableWidgetItem("1,800,000"))
        self.tableWidget.setItem(17, 2, QTableWidgetItem("1,200,000"))

        self.tableWidget.setItem(18, 0, QTableWidgetItem("3,850,000"))
        self.tableWidget.setItem(18, 1, QTableWidgetItem("2,550,000"))
        self.tableWidget.setItem(18, 2, QTableWidgetItem("1,700,000"))

        self.tableWidget.setItem(19, 0, QTableWidgetItem("5,350,000"))
        self.tableWidget.setItem(19, 1, QTableWidgetItem("3,600,000"))
        self.tableWidget.setItem(19, 2, QTableWidgetItem("2,400,000"))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()
