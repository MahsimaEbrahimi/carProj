from PyQt5 import QtCore, QtGui, QtWidgets
from SearchMethods import RecoveryMethodsClass
from searchWindowUi import Ui_resiltTable 
from messagebox import _win32

class Ui_RecoveryWindow(object):
    
    def OpenResWindow(self,searchMethodsClassINSTANCE):
         res=searchMethodsClassINSTANCE.SearchResult()
         if res==False:
                _win32.showerror(title="خطا",message="اطلاعاتی برای ماشین مورد نظر شما وجود ندارد")
         else:
        #  searchMethodsClassINSTANCE=RecoveryMethodsClass(ui)
                self.Window=QtWidgets.QMainWindow()
                self.Resultwindow=Ui_resiltTable()
                self.Resultwindow.setupUi(self.Window)
                self.Resultwindow.showInfo(res)
                self.Window.show()
       

    def setupUi(self, RecoveryWindow,searchMethodsClassINSTANCE):
        RecoveryWindow.setObjectName("RecoveryWindow")
        RecoveryWindow.resize(709, 345)
        font = QtGui.QFont()
        font.setPointSize(12)
        RecoveryWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(RecoveryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.RecoveryFrame = QtWidgets.QFrame(self.centralwidget)
        self.RecoveryFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RecoveryFrame.setFont(font)
        self.RecoveryFrame.setStyleSheet("")
        self.RecoveryFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RecoveryFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RecoveryFrame.setObjectName("RecoveryFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.RecoveryFrame)
        self.gridLayout.setContentsMargins(-1, 11, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.RecoveryFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.RecoveryFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.CarOwnerTxt = QtWidgets.QTextEdit(self.RecoveryFrame)
        self.CarOwnerTxt.setMinimumSize(QtCore.QSize(0, 20))
        self.CarOwnerTxt.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.CarOwnerTxt.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CarOwnerTxt.setFont(font)
        self.CarOwnerTxt.setObjectName("CarOwnerTxt")
        self.gridLayout.addWidget(self.CarOwnerTxt, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.RecoveryFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.CarIdTxt = QtWidgets.QTextEdit(self.RecoveryFrame)
        self.CarIdTxt.setMinimumSize(QtCore.QSize(0, 20))
        self.CarIdTxt.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.CarIdTxt.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CarIdTxt.setFont(font)
        self.CarIdTxt.setObjectName("CarIdTxt")
        self.gridLayout.addWidget(self.CarIdTxt, 1, 0, 1, 1)
        self.ShasiTxt = QtWidgets.QTextEdit(self.RecoveryFrame)
        self.ShasiTxt.setMinimumSize(QtCore.QSize(0, 20))
        self.ShasiTxt.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 217, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.ShasiTxt.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ShasiTxt.setFont(font)
        self.ShasiTxt.setObjectName("ShasiTxt")
        self.gridLayout.addWidget(self.ShasiTxt, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.RecoveryFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.PhoneTxt = QtWidgets.QTextEdit(self.RecoveryFrame)
        self.PhoneTxt.setMinimumSize(QtCore.QSize(0, 20))
        self.PhoneTxt.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PhoneTxt.setFont(font)
        self.PhoneTxt.setObjectName("PhoneTxt")
        self.gridLayout.addWidget(self.PhoneTxt, 3, 0, 1, 1)
        self.SearchBtn = QtWidgets.QPushButton(self.RecoveryFrame,clicked=lambda:self.OpenResWindow(searchMethodsClassINSTANCE))

        self.SearchBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.SearchBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SearchBtn.setSizeIncrement(QtCore.QSize(0, 0))
        self.SearchBtn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchBtn.setFont(font)
        self.SearchBtn.setObjectName("SearchBtn")
        self.gridLayout.addWidget(self.SearchBtn, 4, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RecoveryFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        RecoveryWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RecoveryWindow)
        self.statusbar.setObjectName("statusbar")
        RecoveryWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RecoveryWindow)
        QtCore.QMetaObject.connectSlotsByName(RecoveryWindow)

    def retranslateUi(self, RecoveryWindow):
        _translate = QtCore.QCoreApplication.translate
        RecoveryWindow.setWindowTitle(_translate("RecoveryWindow", "MainWindow"))
        self.label_5.setText(_translate("RecoveryWindow", "شماره پلاك:"))
        self.label_6.setText(_translate("RecoveryWindow", "تلفن:"))
        self.CarOwnerTxt.setHtml(_translate("RecoveryWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("RecoveryWindow", "مالك خودرو:"))
        self.CarIdTxt.setHtml(_translate("RecoveryWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ShasiTxt.setHtml(_translate("RecoveryWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("RecoveryWindow", "شماره شاسی: "))
        self.PhoneTxt.setHtml(_translate("RecoveryWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SearchBtn.setText(_translate("RecoveryWindow", "جستجو"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecoveryWindow = QtWidgets.QMainWindow()
    ui = Ui_RecoveryWindow()
    searchMethodsClassINSTANCE=RecoveryMethodsClass(ui)
    ui.setupUi(RecoveryWindow,searchMethodsClassINSTANCE)   

    RecoveryWindow.show()
    sys.exit(app.exec_())
