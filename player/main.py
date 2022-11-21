from PySide2.QtWidgets import *
from player import *
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QPalette
from media import CMultiMedia
import sys
import datetime
import pandas as pd


class playerWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.mp = CMultiMedia(self, self.ui.view)
        pal = QPalette()        
        pal.setColor(QPalette.Background, Qt.black)
        self.ui.view.setAutoFillBackground(True);
        self.ui.view.setPalette(pal)
        
        self.ui.vol.setRange(0,100)
        self.ui.vol.setValue(50)

        # play time
        self.duration = ''

        self.ui.btn_add.clicked.connect(self.clickAdd)
        self.ui.btn_del.clicked.connect(self.clickDel)
        self.ui.btn_play.clicked.connect(self.clickPlay)
        self.ui.btn_stop.clicked.connect(self.clickStop)
        self.ui.btn_pause.clicked.connect(self.clickPause)
        self.ui.btn_forward.clicked.connect(self.clickForward)
        self.ui.btn_prev.clicked.connect(self.clickPrev)
 
        self.ui.list.itemDoubleClicked.connect(self.dbClickList)
        self.ui.vol.valueChanged.connect(self.volumeChanged)
        self.ui.bar.sliderMoved.connect(self.barChanged)
        
        data = pd.read_csv('20221119205411.csv')
        files = data["곡"]
        if files.bool:
            cnt = len(files)       
            row = self.ui.list.count()        
            for i in range(row, row+cnt):
                self.ui.list.addItem(files[i-row])
            self.ui.list.setCurrentRow(0)
 
            self.mp.addMedia(files)

    def clickAdd(self):
        # files, ext = QFileDialog.getOpenFileNames(self
        #                                      , 'Select one or more files to open'
        #                                      , ''
        #                                      , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)') 
        print()
 
    def clickDel(self):
        row = self.ui.list.currentRow()
        self.ui.list.takeItem(row)
        self.mp.delMedia(row)
 
    def clickPlay(self):
        index = self.ui.list.currentRow()        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = playerWindow()

    Window.show()
    sys.exit(app.exec_())