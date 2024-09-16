import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from signUpPagePy import Ui_MainWindow
from connection import connection
from dbmanager import DbManager
from membership_detail import membership_detail as md
from user_detail import user_detail as ud
from main import Main

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.signUp = Ui_MainWindow()
        self.signUp.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon('icons\logo_1.ico'))
        

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.signUp.centralwidget.setGraphicsEffect(self.shadow)

        # Buton event'leri
        self.signUp.minimize_pushButton.clicked.connect(self.MinimizeEvent)
        self.signUp.close_pushButton.clicked.connect(self.CloseEvent)

        # Taşınabilirlik
        self.dragging = False
        self.offset = QtCore.QPoint()

        # header_frame'i sürüklenebilir yapma
        self.signUp.header_frame.installEventFilter(self)

        # açılış sayfası
        self.signUp.stackedWidget.setCurrentWidget(self.signUp.registerPage)

        # home butonu event'i
        self.signUp.to_register.clicked.connect(lambda: self.signUp.stackedWidget.setCurrentWidget(self.signUp.registerPage))

        # account butonu event'i
        self.signUp.to_login.clicked.connect(lambda: self.signUp.stackedWidget.setCurrentWidget(self.signUp.loginPage))

        # üye olma
        self.signUp.register_pushButton.clicked.connect(self.register_user)

        # üye girişi
        self.signUp.login_pushButton.clicked.connect(self.login_user)

        
        

    def MinimizeEvent(self):
        self.showMinimized()
    
    def CloseEvent(self):
        self.close()

    def eventFilter(self, obj, event):  
        if obj == self.signUp.header_frame:  
            if event.type() == QtCore.QEvent.MouseButtonPress:
                if event.button() == QtCore.Qt.LeftButton:
                    self.dragging = True
                    self.offset = event.globalPos() - self.pos()
                return True
            elif event.type() == QtCore.QEvent.MouseMove:
                if self.dragging:
                    self.move(event.globalPos() - self.offset)
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                if event.button() == QtCore.Qt.LeftButton:
                    self.dragging = False
                return True
        return super(MainWindow, self).eventFilter(obj, event)  
    
    def register_user(self):
        user_name = self.signUp.name_lineEdit.text()
        user_surname = self.signUp.surname_lineEdit.text()
        email = self.signUp.register_email_lineEdit.text()
        password = self.signUp.register_password_lineEdit.text()

        if user_name.strip() and user_name.strip() and email.strip() and password.strip():
            if self.signUp.checkBox.isChecked():
                try:
            
                    conn = connection() 
                    db_manager = DbManager(conn)
                    
                    user_details = ud(user_name, user_surname)
                    
                    user_id = db_manager.register(user_details)
                    
                    membership_details = md(email, password, user_id)
                    
                    db_manager.add_membership(membership_details)

                    self.signUp.name_lineEdit.clear()
                    self.signUp.surname_lineEdit.clear()
                    self.signUp.register_email_lineEdit.clear()
                    self.signUp.register_password_lineEdit.clear()
                    
                    QMessageBox.information(self, "Success", "User registered successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            else:
                QMessageBox.critical(self,"Terms","Agree with our terms!")
        else: 
            QMessageBox.critical(self,"Empty","Plase enter your information!")


    def login_user(self):

        email = self.signUp.email_lineEdit.text()
        password = self.signUp.password_lineEdit.text()

        membership_details = md(email, password, None)
        conn = connection()  
        db_manager = DbManager(conn)

        result = db_manager.login(membership_details)

        if result:
            user_id = result[0] 
            self.open_main_page(user_id)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid email or password")



    def open_main_page(self, user_id):
        self.main_page = Main(user_id)  
        self.main_page.show()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    page = MainWindow()
    page.show()
    sys.exit(app.exec_())
