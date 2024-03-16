import sys

from PyQt5.uic.properties import QtWidgets, QtCore

import first
import LR
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QStringListModel


def read(ui):
    global lr
    if ui.label.text() == "请输入文法：":
        str1 = ui.textEdit.toPlainText()  # 读取输入框中文字写入到文件中
        f = open('grammar.txt', 'w')
        f.write(str1)
        f.close()
        lr = LR.main(ui)
        ui.label.setText("请输入要分析的字符串：")
        ui.textEdit.setText("")
        return
    if ui.label.text() == "请输入要分析的字符串：":
        str2 = ui.textEdit.toPlainText()  # 读取输入框中文字写入到文件中
        f = open('string.txt', 'w')
        f.write(str2)
        f.close()
        lr.analyse(ui)
        ui.checkBox.click()
        # ui.label.setText("请输入文法：")
        return


if __name__ == "__main__":
    global lr
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = first.Ui_QMainWindow()
    ui.setupUi(mainWindow)
    ui.pushButton.clicked.connect(lambda: read(ui))  # 连接确认与读取文法
    mainWindow.show()
    sys.exit(app.exec_())
