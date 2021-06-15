# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\desktop2\projects\pyqt5\ScreenShotToDiscord\g.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nothing = QtWidgets.QFrame(self.centralwidget)
        self.nothing.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nothing.setStyleSheet("QPushButton {\n"
"border: none;\n"
"padding: 5px 10px;\n"
"background-color: #f7f7f7;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QFrame {\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"    background-color: rgb(83, 83, 83);\n"
"}")
        self.nothing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nothing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nothing.setObjectName("nothing")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.nothing)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dragFrame = QtWidgets.QFrame(self.nothing)
        self.dragFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dragFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dragFrame.setObjectName("dragFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.dragFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.dragFrame)
        self.label.setStyleSheet("image: url(:/newPrefix/images/discord.png);\n"
"color: gray;\n"
"font-weight:bold;\n"
"padding: 4px;\n"
"min-width: 20px;\n"
"margin-left:5px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.dragFrame)
        self.label_3.setStyleSheet("font-weight:bold;\n"
"color: lightgray;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.dragFrame)
        self.minimize = QtWidgets.QPushButton(self.nothing)
        self.minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize.setStyleSheet("\n"
"QPushButton {\n"
"image: url(:/newPrefix/images/24x24/cil-window-minimize.png);\n"
"\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666666;\n"
"}")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.horizontalLayout.addWidget(self.minimize)
        self.close = QtWidgets.QPushButton(self.nothing)
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("\n"
"QPushButton {\n"
"    image: url(:/newPrefix/images/20x20/cil-x.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: tomato;\n"
"}")
        self.close.setText("")
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.nothing)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"background-color: rgb(102, 102, 102);\n"
"font-size:16px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setStyleSheet("color: #fff;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.AutoClicker = QtWidgets.QWidget()
        self.AutoClicker.setObjectName("AutoClicker")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AutoClicker)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.AutoClicker)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_13 = QtWidgets.QFrame(self.frame_6)
        self.frame_13.setStyleSheet("QFrame {\n"
"background-color: #727272;\n"
"color: #fff;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_5 = QtWidgets.QFrame(self.frame_13)
        self.frame_5.setStyleSheet("color:lightgray;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.errorMsg = QtWidgets.QLabel(self.frame)
        self.errorMsg.setStyleSheet("color: red;")
        self.errorMsg.setText("")
        self.errorMsg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.errorMsg.setObjectName("errorMsg")
        self.horizontalLayout_2.addWidget(self.errorMsg)
        self.verticalLayout_3.addWidget(self.frame)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setStyleSheet("padding: 5px;\n"
"border-radius: 3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_11.addWidget(self.frame_5)
        self.frame_32 = QtWidgets.QFrame(self.frame_13)
        self.frame_32.setStyleSheet("QRadioButton {\n"
"background-color: none;\n"
"}\n"
"")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_15.setContentsMargins(9, 5, 9, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_39 = QtWidgets.QFrame(self.frame_32)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_15.addWidget(self.frame_39)
        self.verticalLayout_11.addWidget(self.frame_32)
        self.frame_23 = QtWidgets.QFrame(self.frame_13)
        self.frame_23.setStyleSheet("QFrame {\n"
"background-color: #727272;\n"
"color: #fff;\n"
"}\n"
"QRadioButton {\n"
"background-color: none;\n"
"}\n"
"")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_22 = QtWidgets.QFrame(self.frame_23)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.frame_22)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_36 = QtWidgets.QFrame(self.frame_3)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_28 = QtWidgets.QFrame(self.frame_36)
        self.frame_28.setStyleSheet("color:lightgray;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_14.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_37 = QtWidgets.QFrame(self.frame_28)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_37)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.hrs = QtWidgets.QSpinBox(self.frame_37)
        self.hrs.setObjectName("hrs")
        self.verticalLayout_5.addWidget(self.hrs)
        self.horizontalLayout_14.addWidget(self.frame_37)
        self.frame_16 = QtWidgets.QFrame(self.frame_28)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.frame_16)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.mins = QtWidgets.QSpinBox(self.frame_16)
        self.mins.setMaximum(60)
        self.mins.setObjectName("mins")
        self.verticalLayout_4.addWidget(self.mins)
        self.horizontalLayout_14.addWidget(self.frame_16)
        self.horizontalLayout_19.addWidget(self.frame_28)
        self.horizontalLayout_17.addWidget(self.frame_36)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_22)
        self.textBrowser.setStyleSheet("font-size: 8px;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_8.addWidget(self.textBrowser)
        self.frame_34 = QtWidgets.QFrame(self.frame_22)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_35 = QtWidgets.QFrame(self.frame_34)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.stopBtn = QtWidgets.QPushButton(self.frame_35)
        self.stopBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopBtn.setStyleSheet("QPushButton {\n"
"    image: url(:/newPrefix/images/24x24/cil-media-stop.png);\n"
"background-color:#ff6f6f;\n"
"padding:5px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#ff4c4c;\n"
"}")
        self.stopBtn.setText("")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_18.addWidget(self.stopBtn)
        self.startBtn = QtWidgets.QPushButton(self.frame_35)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startBtn.setStyleSheet("QPushButton {\n"
"image: url(:/newPrefix/images/24x24/cil-media-play.png);\n"
"background-color: #84c184;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #66b266;\n"
"}")
        self.startBtn.setText("")
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_18.addWidget(self.startBtn)
        self.horizontalLayout_12.addWidget(self.frame_35)
        self.verticalLayout_8.addWidget(self.frame_34)
        self.verticalLayout_8.setStretch(1, 1)
        self.horizontalLayout_7.addWidget(self.frame_22)
        self.frame_19 = QtWidgets.QFrame(self.frame_23)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_40 = QtWidgets.QFrame(self.frame_19)
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.frame_40)
        self.label_6.setStyleSheet("color: lightgray;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.mouseLastUpdate = QtWidgets.QLabel(self.frame_40)
        self.mouseLastUpdate.setStyleSheet("font-size: 10px;\n"
"color: lightgray;")
        self.mouseLastUpdate.setObjectName("mouseLastUpdate")
        self.horizontalLayout_10.addWidget(self.mouseLastUpdate, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_15.addWidget(self.frame_40)
        self.mouseList = QtWidgets.QListWidget(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.mouseList.setFont(font)
        self.mouseList.setStyleSheet("background-color: rgba(148, 148, 148, 102);\n"
"border-radius:3px;\n"
"padding:5px;\n"
"font-size: 10px;")
        self.mouseList.setObjectName("mouseList")
        self.verticalLayout_15.addWidget(self.mouseList)
        self.progressBar = QtWidgets.QProgressBar(self.frame_19)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"font-size: 1px;\n"
"color: rgba(0,0,0,0.1);\n"
"min-height: 2px;\n"
"max-height: 2px;\n"
"\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_15.addWidget(self.progressBar)
        self.horizontalLayout_7.addWidget(self.frame_19)
        self.horizontalLayout_7.setStretch(0, 20)
        self.horizontalLayout_7.setStretch(1, 60)
        self.verticalLayout_11.addWidget(self.frame_23)
        self.horizontalLayout_6.addWidget(self.frame_13)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.AutoClicker)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bar = QtWidgets.QProgressBar(self.frame_4)
        self.bar.setStyleSheet("font-size: 1px;")
        self.bar.setProperty("value", 24)
        self.bar.setObjectName("bar")
        self.horizontalLayout_3.addWidget(self.bar)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addWidget(self.frame_11)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screen Shot To Discord"))
        self.label_3.setText(_translate("MainWindow", "Screen Shot to Discord"))
        self.label_4.setText(_translate("MainWindow", "Discord Webhook URL"))
        self.label_9.setText(_translate("MainWindow", "Hour(s)"))
        self.label_10.setText(_translate("MainWindow", "Min(s)"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\"><br />The webhook url will be saved in a json file and accessed next time the app is opened. </span><span style=\" font-size:16px; font-style:italic;\"><br /><br />The app will test the URLs validity and notify you if the URL is incorrect. </span><span style=\" font-size:16px;\"><br /><br />According to the interval set the app will send an image to your Discord channel when the progress bar hits zero.</span></p></body></html>"))
        self.stopBtn.setToolTip(_translate("MainWindow", "Stop Auto Clicker!"))
        self.startBtn.setToolTip(_translate("MainWindow", "Start Auto Clicker!"))
        self.label_6.setText(_translate("MainWindow", "Screen Shot Log"))
        self.mouseLastUpdate.setText(_translate("MainWindow", "            00:00:00 am"))
import resources_rc