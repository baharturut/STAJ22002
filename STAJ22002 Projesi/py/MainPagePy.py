# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(1251, 737)
        self.centralwidget = QtWidgets.QWidget(MainPage)
        self.centralwidget.setStyleSheet("background-color: rgb(14, 16, 23);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.main_header.setStyleSheet("QFrame{\n"
"\n"
"    border-bottom: 1px solid rgb(14, 16, 23);\n"
"    background-color: rgb(14, 16, 23);\n"
"    border-radius: 5px 5px 0px 0px;\n"
"\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_bar_container = QtWidgets.QFrame(self.main_header)
        self.title_bar_container.setStyleSheet("")
        self.title_bar_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar_container.setObjectName("title_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(self.title_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(60, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"    background-color: rgb(14, 16, 23);\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(14, 16, 23);\n"
"    color: rgb(245, 245, 255);\n"
"    font: 10pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 192, 239);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_pushButton = QtWidgets.QPushButton(self.left_menu_toggle)
        self.menu_pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.menu_pushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.menu_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon-w/menu-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_pushButton.setIcon(icon)
        self.menu_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.menu_pushButton.setObjectName("menu_pushButton")
        self.horizontalLayout_4.addWidget(self.menu_pushButton)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.title_bar = QtWidgets.QFrame(self.title_bar_container)
        self.title_bar.setStyleSheet("font: 75 20pt \"Verdana\";\n"
"color: rgb(245, 245, 255);")
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.title_bar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.title_bar)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addWidget(self.title_bar)
        self.horizontalLayout_2.addWidget(self.title_bar_container)
        self.top_right_btns = QtWidgets.QFrame(self.main_header)
        self.top_right_btns.setMaximumSize(QtCore.QSize(120, 16777215))
        self.top_right_btns.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 192, 239);\n"
"\n"
"}")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimizeButton = QtWidgets.QPushButton(self.top_right_btns)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.setStyleSheet("")
        self.minimizeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon-w/minimize-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QtCore.QSize(30, 30))
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_3.addWidget(self.minimizeButton)
        self.restoreButton = QtWidgets.QPushButton(self.top_right_btns)
        self.restoreButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restoreButton.setStyleSheet("")
        self.restoreButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon-w/square-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setIconSize(QtCore.QSize(28, 28))
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_3.addWidget(self.restoreButton)
        self.closeButton = QtWidgets.QPushButton(self.top_right_btns)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("")
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon-w/close-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QtCore.QSize(30, 30))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("background-color: rgb(87, 0, 130);")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(60, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"    background-color: rgb(14, 16, 23);\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(14, 16, 23);\n"
"    color: rgb(245, 245, 255);\n"
"    font: 10pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 192, 239);\n"
"}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_menu_top_buttons = QtWidgets.QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.account_pushButton = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.account_pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.account_pushButton.setStyleSheet("background-repeat: none;\n"
"padding-left:60px;\n"
"background-image: url(:/icon-w/avatar-w_1.ico);\n"
"background-position: center left;")
        self.account_pushButton.setObjectName("account_pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.account_pushButton)
        self.home_pushButton = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.home_pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.home_pushButton.setStyleSheet("background-image: url(:/icon-w/home-w.ico);\n"
"background-repeat: none;\n"
"padding-left:60px;\n"
"background-position: center left;")
        self.home_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.home_pushButton.setObjectName("home_pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.home_pushButton)
        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)
        self.history_pushButton = QtWidgets.QPushButton(self.left_side_menu)
        self.history_pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.history_pushButton.setStyleSheet("background-image: url(:/icon-w/history-w.ico);\n"
"background-repeat: none;\n"
"padding-left:60px;\n"
"background-position: center left;")
        self.history_pushButton.setObjectName("history_pushButton")
        self.verticalLayout_2.addWidget(self.history_pushButton)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("background-color: rgb(87, 0, 130);")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("")
        self.home_page.setObjectName("home_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.home_page)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    border:2px solid qlineargradient(spread:pad, x1:0, y1:0.585, x2:0.995025, y2:0.517, stop:0 rgba(0, 192, 239, 255), stop:1 rgba(173, 65, 255, 255));\n"
"    font: 15pt \"Verdana\";\n"
"    color: rgb(245, 245, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"}\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.text_frame = QtWidgets.QFrame(self.home_page)
        self.text_frame.setMaximumSize(QtCore.QSize(16777215, 250))
        self.text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text_frame.setObjectName("text_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.text_frame)
        self.horizontalLayout_6.setContentsMargins(10, 20, 10, 20)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.statement_textEdit = QtWidgets.QTextEdit(self.text_frame)
        self.statement_textEdit.setToolTip("")
        self.statement_textEdit.setStyleSheet("QTextEdit{\n"
"    font: 10pt \"Verdana\";\n"
"    color: rgb(245, 245, 255);\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.585, x2:0.995025, y2:0.517, stop:0 rgba(0, 192, 239, 255), stop:1 rgba(173, 65, 255, 255));\n"
"    border-radius: 10px;\n"
"    background-color: rgb(14, 16, 23,50);\n"
"}\n"
"")
        self.statement_textEdit.setObjectName("statement_textEdit")
        self.horizontalLayout_6.addWidget(self.statement_textEdit)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.send_pushButton = QtWidgets.QPushButton(self.text_frame)
        self.send_pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.send_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 192, 239);\n"
"\n"
"}")
        self.send_pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon-w/send-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_pushButton.setIcon(icon4)
        self.send_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.send_pushButton.setObjectName("send_pushButton")
        self.verticalLayout_8.addWidget(self.send_pushButton)
        self.clear_pushButton = QtWidgets.QPushButton(self.text_frame)
        self.clear_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 192, 239);\n"
"\n"
"}")
        self.clear_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon-w/clear-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_pushButton.setIcon(icon5)
        self.clear_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.verticalLayout_8.addWidget(self.clear_pushButton)
        self.save_pushButton = QtWidgets.QPushButton(self.text_frame)
        self.save_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 192, 239);\n"
"\n"
"}")
        self.save_pushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon-w/save-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_pushButton.setIcon(icon6)
        self.save_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.save_pushButton.setObjectName("save_pushButton")
        self.verticalLayout_8.addWidget(self.save_pushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addWidget(self.text_frame)
        self.result_label = QtWidgets.QLabel(self.home_page)
        self.result_label.setMaximumSize(QtCore.QSize(16777215, 150))
        self.result_label.setStyleSheet("\n"
"QFrame{\n"
"    border:2px solid qlineargradient(spread:pad, x1:0, y1:0.585, x2:0.995025, y2:0.517, stop:0 rgba(0, 192, 239, 255), stop:1 rgba(173, 65, 255, 255));\n"
"    font: 15pt \"Verdana\";\n"
"    color: rgb(245, 245, 255);\n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"}\n"
"\n"
"")
        self.result_label.setText("")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.verticalLayout_5.addWidget(self.result_label)
        self.stackedWidget.addWidget(self.home_page)
        self.account_page = QtWidgets.QWidget()
        self.account_page.setStyleSheet("")
        self.account_page.setObjectName("account_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.account_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.account_frame = QtWidgets.QFrame(self.account_page)
        self.account_frame.setStyleSheet("QLabel{\n"
"    \n"
"    font: 10pt \"Verdana\";\n"
"    \n"
"    color: rgb(245, 245, 255);\n"
"\n"
"}")
        self.account_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_frame.setObjectName("account_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.account_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.account_frame)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icon-w/profile-w.png"))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.account_frame)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 20pt \"Verdana\";")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.account_detail_frame = QtWidgets.QFormLayout()
        self.account_detail_frame.setContentsMargins(-1, -1, -1, 0)
        self.account_detail_frame.setHorizontalSpacing(29)
        self.account_detail_frame.setVerticalSpacing(36)
        self.account_detail_frame.setObjectName("account_detail_frame")
        self.name_label = QtWidgets.QLabel(self.account_frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.account_detail_frame.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_result_label = QtWidgets.QLabel(self.account_frame)
        self.name_result_label.setObjectName("name_result_label")
        self.account_detail_frame.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_result_label)
        self.surname_label = QtWidgets.QLabel(self.account_frame)
        self.surname_label.setObjectName("surname_label")
        self.account_detail_frame.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surname_label)
        self.surname_result_label = QtWidgets.QLabel(self.account_frame)
        self.surname_result_label.setObjectName("surname_result_label")
        self.account_detail_frame.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surname_result_label)
        self.e_mail_label = QtWidgets.QLabel(self.account_frame)
        self.e_mail_label.setObjectName("e_mail_label")
        self.account_detail_frame.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.e_mail_label)
        self.e_mail_result_label = QtWidgets.QLabel(self.account_frame)
        self.e_mail_result_label.setObjectName("e_mail_result_label")
        self.account_detail_frame.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.e_mail_result_label)
        self.password_label = QtWidgets.QLabel(self.account_frame)
        self.password_label.setObjectName("password_label")
        self.account_detail_frame.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_result_label = QtWidgets.QLabel(self.account_frame)
        self.password_result_label.setObjectName("password_result_label")
        self.account_detail_frame.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password_result_label)
        self.verticalLayout_6.addLayout(self.account_detail_frame)
        self.logout_pushButton = QtWidgets.QPushButton(self.account_frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.logout_pushButton.setFont(font)
        self.logout_pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(245, 245, 255);\n"
"    border : solid 5px ;\n"
"    border-radius: 5px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.585, x2:0.995025, y2:0.517, stop:0 rgba(0, 192, 239, 255), stop:1 rgba(173, 65, 255, 255));\n"
"\n"
"}\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon-w/logout-w.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_pushButton.setIcon(icon7)
        self.logout_pushButton.setObjectName("logout_pushButton")
        self.verticalLayout_6.addWidget(self.logout_pushButton)
        self.horizontalLayout_7.addWidget(self.account_frame)
        self.line = QtWidgets.QFrame(self.account_page)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.account_page)
        self.frame_2.setStyleSheet("QProgressBar{\n"
"    color: rgb(245, 245, 255);\n"
"    background-color: rgb(14, 16, 24);\n"
"    border-style: none;\n"
"    border-radius: 15px;\n"
"    font: 75 10pt \"Verdana\";\n"
"    \n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.585, x2:0.995025, y2:0.517, stop:0 rgba(0, 192, 239, 255), stop:1 rgba(173, 65, 255, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"    \n"
"    font: 10pt \"Verdana\";\n"
"    \n"
"    color: rgb(245, 245, 255);\n"
"\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(130, 70, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 75 24pt \"Verdana\";")
        self.label_18.setObjectName("label_18")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 167, 796, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 3)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 6, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.normal_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.normal_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.normal_progressBar.setProperty("value", 0)
        self.normal_progressBar.setObjectName("normal_progressBar")
        self.gridLayout.addWidget(self.normal_progressBar, 3, 3, 1, 1)
        self.depression_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.depression_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.depression_progressBar.setProperty("value", 0)
        self.depression_progressBar.setObjectName("depression_progressBar")
        self.gridLayout.addWidget(self.depression_progressBar, 2, 3, 1, 1)
        self.anxiety_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.anxiety_progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.anxiety_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.anxiety_progressBar.setStyleSheet("")
        self.anxiety_progressBar.setProperty("value", 0)
        self.anxiety_progressBar.setObjectName("anxiety_progressBar")
        self.gridLayout.addWidget(self.anxiety_progressBar, 0, 3, 1, 1)
        self.bipolar_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.bipolar_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.bipolar_progressBar.setProperty("value", 0)
        self.bipolar_progressBar.setObjectName("bipolar_progressBar")
        self.gridLayout.addWidget(self.bipolar_progressBar, 1, 3, 1, 1)
        self.stress_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.stress_progressBar.setMinimumSize(QtCore.QSize(350, 0))
        self.stress_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.stress_progressBar.setProperty("value", 0)
        self.stress_progressBar.setObjectName("stress_progressBar")
        self.gridLayout.addWidget(self.stress_progressBar, 5, 3, 1, 1)
        self.suicidal_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.suicidal_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.suicidal_progressBar.setProperty("value", 0)
        self.suicidal_progressBar.setObjectName("suicidal_progressBar")
        self.gridLayout.addWidget(self.suicidal_progressBar, 6, 3, 1, 1)
        self.pd_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.pd_progressBar.setEnabled(True)
        self.pd_progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.pd_progressBar.setMaximumSize(QtCore.QSize(700, 16777215))
        self.pd_progressBar.setProperty("value", 0)
        self.pd_progressBar.setObjectName("pd_progressBar")
        self.gridLayout.addWidget(self.pd_progressBar, 4, 3, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.account_page)
        self.history_page = QtWidgets.QWidget()
        self.history_page.setStyleSheet("")
        self.history_page.setObjectName("history_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.history_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.history_page)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"        background-color: rgb(245, 245, 255); \n"
"        color: rgb(14, 16, 23);  \n"
"        font: 10pt \"Verdana\";\n"
"    }\n"
"\n"
"QHeaderView::section {\n"
"\n"
"    font: 75 12pt \"Verdana\";\n"
"    background-color: rgb(14, 16, 23);\n"
"    color: rgb(245, 245, 255);\n"
"    \n"
"\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.edit_pushButton = QtWidgets.QPushButton(self.history_page)
        self.edit_pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.edit_pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.edit_pushButton.setFont(font)
        self.edit_pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(245, 245, 255);\n"
"    border : solid 5px ;\n"
"    border-radius: 5px;}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.585, x2:0.995025, y2:0.517, stop:0 rgba(0, 192, 239, 255), stop:1 rgba(173, 65, 255, 255));\n"
"\n"
"}")
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.verticalLayout_7.addWidget(self.edit_pushButton)
        self.stackedWidget.addWidget(self.history_page)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.right_side_menu = QtWidgets.QFrame(self.main_body)
        self.right_side_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.right_side_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.right_side_menu.setStyleSheet("QFrame{\n"
"    border-left:2px solid rgb(14, 16, 23);\n"
"}\n"
"\n"
"QLabel{\n"
"    border: solid 2px rgb(245, 245, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.right_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side_menu.setObjectName("right_side_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.right_side_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.right_side_menu)
        self.label_4.setStyleSheet("background-image: url(:/img/gif-small.gif);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.right_side_menu)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame{\n"
"    background-color: rgb(14, 16, 23);\n"
"    border-top-color: sold 1px rgb(14, 16, 23);\n"
"    border-radius: 0px 0px 5px 5px;\n"
"}")
        self.main_footer.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        MainPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPage)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "MainWindow"))
        self.label_3.setText(_translate("MainPage", "DR. HILL"))
        self.account_pushButton.setText(_translate("MainPage", "ACCOUNT"))
        self.home_pushButton.setText(_translate("MainPage", "HOME"))
        self.history_pushButton.setText(_translate("MainPage", "HISTORY"))
        self.label_2.setText(_translate("MainPage", "Enter the text you want to detect:"))
        self.label.setText(_translate("MainPage", "Account Information:"))
        self.name_label.setText(_translate("MainPage", "Name:"))
        self.name_result_label.setText(_translate("MainPage", "TextLabel"))
        self.surname_label.setText(_translate("MainPage", "Surname:"))
        self.surname_result_label.setText(_translate("MainPage", "TextLabel"))
        self.e_mail_label.setText(_translate("MainPage", "E-Mail:"))
        self.e_mail_result_label.setText(_translate("MainPage", "TextLabel"))
        self.password_label.setText(_translate("MainPage", "Password:"))
        self.password_result_label.setText(_translate("MainPage", "TextLabel"))
        self.logout_pushButton.setText(_translate("MainPage", "   Logout"))
        self.label_18.setText(_translate("MainPage", "Total Result"))
        self.label_13.setText(_translate("MainPage", "Depression"))
        self.label_11.setText(_translate("MainPage", "Anxiety"))
        self.label_16.setText(_translate("MainPage", "Stress"))
        self.label_14.setText(_translate("MainPage", "Normal"))
        self.label_15.setText(_translate("MainPage", "Personality disorder"))
        self.label_17.setText(_translate("MainPage", "Suicidal"))
        self.label_12.setText(_translate("MainPage", "Bipolar"))
        self.edit_pushButton.setText(_translate("MainPage", "Edit"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainPage = QtWidgets.QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(MainPage)
    MainPage.show()
    sys.exit(app.exec_())
