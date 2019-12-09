import sys
from PyQt5.QtWidgets import QApplication
# QCoreApplication包含了事件的主循环，它能添加和删除所有的事件
from PyQt5.QtWidgets import QWidget, QToolTip
# QWidget控件是一个用户界面的基本控件，提供了基本的应用构造器。
from PyQt5.QtWidgets import QPushButton, QMessageBox
#
from PyQt5.QtWidgets import QDesktopWidget
# QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小
# 以上引入了PyQt5.QtWidgets模块的不少组件，这个模块包含了基本的组件。

from PyQt5.QtGui import QIcon, QFont
# 有关图标和字体的设置
from PyQt5.QtCore import QCoreApplication

# 如何用程序关闭一个窗口。这里我们将接触到一点single和slots的知识。


class Example(QWidget):
    # QWidget是UI的基本控件，提供基本的应用构造器。
    # 默认情况下构造器没有父级，没有父级的构造器被称为“窗口”（window）。
    # 这里意味着我们调用两个构造器，一是类本身，二是这个类继承的。

    def __init__(self):
        # super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建了有图标的窗口，并且有提示框和按钮，再实现按钮的功能(Quit)。

        QToolTip.setFont(QFont('SansSerif', 10))  # 设置提示框字体。

        self.setToolTip("This is a <b>Qwidget</b> widget")
        # 调用这个方法创建提示框可以使用富文本格式的内容。

        btn = QPushButton('Button', self)
        # QPushButton(string text, QWidget parent = None)
        # text参数是想要显示的按钮名称，parent参数是放在按钮上的组件，在本例中，这个参数是QWidget。
        # 应用中的组件都是一层一层（继承而来的？）的。
        # 在这个层里，大部分的组件都有自己的父级，没有父级的组件，是顶级的窗口。

        btn.setToolTip("This is a <b>QPushButton</b> widget")
        # 添加了一个按钮，并为其添加了一个提示框。
        btn.resize(btn.sizeHint())
        # 调整按钮大小，sizeHint()方法提供默认大小
        btn.move(50, 50)
        btn.clicked.connect(self.btnTips)
        # 自己写的btnTips弹窗信息框， 连接信号和时间时的方法应该传递地址(即不带"()")

        QuitBtn = QPushButton('Quit', self)
        # QuitBtn.clicked.connect(QCoreApplication.instance().quit)
        # 点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        # 在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        QuitBtn.clicked.connect(self.closeBtn)
        QuitBtn.resize(QuitBtn.sizeHint())
        QuitBtn.move(50, 100)
        # 事件传递系统在PyQt5内建的single和slot机制里面。点击按钮后，信号会被捕捉并给出既定的反应。
        # QCoreApplication包含了事件的主循环，它能添加和删除所有的事件。
        # instance()创建了一个它的实例。QCoreApplication是在QApplication里创建的。

        self.setGeometry(300, 300, 500, 300)  # 前两是位置，后两是大小
        # move(移动放置的位置)和resize(改变控件大小)方法的组合
        self.setWindowTitle("Example")  # SetWindowTitle
        self.setWindowIcon(QIcon('./timg.jpg'))  # SetWindowIcon
        self.center()  # 自己写的使窗口居中的类函数
        self.show()  # 为了让控件显示的方法，在内存创建而后显示器上有所显示。

    def closeEvent(self, event):
        # 如果关闭QWidget，就会产生一个QCloseEvent，
        # 并且把它传入到closeEvent函数的event参数中。
        # 改变控件的默认行为，就是替换掉默认的事件处理。
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        # 创建了一个消息框，上面有俩按钮：Yes和No.
        # 第一个参数是父级窗口，此处self为主窗口QWidget生成的Example
        # 第二个字符串显示在消息框的标题栏，
        # 第三个参数(字符串)显示在对话框，第四个参数是消息框的俩按钮，
        # 最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量reply里。
        if reply == QMessageBox.Yes:
            event.accept()
            # QCoreApplication.instance().quit()
        else:  # == QMessageBox.No
            event.ignore()
        # 判断reply值，如果点击的是Yes按钮，就关闭组件和应用，否则忽略关闭事件。

    # 该事件处理系统建立在 PyQt5 的信号/槽的机制上。如果我们点击该按钮，按钮将会发出信号，
    # 单击信号连接到 quit() 方法使应用程序终止。槽可以是 Qt 的槽也可以是 Python 的任何调用。
    # QCoreApplication 包含主事件循环；它处理和调度所有事件。instance()方法为我们提供了其当前实例。
    # 注意，区分 QCoreApplication 与 QApplication。
    # 发送器和接收器：在通信的两个对象之间进行。发送器是按钮，接收器是应用对象
    # !!整理概念
    # 按钮(btn)是发送器。点击(clicked)按钮后，发出点击信号。点击信号连接(connect)到槽(可以是 Qt 的槽也可以是 Python 的任何调用)。
    # 在我们的例子中是Qt的槽，QCoreApplication处理和调度所有Qt事件，调度出instance（这个实例（接收器））的 quit 事件。

    def closeBtn(self):
        reply = QMessageBox.question(self, "Quit", "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        else:
            pass

    def btnTips(self):
        QMessageBox.information(self, "Btn", "Clicked Btn")

    def center(self):
        qr = self.frameGeometry()
        # 获得主窗口所在的框架。
        cp = QDesktopWidget().availableGeometry().center()
        # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)
        # 把主窗口框架的中心点放置到屏幕的中心位置。
        self.move(qr.topLeft())
        # 把主窗口左上角移动到其框架的左上角，这样就把窗口居中了。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。
    # Python可以在shell里运行，这个参数提供对脚本控制的功能。
    ex = Example()
    # 实例化
    sys.exit(app.exec())
    # 进入应用主循环，事件处理器开始工作。
    # 从窗口接收事件并把事件派送到应用控件。
    # 当调用sys.exit方法或直接销毁主控件时，主循环结束。
    # exit方法确保主循环安全退出。外部环境能通知主控件如何结束
    # 有exec()与exec_() 是因为exec在py中是关键字，方便区分。
