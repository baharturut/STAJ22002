# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LabelEditPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName("Edit")
        Edit.resize(505, 241)
        Edit.setMinimumSize(QtCore.QSize(505, 241))
        Edit.setMaximumSize(QtCore.QSize(505, 241))
        Edit.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(87, 0, 130);\n"
"}\n"
"\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(Edit)
        self.buttonBox.setGeometry(QtCore.QRect(130, 150, 221, 31))
        self.buttonBox.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(245, 245, 255);\n"
"")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Edit)
        self.comboBox.setGeometry(QtCore.QRect(54, 50, 401, 41))
        self.comboBox.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(245, 245, 255);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Edit)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        _translate = QtCore.QCoreApplication.translate
        Edit.setWindowTitle(_translate("Edit", "Edit"))
        self.comboBox.setItemText(0, _translate("Edit", "Normal"))
        self.comboBox.setItemText(1, _translate("Edit", "Anxiety"))
        self.comboBox.setItemText(2, _translate("Edit", "Bipolar"))
        self.comboBox.setItemText(3, _translate("Edit", "Depression"))
        self.comboBox.setItemText(4, _translate("Edit", "Personality disorder"))
        self.comboBox.setItemText(5, _translate("Edit", "Stress"))
        self.comboBox.setItemText(6, _translate("Edit", "Suicidal"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edit = QtWidgets.QWidget()
    ui = Ui_Edit()
    ui.setupUi(Edit)
    Edit.show()
    sys.exit(app.exec_())
