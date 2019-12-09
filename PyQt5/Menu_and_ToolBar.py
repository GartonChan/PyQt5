import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
# QMainWindow提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏。
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QMenu
# 子菜单中使用QMenu创建一个新菜单。
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = self.statusBar()
        self.initUI()

    def initUI(self):
        # self.status_bar = self.statusBar()
        self.status_bar.showMessage("App Ready")
        # 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
        # 第一次调用创建一个状态栏，返回一个状态栏对象。
        # showMessage()方法在状态栏上显示一条信息。

        self.setGeometry(300, 300, 500, 300)
        self.setWindowIcon(QIcon('./timg.jpg'))
        self.setWindowTitle("Test")

        exitAct = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        # QAction是菜单栏、工具栏或者快捷键的动作的组合。
        # 先创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作。

        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # 在已有状态栏基础上，当鼠标悬停在菜单栏的时候，能改变状态栏显示当前状态。

        exitAct.triggered.connect(self.closeBtn)
        # exitAct.triggered.connect(QApplication.quit)
        # 这个事件跟QApplication的quit()行为相关联，上面两条语句等价？
        # 创建了只有一个命令的菜单file-exit，这个命令就是终止应用。
        # 同时也创建(不是，而是原先已有)了一个状态栏。还能使用快捷键Ctrl+Q退出应用。

        authorAct = QAction(QIcon('./icon/info.png'), "Author", self)
        authorAct.triggered.connect(self.authorTips)

        menu_bar = self.menuBar()
        fileMenu = menu_bar.addMenu('&File')
        moreMenu = menu_bar.addMenu('&More')
        # fileMenu.addAction(exitAct)
        # 创建了一个菜单栏，并在上面添加了一个file, more菜单.
        # file关联了点击退出应用的事件。
        newAct = QAction(QIcon('./icon/plus.png'), 'New', self)

        impMenu = QMenu('Import', self)
        # 这里通过QMenu创建子菜单。
        impAct = QAction(QIcon('./icon/book.png'), 'Import mail', self)
        impMenu.addAction(impAct)
        # 后面设置impAct的属性即可完成一定功能(点击与事件连接)。

        fileMenu.addAction(newAct)  # newAct是QAction类，不能addMenu
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)
        # addAction将QAction加入主菜单。
        # addMenu将子菜单加入到主菜单里面。

        moreMenu.addAction(authorAct)

        viewMenu = menu_bar.addMenu("View")  # &View和View当名字的区别在于首字母有无下划线
        viewStatAct = QAction('View statusBar', self, checkable=True)
        viewStatAct.setStatusTip('View statusBar')
        viewStatAct.setChecked(True)  # 默认值为勾选
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)
        # 添加勾选菜单，并对其属性进行设置。

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        # 创建一个文本编辑区，并且放置于QMainWindow中间区域

        tool_bar = self.addToolBar("Exit")
        tool_bar.addAction(exitAct)

        self.show()

    def authorTips(self):
        QMessageBox.information(self, "AuthorInfo", "Author: 圣雄肝帝·猛男·CJT\n"
                                                    "Version: 0.0.1_beta\n"
                                                    "Date: 2019/12/08\n", QMessageBox.Ok)

    def toggleMenu(self, state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()

    def contextMenuEvent(self, event):
        # 使用contextMenuEvent()方法实现这个菜单。

        cMenu = QMenu(self)
        # 右键菜单也叫弹出框（！？），是在某些场合下显示的一组命令。
        # 例如，Opera浏览器里，网页上的右键菜单里会有刷新，返回或者查看页面源代码。
        # 如果在工具栏上右键，会得到一个不同的用来管理工具栏的菜单。

        newAct = cMenu.addAction('New')
        openAct = cMenu.addAction('Open')
        quitAct = cMenu.addAction('Quit')

        action = cMenu.exec(self.mapToGlobal(event.pos()))
        # 使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标
        # 如果右键菜单里触发了事件，也就触发了退出事件，执行关闭菜单行为。
        # 与global对应的有mapToParent
        if action == quitAct:
            qApp.quit()
            # self.closeEvent()

    # 个人体会：Menu 和 toolBar 的关系
    # 可以类比为浏览器中的书签收藏夹(进入里面细选)和书签栏(直接展示具体每一项)
    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     "Cancel",
                                     "Are you sure to cancel?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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
    ex = Example()
    sys.exit(app.exec())
