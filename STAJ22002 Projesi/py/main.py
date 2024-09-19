import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QHeaderView
from PyQt5.QtGui import QColor,QIcon
from PyQt5.QtCore import QPropertyAnimation
from MainPagePy import Ui_MainPage
import joblib
from connection import connection
from dbmanager import DbManager
from LabelEditPagePy_ import Ui_Edit

windowSize = 0

class Main(QtWidgets.QMainWindow):
    def __init__(self, user_id):
        super(Main, self).__init__()
        self.main = Ui_MainPage()
        self.main.setupUi(self)
        self.setWindowIcon(QIcon('icons\logo_1.ico'))

        self.user_id = user_id

        # eğitilen modeli alma
        self.model, self.tfidf = joblib.load(r'py\mental_health_model.pkl')

        # tahmin etme event'i
        self.main.send_pushButton.clicked.connect(self.PredictEvent)

        # Window title bar'ı kaldırma ve gölge ekleme
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.main.centralwidget.setGraphicsEffect(self.shadow)

        # Buton event'leri
        self.main.minimizeButton.clicked.connect(self.MinimizeEvent)
        self.main.restoreButton.clicked.connect(self.RestoreEvent)
        self.main.closeButton.clicked.connect(self.CloseEvent)

        # Taşınabilirlik için başlangıçta fare olaylarını başlat
        self.dragging = False
        self.offset = QtCore.QPoint()

        # main_header'ı sürüklenebilir yapma
        self.main.main_header.installEventFilter(self)

        # açılış sayfası
        self.main.stackedWidget.setCurrentWidget(self.main.home_page)

        # menü butonu event'i
        self.main.menu_pushButton.clicked.connect(self.SlideEvent)

        # home butonu event'i
        self.main.home_pushButton.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.home_page))

        # account butonu event'i
        self.main.account_pushButton.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.account_page))

        # history butonu event'i
        self.main.history_pushButton.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.history_page))

        #table widget edit
        self.main.tableWidget.setRowCount(0) 
        self.main.tableWidget.setColumnCount(2) 
        self.main.tableWidget.setHorizontalHeaderLabels(['Text', 'Result'])
        self.main.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        
        # nlp işlemleri aktarımı
        self.load_user_data()

        # kullanıcı bilgisi aktarımı
        self.display_user_info()

        # progress barları ayarlama
        self.update_user_progress_bars(self.user_id)

        # yazılan yazıyı temizleme
        self.main.clear_pushButton.clicked.connect(self.clearLabel)

        # tablo düzenleme
        self.main.edit_pushButton.clicked.connect(self.openLabelEditPage)


        # çıkış işlemi
        self.main.logout_pushButton.clicked.connect(self.close)




    def PredictEvent(self):
        text = self.main.statement_textEdit.toPlainText()

        if not text.strip():
            self.main.result_label.setText("Enter a valid sentence!")
            return

        if any(char.isalpha() for char in text):
            pre = self.Predict(text)
            self.main.result_label.setText(f'Result: {pre}')
            self.main.save_pushButton.clicked.connect(self.saveData)     
            
        else:
            self.main.result_label.setText("Enter a valid sentence!")

    def Predict(self, text):
        if hasattr(self.model, 'predict'):
            text_tfidf = self.tfidf.transform([text])
            prediction = self.model.predict(text_tfidf)
            return prediction[0]
        else:
            raise AttributeError("The model does not have a 'predict' method.")


    def MinimizeEvent(self):
        self.showMinimized()

    def RestoreEvent(self):
        global windowSize
        win_status = windowSize

        if win_status == 0:
            windowSize = 1
            self.showMaximized()
            self.main.restoreButton.setIcon(QtGui.QIcon(":/icon-w/restore-w.ico"))
        else:
            windowSize = 0
            self.showNormal()
            self.main.restoreButton.setIcon(QtGui.QIcon(":/icon-w/square-w.ico"))

    def CloseEvent(self):
        self.close()

    def eventFilter(self, obj, event):
        if obj == self.main.main_header:
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
        return super(Main, self).eventFilter(obj, event)
    
    def SlideEvent(self):
        width = self.main.left_side_menu.width()

        if width == 60:
            new_width = 180
        else:
            new_width=60

        self.animation = QPropertyAnimation(self.main.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    def load_user_data(self):
        conn = connection()
        db_manager = DbManager(conn)
        nlp_results = db_manager.get_nlp_results(self.user_id)

        self.main.tableWidget.setRowCount(0)  

        for nlp in nlp_results:
            row_position = self.main.tableWidget.rowCount()
            self.main.tableWidget.insertRow(row_position)
            self.main.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nlp.nlp_text))
            self.main.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(nlp.nlp_result_text))

    def saveData(self):
        text = self.main.statement_textEdit.toPlainText()
        result_full = self.main.result_label.text()
        result = result_full[8:]

        if text.strip():
            db_manager = DbManager(connection())
            db_manager.insertNLPResultToDatabase(text, result, self.user_id)

            QMessageBox.information(self, "Success", "NLP created successfully!")
            
            self.updateTable()

        else:
            QMessageBox.critical(self, "Null Text", "Text not found!")

    def updateTable(self):
        db_manager = DbManager(connection())
        results = db_manager.get_nlp_results(self.user_id)  

        self.main.tableWidget.setRowCount(0) 
        
        for row_number, result in enumerate(results):
            self.main.tableWidget.insertRow(row_number)
            self.main.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(result.nlp_text))
            self.main.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(result.nlp_result_text))
        self.update_user_progress_bars(self.user_id)

    def display_user_info(self):
        db_manager = DbManager(connection())
        user_info = db_manager.get_user_details(self.user_id)

        self.main.name_result_label.setText(user_info['user_name'])
        self.main.surname_result_label.setText(user_info['user_surname'])
        self.main.e_mail_result_label.setText(user_info['membership_e_mail'])
        self.main.password_result_label.setText(user_info['membership_password'])


    def update_user_progress_bars(self, user_id):
     
        db_manager = DbManager(connection())

        result_counts = db_manager.get_user_nlp_result_counts(user_id)
        total_count = sum(result_counts.values())

        if total_count == 0:
            self.main.anxiety_progressBar.setValue(0)
            self.main.bipolar_progressBar.setValue(0)
            self.main.depression_progressBar.setValue(0)
            self.main.normal_progressBar.setValue(0)
            self.main.stress_progressBar.setValue(0)
            self.main.pd_progressBar.setValue(0)
            self.main.suicidal_progressBar.setValue(0)
            
            return

        self.main.anxiety_progressBar.setValue(int((result_counts.get("Anxiety", 0) / total_count) * 100))
        self.main.bipolar_progressBar.setValue(int((result_counts.get("Bipolar", 0) / total_count) * 100))
        self.main.depression_progressBar.setValue(int((result_counts.get("Depression", 0) / total_count) * 100))
        self.main.normal_progressBar.setValue(int((result_counts.get("Normal", 0) / total_count) * 100))
        self.main.pd_progressBar.setValue(int((result_counts.get("Personality disorder", 0) / total_count) * 100))
        self.main.stress_progressBar.setValue(int((result_counts.get("Stress", 0) / total_count) * 100))
        self.main.suicidal_progressBar.setValue(int((result_counts.get("Suicidal", 0) / total_count) * 100))

    def clearLabel(self):
        self.main.statement_textEdit.clear()
        self.main.result_label.clear()
        

    def openLabelEditPage(self):
       
        selected_row = self.main.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a row to edit.")
            return

        nlp_result_text = self.main.tableWidget.item(selected_row, 1).text()

        dialog = QtWidgets.QDialog(self)
        self.lep = Ui_Edit()
        self.lep.setupUi(dialog)
         
        index = self.lep.comboBox.findText(nlp_result_text, QtCore.Qt.MatchFixedString)

        if index >= 0:
            self.lep.comboBox.setCurrentIndex(index)

        self.lep.buttonBox.accepted.connect(lambda: self.updateNlpResultText(selected_row, self.lep.comboBox.currentText()))
        self.lep.buttonBox.accepted.connect(dialog.reject)
        self.lep.buttonBox.rejected.connect(dialog.reject)
        dialog.exec_()

    def updateNlpResultText(self, row, new_text):
        db_manager = DbManager(connection())
    
        nlp_text = self.main.tableWidget.item(row, 0).text()
        db_manager.update_nlp_result_text(nlp_text, new_text)

        self.main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(new_text))
        QMessageBox.information(self,"Success","Result changed successfully!")

        self.update_user_progress_bars(self.user_id)
    
       
    def close(self):   
        QtWidgets.QApplication.quit() 

        

    
