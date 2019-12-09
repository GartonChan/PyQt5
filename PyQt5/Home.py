from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QMessageBox,
                             QLineEdit, QGridLayout)
from PyQt5.QtGui import QIcon
import sys

'''
elf.lineEdit.setEchoMode(QLineEdit.Password) 设置密码隐藏
self.lineEdit.setClearButtonEnabled(True) 设置对输入内容的删除提示
self.lineEdit.setFixedSize() 总的设置控件大小
self.lineEdit.setFixedWidth() 设置宽度
self.lineEdit.setFixedHeight() 设置高度
self.lineEdit.setFrame(False) 设置无边框
self.lineEdit.text() 获得文本输入
self.lineEdit.setText() 设置文本
self.lineEdit.clear() 清除输入
self.lineEdit.hide() 设置隐藏
self.lineEdit.show() 设置展示
调用QLineEdit的setPlaceholderText函数即可设置背景文字
'''

id = '圣雄肝帝'
psw = '123456'


class LoginUI(QWidget):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.initUI()

    def initUI(self):
        idLabel = QLabel("ID: ", self)
        pswLabel = QLabel("Psw: ", self)

        self.idText = QLineEdit(self)
        self.idText.setPlaceholderText("Enter your ID")
        self.pswText = QLineEdit(self)
        self.pswText.setPlaceholderText("Enter your Password")
        self.pswText.setEchoMode(QLineEdit.Password)

        loginBtn = QPushButton(QIcon('./icon/user.png'), "Login", self)
        loginBtn.clicked.connect(self.loginTips)
        cancelBtn = QPushButton("Cancel", self)
        cancelBtn.clicked.connect(self.closeBtn)

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        grid.addWidget(idLabel, 1, 0, 1, 1)
        grid.addWidget(self.idText, 1, 1, 1, 5)
        grid.addWidget(pswLabel, 2, 0, 1, 1)
        grid.addWidget(self.pswText, 2, 1, 1, 5)
        grid.addWidget(loginBtn, 3, 4)
        grid.addWidget(cancelBtn, 3, 5)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon('./timg.jpg'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Cancel", "Are you sure to cancel?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def closeBtn(self):
        reply = QMessageBox.question(self, "Cancel", "Are you sure to cancel?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # self.close()
            QApplication.quit()
        else:
            pass

    def loginTips(self):
        if self.idText.text() == id and self.pswText.text() == psw:
            QMessageBox.information(self, "Aloha", "Login successfully", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Error", "Failed to login", QMessageBox.Ok)
        print(self.idText.text(), self.pswText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginUI()
    sys.exit(app.exec())
