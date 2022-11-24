import sys
import os
from PySide2 import QtWidgets, QtSql
from login import *
from soweMusic import *
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QPalette
from media import CMultiMedia
import sys
import datetime
import pandas as pd
from PySide2.QtCore import Signal, Slot
import mlxtend
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QVBoxLayout
from getHtml import *
import ast

class MainWindow(QMainWindow):
    def __init__(self, id, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        
        query = QtSql.QSqlQuery()
        query.exec_("select DISTINCT comboName from playlist")
        while query.next():
            self.ui.comboBox.addItem(query.value(0))
        self.ui.comboBox.setCurrentIndex(0)
        self.layout = QVBoxLayout()
        self.view = QWebEngineView()
        self.layout.addWidget(self.view)
        self.ui.frame_16.setLayout(self.layout)
        self.id=id
        self.ui.tableWidget.setColumnWidth(0,300)
        self.ui.tableWidget.setColumnWidth(1,300)
        self.ui.tableWidget.setColumnWidth(2,300)
        self.ui.tableWidget.setColumnWidth(3,100)
        self.ui.tableWidget.setColumnWidth(4,100)
        self.ui.tableWidget.setColumnWidth(5,100)

        self.ui.tableWidget_2.setColumnWidth(0,300)
        self.ui.tableWidget_2.setColumnWidth(1,300)
        self.ui.tableWidget_2.setColumnWidth(2,300)
        self.ui.tableWidget_2.setColumnWidth(3,100)
        self.ui.tableWidget_2.setColumnWidth(4,100)
        self.ui.tableWidget_2.setColumnWidth(5,100)
        
        self.ui.tableWidget_3.setColumnWidth(0,300)
        self.ui.tableWidget_3.setColumnWidth(1,300)
        self.ui.tableWidget_3.setColumnWidth(2,300)
        self.ui.tableWidget_3.setColumnWidth(3,100)
        self.ui.tableWidget_3.setColumnWidth(4,100)

        self.ui.tableWidget_4.setColumnWidth(0,300)
        self.ui.tableWidget_4.setColumnWidth(1,300)
        self.ui.tableWidget_4.setColumnWidth(2,300)
        self.ui.tableWidget_4.setColumnWidth(3,100)
        self.ui.tableWidget_4.setColumnWidth(4,100)
        self.ui.tableWidget_4.setColumnWidth(5,100)
        

        


        self.ui.settingsBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(
            lambda: self.ui.rightLoginContainer.expandMenu())
        self.ui.loginBtn.clicked.connect(
            lambda: self.ui.rightLoginContainer.expandMenu())
        self.ui.closeLoginBtn.clicked.connect(
            lambda: self.ui.rightLoginContainer.collapseMenu())
      
        
        
        self.mp = CMultiMedia(self, self.ui.view)
        # pal = QPalette()        
        # pal.setColor(QPalette.Background, Qt.black)
        # self.ui.view.setAutoFillBackground(True)
        # self.ui.view.setPalette(pal)
        
        self.ui.vol.setRange(0,100)
        self.ui.vol.setValue(50)

        # play time
        self.duration = ''

        self.ui.btn_play.clicked.connect(self.clickPlay)
        self.ui.btn_stop.clicked.connect(self.clickStop)
        self.ui.btn_pause.clicked.connect(self.clickPause)
        self.ui.btn_forward.clicked.connect(self.clickForward)
        self.ui.btn_prev.clicked.connect(self.clickPrev)
        self.ui.pushButton_3.clicked.connect(self.addfavoritesClicked)
        self.ui.pushButton_2.clicked.connect(self.addPlayListClicked)
        self.ui.list.itemDoubleClicked.connect(self.dbClickList)
        self.ui.vol.valueChanged.connect(self.volumeChanged)
        self.ui.bar.sliderMoved.connect(self.barChanged)
        self.ui.pushButton.clicked.connect(self.addDataCombobox)
        self.ui.pushButton_4.clicked.connect(self.removeDataCombobox)
        self.ui.comboBox.activated[str].connect(self.loadPlayList)
        self.ui.recyclingListBtn.clicked.connect(self.loadPlayList)
        self.ui.recommendListBtn.clicked.connect(self.getRecommendData)
        self.ui.recommendListBtn.clicked.connect(self.loadRecommendList)
        self.ui.pushButton_5.clicked.connect(self.loadYoutube)


        data = pd.read_csv('20221119205411.csv')
        files = data["곡"]
        if files.bool:
            cnt = len(files)       
            row = self.ui.list.count()        
            for i in range(row, row+cnt):
                self.ui.list.addItem(files[i-row])
            self.ui.list.setCurrentRow(0)

            self.mp.addMedia(files)

        
        self.insertData()
        self.loaddata()
        self.loadFavorits()
        self.loadPlayList()
        self.ui.favoritesBtn.clicked.connect(self.loadFavorits)
        self.getApriori()
        self.getRecommendData()
        self.loadRecommendList()

    def clickPlay(self):
        index = self.ui.list.currentRow()   
        self.query.exec_("select song, artist from ranking where id = '%s'"%(index+1))
        self.query.first()
        self.ui.label_9.setText(self.query.value(0))
        self.ui.label_14.setText(self.query.value(1))
        self.mp.playMedia(index)
 
    def clickStop(self):
        self.mp.stopMedia()
 
    def clickPause(self):
        self.mp.pauseMedia()
 
    def clickForward(self):
        cnt = self.ui.list.count()
        curr = self.ui.list.currentRow()
        if curr<cnt-1:
            self.ui.list.setCurrentRow(curr+1)
            self.mp.forwardMedia()
        else:
            self.ui.list.setCurrentRow(0)
            self.mp.forwardMedia(end=True)
 
    def clickPrev(self):
        cnt = self.ui.list.count()
        curr = self.ui.list.currentRow()
        if curr==0:
            self.ui.list.setCurrentRow(cnt-1)    
            self.mp.prevMedia(begin=True)
        else:
            self.ui.list.setCurrentRow(curr-1)    
            self.mp.prevMedia()
 
    def dbClickList(self, item):
        row = self.ui.list.row(item)
        self.query.exec_("select song, artist from ranking where id = '%s'"%(row+1))
        self.query.first()
        self.ui.label_9.setText(self.query.value(0))
        self.ui.label_14.setText(self.query.value(1))
        self.mp.playMedia(row)
 
    def volumeChanged(self, vol):
        self.mp.volumeMedia(vol)
 
    def barChanged(self, pos):   
        print(pos)
        self.mp.posMoveMedia(pos)    
 
    def updateState(self, msg):
        self.ui.state.setText(msg)
 
    def updateBar(self, duration):
        self.ui.bar.setRange(0,duration)    
        self.ui.bar.setSingleStep(int(duration/10))
        self.ui.bar.setPageStep(int(duration/10))
        self.ui.bar.setTickInterval(int(duration/10))
        td = datetime.timedelta(milliseconds=duration)        
        stime = str(td)
        idx = stime.rfind('.')
        self.duration = stime[:idx]
 
    def updatePos(self, pos):
        self.ui.bar.setValue(pos)
        td = datetime.timedelta(milliseconds=pos)
        stime = str(td)
        idx = stime.rfind('.')
        stime = f'{stime[:idx]} / {self.duration}'
        self.ui.playtime.setText(stime)

    # def openDB(self):
    #     self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    #     self.db.setDatabaseName("data.sqlite") 
    #     query = QtSql.QSqlQuery()
    #     query.exec_("create table ranking (id INTEGER PRIMARY KEY NOT NULL, song VARCHAR(100) NOT NULL, artist VARCHAR(100) NOT NULL, album VARCHAR(100) NOT NULL);")
    #     if not self.db.open():
    #         print("Error")
    #     self.query = QtSql.QSqlQuery()

    def insertData(self):
        data = pd.read_csv('20221119205411.csv')

        data['곡'] = data['곡'].str.replace(pat=r"'", repl = r"''", regex=True)
        data['아티스트'] = data['아티스트'].str.replace(pat=r"'", repl = r"''", regex=True)
        data['앨범'] = data['앨범'].str.replace(pat=r"'", repl = r"''", regex=True)
        self.query = QtSql.QSqlQuery()
        
        self.query.exec_("create table ranking (id INTEGER PRIMARY KEY NOT NULL, song VARCHAR(100) NOT NULL, artist VARCHAR(100) NOT NULL, album VARCHAR(100) NOT NULL);")
        self.query.exec_("create table favorits (userId VARCHAR(100), songId VARCHAR(100), PRIMARY KEY(userId, songId));")
        self.query.exec_("create table playlist (id VARCHAR(100) NOT NULL, comboName VARCHAR(100) NOT NULL, userId VARCHAR(100) NOT NULL, songId VARCHAR(100) NOT NULL);")
        
        for index, row in data.iterrows(): 
            self.query.exec_("INSERT INTO ranking (id, song, artist, album) VALUES ('%s','%s','%s','%s');"%(row.랭킹, row.곡, row.아티스트, row.앨범))
        

    def loaddata(self):
        # self.query = QtSql.QSqlQuery()
        self.query.exec_("select * from ranking")
        tablerow=0
        self.ui.tableWidget.setRowCount(100)
        query = QtSql.QSqlQuery()
            

        while self.query.next():
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(self.query.value(1)))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.query.value(2)))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(self.query.value(3)))

            listenButton = QPushButton()
            listenButton.setObjectName(str(tablerow))
            listenButton.clicked.connect(self.listenButtonClicked)
            listenButton.setIcon(QIcon('icons/play-circle.svg'))
            self.ui.tableWidget.setCellWidget(tablerow, 3, listenButton)

            addPlayListBtn = QPushButton()
            addPlayListBtn.setObjectName(str(tablerow))
            addPlayListBtn.clicked.connect(self.addPlayListClicked)
            addPlayListBtn.setIcon(QIcon('icons/folder-plus.svg'))
            self.ui.tableWidget.setCellWidget(tablerow, 4, addPlayListBtn)

            addfavoritesBtn = QPushButton()
            addfavoritesBtn.setCheckable(True)
            addfavoritesBtn.setObjectName(str(tablerow))
            addfavoritesBtn.clicked.connect(self.addfavoritesClicked)
            query.exec_("select count(*) from favorits where userId = '%s' and songId = '%s';"%(self.id, tablerow+1))
            query.first()
            if query.value("count(*)") != 0:
                addfavoritesBtn.setIcon(QIcon('images/4_favorite_full.svg'))
            else:
                addfavoritesBtn.setIcon(QIcon('images/heart.svg'))
                
            self.ui.tableWidget.setCellWidget(tablerow, 5, addfavoritesBtn)
            tablerow+=1

    def loadFavorits(self):
        self.query.exec_("select * from ranking where id in (select songId from favorits where userId = '%s')"%(self.id))
        tablerow=0
        query = QtSql.QSqlQuery()
        query.exec_("select count(*) from ranking where id in (select songId from favorits where userId = '%s')"%(self.id))
        query.first()
        self.ui.tableWidget_2.setRowCount(query.value("count(*)"))
            

        while self.query.next():
            self.ui.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(self.query.value(1)))
            self.ui.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.query.value(2)))
            self.ui.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(self.query.value(3)))

            listenButton = QPushButton()
            listenButton.setObjectName(str(tablerow))
            listenButton.clicked.connect(self.listenButtonClicked)
            listenButton.setIcon(QIcon('icons/play-circle.svg'))
            self.ui.tableWidget_2.setCellWidget(tablerow, 3, listenButton)

            addPlayListBtn = QPushButton()
            addPlayListBtn.setObjectName(str(tablerow))
            addPlayListBtn.clicked.connect(self.addPlayListClicked)
            addPlayListBtn.setIcon(QIcon('icons/folder-plus.svg'))
            self.ui.tableWidget_2.setCellWidget(tablerow, 4, addPlayListBtn)

            addfavoritesBtn = QPushButton()
            addfavoritesBtn.setCheckable(True)
            addfavoritesBtn.setObjectName(str(tablerow))
            addfavoritesBtn.clicked.connect(self.addfavoritesClicked)            
            addfavoritesBtn.setIcon(QIcon('images/4_favorite_full.svg'))
                
            self.ui.tableWidget_2.setCellWidget(tablerow, 5, addfavoritesBtn)
            tablerow+=1    
    
        self.ui.tableWidget.setStyleSheet("QTableView::item:alternate { background-color: #ED1C24; } QTableView::item { background-color: #fff; }")
    
    def loadPlayList(self):
        query = QtSql.QSqlQuery()
        query.exec_("select count(*) from ranking where id in (select songId from playlist where userId = '%s' and comboName = '%s')"%(self.id, self.ui.comboBox.currentText()))
        query.first()
        self.ui.tableWidget_3.setRowCount(query.value("count(*)"))
        self.ui.tableWidget_3.setRowCount(100)
        self.query.exec_("select * from ranking where id in (select songId from playlist where userId = '%s' and comboName = '%s')"%(self.id, self.ui.comboBox.currentText()))
        tablerow=0
        
        query = QtSql.QSqlQuery()
            

        while self.query.next():
            self.ui.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(self.query.value(1)))
            self.ui.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.query.value(2)))
            self.ui.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(self.query.value(3)))

            listenButton = QPushButton()
            listenButton.setObjectName(str(tablerow))
            listenButton.clicked.connect(self.listenButtonClicked)
            listenButton.setIcon(QIcon('icons/play-circle.svg'))
            self.ui.tableWidget_3.setCellWidget(tablerow, 3, listenButton)

            addfavoritesBtn = QPushButton()
            addfavoritesBtn.setCheckable(True)
            addfavoritesBtn.setObjectName(str(tablerow))
            addfavoritesBtn.clicked.connect(self.addfavoritesClicked)
            query.exec_("select count(*) from favorits where userId = '%s' and songId = '%s';"%(self.id, tablerow+1))
            query.first()
            if query.value("count(*)") != 0:
                addfavoritesBtn.setIcon(QIcon('images/4_favorite_full.svg'))
            else:
                addfavoritesBtn.setIcon(QIcon('images/heart.svg'))
                
            self.ui.tableWidget_3.setCellWidget(tablerow, 4, addfavoritesBtn)
            tablerow+=1

    def loadRecommendList(self):
        self.ui.tableWidget_4.setRowCount(len(self.recommend_list))
        tablerow=0
        
        for i in self.recommend_list:
            self.query.exec_("select * from ranking where id = '%s'"%(str(i)))
            query = QtSql.QSqlQuery()
                

            while self.query.next():
                self.ui.tableWidget_4.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(self.query.value(1)))
                self.ui.tableWidget_4.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.query.value(2)))
                self.ui.tableWidget_4.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(self.query.value(3)))

                listenButton = QPushButton()
                listenButton.setObjectName(str(tablerow))
                listenButton.clicked.connect(self.listenButtonClicked)
                listenButton.setIcon(QIcon('icons/play-circle.svg'))
                self.ui.tableWidget_4.setCellWidget(tablerow, 3, listenButton)

                addPlayListBtn = QPushButton()
                addPlayListBtn.setObjectName(str(tablerow))
                addPlayListBtn.clicked.connect(self.addPlayListClicked)
                addPlayListBtn.setIcon(QIcon('icons/folder-plus.svg'))
                self.ui.tableWidget_4.setCellWidget(tablerow, 4, addPlayListBtn)


                addfavoritesBtn = QPushButton()
                addfavoritesBtn.setCheckable(True)
                addfavoritesBtn.setObjectName(str(tablerow))
                addfavoritesBtn.clicked.connect(self.addfavoritesClicked)
                addfavoritesBtn.setIcon(QIcon('images/heart.svg'))
                    
                self.ui.tableWidget_4.setCellWidget(tablerow, 5, addfavoritesBtn)
                tablerow+=1

    def loadYoutube(self):
        createDirectory("html")
        URL = extract_url(self.ui.lineEdit_2.text())
        get_MV(URL, self.ui.lineEdit_2.text())
        
        html_url = "\\html\\%s.html"%(self.ui.lineEdit_2.text())
        self.view.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+html_url))
        


    def listenButtonClicked(self):
        sender = self.sender()
        push_button = self.findChild(QPushButton, sender.objectName())
        print(f'click: {push_button.objectName()}')
        self.ui.mainPages.setCurrentWidget(self.ui.page_10)
        self.mp.playMedia(int(push_button.objectName()))

    def addPlayListClicked(self):
        sender = self.sender()
        push_button = self.findChild(QPushButton, sender.objectName())
        print(f'click: {push_button.objectName()}')
        self.query.exec_("INSERT INTO playlist (id, comboName, userId, songId) VALUES ('%s', '%s', '%s','%s');"%(self.ui.comboBox.currentIndex(),  self.ui.comboBox.currentText(), self.id, int(push_button.objectName())+1))
        print(self.ui.comboBox.currentText(), self.ui.comboBox.currentIndex())
    
    
    def addfavoritesClicked(self):
        sender = self.sender()
        push_button = self.findChild(QPushButton, sender.objectName())
        print(f'click: {push_button.objectName()}')
        if sender.isChecked():
            sender.setIcon(QIcon('images/4_favorite_full.svg'))
            self.query.exec_("INSERT INTO favorits (userId, songId) VALUES ('%s','%s');"%(self.id, int(push_button.objectName())+1))
        else:
            print("aa")
            sender.setIcon(QIcon('images/heart.svg'))
            self.query.exec_("delete from favorits where userId ='%s' and songId = '%s'"%(self.id, int(push_button.objectName())+1))
    
                
       

    def addDataCombobox(self):
        self.ui.comboBox.addItem(self.ui.lineEdit.text())
        self.ui.comboBox.setCurrentText(self.ui.lineEdit.text())
        self.ui.tableWidget_3.clearContents()

    def removeDataCombobox(self):
        self.query.exec_("delete from playlist where userId = '%s' and comboName = '%s'"%(self.id, self.ui.comboBox.currentText()))
        self.ui.comboBox.removeItem(self.ui.comboBox.currentIndex())
        self.ui.tableWidget_3.clearContents()
        self.loadPlayList()

    def getApriori(self):
        # song_list = []
        # for i in range(1,101):
        #     self.query.exec_("select songId from favorits where userId = '%s'"%(i))
        #     user_list = []
        #     while self.query.next():
        #         user_list.append(int(self.query.value(0)))
        #     song_list.append(user_list)

        # data = np.array(song_list)
        # df_data = pd.DataFrame(data)
        # te = TransactionEncoder()
        # te_array = te.fit(data).transform(data)

        # df = pd.DataFrame(te_array, columns=te.columns_)

        # self.apr = apriori(df, min_support=0.05,use_colnames=True)
        print()
        


    def getRecommendData(self):
        self.query.exec_("select songId from favorits where userId ='%s'"%(self.id))
        user_items=[]
        self.recommend_list=[]
        while self.query.next():
            user_items.append(int(self.query.value(0)))
        
        self.query.exec_("select list from apriori order by id DESC;")
        while self.query.next():
            list_data = ast.literal_eval(self.query.value("list"))
            if len(user_items) != 0 and len(list_data) > len(user_items):
                if all(x in list_data for x in user_items):
                    print(list_data)
                    self.recommend_list = list_data.copy()
                    for j in user_items:
                        self.recommend_list.remove(j)
                    break
            if len(list_data) <= 5:
                break

        print(self.recommend_list)       
       
class loginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = login_MainWindow()
        self.ui.setupUi(self)
        self.openDB()
        self.ui.pushButton.clicked.connect(self.checkUser)
        self.ui.createAccountBtn.clicked.connect(self.createUser)
        loadJsonStyle(self, self.ui, jsonFiles={"login_style.json"})
        self.show()
        

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")

        print("a")
        if not self.db.open():
            print("Error")
        self.query = QtSql.QSqlQuery()
        self.query.exec_(
            "create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(100) NOT NULL);")
        self.query.exec_(
            "insert into userdata (username, password) values('abc','1234');")

    def checkUser(self):
        username1 = self.ui.lineEdit.text()
        password1 = self.ui.lineEdit_2.text()
        self.query.exec_(
            "select * from userdata where username = '%s' and password = '%s';" % (username1, password1))
        self.query.first()
        print(self.query.value("id"))
        if self.query.value("username") != None and self.query.value("password") != None:
            Window = MainWindow(self.query.value("id"))
            self.close()
            Window.show()
        else:
            print("Login failed!")

    def createUser(self):
        if self.ui.userIdLine.text() != "" and self.ui.passwordLine.text() == self.ui.confrimPasswordLine.text():
            userId = self.ui.userIdLine.text()
            password = self.ui.passwordLine.text()
            if self.query.exec_("insert into userdata (username, password) values('%s','%s');" % (userId, password)):
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
