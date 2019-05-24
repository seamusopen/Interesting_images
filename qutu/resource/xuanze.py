# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xuanze.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(486, 413)
        Form.setMinimumSize(QtCore.QSize(450, 352))
        Form.setMaximumSize(QtCore.QSize(2000, 2000))
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"/*background-image: url(:/shouyexuanze/image/full.png);\n"
"border-image: url(:/shouyexuanze/image/background.png);*/\n"
"    background-color: rgb(38, 38, 38);\n"
"    /*border-style:outset; \n"
"        border-width:1px;\n"
"        border-color:balck;\n"
"        border-radius:30px;*/\n"
"\n"
"}\n"
"QPushButton{\n"
"font: 40pt \"微软雅黑\";\n"
"color:rgb(212, 212, 212);\n"
"        /*border-bottom:1px solid white;*/\n"
"        font-size:20px;\n"
"        font-weight:700;\n"
"        font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"\n"
"        border-style:outset; \n"
"        border-width:1px;\n"
"        border-color:balck;\n"
"        border-radius:25px;\n"
"\n"
"        \n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(150, 150, 150);\n"
"    background-color: rgb(138, 138, 138);\n"
"    color: rgb(38, 38, 38);\n"
"}\n"
"QMessageBox{\n"
"        background-color: rgb(38, 38, 38);\n"
"        font: 40pt \"微软雅黑\";\n"
"        color:rgb(212, 212, 212);\n"
"        /*border-bottom:1px solid white;*/\n"
"        font-size:20px;\n"
"        font-weight:700;\n"
"        font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"\n"
"}")
        self.main_menue_btn = QtWidgets.QPushButton(Form)
        self.main_menue_btn.setGeometry(QtCore.QRect(-60, 130, 121, 121))
        self.main_menue_btn.setStyleSheet("QPushButton{\n"
"font: 20pt \"方正舒体\";\n"
"border:white;\n"
"border:1px solid;\n"
"border-radius:60px;\n"
"    background-color: rgb(50, 11, 51);\n"
"\n"
"padding-right:-45px;\n"
"\n"
"padding-top:-7px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(38, 38, 38);\n"
"background-color:;\n"
"    color: rgb(103, 182, 204);\n"
"font: 31pt;\n"
"color:rgb(212, 212, 212);\n"
"\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"\n"
"    border:4px double;\n"
"\n"
"}")
        self.main_menue_btn.setCheckable(True)
        self.main_menue_btn.setObjectName("main_menue_btn")
        self.set_menue_btn = QtWidgets.QPushButton(Form)
        self.set_menue_btn.setGeometry(QtCore.QRect(50, 100, 51, 41))
        self.set_menue_btn.setStyleSheet("QPushButton{\n"
"font: 15pt \"方正舒体\";\n"
"background-color: rgb(50, 11, 51);\n"
"border:white;\n"
"border:1px solid;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:4px double;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"\n"
"background-color:rgb(166, 166, 166);\n"
"\n"
"}")
        self.set_menue_btn.setCheckable(False)
        self.set_menue_btn.setObjectName("set_menue_btn")
        self.about_menue_btn = QtWidgets.QPushButton(Form)
        self.about_menue_btn.setGeometry(QtCore.QRect(40, 240, 51, 41))
        self.about_menue_btn.setStyleSheet("QPushButton{\n"
"font: 15pt \"方正舒体\";\n"
"background-color: rgb(50, 11, 51);\n"
"border:white;\n"
"border:1px solid;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:4px double;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"\n"
"background-color:rgb(166, 166, 166);\n"
"\n"
"}")
        self.about_menue_btn.setCheckable(False)
        self.about_menue_btn.setObjectName("about_menue_btn")
        self.example_menue_btn = QtWidgets.QPushButton(Form)
        self.example_menue_btn.setGeometry(QtCore.QRect(80, 170, 51, 41))
        self.example_menue_btn.setStyleSheet("QPushButton{\n"
"font: 15pt \"方正舒体\";\n"
"background-color: rgb(50, 11, 51);\n"
"border:white;\n"
"border:1px solid;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"border:4px double;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"\n"
"background-color:rgb(166, 166, 166);\n"
"\n"
"}")
        self.example_menue_btn.setCheckable(False)
        self.example_menue_btn.setObjectName("example_menue_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 30, 251, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 20, 21, 21))
        self.pushButton_6.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font:26px \"微软雅黑\";\n"
"font-weight:600;\n"
"padding-top:-4px;\n"
"}\n"
"QPushButton:hover{background:green;}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 20, 21, 21))
        self.pushButton_7.setStyleSheet("QPushButton{background:#F7D674;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font-weight:bolder;\n"
"padding-top:-5px;\n"
"font: 20px\"微软雅黑\";\n"
"}\n"
"QPushButton:hover{background:yellow;}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 20, 21, 21))
        self.pushButton_8.setStyleSheet("QPushButton{background:#F76677;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font-weight:bolder;\n"
"font:18px;\n"
"font-weight:bolder;\n"
"}\n"
"QPushButton:hover{background:red;}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.layoutWidget.raise_()
        self.set_menue_btn.raise_()
        self.about_menue_btn.raise_()
        self.example_menue_btn.raise_()
        self.main_menue_btn.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()

        self.retranslateUi(Form)
        self.main_menue_btn.clicked['bool'].connect(Form.show_hide_menue)
        self.set_menue_btn.clicked.connect(Form.set_qt)
        self.example_menue_btn.clicked.connect(Form.example_qt)
        self.about_menue_btn.clicked.connect(Form.about_qt)
        self.pushButton_3.clicked.connect(Form.show_tu_wen)
        self.pushButton_2.clicked.connect(Form.show_erweima)
        self.pushButton.clicked.connect(Form.show_ciyun)
        self.pushButton_4.clicked.connect(Form.show_shi_wen)
        self.pushButton_5.clicked.connect(Form.show_masai)
        self.pushButton_8.clicked.connect(Form.xuanze_guanbi)
        self.pushButton_7.clicked.connect(Form.xuanze_fangda)
        self.pushButton_6.clicked.connect(Form.xuanze_yincang)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menue_btn.setText(_translate("Form", "菜\n"
"单"))
        self.set_menue_btn.setText(_translate("Form", "设置"))
        self.about_menue_btn.setText(_translate("Form", "关于"))
        self.example_menue_btn.setText(_translate("Form", "样例"))
        self.pushButton_5.setText(_translate("Form", "马赛克风格图片"))
        self.pushButton_3.setText(_translate("Form", "图片转文字"))
        self.pushButton_4.setText(_translate("Form", "视频转文字"))
        self.pushButton_2.setText(_translate("Form", "趣味二维码"))
        self.pushButton.setText(_translate("Form", "中英文词云"))
        self.pushButton_6.setText(_translate("Form", "-"))
        self.pushButton_7.setText(_translate("Form", "□"))
        self.pushButton_8.setText(_translate("Form", "X"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

