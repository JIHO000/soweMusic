import sys
import os
from PyQt5 import QtWidgets, QtSql
from login import *
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

class loginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = login_MainWindow()
        self.ui.setupUi(self)
        self.openDB()
        self.ui.pushButton.clicked.connect(self.checkUser)
        self.ui.createAccountBtn.clicked.connect(self.createUser)
        loadJsonStyle(self, self.ui, jsonFiles ={"login_style.json"})
        self.show()


    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")
       
        
        print("a")
        if not self.db.open():
            print("Error")
        self.query = QtSql.QSqlQuery()
        self.query.exec_("create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(100) NOT NULL);")
        self.query.exec_("insert into userdata (username, password) values('abc','1234');")

    def checkUser(self):
        username1 = self.ui.lineEdit.text()
        password1 = self.ui.lineEdit_2.text()
        self.query.exec_("select * from userdata where username = '%s' and password = '%s';"%(username1,password1))
        self.query.first()
        if self.query.value("username") != None and self.query.value("password") != None:
            Window = MainWindow()
            self.close()
            Window.show()
        else:
            print("Login failed!")
    
    def createUser(self):
        if self.ui.userIdLine.text() != "" and self.ui.passwordLine.text() == self.ui.confrimPasswordLine.text():
            userId = self.ui.userIdLine.text()
            password = self.ui.passwordLine.text()
            if self.query.exec_("insert into userdata (username, password) values('%s','%s');"%(userId,password)):
                self.ui.loginPages.setCurrentWidget(self.ui.loginPage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = loginWindow()

    Window.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     Window = MainWindow()

#     Window.show()
#     sys.exit(app.exec_())