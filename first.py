# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("QMainWindow")
        QMainWindow.resize(1123, 801)
        QMainWindow.setStyleSheet("QMainWindow{\n"
                                  "    background:#1D9BC9;\n"
                                  "}\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 190, 93, 28))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    border: 1px solid; /* QPushButton边框的宽度、样式和颜色 */\n"
                                      "    border-radius: 5px; /* 边框圆角 */\n"
                                      "    background-color: #394E56; /* 背景颜色 */\n"
                                      "    color: white; /* 文本颜色 */\n"
                                      "    font-size: 10pt; /* 文本字体大小 */\n"
                                      "}\n"
                                      " \n"
                                      "QPushButton:hover {    /* 鼠标悬浮在QPushButton上时的状态 */\n"
                                      "    background-color: #444444;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      " \n"
                                      "QPushButton:pressed { /* 鼠标按压在QPushButton上时的状态 */\n"
                                      "    background-color: #525252;\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 50, 231, 101))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setStyleSheet("QTextEdit {\n"
                                    "    border: 1px solid;\n"
                                    "    border-radius: 3px; /* 边框圆角 */\n"
                                    "    background-color: #394E56; /* 背景颜色 */\n"
                                    "    color: white; /* 文本颜色 */\n"
                                    "    font-size: 10pt; /* 文本字体大小 */\n"
                                    "}\n"
                                    "")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 190, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    border: 1px solid; /* QPushButton边框的宽度、样式和颜色 */\n"
                                        "    border-radius: 5px; /* 边框圆角 */\n"
                                        "    background-color: #394E56; /* 背景颜色 */\n"
                                        "    color: white; /* 文本颜色 */\n"
                                        "    font-size: 10pt; /* 文本字体大小 */\n"
                                        "}\n"
                                        " \n"
                                        "QPushButton:hover {    /* 鼠标悬浮在QPushButton上时的状态 */\n"
                                        "    background-color: #444444;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        " \n"
                                        "QPushButton:pressed { /* 鼠标按压在QPushButton上时的状态 */\n"
                                        "    background-color: #525252;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QtCore.QRect(580, 10, 531, 311))
        self.textEdit_2.setStyleSheet("QTextEdit {\n"
                                      "    border: 1px solid;\n"
                                      "    border-radius: 3px; /* 边框圆角 */\n"
                                      "    background-color: #394E56; /* 背景颜色 */\n"
                                      "    color: white; /* 文本颜色 */\n"
                                      "    font-size: 10pt; /* 文本字体大小 */\n"
                                      "}\n"
                                      "")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setEnabled(True)
        self.tableView.setGeometry(QtCore.QRect(70, 380, 1001, 391))
        self.tableView.setStyleSheet("QTableWidget{\n"
                                     "color:#DCDCDC;\n"
                                     "background:#1D9BC9;\n"
                                     "border:1px solid #1D9BC9;\n"
                                     "alternate-background-color:#1D9BC9;\n"
                                     "gridline-color:#1D9BC9;\n"
                                     "}\n"
                                     "\n"
                                     "QTableWidget::item:selected{\n"
                                     "color:#1D9BC9;\n"
                                     "background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #1D9BC9,stop:1 #1D9BC9);\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView::section{\n"
                                     "text-align:center;\n"
                                     "background:#1D9BC9;\n"
                                     "padding:3px;\n"
                                     "margin:0px;\n"
                                     "color:#DCDCDC;\n"
                                     "border:1px solid #1D9BC9;\n"
                                     "border-left-width:0;\n"
                                     "}\n"
                                     " \n"
                                     "QScrollBar:vertical{\n"
                                     "background:#1D9BC9;\n"
                                     "padding:0px;\n"
                                     "border-radius:6px;\n"
                                     "max-width:12px;\n"
                                     "}\n"
                                     " \n"
                                     " \n"
                                     "QScrollBar::handle:vertical{\n"
                                     "background:#1D9BC9;\n"
                                     "}\n"
                                     " \n"
                                     "QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
                                     "background:#1D9BC9;\n"
                                     "}\n"
                                     "QScrollBar::sub-page:vertical{\n"
                                     "background:#1D9BC9;\n"
                                     "}\n"
                                     " \n"
                                     " \n"
                                     "QScrollBar::add-page:vertical{\n"
                                     "background:#1D9BC9;\n"
                                     "}\n"
                                     " \n"
                                     "QScrollBar::add-line:vertical{\n"
                                     "background:none;\n"
                                     "}\n"
                                     "QScrollBar::sub-line:vertical{\n"
                                     "background:none;\n"
                                     "}\n"
                                     "")
        self.tableView.setObjectName("tableView")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(80, 340, 241, 31))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(70, 380, 1001, 391))
        self.tableView_2.setStyleSheet("QTableWidget{\n"
                                       "color:#DCDCDC;\n"
                                       "background:#1D9BC9;\n"
                                       "border:1px solid #1D9BC9;\n"
                                       "alternate-background-color:#1D9BC9;\n"
                                       "gridline-color:#1D9BC9;\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget::item:selected{\n"
                                       "color:#1D9BC9;\n"
                                       "background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #1D9BC9,stop:1 #1D9BC9);\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section{\n"
                                       "text-align:center;\n"
                                       "background:#1D9BC9;\n"
                                       "padding:3px;\n"
                                       "margin:0px;\n"
                                       "color:#DCDCDC;\n"
                                       "border:1px solid #1D9BC9;\n"
                                       "border-left-width:0;\n"
                                       "}\n"
                                       " \n"
                                       "QScrollBar:vertical{\n"
                                       "background:#1D9BC9;\n"
                                       "padding:0px;\n"
                                       "border-radius:6px;\n"
                                       "max-width:12px;\n"
                                       "}\n"
                                       " \n"
                                       " \n"
                                       "QScrollBar::handle:vertical{\n"
                                       "background:#1D9BC9;\n"
                                       "}\n"
                                       " \n"
                                       "QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
                                       "background:#1D9BC9;\n"
                                       "}\n"
                                       "QScrollBar::sub-page:vertical{\n"
                                       "background:#1D9BC9;\n"
                                       "}\n"
                                       " \n"
                                       " \n"
                                       "QScrollBar::add-page:vertical{\n"
                                       "background:#1D9BC9;\n"
                                       "}\n"
                                       " \n"
                                       "QScrollBar::add-line:vertical{\n"
                                       "background:none;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical{\n"
                                       "background:none;\n"
                                       "}\n"
                                       "")
        self.tableView_2.setObjectName("tableView_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(680, 330, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("QTextEdit {\n"
                                      "    border: 1px solid;\n"
                                      "    border-radius: 3px; /* 边框圆角 */\n"
                                      "    background-color: #525252; /* 背景颜色 */\n"
                                      "    color: white; /* 文本颜色 */\n"
                                      "    font-size: 10pt; /* 文本字体大小 */\n"
                                      "}\n"
                                      "")
        self.textEdit_3.setObjectName("textEdit_3")
        self.tableView_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.pushButton_2.raise_()
        self.textEdit_2.raise_()
        self.checkBox.raise_()
        self.tableView.raise_()
        self.textEdit_3.raise_()
        QMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)
        self.pushButton_2.clicked.connect(QMainWindow.close)
        self.checkBox.toggled['bool'].connect(self.tableView.setVisible)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "LR(0)语法分析器"))
        self.pushButton.setText(_translate("QMainWindow", "确定"))
        self.label.setText(_translate("QMainWindow", "请输入文法："))
        self.pushButton_2.setText(_translate("QMainWindow", "退出"))
        self.checkBox.setText(_translate("QMainWindow", "LR(0)分析表/字符串分析过程"))
