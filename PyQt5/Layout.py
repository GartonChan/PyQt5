import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QGridLayout, QMessageBox
from PyQt5.QtWidgets import QLineEdit, QTextEdit  # QLineEdit无法跨行，但可以在跨行居中显示
from PyQt5.QtCore import QCoreApplication


class Example_absolute(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel("Zetcode", self)
        lbl1.move(15, 10)

        lbl2 = QLabel("Tutorials", self)
        lbl2.move(35, 40)

        lbl3 = QLabel("for programmers", self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Absolute")
        self.show()


class Example_layout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        # !!

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Buttons")
        self.show()


class Example_gridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for positions, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *positions)
        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()


class Example_feedBack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Name')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        sendButton = QPushButton("Send")
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        # 这个使得全部窗口都退出了！！！


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1, 1, 5)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1, 1, 5)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 5)  # 5, 3 表示跨5行3列
        grid.addWidget(sendButton, 8, 4)
        grid.addWidget(cancelButton, 8, 5)
        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Feedback")
        self.show()
    
    def closeBtn(self):
        reply = QMessageBox.question(self,
                                     "Cancel",
                                     "Are you sure to cancel?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex1 = Example_absolute()
    ex2 = Example_layout()
    ex3 = Example_gridLayout()
    ex4 = Example_feedBack()
    sys.exit(app.exec())