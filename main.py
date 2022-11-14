import sys
import os


from soweMusic import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

        self.show()
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightLoginContainer.expandMenu())
        self.ui.loginBtn.clicked.connect(lambda: self.ui.rightLoginContainer.expandMenu())
        self.ui.closeLoginBtn.clicked.connect(lambda: self.ui.rightLoginContainer.collapseMenu())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()

    Window.show()
    sys.exit(app.exec_())