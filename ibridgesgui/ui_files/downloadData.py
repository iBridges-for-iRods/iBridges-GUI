# Form implementation generated from reading ui file 'ibridgesgui/ui_files/downloadData.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_downloadData(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(936, 395)
        Form.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(211,211,211);\n"
"    color: rgb(88, 88, 90);\n"
"    selection-background-color: rgb(21, 165, 137);\n"
"    selection-color: rgb(245, 244, 244);\n"
"    font: 16pt\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"  background-color: rgb(21, 165, 137);\n"
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.download_button = QtWidgets.QPushButton(parent=Form)
        self.download_button.setObjectName("download_button")
        self.horizontalLayout.addWidget(self.download_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.hide_button = QtWidgets.QPushButton(parent=Form)
        self.hide_button.setObjectName("hide_button")
        self.horizontalLayout.addWidget(self.hide_button)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 1)
        self.metadata = QtWidgets.QCheckBox(parent=Form)
        self.metadata.setObjectName("metadata")
        self.gridLayout.addWidget(self.metadata, 6, 1, 1, 1)
        self.destination_label = QtWidgets.QLabel(parent=Form)
        self.destination_label.setText("")
        self.destination_label.setObjectName("destination_label")
        self.gridLayout.addWidget(self.destination_label, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.overwrite = QtWidgets.QCheckBox(parent=Form)
        self.overwrite.setObjectName("overwrite")
        self.gridLayout.addWidget(self.overwrite, 5, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.folder_button = QtWidgets.QPushButton(parent=Form)
        self.folder_button.setObjectName("folder_button")
        self.horizontalLayout_3.addWidget(self.folder_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 12, 0, 1, 4)
        self.source_browser = QtWidgets.QTextBrowser(parent=Form)
        self.source_browser.setObjectName("source_browser")
        self.gridLayout.addWidget(self.source_browser, 3, 1, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(parent=Form)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 9, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Download"))
        self.download_button.setText(_translate("Form", "Download"))
        self.hide_button.setText(_translate("Form", "Close window"))
        self.metadata.setText(_translate("Form", "Download metadata as ibridges_metadata.json"))
        self.label.setText(_translate("Form", "Download to:"))
        self.overwrite.setText(_translate("Form", "Overwrite existing data"))
        self.folder_button.setText(_translate("Form", "Open Folders"))
        self.label_5.setText(_translate("Form", "Downloading"))
        self.label_2.setText(_translate("Form", "Options:"))
