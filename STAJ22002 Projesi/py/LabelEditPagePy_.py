from LabelEditPagePy import Ui_Edit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class LabelEditPage(QtWidgets.QDialog):
    def __init__(self,nlp_record):
        super(LabelEditPage, self).__init__()
        self.lep = Ui_Edit()
        self.lep.setupUi(self)
        self.setWindowIcon(QIcon('icons\logo_1.ico'))

    def reject(self):
        super(LabelEditPage, self).reject()
