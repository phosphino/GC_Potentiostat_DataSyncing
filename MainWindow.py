# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 216)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.GCFile_label = QtWidgets.QLabel(self.groupBox)
        self.GCFile_label.setText("")
        self.GCFile_label.setObjectName("GCFile_label")
        self.horizontalLayout.addWidget(self.GCFile_label)
        self.GCFile_button = QtWidgets.QPushButton(self.groupBox)
        self.GCFile_button.setMaximumSize(QtCore.QSize(75, 16777215))
        self.GCFile_button.setObjectName("GCFile_button")
        self.horizontalLayout.addWidget(self.GCFile_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.calibrationslope_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.calibrationslope_Edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.calibrationslope_Edit.setObjectName("calibrationslope_Edit")
        self.horizontalLayout_5.addWidget(self.calibrationslope_Edit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.flowrate_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.flowrate_Edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.flowrate_Edit.setObjectName("flowrate_Edit")
        self.horizontalLayout_5.addWidget(self.flowrate_Edit)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.temperature_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.temperature_Edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.temperature_Edit.setObjectName("temperature_Edit")
        self.horizontalLayout_5.addWidget(self.temperature_Edit)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.baseline_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.baseline_Edit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.baseline_Edit.setObjectName("baseline_Edit")
        self.horizontalLayout_5.addWidget(self.baseline_Edit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GCPot_syncingBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.GCPot_syncingBox.setChecked(True)
        self.GCPot_syncingBox.setObjectName("GCPot_syncingBox")
        self.horizontalLayout_2.addWidget(self.GCPot_syncingBox)
        self.startdate_label = QtWidgets.QLabel(self.groupBox_2)
        self.startdate_label.setEnabled(False)
        self.startdate_label.setObjectName("startdate_label")
        self.horizontalLayout_2.addWidget(self.startdate_label)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.Format_button = QtWidgets.QPushButton(self.centralwidget)
        self.Format_button.setObjectName("Format_button")
        self.horizontalLayout_4.addWidget(self.Format_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Gas Chromatograph .xlsx File"))
        self.label_2.setText(_translate("MainWindow", "File:"))
        self.GCFile_button.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Calibration Slope"))
        self.label_4.setText(_translate("MainWindow", "Flow Rate (mL / min)"))
        self.label_5.setText(_translate("MainWindow", "Temperature (C)"))
        self.label_6.setText(_translate("MainWindow", "Baseline"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Potentiostat Start Time"))
        self.GCPot_syncingBox.setText(_translate("MainWindow", "Potentiostat Started Same Day As GC"))
        self.startdate_label.setText(_translate("MainWindow", "Select Potentiostat Start Date:"))
        self.label_3.setText(_translate("MainWindow", "Potentiostat Start Time:"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "hh:mm:ss "))
        self.Format_button.setText(_translate("MainWindow", "Format"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

