# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mahsima\Desktop\carProj\UIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def OpenWindow(self):
        self.Window=QtWidgets.QMainWindow()
        self.ui= Ui_RecoveryWindow()
        self.ui.setupUi(self.Window)
        self.Window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 959)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 210, 31, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 210, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 110, 51, 21))
        self.label_11.setObjectName("label_11")
        self.OptionTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.OptionTxt.setGeometry(QtCore.QRect(160, 630, 481, 81))
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
        self.OptionTxt.setPalette(palette)
        self.OptionTxt.setObjectName("OptionTxt")
        self.GirboxCondTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.GirboxCondTxt.setGeometry(QtCore.QRect(160, 520, 481, 81))
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
        self.GirboxCondTxt.setPalette(palette)
        self.GirboxCondTxt.setObjectName("GirboxCondTxt")
        self.RemoveOptionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveOptionBtn.setGeometry(QtCore.QRect(60, 660, 93, 28))
        self.RemoveOptionBtn.setObjectName("RemoveOptionBtn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 160, 71, 21))
        self.label_8.setObjectName("label_8")
        self.TimeTxt = QtWidgets.QTimeEdit(self.centralwidget)
        self.TimeTxt.setGeometry(QtCore.QRect(10, 110, 118, 22))
        self.TimeTxt.setObjectName("TimeTxt")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 110, 41, 21))
        self.label_7.setObjectName("label_7")
        self.InfTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.InfTxt.setGeometry(QtCore.QRect(160, 830, 481, 81))
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
        self.InfTxt.setPalette(palette)
        self.InfTxt.setObjectName("InfTxt")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 360, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(670, 760, 111, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(670, 860, 111, 21))
        self.label_17.setObjectName("label_17")
        self.DateTxt = QtWidgets.QDateEdit(self.centralwidget)
        self.DateTxt.setGeometry(QtCore.QRect(200, 110, 110, 22))
        self.DateTxt.setObjectName("DateTxt")
        self.RemoveInfBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveInfBtn.setGeometry(QtCore.QRect(60, 860, 93, 28))
        self.RemoveInfBtn.setObjectName("RemoveInfBtn")
        self.CarOwnerTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.CarOwnerTxt.setGeometry(QtCore.QRect(480, 310, 211, 31))
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
        self.CarOwnerTxt.setObjectName("CarOwnerTxt")
        self.PhoneTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.PhoneTxt.setGeometry(QtCore.QRect(480, 360, 211, 31))
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
        self.PhoneTxt.setPalette(palette)
        self.PhoneTxt.setObjectName("PhoneTxt")
        self.CarIdTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.CarIdTxt.setGeometry(QtCore.QRect(480, 260, 211, 31))
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
        self.CarIdTxt.setObjectName("CarIdTxt")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(670, 450, 111, 21))
        self.label_13.setObjectName("label_13")
        self.CarTypeComb = QtWidgets.QComboBox(self.centralwidget)
        self.CarTypeComb.setGeometry(QtCore.QRect(600, 160, 91, 21))
        self.CarTypeComb.setObjectName("CarTypeComb")
        self.CarTypeComb.addItem("")
        self.CarTypeComb.addItem("")
        self.CarTypeComb.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 160, 61, 21))
        self.label_2.setObjectName("label_2")
        self.ShasiTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.ShasiTxt.setGeometry(QtCore.QRect(420, 110, 241, 31))
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
        self.ShasiTxt.setObjectName("ShasiTxt")
        self.AddCarTypeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddCarTypeBtn.setGeometry(QtCore.QRect(560, 160, 31, 21))
        self.AddCarTypeBtn.setObjectName("AddCarTypeBtn")
        self.RemoveGirboxCondBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveGirboxCondBtn.setGeometry(QtCore.QRect(60, 550, 93, 28))
        self.RemoveGirboxCondBtn.setObjectName("RemoveGirboxCondBtn")
        self.TypeTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.TypeTxt.setGeometry(QtCore.QRect(480, 200, 71, 31))
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
        self.TypeTxt.setPalette(palette)
        self.TypeTxt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TypeTxt.setObjectName("TypeTxt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 110, 91, 21))
        self.label.setObjectName("label")
        self.CarColorCondTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.CarColorCondTxt.setGeometry(QtCore.QRect(160, 420, 481, 81))
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
        self.CarColorCondTxt.setPalette(palette)
        self.CarColorCondTxt.setObjectName("CarColorCondTxt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, 260, 81, 21))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 310, 71, 21))
        self.label_4.setObjectName("label_4")
        self.PayTypeComb = QtWidgets.QComboBox(self.centralwidget)
        self.PayTypeComb.setGeometry(QtCore.QRect(190, 160, 91, 21))
        self.PayTypeComb.setObjectName("PayTypeComb")
        self.PayTypeComb.addItem("")
        self.PayTypeComb.addItem("")
        self.PayTypeComb.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(600, 210, 91, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.RemoveCarColorCondBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveCarColorCondBtn.setGeometry(QtCore.QRect(60, 450, 93, 28))
        self.RemoveCarColorCondBtn.setObjectName("RemoveCarColorCondBtn")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(670, 660, 111, 21))
        self.label_15.setObjectName("label_15")
        self.RemoveShasiCondBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveShasiCondBtn.setGeometry(QtCore.QRect(60, 760, 93, 28))
        self.RemoveShasiCondBtn.setObjectName("RemoveShasiCondBtn")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(650, 550, 131, 21))
        self.label_14.setObjectName("label_14")
        self.UseTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.UseTxt.setGeometry(QtCore.QRect(400, 310, 71, 31))
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
        self.UseTxt.setPalette(palette)
        self.UseTxt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UseTxt.setObjectName("UseTxt")
        self.ShasiCondTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.ShasiCondTxt.setGeometry(QtCore.QRect(160, 730, 481, 81))
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
        self.ShasiCondTxt.setPalette(palette)
        self.ShasiCondTxt.setObjectName("ShasiCondTxt")
        self.AddBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddBtn.setGeometry(QtCore.QRect(670, 30, 93, 28))
        self.AddBtn.setObjectName("AddBtn")
        self.SaveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SaveBtn.setGeometry(QtCore.QRect(570, 30, 93, 28))
        self.SaveBtn.setObjectName("SaveBtn")
        self.RecoveryBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RecoveryBtn.setGeometry(QtCore.QRect(470, 30, 93, 28))
        self.RecoveryBtn.setObjectName("RecoveryBtn")
        self.PrintBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PrintBtn.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.PrintBtn.setObjectName("PrintBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.label_3.setText(_translate("MainWindow", "رنگ خودرو:"))
        self.label_11.setText(_translate("MainWindow", "ساعت:"))
        self.OptionTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">تمام آپشن ها فعال ميباشد</p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.GirboxCondTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">موتور و گيربكس پلمپ ميباشد</p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RemoveOptionBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.label_8.setText(_translate("MainWindow", "نوع پرداخت:"))
        self.label_7.setText(_translate("MainWindow", "تاريخ:"))
        self.InfTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "تلفن:"))
        self.label_16.setText(_translate("MainWindow", "وضعيت شاسي:"))
        self.label_17.setText(_translate("MainWindow", "توضيحات:"))
        self.RemoveInfBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.CarOwnerTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.PhoneTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CarIdTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "وضعيت رنگ بدنه:"))
        self.CarTypeComb.setItemText(0, _translate("MainWindow", "option1"))
        self.CarTypeComb.setItemText(1, _translate("MainWindow", "option2"))
        self.CarTypeComb.setItemText(2, _translate("MainWindow", "option3"))
        self.label_2.setText(_translate("MainWindow", "نوع خودرو:"))
        self.ShasiTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.AddCarTypeBtn.setText(_translate("MainWindow", "+"))
        self.RemoveGirboxCondBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.TypeTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TypeTxt.setPlaceholderText(_translate("MainWindow", "مدل"))
        self.label.setText(_translate("MainWindow", "شماره شاسی: "))
        self.CarColorCondTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">اتوموبيل فاقد رنگ شدگي ميباشد</p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "شماره پلاك:"))
        self.label_4.setText(_translate("MainWindow", "مالك خودرو:"))
        self.PayTypeComb.setItemText(0, _translate("MainWindow", "option1"))
        self.PayTypeComb.setItemText(1, _translate("MainWindow", "option2"))
        self.PayTypeComb.setItemText(2, _translate("MainWindow", "option3"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "option1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "option2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "option3"))
        self.RemoveCarColorCondBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.label_15.setText(_translate("MainWindow", "وضعيت آپشن ها:"))
        self.RemoveShasiCondBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.label_14.setText(_translate("MainWindow", "وضعيت موتور و گيربكس:"))
        self.UseTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.UseTxt.setPlaceholderText(_translate("MainWindow", "كاركرد"))
        self.ShasiCondTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">شاسي هاي عقب و جلو سالم است</p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.AddBtn.setText(_translate("MainWindow", "جديد"))
        self.SaveBtn.setText(_translate("MainWindow", "ذخيره"))
        self.RecoveryBtn.setText(_translate("MainWindow", "بازيابي"))
        self.PrintBtn.setText(_translate("MainWindow", "چاپ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
