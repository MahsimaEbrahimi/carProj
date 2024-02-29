from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resiltTable(object):
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
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
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
