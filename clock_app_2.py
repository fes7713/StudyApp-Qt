# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock_app_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QTimer, QTime, Qt, pyqtSignal, QDate


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(678, 604)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.appTab = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appTab.sizePolicy().hasHeightForWidth())
        self.appTab.setSizePolicy(sizePolicy)
        self.appTab.setObjectName("appTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.clockLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.clockLabel.setFont(font)
        self.clockLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clockLabel.setObjectName("clockLabel")
        self.verticalLayout_8.addWidget(self.clockLabel)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.widget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.verticalLayout_11.addWidget(self.widget)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_22.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_22.addWidget(self.pushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_22)
        self.listView = QtWidgets.QListView(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setAutoScrollMargin(5)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setGridSize(QtCore.QSize(0, 5))
        self.listView.setUniformItemSizes(False)
        self.listView.setBatchSize(50)
        self.listView.setObjectName("listView")


        self.verticalLayout_11.addWidget(self.listView)
        self.horizontalLayout_21.addLayout(self.verticalLayout_11)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.appTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addHourButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addHourButton.sizePolicy().hasHeightForWidth())
        self.addHourButton.setSizePolicy(sizePolicy)
        self.addHourButton.setMinimumSize(QtCore.QSize(80, 80))
        self.addHourButton.setText("")
        self.addHourButton.setObjectName("addHourButton")
        self.horizontalLayout_7.addWidget(self.addHourButton)
        self.addMinuteButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addMinuteButton.sizePolicy().hasHeightForWidth())
        self.addMinuteButton.setSizePolicy(sizePolicy)
        self.addMinuteButton.setMinimumSize(QtCore.QSize(80, 80))
        self.addMinuteButton.setText("")
        self.addMinuteButton.setObjectName("addMinuteButton")
        self.horizontalLayout_7.addWidget(self.addMinuteButton)
        self.addSecondButton = QtWidgets.QPushButton(self.tab_2)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem3 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.lblStopwatchHour = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.lblStopwatchHour.setFont(font)
        self.lblStopwatchHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStopwatchHour.setObjectName("lblStopwatchHour")
        self.horizontalLayout_13.addWidget(self.lblStopwatchHour)
        self.stopwatchSpace_1 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatchSpace_1.sizePolicy().hasHeightForWidth())
        self.stopwatchSpace_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.stopwatchSpace_1.setFont(font)
        self.stopwatchSpace_1.setAlignment(QtCore.Qt.AlignCenter)
        self.stopwatchSpace_1.setObjectName("stopwatchSpace_1")
        self.horizontalLayout_13.addWidget(self.stopwatchSpace_1)
        self.lblStopwatchMnt = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.lblStopwatchMnt.setFont(font)
        self.lblStopwatchMnt.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStopwatchMnt.setObjectName("lblStopwatchMnt")
        self.horizontalLayout_13.addWidget(self.lblStopwatchMnt)
        self.stopwatchSpace_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatchSpace_2.sizePolicy().hasHeightForWidth())
        self.stopwatchSpace_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.stopwatchSpace_2.setFont(font)
        self.stopwatchSpace_2.setAlignment(QtCore.Qt.AlignCenter)
        self.stopwatchSpace_2.setObjectName("stopwatchSpace_2")
        self.horizontalLayout_13.addWidget(self.stopwatchSpace_2)
        self.lblStopwatchSec = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.lblStopwatchSec.setFont(font)
        self.lblStopwatchSec.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStopwatchSec.setObjectName("lblStopwatchSec")
        self.horizontalLayout_13.addWidget(self.lblStopwatchSec)
        spacerItem4 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.takeHourButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeHourButton.sizePolicy().hasHeightForWidth())
        self.takeHourButton.setSizePolicy(sizePolicy)
        self.takeHourButton.setMinimumSize(QtCore.QSize(80, 80))
        self.takeHourButton.setText("")
        self.takeHourButton.setObjectName("takeHourButton")
        self.horizontalLayout_6.addWidget(self.takeHourButton)
        self.takeMinuteButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeMinuteButton.sizePolicy().hasHeightForWidth())
        self.takeMinuteButton.setSizePolicy(sizePolicy)
        self.takeMinuteButton.setMinimumSize(QtCore.QSize(80, 80))
        self.takeMinuteButton.setText("")
        self.takeMinuteButton.setObjectName("takeMinuteButton")
        self.horizontalLayout_6.addWidget(self.takeMinuteButton)
        self.takeSecondButton = QtWidgets.QPushButton(self.tab_2)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.startStopwatchButton = QtWidgets.QPushButton(self.tab_2)
        self.startStopwatchButton.setObjectName("startStopwatchButton")
        self.horizontalLayout_20.addWidget(self.startStopwatchButton)
        self.stopStopwatchButton = QtWidgets.QPushButton(self.tab_2)
        self.stopStopwatchButton.setObjectName("stopStopwatchButton")
        self.horizontalLayout_20.addWidget(self.stopStopwatchButton)
        self.resetStopwatchButton = QtWidgets.QPushButton(self.tab_2)
        self.resetStopwatchButton.setObjectName("resetStopwatchButton")
        self.horizontalLayout_20.addWidget(self.resetStopwatchButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.appTab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toDoListView = QtWidgets.QListView(self.tab_3)
        self.toDoListView.setAlternatingRowColors(True)
        self.toDoListView.setObjectName("toDoListView")
        self.verticalLayout_2.addWidget(self.toDoListView)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_18.addWidget(self.label_5)
        self.toDoLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.toDoLineEdit.setObjectName("toDoLineEdit")
        self.horizontalLayout_18.addWidget(self.toDoLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.toDoAddButton = QtWidgets.QPushButton(self.tab_3)
        self.toDoAddButton.setObjectName("toDoAddButton")
        self.horizontalLayout_2.addWidget(self.toDoAddButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.toDoRemoveButton = QtWidgets.QPushButton(self.tab_3)
        self.toDoRemoveButton.setObjectName("toDoRemoveButton")
        self.horizontalLayout_2.addWidget(self.toDoRemoveButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.appTab.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.memoTab = QtWidgets.QTabWidget(self.tab_4)
        self.memoTab.setObjectName("memoTab")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_23.addWidget(self.textEdit)
        self.memoTab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_25.addWidget(self.textEdit_2)
        self.memoTab.addTab(self.tab_6, "")
        self.verticalLayout_5.addWidget(self.memoTab)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.addMemoButton = QtWidgets.QPushButton(self.tab_4)
        self.addMemoButton.setObjectName("addMemoButton")
        self.horizontalLayout_9.addWidget(self.addMemoButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.removeMemoButton = QtWidgets.QPushButton(self.tab_4)
        self.removeMemoButton.setObjectName("removeMemoButton")
        self.horizontalLayout_9.addWidget(self.removeMemoButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.appTab.addTab(self.tab_4, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.appTab.addTab(self.tab_7, "")
        self.verticalLayout_4.addWidget(self.appTab)

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

        timer_clock = QTimer(self)
        # timer_clock.timeout.connect(lambda: self.displayTime(self.lblStopwatchHour))
        timer_clock.timeout.connect(lambda: self.displayTime(self.clockLabel))
        timer_clock.start(1000)

        self.timer_stopwatch = QTimer(self)
        self.stopwatch = QTime(0, 0, 0)
        self.stopwatch_resetTime = QTime(0, 0, 0)
        self.timer_stopwatch.timeout.connect(self.displayStopwatchTime)

        self.startStopwatchButton.clicked.connect(self.startStopwatch)
        self.stopStopwatchButton.clicked.connect(self.stopStopwatch)
        self.resetStopwatchButton.clicked.connect(self.resetStopwatch)

        # Model作成
        self.model = QtCore.QStringListModel()
        self.model.setStringList(['aaa', 'bbb', 'ccc'])
        self.toDoListView.setModel(self.model)
        self.toDoSelectedLineIndex = None

        # Signal-Slot作成
        self.toDoAddButton.clicked.connect(self.addList)
        self.toDoLineEdit.returnPressed.connect(self.addList)
        self.toDoListView.clicked.connect(self.listClicked)
        self.toDoRemoveButton.clicked.connect(self.removeList)

        self.retranslateUi(Form)
        self.appTab.setCurrentIndex(3)
        self.memoTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clockLabel.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "StopWatch"))
        self.label_7.setText(_translate("Form", "ToDo"))
        self.pushButton.setText(_translate("Form", "Done"))
        self.appTab.setTabText(self.appTab.indexOf(self.tab), _translate("Form", "Clock"))
        self.lblStopwatchHour.setText(_translate("Form", "00"))
        self.stopwatchSpace_1.setText(_translate("Form", ":"))
        self.lblStopwatchMnt.setText(_translate("Form", "00"))
        self.stopwatchSpace_2.setText(_translate("Form", ":"))
        self.lblStopwatchSec.setText(_translate("Form", "00"))
        self.startStopwatchButton.setText(_translate("Form", "Start"))
        self.stopStopwatchButton.setText(_translate("Form", "Stop"))
        self.resetStopwatchButton.setText(_translate("Form", "Reset"))
        self.appTab.setTabText(self.appTab.indexOf(self.tab_2), _translate("Form", "Stop Watch"))
        self.label_5.setText(_translate("Form", "ToDo"))
        self.toDoAddButton.setText(_translate("Form", "Add"))
        self.toDoRemoveButton.setText(_translate("Form", "Remove"))
        self.appTab.setTabText(self.appTab.indexOf(self.tab_3), _translate("Form", "To Do"))
        self.memoTab.setTabText(self.memoTab.indexOf(self.tab_5), _translate("Form", "Memo 1"))
        self.memoTab.setTabText(self.memoTab.indexOf(self.tab_6), _translate("Form", "Memo 2"))
        self.addMemoButton.setText(_translate("Form", "Add"))
        self.removeMemoButton.setText(_translate("Form", "Remove"))
        self.appTab.setTabText(self.appTab.indexOf(self.tab_4), _translate("Form", "Memo"))
        self.appTab.setTabText(self.appTab.indexOf(self.tab_7), _translate("Form", "Setting"))

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
        print(displayText)

        label.setText(displayText)

    def displayStopwatchTime(self):
        print("Yes")

        if self.stopwatch == QTime(0, 0, 0):
            self.resetStopwatch()
            return

        self.stopwatch = self.stopwatch.addSecs(-1)
        self.lblStopwatchHour.setText(self.stopwatch.toString("hh"))
        self.lblStopwatchMnt.setText(self.stopwatch.toString("mm"))
        self.lblStopwatchSec.setText(self.stopwatch.toString("ss"))

    def startStopwatch(self):
        print("Yes")
        self.timer_stopwatch.start(1000)



    def stopStopwatch(self):
        self.timer_stopwatch.stop()

    def resetStopwatch(self):
        self.stopStopwatch()
        self.stopwatch = self.stopwatch_resetTime
        self.lblStopwatchHour.setText("00")
        self.lblStopwatchMnt.setText("00")
        self.lblStopwatchSec.setText("00")

    def addTime(self, button):
        if button == self.addHourButton:
            self.stopwatch = self.stopwatch.addSecs(3600)
            self.lblStopwatchHour.setText(self.stopwatch.toString("hh"))

        elif button == self.addMinuteButton:
            self.stopwatch = self.stopwatch.addSecs(60)
            self.lblStopwatchMnt.setText(self.stopwatch.toString("mm"))
        else:
            self.stopwatch = self.stopwatch.addSecs(1)
            self.lblStopwatchSec.setText(self.stopwatch.toString("ss"))

    def takeTime(self, button):
        if button == self.takeHourButton:
            self.stopwatch = self.stopwatch.addSecs(-3600)
            self.lblStopwatchHour.setText(self.stopwatch.toString("hh"))

        elif button == self.takeMinuteButton:
            self.stopwatch = self.stopwatch.addSecs(-60)
            self.lblStopwatchMnt.setText(self.stopwatch.toString("mm"))
        else:
            self.stopwatch = self.stopwatch.addSecs(-1)
            self.lblStopwatchSec.setText(self.stopwatch.toString("ss"))
        print(self.stopwatch)

    #Need to edit variable names to match with main program

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





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())