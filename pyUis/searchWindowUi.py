from PyQt5 import QtCore, QtGui, QtWidgets
from Car import CarClass
from Carinfo import CarinfoClass
from connection_Maker import connectionMaker
from ownerModel import OwnerModelclass
from CarOwnerInterfaceModel import CarOwnerInterfaceModel
class Ui_resiltTable(object):
    def __init__(self) -> None:
        self.CarClassObj=CarClass(connectionMaker.classConnection)
        self.CarInfoClassObj=CarinfoClass(connectionMaker.classConnection)

    def showInfo(self,res):
        self.tableWidget.setRowCount(0)
        row_number=0
        for row_number,row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(row_number,0, QtWidgets.QTableWidgetItem(str(row_data.ShasiNum)))
            self.tableWidget.setItem(row_number,1, QtWidgets.QTableWidgetItem(str(row_data.CarId)))
            self.tableWidget.setItem(row_number,2, QtWidgets.QTableWidgetItem(str(row_data.nameLastname)))
            self.tableWidget.setItem(row_number,3, QtWidgets.QTableWidgetItem(str(row_data.Date)))
            self.tableWidget.setItem(row_number,4, QtWidgets.QTableWidgetItem(str(row_data.Phone)))
            self.tableWidget.setItem(row_number,5, QtWidgets.QTableWidgetItem(str(row_data.Thekey)))
            row_number =+ 1

    def handleRowDoubleClick(self, index):
        print(self.CarClassObj)
        row = index.row()
        # Get information from the clicked row
        row_data = []
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            row_data.append(item.text())
        print(row_data)
        sendToForm_Car=self.CarClassObj.get(row_data[0],row_data[1])
        sendToForm_CarInfo=self.CarInfoClassObj.get(row_data[5])
        sendToForm_Owner=OwnerModelclass(nameLastname=row_data[2],phone=row_data[4])
        sendToForm_ROwner=CarOwnerInterfaceModel(Thekey=row_data[5],CarId=row_data[1],ShasiNum=row_data[0],
                                          nameLastname=row_data[2],Date=row_data[3],Phone=row_data[4])     
        self.Update_form(sendToForm_Car,sendToForm_CarInfo,sendToForm_Owner,sendToForm_ROwner)  
        # print(sendToForm_Car)
        # print(sendToForm_CarInfo)
        row_data.clear()
    
    def Update_form(self,sendToForm_Car,sendToForm_CarInfo,sendToForm_Owner,sendToForm_ROwner):
        from UIMain import Ui_MainWindow,FormMethod,MainWindow
        mainWindow = MainWindow()
        ui = Ui_MainWindow()    
        frmMethod=FormMethod(ui)    
        ui.setupUi(mainWindow,frmMethod)
        ui.ShasiTxt.setText(sendToForm_Car.ShasiNum)
        mainWindow.show()


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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        self.tableWidget.hideColumn(5)
        self.tableWidget.setHorizontalHeaderLabels(['شماره شاسی','شماره پلاک','اسم','تاریخ','تلفن','کلید'])
        self.tableWidget.doubleClicked.connect(self.handleRowDoubleClick)
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
