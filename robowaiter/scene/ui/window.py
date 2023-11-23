# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 1080)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_say = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_say.setGeometry(QtCore.QRect(520, 390, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.edit_say.setFont(font)
        self.edit_say.setObjectName("edit_say")
        self.btn_say = QtWidgets.QPushButton(self.centralwidget)
        self.btn_say.setGeometry(QtCore.QRect(760, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_say.setFont(font)
        self.btn_say.setObjectName("btn_say")
        self.img_label_seg = QtWidgets.QLabel(self.centralwidget)
        self.img_label_seg.setGeometry(QtCore.QRect(80, 540, 321, 231))
        self.img_label_seg.setStyleSheet("border: 2px solid black;")
        self.img_label_seg.setText("")
        self.img_label_seg.setObjectName("img_label_seg")
        self.img_label_bt = QtWidgets.QLabel(self.centralwidget)
        self.img_label_bt.setGeometry(QtCore.QRect(40, 830, 831, 161))
        self.img_label_bt.setStyleSheet("border: 2px solid black;")
        self.img_label_bt.setText("")
        self.img_label_bt.setObjectName("img_label_bt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 800, 121, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.img_label_obj = QtWidgets.QLabel(self.centralwidget)
        self.img_label_obj.setGeometry(QtCore.QRect(520, 540, 321, 231))
        self.img_label_obj.setStyleSheet("border: 2px solid black;")
        self.img_label_obj.setText("")
        self.img_label_obj.setObjectName("img_label_obj")
        self.img_label_map = QtWidgets.QLabel(self.centralwidget)
        self.img_label_map.setGeometry(QtCore.QRect(80, 320, 321, 161))
        self.img_label_map.setStyleSheet("border: 2px solid black;")
        self.img_label_map.setText("")
        self.img_label_map.setObjectName("img_label_map")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 290, 121, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 500, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 510, 121, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_AEM = QtWidgets.QPushButton(self.centralwidget)
        self.btn_AEM.setGeometry(QtCore.QRect(30, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_AEM.setFont(font)
        self.btn_AEM.setObjectName("btn_AEM")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btn_VLN = QtWidgets.QPushButton(self.centralwidget)
        self.btn_VLN.setGeometry(QtCore.QRect(30, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_VLN.setFont(font)
        self.btn_VLN.setObjectName("btn_VLN")
        self.btn_VLM = QtWidgets.QPushButton(self.centralwidget)
        self.btn_VLM.setGeometry(QtCore.QRect(30, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_VLM.setFont(font)
        self.btn_VLM.setObjectName("btn_VLM")
        self.btn_GQA = QtWidgets.QPushButton(self.centralwidget)
        self.btn_GQA.setGeometry(QtCore.QRect(200, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_GQA.setFont(font)
        self.btn_GQA.setObjectName("btn_GQA")
        self.btn_OT = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OT.setGeometry(QtCore.QRect(200, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_OT.setFont(font)
        self.btn_OT.setObjectName("btn_OT")
        self.btn_AT = QtWidgets.QPushButton(self.centralwidget)
        self.btn_AT.setGeometry(QtCore.QRect(200, 170, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_AT.setFont(font)
        self.btn_AT.setObjectName("btn_AT")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(30, 220, 311, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")
        self.list_customer = QtWidgets.QListWidget(self.centralwidget)
        self.list_customer.setGeometry(QtCore.QRect(380, 50, 151, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.list_customer.setFont(font)
        self.list_customer.setObjectName("list_customer")
        item = QtWidgets.QListWidgetItem()
        self.list_customer.addItem(item)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 20, 141, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(740, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.edit_local_history = QtWidgets.QTextEdit(self.centralwidget)
        self.edit_local_history.setEnabled(True)
        self.edit_local_history.setGeometry(QtCore.QRect(550, 50, 171, 261))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_local_history.setFont(font)
        self.edit_local_history.setReadOnly(True)
        self.edit_local_history.setObjectName("edit_local_history")
        self.edit_global_history = QtWidgets.QTextEdit(self.centralwidget)
        self.edit_global_history.setEnabled(True)
        self.edit_global_history.setGeometry(QtCore.QRect(740, 50, 161, 261))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_global_history.setFont(font)
        self.edit_global_history.setReadOnly(True)
        self.edit_global_history.setObjectName("edit_global_history")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.edit_say.setText(_translate("MainWindow", "Is(AC,On)"))
        self.btn_say.setText(_translate("MainWindow", "说话"))
        self.label_5.setText(_translate("MainWindow", "当前行为树"))
        self.label_6.setText(_translate("MainWindow", "可达性地图"))
        self.label_7.setText(_translate("MainWindow", "实例分割"))
        self.label_8.setText(_translate("MainWindow", "目标检测"))
        self.btn_AEM.setText(_translate("MainWindow", "环境主动探索"))
        self.label_9.setText(_translate("MainWindow", "任务演示：（播放动画时需等待动画播放完毕才会重置场景）"))
        self.btn_VLN.setText(_translate("MainWindow", "视觉语言导航"))
        self.btn_VLM.setText(_translate("MainWindow", "视觉语言操作"))
        self.btn_GQA.setText(_translate("MainWindow", "具身多轮对话"))
        self.btn_OT.setText(_translate("MainWindow", "开放具身任务"))
        self.btn_AT.setText(_translate("MainWindow", "自主具身任务"))
        self.btn_reset.setText(_translate("MainWindow", "重置"))
        __sortingEnabled = self.list_customer.isSortingEnabled()
        self.list_customer.setSortingEnabled(False)
        item = self.list_customer.item(0)
        item.setText(_translate("MainWindow", "System"))
        self.list_customer.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("MainWindow", "顾客列表："))
        self.label_11.setText(_translate("MainWindow", "顾客历史对话："))
        self.label_12.setText(_translate("MainWindow", "全局历史对话："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())