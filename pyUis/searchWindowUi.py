from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resiltTable(object):
    def showInfo(self,res):
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(row_number,0, QtWidgets.QTableWidgetItem(str(row_data.ShasiNum)))
            self.tableWidget.setItem(row_number,1, QtWidgets.QTableWidgetItem(str(row_data.CarId)))
            self.tableWidget.setItem(row_number,2, QtWidgets.QTableWidgetItem(str(row_data.nameLastname)))
            self.tableWidget.setItem(row_number,3, QtWidgets.QTableWidgetItem(str(row_data.Date)))
            self.tableWidget.setItem(row_number,4, QtWidgets.QTableWidgetItem(str(row_data.Phone)))
            row_number =+ 1



    def setupUi(self, resiltTable):
        resiltTable.setObjectName("resiltTable")
        resiltTable.resize(971, 898)
        self.centralwidget = QtWidgets.QWidget(resiltTable)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame)
        resiltTable.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(resiltTable)
        self.statusbar.setObjectName("statusbar")
        resiltTable.setStatusBar(self.statusbar)

        self.retranslateUi(resiltTable)
        QtCore.QMetaObject.connectSlotsByName(resiltTable)

    def retranslateUi(self, resiltTable):
        _translate = QtCore.QCoreApplication.translate
        resiltTable.setWindowTitle(_translate("resiltTable", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resiltTable = QtWidgets.QMainWindow()
    ui = Ui_resiltTable()
    ui.setupUi(resiltTable)
    resiltTable.show()
    sys.exit(app.exec_())
