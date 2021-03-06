# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock_app_6.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QTimer, QTime, Qt, pyqtSignal, QDate
from KClass.Custom_Bar import Progress_Bar

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(732, 683)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.appTab = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appTab.sizePolicy().hasHeightForWidth())
        self.appTab.setSizePolicy(sizePolicy)
        self.appTab.setObjectName("appTab")
        self.clockTab = QtWidgets.QWidget()
        self.clockTab.setObjectName("clockTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.clockTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.clockLabel = QtWidgets.QLabel(self.clockTab)
        font = QtGui.QFont()
        font.setPointSize(85)
        self.clockLabel.setFont(font)
        self.clockLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.clockLabel.setObjectName("clockLabel")
        self.verticalLayout_8.addWidget(self.clockLabel)
        self.mainGroupBox = QtWidgets.QGroupBox(self.clockTab)
        self.mainGroupBox.setTitle("")
        self.mainGroupBox.setObjectName("mainGroupBox")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.mainGroupBox)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mainStopwatchLabel = QtWidgets.QLabel(self.mainGroupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mainStopwatchLabel.setFont(font)
        self.mainStopwatchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainStopwatchLabel.setObjectName("mainStopwatchLabel")
        self.horizontalLayout_5.addWidget(self.mainStopwatchLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.mainStopwatchStart = QtWidgets.QPushButton(self.mainGroupBox)
        self.mainStopwatchStart.setObjectName("mainStopwatchStart")
        self.horizontalLayout_5.addWidget(self.mainStopwatchStart)
        self.mainStopwatchStop = QtWidgets.QPushButton(self.mainGroupBox)
        self.mainStopwatchStop.setObjectName("mainStopwatchStop")
        self.horizontalLayout_5.addWidget(self.mainStopwatchStop)
        self.mainStopwatchReset = QtWidgets.QPushButton(self.mainGroupBox)
        self.mainStopwatchReset.setObjectName("mainStopwatchReset")
        self.horizontalLayout_5.addWidget(self.mainStopwatchReset)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 25, -1, 25)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        #########################################
        self.prog_Stopwatch = Progress_Bar(
            colors=["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43",
                    "#d53e4f", "#9e0142"],
            gaps=True)

        self.prog_Stopwatch.setBarPadding(10)
        self.prog_Stopwatch.setBarSolidPercent(0.9)
        self.prog_Stopwatch.setBackgroundColor('#eaeaea')
        self.prog_Stopwatch.setValue(0)
        self.prog_Stopwatch.disableDrag()
        ##################################################

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prog_Stopwatch.sizePolicy().hasHeightForWidth())
        self.prog_Stopwatch.setSizePolicy(sizePolicy)
        self.prog_Stopwatch.setMinimumSize(QtCore.QSize(0, 50))
        self.prog_Stopwatch.setObjectName("prog_Stopwatch")
        self.horizontalLayout_10.addWidget(self.prog_Stopwatch)
        self.mainStopwatchTime = QtWidgets.QLabel(self.mainGroupBox)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mainStopwatchTime.setFont(font)
        self.mainStopwatchTime.setObjectName("mainStopwatchTime")
        self.horizontalLayout_10.addWidget(self.mainStopwatchTime)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_7 = QtWidgets.QLabel(self.mainGroupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_22.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.mainDoneButton = QtWidgets.QPushButton(self.mainGroupBox)
        self.mainDoneButton.setObjectName("mainDoneButton")
        self.horizontalLayout_22.addWidget(self.mainDoneButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_22)
        self.mainListView = QtWidgets.QListView(self.mainGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainListView.sizePolicy().hasHeightForWidth())
        self.mainListView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mainListView.setFont(font)
        self.mainListView.setAutoScrollMargin(5)
        self.mainListView.setResizeMode(QtWidgets.QListView.Adjust)
        self.mainListView.setUniformItemSizes(False)
        self.mainListView.setBatchSize(50)
        self.mainListView.setObjectName("mainListView")
        self.verticalLayout_11.addWidget(self.mainListView)
        self.horizontalLayout_21.addLayout(self.verticalLayout_11)
        self.verticalLayout_8.addWidget(self.mainGroupBox)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.appTab.addTab(self.clockTab, "")
        self.stopwatchTab = QtWidgets.QWidget()
        self.stopwatchTab.setObjectName("stopwatchTab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.stopwatchTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addHourButton = QtWidgets.QPushButton(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addHourButton.sizePolicy().hasHeightForWidth())
        self.addHourButton.setSizePolicy(sizePolicy)
        self.addHourButton.setMinimumSize(QtCore.QSize(80, 80))
        self.addHourButton.setText("")
        self.addHourButton.setObjectName("addHourButton")
        self.horizontalLayout_7.addWidget(self.addHourButton)
        self.addMinuteButton = QtWidgets.QPushButton(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addMinuteButton.sizePolicy().hasHeightForWidth())
        self.addMinuteButton.setSizePolicy(sizePolicy)
        self.addMinuteButton.setMinimumSize(QtCore.QSize(80, 80))
        self.addMinuteButton.setText("")
        self.addMinuteButton.setObjectName("addMinuteButton")
        self.horizontalLayout_7.addWidget(self.addMinuteButton)
        self.addSecondButton = QtWidgets.QPushButton(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSecondButton.sizePolicy().hasHeightForWidth())
        self.addSecondButton.setSizePolicy(sizePolicy)
        self.addSecondButton.setMinimumSize(QtCore.QSize(80, 80))
        self.addSecondButton.setText("")
        self.addSecondButton.setObjectName("addSecondButton")
        self.horizontalLayout_7.addWidget(self.addSecondButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.lblStopwatchHour = QtWidgets.QLabel(self.stopwatchTab)
        font = QtGui.QFont()
        font.setPointSize(85)
        self.lblStopwatchHour.setFont(font)
        self.lblStopwatchHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStopwatchHour.setObjectName("lblStopwatchHour")
        self.horizontalLayout_13.addWidget(self.lblStopwatchHour)
        self.stopwatchColon = QtWidgets.QLabel(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatchColon.sizePolicy().hasHeightForWidth())
        self.stopwatchColon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.stopwatchColon.setFont(font)
        self.stopwatchColon.setAlignment(QtCore.Qt.AlignCenter)
        self.stopwatchColon.setObjectName("stopwatchColon")
        self.horizontalLayout_13.addWidget(self.stopwatchColon)
        self.lblStopwatchMnt = QtWidgets.QLabel(self.stopwatchTab)
        font = QtGui.QFont()
        font.setPointSize(85)
        self.lblStopwatchMnt.setFont(font)
        self.lblStopwatchMnt.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStopwatchMnt.setObjectName("lblStopwatchMnt")
        self.horizontalLayout_13.addWidget(self.lblStopwatchMnt)
        self.stopwatchColon_1 = QtWidgets.QLabel(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatchColon_1.sizePolicy().hasHeightForWidth())
        self.stopwatchColon_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.stopwatchColon_1.setFont(font)
        self.stopwatchColon_1.setAlignment(QtCore.Qt.AlignCenter)
        self.stopwatchColon_1.setObjectName("stopwatchColon_1")
        self.horizontalLayout_13.addWidget(self.stopwatchColon_1)
        self.lblStopwatchSec = QtWidgets.QLabel(self.stopwatchTab)
        font = QtGui.QFont()
        font.setPointSize(85)
        self.lblStopwatchSec.setFont(font)
        self.lblStopwatchSec.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStopwatchSec.setObjectName("lblStopwatchSec")
        self.horizontalLayout_13.addWidget(self.lblStopwatchSec)
        spacerItem5 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.takeHourButton = QtWidgets.QPushButton(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeHourButton.sizePolicy().hasHeightForWidth())
        self.takeHourButton.setSizePolicy(sizePolicy)
        self.takeHourButton.setMinimumSize(QtCore.QSize(80, 80))
        self.takeHourButton.setText("")
        self.takeHourButton.setObjectName("takeHourButton")
        self.horizontalLayout_6.addWidget(self.takeHourButton)
        self.takeMinuteButton = QtWidgets.QPushButton(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeMinuteButton.sizePolicy().hasHeightForWidth())
        self.takeMinuteButton.setSizePolicy(sizePolicy)
        self.takeMinuteButton.setMinimumSize(QtCore.QSize(80, 80))
        self.takeMinuteButton.setText("")
        self.takeMinuteButton.setObjectName("takeMinuteButton")
        self.horizontalLayout_6.addWidget(self.takeMinuteButton)
        self.takeSecondButton = QtWidgets.QPushButton(self.stopwatchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeSecondButton.sizePolicy().hasHeightForWidth())
        self.takeSecondButton.setSizePolicy(sizePolicy)
        self.takeSecondButton.setMinimumSize(QtCore.QSize(80, 80))
        self.takeSecondButton.setText("")
        self.takeSecondButton.setObjectName("takeSecondButton")
        self.horizontalLayout_6.addWidget(self.takeSecondButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.startStopwatchButton = QtWidgets.QPushButton(self.stopwatchTab)
        self.startStopwatchButton.setObjectName("startStopwatchButton")
        self.horizontalLayout_20.addWidget(self.startStopwatchButton)
        self.stopStopwatchButton = QtWidgets.QPushButton(self.stopwatchTab)
        self.stopStopwatchButton.setObjectName("stopStopwatchButton")
        self.horizontalLayout_20.addWidget(self.stopStopwatchButton)
        self.resetStopwatchButton = QtWidgets.QPushButton(self.stopwatchTab)
        self.resetStopwatchButton.setObjectName("resetStopwatchButton")
        self.horizontalLayout_20.addWidget(self.resetStopwatchButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.appTab.addTab(self.stopwatchTab, "")
        self.toDoTab = QtWidgets.QWidget()
        self.toDoTab.setObjectName("toDoTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.toDoTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toDoListView = QtWidgets.QListView(self.toDoTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toDoListView.setFont(font)
        self.toDoListView.setAlternatingRowColors(True)
        self.toDoListView.setObjectName("toDoListView")
        self.verticalLayout_2.addWidget(self.toDoListView)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.toDoLabel = QtWidgets.QLabel(self.toDoTab)
        self.toDoLabel.setObjectName("toDoLabel")
        self.horizontalLayout_18.addWidget(self.toDoLabel)
        self.toDoLineEdit = QtWidgets.QLineEdit(self.toDoTab)
        self.toDoLineEdit.setObjectName("toDoLineEdit")
        self.horizontalLayout_18.addWidget(self.toDoLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.toDoAddButton = QtWidgets.QPushButton(self.toDoTab)
        self.toDoAddButton.setObjectName("toDoAddButton")
        self.horizontalLayout_2.addWidget(self.toDoAddButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.toDoRemoveButton = QtWidgets.QPushButton(self.toDoTab)
        self.toDoRemoveButton.setObjectName("toDoRemoveButton")
        self.horizontalLayout_2.addWidget(self.toDoRemoveButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.appTab.addTab(self.toDoTab, "")
        self.memoTab = QtWidgets.QWidget()
        self.memoTab.setObjectName("memoTab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.memoTab)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.memoListTab = QtWidgets.QTabWidget(self.memoTab)
        self.memoListTab.setObjectName("memoListTab")
        self.memoListTab_1 = QtWidgets.QWidget()
        self.memoListTab_1.setObjectName("memoListTab_1")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.memoListTab_1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.memoTextEdit_1 = QtWidgets.QTextEdit(self.memoListTab_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.memoTextEdit_1.setFont(font)
        self.memoTextEdit_1.setObjectName("memoTextEdit_1")
        self.horizontalLayout_23.addWidget(self.memoTextEdit_1)
        self.memoListTab.addTab(self.memoListTab_1, "")
        self.memoListTab_2 = QtWidgets.QWidget()
        self.memoListTab_2.setObjectName("memoListTab_2")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.memoListTab_2)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.memoTextEdit_2 = QtWidgets.QTextEdit(self.memoListTab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.memoTextEdit_2.setFont(font)
        self.memoTextEdit_2.setObjectName("memoTextEdit_2")
        self.horizontalLayout_25.addWidget(self.memoTextEdit_2)
        self.memoListTab.addTab(self.memoListTab_2, "")
        self.verticalLayout_5.addWidget(self.memoListTab)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.addMemoButton = QtWidgets.QPushButton(self.memoTab)
        self.addMemoButton.setObjectName("addMemoButton")
        self.horizontalLayout_9.addWidget(self.addMemoButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.removeMemoButton = QtWidgets.QPushButton(self.memoTab)
        self.removeMemoButton.setObjectName("removeMemoButton")
        self.horizontalLayout_9.addWidget(self.removeMemoButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.appTab.addTab(self.memoTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.appTab.addTab(self.settingTab, "")
        self.verticalLayout_4.addWidget(self.appTab)

        ##################################################################
        self.clockLabel.setMargin(30)
        # Stopwatch Display setting and Signal and Slots
        self.addHourButton.setIcon(QIcon("arrow_up.png"))
        self.addHourButton.setIconSize(QSize(80, 80))
        self.addHourButton.setStyleSheet("QPushButton{background:transparent;}")
        self.addHourButton.pressed.connect(lambda: self.pressed_up(self.addHourButton))
        self.addHourButton.released.connect(lambda: [self.released_up(self.addHourButton),
                                                     self.addTime(self.addHourButton)])
        self.addMinuteButton.setIcon(QIcon("arrow_up.png"))
        self.addMinuteButton.setIconSize(QSize(80, 80))
        self.addMinuteButton.setStyleSheet("QPushButton{background:transparent;}")
        self.addMinuteButton.pressed.connect(lambda: self.pressed_up(self.addMinuteButton))
        self.addMinuteButton.released.connect(lambda: [self.released_up(self.addMinuteButton),
                                                       self.addTime(self.addMinuteButton)])
        self.addSecondButton.setIcon(QIcon("arrow_up.png"))
        self.addSecondButton.setIconSize(QSize(80, 80))
        self.addSecondButton.setStyleSheet("QPushButton{background:transparent;}")
        self.addSecondButton.pressed.connect(lambda: self.pressed_up(self.addSecondButton))
        self.addSecondButton.released.connect(lambda: [self.released_up(self.addSecondButton),
                                                       self.addTime(self.addSecondButton)])
        self.takeHourButton.setIcon(QIcon("arrow_down.png"))
        self.takeHourButton.setIconSize(QSize(80, 80))
        self.takeHourButton.setStyleSheet("QPushButton{background:transparent;}")
        self.takeHourButton.pressed.connect(lambda: self.pressed_down(self.takeHourButton))
        self.takeHourButton.released.connect(lambda: [self.released_down(self.takeHourButton),
                                                      self.takeTime(self.takeHourButton)])
        self.takeMinuteButton.setIcon(QIcon("arrow_down.png"))
        self.takeMinuteButton.setIconSize(QSize(80, 80))
        self.takeMinuteButton.setStyleSheet("QPushButton{background:transparent;}")
        self.takeMinuteButton.pressed.connect(lambda: self.pressed_down(self.takeMinuteButton))
        self.takeMinuteButton.released.connect(lambda: [self.released_down(self.takeMinuteButton),
                                                        self.takeTime(self.takeMinuteButton)])
        self.takeSecondButton.setIcon(QIcon("arrow_down.png"))
        self.takeSecondButton.setIconSize(QSize(80, 80))
        self.takeSecondButton.setStyleSheet("QPushButton{background:transparent;}")
        self.takeSecondButton.pressed.connect(lambda: self.pressed_down(self.takeSecondButton))
        self.takeSecondButton.released.connect(lambda: [self.released_down(self.takeSecondButton),
                                                        self.takeTime(self.takeSecondButton)])

        # Clock setting
        timer_clock = QTimer(self)
        # timer_clock.timeout.connect(lambda: self.displayTime(self.lblStopwatchHour))
        timer_clock.timeout.connect(lambda: self.displayTime(self.clockLabel))
        timer_clock.start(1000)

        # Stopwatch Setting
        self.timer_stopwatch = QTimer(self)
        self.stopwatch = QTime(1, 0, 0)
        self.stopwatch_resetTime = QTime(0, 0, 0)
        self.timer_max = QTime(1, 0, 0)
        self.prog_Stopwatch.setLimit(3600, 0)
        self.prog_Stopwatch.setValue(3600)
        self.lastCalled = QTime.currentTime()
        self.resetOn = True

        # Model??????
        self.model = QtCore.QStringListModel()
        self.model.setStringList(['aaa', 'bbb', 'ccc'])
        self.toDoListView.setModel(self.model)
        self.mainListView.setModel(self.model)
        self.toDoSelectedLineIndex = None

        # To Do Signal-Slot??????
        self.toDoAddButton.clicked.connect(self.addList)
        self.toDoLineEdit.returnPressed.connect(self.addList)
        self.toDoListView.clicked.connect(self.listClicked)
        self.toDoRemoveButton.clicked.connect(self.removeList)
        self.mainListView.clicked.connect(self.listClicked)
        self.mainDoneButton.clicked.connect(self.removeList)

        # Timer Sginal and Slot
        self.timer_stopwatch.timeout.connect(self.displayStopwatchTime)
        self.startStopwatchButton.clicked.connect(self.startStopwatch)
        self.stopStopwatchButton.clicked.connect(self.stopStopwatch)
        self.resetStopwatchButton.clicked.connect(self.resetStopwatch)
        self.mainStopwatchStart.clicked.connect(self.startStopwatch)
        self.mainStopwatchStop.clicked.connect(self.stopStopwatch)
        self.mainStopwatchReset.clicked.connect(self.resetStopwatch)
        self.prog_Stopwatch.clickedValue.connect(self.progressChanged)

        # Memo Signal and Slot
        self.addMemoButton.clicked.connect(self.addMomoTab)
        self.removeMemoButton.clicked.connect(self.removeTab)

        # Memo Tab
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.memoListTab.addTab(self.tab_8, "")
        # self.memoListTab.removeTab(self.memoListTab.indexOf(self.tab_8))

        self.retranslateUi(Form)
        self.appTab.setCurrentIndex(3)
        self.memoListTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clockLabel.setText(_translate("Form", "00:00:00"))
        self.mainStopwatchLabel.setText(_translate("Form", "StopWatch"))
        self.mainStopwatchStart.setText(_translate("Form", "Start"))
        self.mainStopwatchStop.setText(_translate("Form", "Stop"))
        self.mainStopwatchReset.setText(_translate("Form", "Reset"))
        self.mainStopwatchTime.setText(_translate("Form", "00:00:00"))
        self.label_7.setText(_translate("Form", "To Do"))
        self.mainDoneButton.setText(_translate("Form", "Done"))
        self.appTab.setTabText(self.appTab.indexOf(self.clockTab), _translate("Form", "Clock"))
        self.lblStopwatchHour.setText(_translate("Form", "00"))
        self.stopwatchColon.setText(_translate("Form", ":"))
        self.lblStopwatchMnt.setText(_translate("Form", "00"))
        self.stopwatchColon_1.setText(_translate("Form", ":"))
        self.lblStopwatchSec.setText(_translate("Form", "00"))
        self.startStopwatchButton.setText(_translate("Form", "Start"))
        self.stopStopwatchButton.setText(_translate("Form", "Stop"))
        self.resetStopwatchButton.setText(_translate("Form", "Reset"))
        self.appTab.setTabText(self.appTab.indexOf(self.stopwatchTab), _translate("Form", "Stopwatch"))
        self.toDoLabel.setText(_translate("Form", "ToDo"))
        self.toDoAddButton.setText(_translate("Form", "Add"))
        self.toDoRemoveButton.setText(_translate("Form", "Remove"))
        self.appTab.setTabText(self.appTab.indexOf(self.toDoTab), _translate("Form", "To Do"))
        self.memoListTab.setTabText(self.memoListTab.indexOf(self.memoListTab_1), _translate("Form", "Memo 1"))
        self.memoListTab.setTabText(self.memoListTab.indexOf(self.memoListTab_2), _translate("Form", "Memo 2"))
        self.addMemoButton.setText(_translate("Form", "Add"))
        self.removeMemoButton.setText(_translate("Form", "Remove"))
        self.appTab.setTabText(self.appTab.indexOf(self.memoTab), _translate("Form", "Memo"))
        self.appTab.setTabText(self.appTab.indexOf(self.settingTab), _translate("Form", "Setting"))

    def pressed_up(self, obj):
        obj.setIcon(QIcon("arrow_up_pressed.png"))

    def released_up(self, obj):
        obj.setIcon(QIcon("arrow_up.png"))

    def pressed_down(self, obj):
        obj.setIcon(QIcon("arrow_down_pressed.png"))

    def released_down(self, obj):
        obj.setIcon(QIcon("arrow_down.png"))

    def displayTime(self, label):
        currentTime = QTime.currentTime()

        displayText = currentTime.toString("hh:mm:ss")
        # print(displayText)

        label.setText(displayText)

    def displayStopwatchTime(self):
        if self.stopwatch == QTime(0, 0, 0):
            self.resetStopwatch()
            return
        if self.timer_stopwatch.isActive():
            if self.lastCalled.secsTo(QTime.currentTime()):
                self.stopwatch = self.stopwatch.addSecs(-1)
                self.lastCalled = QTime.currentTime()

        self.lblStopwatchHour.setText(self.stopwatch.toString("hh"))
        self.lblStopwatchMnt.setText(self.stopwatch.toString("mm"))
        self.lblStopwatchSec.setText(self.stopwatch.toString("ss"))
        self.mainStopwatchTime.setText(self.stopwatch.toString("hh:mm:ss"))

        secs = QTime(0, 0, 0).secsTo(self.stopwatch)
        self.prog_Stopwatch.setValue(secs)

    def startStopwatch(self):
        print("Start")
        secs = QTime(0, 0, 0).secsTo(self.stopwatch)
        if self.resetOn:
            self.timer_max = self.stopwatch
            self.prog_Stopwatch.setLimit(secs, 0)
            self.resetOn = False
        self.prog_Stopwatch.setValue(secs)
        self.timer_stopwatch.start(1000)

    def stopStopwatch(self):
        self.timer_stopwatch.stop()

    def resetStopwatch(self):
        self.stopStopwatch()
        self.stopwatch = self.stopwatch_resetTime
        self.mainStopwatchTime.setText("00:00:00")
        self.lblStopwatchHour.setText("00")
        self.lblStopwatchMnt.setText("00")
        self.lblStopwatchSec.setText("00")
        # self.timer_max = QTime(0,0,0)
        self.prog_Stopwatch.setValue(0)
        print("reset")
        self.resetOn = True

    def addTime(self, button):
        if button == self.addHourButton:
            self.stopwatch = self.stopwatch.addSecs(3600)
            # self.lblStopwatchHour.setText(self.stopwatch.toString("hh"))

        elif button == self.addMinuteButton:
            self.stopwatch = self.stopwatch.addSecs(60)
            # self.lblStopwatchMnt.setText(self.stopwatch.toString("mm"))
        elif button == self.addSecondButton:
            self.stopwatch = self.stopwatch.addSecs(1)
            print(QTime(0, 0, 0).secsTo(self.stopwatch))
            # self.lblStopwatchSec.setText(self.stopwatch.toString("ss"))
        else:
            raise RuntimeError("Unexpected Input")
        self.displayStopwatchTime()

        secs = QTime(0, 0, 0).secsTo(self.stopwatch)
        if self.resetOn:
            self.timer_max = self.stopwatch
            self.prog_Stopwatch.setLimit(secs, 0)
            self.prog_Stopwatch.setValue(secs)

        if self.stopwatch > self.timer_max:
            self.timer_max = self.stopwatch
            self.prog_Stopwatch.setLimit(secs, 0)

    def takeTime(self, button):
        if button == self.takeHourButton:
            self.stopwatch = self.stopwatch.addSecs(-3600)
            # self.lblStopwatchHour.setText(self.stopwatch.toString("hh"))

        elif button == self.takeMinuteButton:
            self.stopwatch = self.stopwatch.addSecs(-60)
            # self.lblStopwatchMnt.setText(self.stopwatch.toString("mm"))
        else:
            self.stopwatch = self.stopwatch.addSecs(-1)
            # self.lblStopwatchSec.setText(self.stopwatch.toString("ss"))
        self.displayStopwatchTime()

        secs = QTime(0, 0, 0).secsTo(self.stopwatch)
        if self.resetOn:
            self.timer_max = self.stopwatch
            self.prog_Stopwatch.setLimit(secs, 0)
            self.prog_Stopwatch.setValue(secs)

    def listClicked(self, index):
        print(index.row())
        self.toDoSelectedLineIndex = index.row()

    def addList(self):
        txt = self.toDoLineEdit.text()
        strList = self.model.stringList()
        strList.append(txt)
        self.model.setStringList(strList)
        self.toDoLineEdit.clear()

    def removeList(self):
        if self.toDoSelectedLineIndex is not None:
            self.model.removeRow(self.toDoSelectedLineIndex)
            return
        if self.toDoLineEdit.text():
            txt = self.toDoLineEdit.text()
            stIndex = self.model.index(0, 0)
            searchIndex = self.model.match(stIndex, QtCore.Qt.DisplayRole, txt)
            self.model.removeRow(searchIndex[0].row())
            self.toDoLineEdit.clear()

    def progressChanged(self, pc):
        time = QTime(0,0,0).secsTo(self.timer_max) * pc
        # print(time)
        qtime = QTime(0,0,0).addSecs(time)
        self.prog_Stopwatch.setValue(time)
        if self.resetOn:
            self.stopwatch = qtime
        self.displayStopwatchTime()

    def addMomoTab(self):
        # Memo Tab

        self.tab = QtWidgets.QWidget()

        self.tab.setObjectName("tab_8")
        self.memoListTab.addTab(self.tab_8, "")
        index = self.memoListTab.indexOf(self.tab)
        self.memoListTab.setTabText(self.memoListTab.indexOf(self.tab), "Memo 3")

    def removeTab(self):
        self.memoListTab.removeTab(self.memoListTab.indexOf(self.tab_8))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())
