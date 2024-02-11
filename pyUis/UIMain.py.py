
from PyQt5 import QtCore, QtGui, QtWidgets
from RecoveryUI import Ui_RecoveryWindow
from FormsMethod import FormMethod


class Ui_MainWindow(object):
    
    def OpenWindow(self):
        self.Window=QtWidgets.QMainWindow()
        self.ui= Ui_RecoveryWindow()
        self.ui.setupUi(self.Window)
        self.Window.show()
        
    def setupUi(self, MainWindow,FromsMethodInstance):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.PrintBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PrintBtn.setFont(font)
        self.PrintBtn.setObjectName("PrintBtn")
        self.horizontalLayout.addWidget(self.PrintBtn)
        self.RecoveryBtn = QtWidgets.QPushButton(self.frame_3,clicked=lambda:self.OpenWindow())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RecoveryBtn.setFont(font)
        self.RecoveryBtn.setObjectName("RecoveryBtn")
        self.horizontalLayout.addWidget(self.RecoveryBtn)
        self.SaveBtn = QtWidgets.QPushButton(self.frame_3,clicked=lambda:FromsMethodInstance.SaveMethod())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setObjectName("SaveBtn")
        self.horizontalLayout.addWidget(self.SaveBtn)
        self.AddBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AddBtn.setFont(font)
        self.AddBtn.setObjectName("AddBtn")
        self.horizontalLayout.addWidget(self.AddBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.TimeTxt = QtWidgets.QTimeEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TimeTxt.setFont(font)
        self.TimeTxt.setObjectName("TimeTxt")
        self.horizontalLayout_2.addWidget(self.TimeTxt)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.DateTxt = QtWidgets.QDateEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateTxt.setFont(font)
        self.DateTxt.setObjectName("DateTxt")
        self.horizontalLayout_2.addWidget(self.DateTxt)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.ShasiTxt = QtWidgets.QTextEdit(self.frame_2)
        self.ShasiTxt.setMaximumSize(QtCore.QSize(16777215, 30))
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
        self.horizontalLayout_2.addWidget(self.ShasiTxt)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.PayTypeComb = QtWidgets.QComboBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PayTypeComb.setFont(font)
        self.PayTypeComb.setObjectName("PayTypeComb")
        self.PayTypeComb.addItem("")
        self.PayTypeComb.addItem("")
        self.PayTypeComb.addItem("")
        self.horizontalLayout_3.addWidget(self.PayTypeComb)
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.AddCarTypeBtn = QtWidgets.QPushButton(self.frame_7)
        self.AddCarTypeBtn.setObjectName("AddCarTypeBtn")
        self.horizontalLayout_3.addWidget(self.AddCarTypeBtn)
        self.CarTypeComb = QtWidgets.QComboBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CarTypeComb.setFont(font)
        self.CarTypeComb.setObjectName("CarTypeComb")
        self.CarTypeComb.addItem("")
        self.CarTypeComb.addItem("")
        self.CarTypeComb.addItem("")
        self.horizontalLayout_3.addWidget(self.CarTypeComb)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.TypeTxt = QtWidgets.QTextEdit(self.frame_4)
        self.TypeTxt.setMaximumSize(QtCore.QSize(100, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TypeTxt.setFont(font)
        self.TypeTxt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TypeTxt.setObjectName("TypeTxt")
        self.horizontalLayout_4.addWidget(self.TypeTxt)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_5.setStyleSheet("\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 4, 1, 1)
        self.CarIdTxt = QtWidgets.QTextEdit(self.frame_5)
        self.CarIdTxt.setMaximumSize(QtCore.QSize(700, 50))
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
        self.gridLayout.addWidget(self.CarIdTxt, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 2)
        self.CarOwnerTxt = QtWidgets.QTextEdit(self.frame_5)
        self.CarOwnerTxt.setMaximumSize(QtCore.QSize(700, 50))
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
        self.gridLayout.addWidget(self.CarOwnerTxt, 1, 2, 1, 1)
        self.PhoneTxt = QtWidgets.QTextEdit(self.frame_5)
        self.PhoneTxt.setMaximumSize(QtCore.QSize(700, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PhoneTxt.setFont(font)
        self.PhoneTxt.setObjectName("PhoneTxt")
        self.gridLayout.addWidget(self.PhoneTxt, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.UseTxt = QtWidgets.QTextEdit(self.frame_5)
        self.UseTxt.setMaximumSize(QtCore.QSize(100, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UseTxt.setFont(font)
        self.UseTxt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UseTxt.setObjectName("UseTxt")
        self.gridLayout.addWidget(self.UseTxt, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 2, 1, 1)
        self.OptionTxt = QtWidgets.QTextEdit(self.frame_6)
        self.OptionTxt.setMaximumSize(QtCore.QSize(16777215, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OptionTxt.setFont(font)
        self.OptionTxt.setObjectName("OptionTxt")
        self.gridLayout_2.addWidget(self.OptionTxt, 2, 1, 1, 1)
        self.RemoveCarColorCondBtn = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RemoveCarColorCondBtn.setFont(font)
        self.RemoveCarColorCondBtn.setObjectName("RemoveCarColorCondBtn")
        self.gridLayout_2.addWidget(self.RemoveCarColorCondBtn, 0, 0, 1, 1)
        self.ShasiCondTxt = QtWidgets.QTextEdit(self.frame_6)
        self.ShasiCondTxt.setMaximumSize(QtCore.QSize(16777215, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ShasiCondTxt.setFont(font)
        self.ShasiCondTxt.setObjectName("ShasiCondTxt")
        self.gridLayout_2.addWidget(self.ShasiCondTxt, 3, 1, 1, 1)
        self.RemoveOptionBtn = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RemoveOptionBtn.setFont(font)
        self.RemoveOptionBtn.setObjectName("RemoveOptionBtn")
        self.gridLayout_2.addWidget(self.RemoveOptionBtn, 2, 0, 1, 1)
        self.RemoveShasiCondBtn = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RemoveShasiCondBtn.setFont(font)
        self.RemoveShasiCondBtn.setObjectName("RemoveShasiCondBtn")
        self.gridLayout_2.addWidget(self.RemoveShasiCondBtn, 3, 0, 1, 1)
        self.CarColorCondTxt = QtWidgets.QTextEdit(self.frame_6)
        self.CarColorCondTxt.setMaximumSize(QtCore.QSize(16777215, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CarColorCondTxt.setFont(font)
        self.CarColorCondTxt.setObjectName("CarColorCondTxt")
        self.gridLayout_2.addWidget(self.CarColorCondTxt, 0, 1, 1, 1)
        self.GirboxCondTxt = QtWidgets.QTextEdit(self.frame_6)
        self.GirboxCondTxt.setMaximumSize(QtCore.QSize(16777215, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GirboxCondTxt.setFont(font)
        self.GirboxCondTxt.setObjectName("GirboxCondTxt")
        self.gridLayout_2.addWidget(self.GirboxCondTxt, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 2, 1, 1)
        self.RemoveInfBtn = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RemoveInfBtn.setFont(font)
        self.RemoveInfBtn.setObjectName("RemoveInfBtn")
        self.gridLayout_2.addWidget(self.RemoveInfBtn, 5, 0, 1, 1)
        self.RemoveGirboxCondBtn = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RemoveGirboxCondBtn.setFont(font)
        self.RemoveGirboxCondBtn.setObjectName("RemoveGirboxCondBtn")
        self.gridLayout_2.addWidget(self.RemoveGirboxCondBtn, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 5, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 2, 1, 1)
        self.InfTxt = QtWidgets.QTextEdit(self.frame_6)
        self.InfTxt.setMaximumSize(QtCore.QSize(16777215, 50))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InfTxt.setFont(font)
        self.InfTxt.setObjectName("InfTxt")
        self.gridLayout_2.addWidget(self.InfTxt, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PrintBtn.setText(_translate("MainWindow", "چاپ"))
        self.RecoveryBtn.setText(_translate("MainWindow", "بازيابي"))
        self.SaveBtn.setText(_translate("MainWindow", "ذخيره"))
        self.AddBtn.setText(_translate("MainWindow", "جديد"))
        self.label_11.setText(_translate("MainWindow", "ساعت:"))
        self.label_7.setText(_translate("MainWindow", "تاريخ:"))
        self.ShasiTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "شماره شاسی: "))
        self.PayTypeComb.setItemText(0, _translate("MainWindow", "option1"))
        self.PayTypeComb.setItemText(1, _translate("MainWindow", "option2"))
        self.PayTypeComb.setItemText(2, _translate("MainWindow", "option3"))
        self.label_8.setText(_translate("MainWindow", "نوع پرداخت:"))
        self.AddCarTypeBtn.setText(_translate("MainWindow", "+"))
        self.CarTypeComb.setItemText(0, _translate("MainWindow", "option1"))
        self.CarTypeComb.setItemText(1, _translate("MainWindow", "option2"))
        self.CarTypeComb.setItemText(2, _translate("MainWindow", "option3"))
        self.label_2.setText(_translate("MainWindow", "نوع خودرو:"))
        self.TypeTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TypeTxt.setPlaceholderText(_translate("MainWindow", "مدل"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "option1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "option2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "option3"))
        self.label_3.setText(_translate("MainWindow", "رنگ خودرو:"))
        self.label_6.setText(_translate("MainWindow", "تلفن:"))
        self.CarIdTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "شماره پلاك:"))
        self.CarOwnerTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.PhoneTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "مالك خودرو:"))
        self.UseTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.UseTxt.setPlaceholderText(_translate("MainWindow", "كاركرد"))
        self.label_13.setText(_translate("MainWindow", "وضعيت رنگ بدنه:"))
        self.OptionTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">تمام آپشن ها فعال میباشد</p></body></html>"))
        self.RemoveCarColorCondBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.ShasiCondTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">شاسی های عقب و جلو سالم است</p></body></html>"))
        self.RemoveOptionBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.RemoveShasiCondBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.CarColorCondTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">اتوموبیل فاقد رنگ شدگی میباشد</p></body></html>"))
        self.GirboxCondTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:norml;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">موتور و گیربکس پلمپ میباشد</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "وضعيت آپشن ها:"))
        self.RemoveInfBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.RemoveGirboxCondBtn.setText(_translate("MainWindow", "پاك كردن"))
        self.label_17.setText(_translate("MainWindow", "توضيحات:"))
        self.label_16.setText(_translate("MainWindow", "وضعيت شاسي:"))
        self.label_14.setText(_translate("MainWindow", "وضعيت موتور و گيربكس:"))
        self.InfTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()    
    frmMethod=FormMethod(ui)
    ui.setupUi(MainWindow,frmMethod)    
    MainWindow.show()   
    sys.exit(app.exec_())
