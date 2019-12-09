import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QLabel, QGridLayout, QPushButton,
                             QSlider, QLCDNumber, QStatusBar,
                             QMainWindow)
from PyQt5.QtCore import QObject, pyqtSignal

# 新的模块： QtCore.Qt、 QtWidgets.QSlider， QtWidgets.QLCDNumber
#           QtCore.QObject，QtCore.pyqtSignal

'''
所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，
当然事件也有其他的产生方式比如网络的连接，窗口管理器或者定时器等。
调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。

在事件模型中，有三个角色：事件源、事件、事件目标
事件源就是发生了状态改变的对象。事件是这个对象状态改变的内容。
事件目标是事件想作用的目标。事件源绑定事件处理函数，然后作用于事件目标身上。

PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。
事件触发的时候，发生一个signal，slot是用来被Python调用的（就是相当于事件的绑定函数）
slot只有在事件触发的时候才能调用。
'''


class Example_SAS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Signal and slot")
        self.show()
    # 显示了QtGui.QLCDNumber和QtGui.QSlider模块，我们能拖动滑块让数字跟着发生改变。
    # sender是信号的发送者，receiver是信号的接收者，slot是对这个信号应该做出的反应。


class Example_EventHandler(QWidget):
    # 在PyQt5中，事件处理器经常被重写（也就是用自己的覆盖库自带的）。
    def __init__(self):
        super(Example_EventHandler, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Event handler")
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


# 这个例子中，我们替换了事件处理器函数keyPressEvent()。
# 按下ESC键程序就会退出。


class Example_EventObject(QWidget):
    # 事件对象是用python来描述一系列的事件自身属性的对象。
    def __init__(self):
        super(Example_EventObject, self).__init__()
        self.text = None
        self.label = None
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)

        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setLayout(grid)

        self.setMouseTracking(True)
        # 事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件。
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Event object")
        self.show()

    def mouseMoveEvent(self, event):
        # event代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。
        # x()和y()方法得到鼠标的x和y坐标点，然后拼成字符串输出到QLabel组件里。
        x = event.x()
        y = event.y()
        self.text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(self.text)
    # 这个示例中，我们在一个组件里显示鼠标的X和Y坐标。
    #  Y坐标显示在QLabel组件里


class Example_EventSender(QMainWindow):
    # 有时候我们会想知道是哪个组件发出了一个信号，
    # PyQt5里的sender()方法能搞定这件事。
    def __init__(self):
        super().__init__()
        # self.status_bar = self.statusBar()
        self.status_bar = QStatusBar(self)
        self.initUI()

    def initUI(self):
        self.status_bar.showMessage("Ready")
        btn1 = QPushButton("Button 1", self)
        btn1.move(50, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        # buttonClicked()方法决定了是哪个按钮能调用sender()方法。
        # 两个按钮都和同一个slot绑定。

        self.setWindowTitle("Event sender")
        self.setGeometry(300, 300, 300, 200)
        self.setStatusBar(self.status_bar)
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.status_bar.showMessage(sender.text() + ' was pressed')
        # 用调用sender()方法的方式决定了事件源。状态栏显示了被点击的按钮。

    # 似乎只有QMainWindow有状态栏
    # 状态栏既可以通过self.StatusBar()生成并展示
    # 也可以通过 self.stB = QStatusBar()生成后再由self.setStatusBar(self.stB)显示（否则显示异常）


class Communicate(QObject):
    closeApp = pyqtSignal()


# 我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发
# 事件与QMainWindow绑定。
# Communicate类创建了一个pyqtSignal()属性的信号。


class Example_EmitSignal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.initUI()

    def initUI(self):
        # self.c = Communicate()
        self.c.closeApp.connect(self.close)
        # closeApp信号QMainWindow的close()方法绑定。
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Emit signal")
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()
        # 点击窗口的时候，发送closeApp信号，程序终止。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex1 = Example_SAS()
    # ex2 = Example_EventHandler()
    # ex3 = Example_EventObject()
    # ex4 = Example_EventSender()
    ex5 = Example_EmitSignal()
    sys.exit(app.exec_())
