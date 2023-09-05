# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1074, 664)
        MainWindow.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chooseButton = QPushButton(self.centralwidget)
        self.chooseButton.setObjectName(u"chooseButton")
        self.chooseButton.setGeometry(QRect(330, 230, 151, 29))
        self.chooseButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(1, 5, 800, 600))
        self.graphicsView.setMinimumSize(QSize(791, 451))
        self.graphicsView.setStyleSheet(u"background-color: rgb(46, 47, 48);")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(810, 180, 251, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.brightnessSlider = QSlider(self.verticalLayoutWidget)
        self.brightnessSlider.setObjectName(u"brightnessSlider")
        self.brightnessSlider.setStyleSheet(u"")
        self.brightnessSlider.setMinimum(-100)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setOrientation(Qt.Horizontal)
        self.brightnessSlider.setTickPosition(QSlider.NoTicks)
        self.brightnessSlider.setTickInterval(10)

        self.horizontalLayout.addWidget(self.brightnessSlider)

        self.brightnessLabel = QLabel(self.verticalLayoutWidget)
        self.brightnessLabel.setObjectName(u"brightnessLabel")
        self.brightnessLabel.setEnabled(True)
        self.brightnessLabel.setMinimumSize(QSize(30, 25))
        self.brightnessLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 47, 48);")

        self.horizontalLayout.addWidget(self.brightnessLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.contrastSlider = QSlider(self.verticalLayoutWidget)
        self.contrastSlider.setObjectName(u"contrastSlider")
        self.contrastSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.contrastSlider)

        self.contrastLabel = QLabel(self.verticalLayoutWidget)
        self.contrastLabel.setObjectName(u"contrastLabel")
        self.contrastLabel.setMinimumSize(QSize(30, 25))
        self.contrastLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 47, 48);")

        self.horizontalLayout_4.addWidget(self.contrastLabel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(820, 570, 111, 29))
        self.saveButton.setMinimumSize(QSize(0, 25))
        self.saveButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.saveasButton = QPushButton(self.centralwidget)
        self.saveasButton.setObjectName(u"saveasButton")
        self.saveasButton.setGeometry(QRect(930, 570, 121, 29))
        self.saveasButton.setMinimumSize(QSize(0, 25))
        self.saveasButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.changeButton = QPushButton(self.centralwidget)
        self.changeButton.setObjectName(u"changeButton")
        self.changeButton.setGeometry(QRect(820, 540, 231, 29))
        self.changeButton.setMinimumSize(QSize(0, 25))
        self.changeButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(810, 10, 251, 81))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 47, 48);")

        self.verticalLayout_3.addWidget(self.label)

        self.filterBox = QComboBox(self.verticalLayoutWidget_2)
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.setObjectName(u"filterBox")
        self.filterBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 47, 48);")

        self.verticalLayout_3.addWidget(self.filterBox)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(810, 100, 251, 81))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filterSlider = QSlider(self.verticalLayoutWidget_3)
        self.filterSlider.setObjectName(u"filterSlider")
        self.filterSlider.setStyleSheet(u"")
        self.filterSlider.setMinimum(1)
        self.filterSlider.setSingleStep(2)
        self.filterSlider.setPageStep(2)
        self.filterSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.filterSlider)

        self.filterLabel = QLabel(self.verticalLayoutWidget_3)
        self.filterLabel.setObjectName(u"filterLabel")
        self.filterLabel.setMinimumSize(QSize(30, 25))
        self.filterLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 47, 48);")

        self.horizontalLayout_3.addWidget(self.filterLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.applyButton = QPushButton(self.centralwidget)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(820, 500, 111, 29))
        self.applyButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(940, 500, 111, 29))
        self.cancelButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.graphicsView.raise_()
        self.chooseButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.saveButton.raise_()
        self.saveasButton.raise_()
        self.changeButton.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.applyButton.raise_()
        self.cancelButton.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1074, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PicTweek", None))
        self.chooseButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0440\u043a\u043e\u0441\u0442\u044c:", None))
        self.brightnessLabel.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.contrastLabel.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.saveasButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.changeButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0440\u0443\u0433\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.filterBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432", None))
        self.filterBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u042f\u0440\u043a\u043e\u0441\u0442\u044c", None))
        self.filterBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u044b\u0442\u0438\u0435", None))
        self.filterBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0427\u0451\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.filterBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0433\u0430\u0442\u0438\u0432", None))
        self.filterBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u043a\u043e\u0441\u0442\u0438", None))
        self.filterBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u043d\u0438\u0446\u044b \u043e\u0431\u044c\u0435\u043a\u0442\u043e\u0432", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c ...", None))
        self.filterLabel.setText(QCoreApplication.translate("MainWindow", u" 0", None))
        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

