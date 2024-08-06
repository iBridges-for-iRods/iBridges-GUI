# Form implementation generated from reading ui file 'ibridgesgui/ui_files/transferData.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_transferData(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(865, 528)
        Form.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(211,211,211);\n"
"    color: rgb(88, 88, 90);\n"
"    selection-background-color: rgb(21, 165, 137);\n"
"    selection-color: rgb(245, 244, 244);\n"
"    font: 16pt\n"
"}\n"
"\n"
"QLabel#error_label\n"
"{\n"
"    color: rgb(220, 130, 30);\n"
"}\n"
"\n"
"QLineEdit, QTextEdit, QTableWidget\n"
"{\n"
"   background-color:  rgb(245, 244, 244)\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(21, 165, 137);\n"
"    color: rgb(245, 244, 244);\n"
"}\n"
"\n"
"QPushButton#home_button, QPushButton#parent_button, QPushButton#refresh_button\n"
"{\n"
"    background-color: rgb(245, 244, 244);\n"
"}\n"
"\n"
"QTabWidget#info_tabs\n"
"{\n"
"     background-color: background-color: rgb(211,211,211);\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.overwrite = QtWidgets.QCheckBox(parent=Form)
        self.overwrite.setObjectName("overwrite")
        self.gridLayout.addWidget(self.overwrite, 7, 0, 1, 1)
        self.dest_path_label = QtWidgets.QLabel(parent=Form)
        self.dest_path_label.setObjectName("dest_path_label")
        self.gridLayout.addWidget(self.dest_path_label, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_button = QtWidgets.QPushButton(parent=Form)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(parent=Form)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout.addWidget(self.stop_button)
        self.cancel_button = QtWidgets.QPushButton(parent=Form)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 14, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 16, 0, 1, 1)
        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 19, 0, 1, 1)
        self.source_path_label = QtWidgets.QLabel(parent=Form)
        self.source_path_label.setObjectName("source_path_label")
        self.gridLayout.addWidget(self.source_path_label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 17, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 18, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.overwrite.setText(_translate("Form", "Overwrite existing data"))
        self.dest_path_label.setText(_translate("Form", "dest_path_label"))
        self.start_button.setText(_translate("Form", "Start"))
        self.stop_button.setText(_translate("Form", "Stop"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.checkBox.setText(_translate("Form", "Download metadata as ibridges_metadata.json"))
        self.label.setText(_translate("Form", "Tranfer data from"))
        self.label_5.setText(_translate("Form", "Status:"))
        self.error_label.setText(_translate("Form", "error_label"))
        self.source_path_label.setText(_translate("Form", "source_path_label"))
        self.label_2.setText(_translate("Form", "Options:"))
        self.label_4.setText(_translate("Form", "status_label"))
        self.label_3.setText(_translate("Form", "to"))
