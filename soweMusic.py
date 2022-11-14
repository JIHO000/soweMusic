# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\UI\sowe\soweMusic.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Custom_Widgets.Widgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    background:transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color:#000;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color:#fff;\n"
"}\n"
"#leftMenuSubContainer{\n"
"    background-color:#F8DE7E;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align:left;\n"
"    padding:5px 10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"#frame_4, #frame_8{\n"
"    background-color:#F8DE7E;\n"
"    border-radius:10px;\n"
"}\n"
"#centerMenuContainer{\n"
"    background-color:#FFE482;\n"
"}\n"
"#headerContainer{\n"
"    background-color:#F8DE7E;\n"
"}\n"
"#headerContainer QPushButton{\n"
"    padding:5px 10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"#rightLoginSubContainer{\n"
"    background-color:#FFE482;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.leftMenuContainer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_3.addWidget(self.menuBtn)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.homeBtn = QtWidgets.QPushButton(self.frame_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_2.addWidget(self.homeBtn)
        self.top100Btn = QtWidgets.QPushButton(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/1_top100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.top100Btn.setIcon(icon2)
        self.top100Btn.setIconSize(QtCore.QSize(24, 24))
        self.top100Btn.setObjectName("top100Btn")
        self.verticalLayout_2.addWidget(self.top100Btn)
        self.recommendListBtn = QtWidgets.QPushButton(self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/2_recommend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recommendListBtn.setIcon(icon3)
        self.recommendListBtn.setIconSize(QtCore.QSize(24, 24))
        self.recommendListBtn.setObjectName("recommendListBtn")
        self.verticalLayout_2.addWidget(self.recommendListBtn)
        self.recyclingListBtn = QtWidgets.QPushButton(self.frame_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/3_mylist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recyclingListBtn.setIcon(icon4)
        self.recyclingListBtn.setIconSize(QtCore.QSize(24, 24))
        self.recyclingListBtn.setObjectName("recyclingListBtn")
        self.verticalLayout_2.addWidget(self.recyclingListBtn)
        self.favoritesBtn = QtWidgets.QPushButton(self.frame_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/4_favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.favoritesBtn.setIcon(icon5)
        self.favoritesBtn.setIconSize(QtCore.QSize(24, 24))
        self.favoritesBtn.setObjectName("favoritesBtn")
        self.verticalLayout_2.addWidget(self.favoritesBtn)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.settingsBtn = QtWidgets.QPushButton(self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/5_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_3.addWidget(self.settingsBtn)
        self.infoBtn = QtWidgets.QPushButton(self.frame_3)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/6_personal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoBtn.setIcon(icon7)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_3.addWidget(self.infoBtn)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.leftMenuSubContainer)
        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, QtCore.Qt.AlignLeft)
        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.centerMenuSubContainer = QtWidgets.QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuSubContainer.setObjectName("centerMenuSubContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.centerMenuSubContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.closeCenterMenuBtn = QtWidgets.QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon8)
        self.closeCenterMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeCenterMenuBtn.setObjectName("closeCenterMenuBtn")
        self.horizontalLayout_5.addWidget(self.closeCenterMenuBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName("centerMenuPages")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.centerMenuPages.addWidget(self.page_2)
        self.verticalLayout_5.addWidget(self.centerMenuPages)
        self.verticalLayout_4.addWidget(self.centerMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.headerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.headerContainer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setMaximumSize(QtCore.QSize(24, 24))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/icons/smsowemusic.png"))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.frame_6 = QtWidgets.QFrame(self.headerContainer)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.moreMenuBtn = QtWidgets.QPushButton(self.frame_6)
        self.moreMenuBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/more-horizontal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QtCore.QSize(24, 24))
        self.moreMenuBtn.setObjectName("moreMenuBtn")
        self.horizontalLayout_9.addWidget(self.moreMenuBtn)
        self.loginBtn = QtWidgets.QPushButton(self.frame_6)
        self.loginBtn.setText("")
        self.loginBtn.setIcon(icon7)
        self.loginBtn.setIconSize(QtCore.QSize(24, 24))
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_9.addWidget(self.loginBtn)
        self.horizontalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.headerContainer)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_7)
        self.minimizeBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon10)
        self.minimizeBtn.setIconSize(QtCore.QSize(24, 24))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_8.addWidget(self.minimizeBtn, 0, QtCore.Qt.AlignLeft)
        self.restoreBtn = QtWidgets.QPushButton(self.frame_7)
        self.restoreBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon11)
        self.restoreBtn.setIconSize(QtCore.QSize(24, 24))
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_8.addWidget(self.restoreBtn, 0, QtCore.Qt.AlignLeft)
        self.closeBtn = QtWidgets.QPushButton(self.frame_7)
        self.closeBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon12)
        self.closeBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_8.addWidget(self.closeBtn, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.headerContainer)
        self.mainBodyContent = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setObjectName("mainBodyContent")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.mainContentsContainer = QtWidgets.QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName("mainContentsContainer")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName("mainPages")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:\\UI\\sowe\\images/sowemusic.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.mainPages.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.page_6)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_9 = QtWidgets.QLabel(self.page_6)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.mainPages.addWidget(self.page_6)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.page_8)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.mainPages.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.page_9)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.mainPages.addWidget(self.page_9)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.page_7)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.mainPages.addWidget(self.page_7)
        self.verticalLayout_8.addWidget(self.mainPages)
        self.horizontalLayout_11.addWidget(self.mainContentsContainer)
        self.rightLoginContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightLoginContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.rightLoginContainer.setObjectName("rightLoginContainer")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.rightLoginContainer)
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.rightLoginSubContainer = QtWidgets.QWidget(self.rightLoginContainer)
        self.rightLoginSubContainer.setObjectName("rightLoginSubContainer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.rightLoginSubContainer)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.rightLoginSubContainer)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_13.addWidget(self.label)
        self.closeLoginBtn = QtWidgets.QPushButton(self.frame_8)
        self.closeLoginBtn.setText("")
        self.closeLoginBtn.setIcon(icon8)
        self.closeLoginBtn.setObjectName("closeLoginBtn")
        self.horizontalLayout_13.addWidget(self.closeLoginBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.loginPages = QCustomStackedWidget(self.rightLoginSubContainer)
        self.loginPages.setObjectName("loginPages")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.loginPages.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.loginPages.addWidget(self.page_4)
        self.verticalLayout_7.addWidget(self.loginPages)
        self.horizontalLayout_12.addWidget(self.rightLoginSubContainer)
        self.horizontalLayout_11.addWidget(self.rightLoginContainer)
        self.verticalLayout_6.addWidget(self.mainBodyContent)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.centerMenuPages.setCurrentIndex(1)
        self.mainPages.setCurrentIndex(0)
        self.loginPages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.menuBtn.setText(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.top100Btn.setToolTip(_translate("MainWindow", "top 100"))
        self.top100Btn.setText(_translate("MainWindow", "top 100"))
        self.recommendListBtn.setToolTip(_translate("MainWindow", "추천 목록"))
        self.recommendListBtn.setText(_translate("MainWindow", "추천 목록"))
        self.recyclingListBtn.setToolTip(_translate("MainWindow", "내 재생목록"))
        self.recyclingListBtn.setText(_translate("MainWindow", "내 재생목록"))
        self.favoritesBtn.setToolTip(_translate("MainWindow", "즐겨찾기"))
        self.favoritesBtn.setText(_translate("MainWindow", "즐겨찾기"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "설정"))
        self.settingsBtn.setText(_translate("MainWindow", "설정"))
        self.infoBtn.setToolTip(_translate("MainWindow", "개인정보"))
        self.infoBtn.setText(_translate("MainWindow", "개인정보"))
        self.label_3.setText(_translate("MainWindow", "More Menu"))
        self.label_4.setText(_translate("MainWindow", "settings"))
        self.label_5.setText(_translate("MainWindow", "info"))
        self.label_8.setText(_translate("MainWindow", "SoWe Music"))
        self.label_9.setText(_translate("MainWindow", "top 100"))
        self.label_11.setText(_translate("MainWindow", "내 재생목록"))
        self.label_12.setText(_translate("MainWindow", "즐겨찾기"))
        self.label_10.setText(_translate("MainWindow", "추천 목록"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "login"))
        self.label_13.setText(_translate("MainWindow", "more"))
from Custom_Widgets.Widgets import QCustomSlideMenu, QCustomStackedWidget
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())