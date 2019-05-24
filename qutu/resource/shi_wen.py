# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shi_wen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(909, 737)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"/*background-image: url(:/shouyexuanze/image/full.png);\n"
"border-image: url(:/shouyexuanze/image/background.png);*/\n"
"    background-color: rgb(38, 38, 38);\n"
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
"        border-width:2px;\n"
"        border-color:balck;\n"
"        border-radius:15px;\n"
"        \n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(150, 150, 150);\n"
"    background-color: rgb(138, 138, 138);\n"
"    color: rgb(38, 38, 38);\n"
"}")
        self.yuanzetupian = QtWidgets.QPushButton(Form)
        self.yuanzetupian.setGeometry(QtCore.QRect(370, 40, 121, 41))
        self.yuanzetupian.setStyleSheet("font: 18pt \"方正舒体\";\n"
"border-width:2px;")
        self.yuanzetupian.setObjectName("yuanzetupian")
        self.dudu = QtWidgets.QTextBrowser(Form)
        self.dudu.setGeometry(QtCore.QRect(40, 90, 831, 621))
        self.dudu.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"border-radius:30px;\n"
"\n"
"border:2px solid;\n"
"border-color: rgb(127, 188, 248);\n"
"")
        self.dudu.setObjectName("dudu")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.pushButton_7.setStyleSheet("QPushButton{background:#F7D674;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font-weight:bolder;\n"
"padding-top:-5px;\n"
"font: 20px\"微软雅黑\";\n"
"border-width:1px;\n"
"}\n"
"QPushButton:hover{background:yellow;}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 30, 21, 21))
        self.pushButton_6.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font:26px \"微软雅黑\";\n"
"font-weight:600;\n"
"padding-top:-4px;\n"
"border-width:1px;\n"
"}\n"
"QPushButton:hover{background:green;}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 30, 21, 21))
        self.pushButton_8.setStyleSheet("QPushButton{background:#F76677;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font-weight:bolder;\n"
"font:18px;\n"
"font-weight:bolder;\n"
"border-width:1px;\n"
"}\n"
"QPushButton:hover{background:red;}")
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Form)
        self.yuanzetupian.clicked.connect(Form.shi_wen)
        self.pushButton_8.clicked.connect(Form.guanbi)
        self.pushButton_7.clicked.connect(Form.judahua)
        self.pushButton_6.clicked.connect(Form.zuixiaohua)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yuanzetupian.setText(_translate("Form", "选择视频"))
        self.pushButton_7.setText(_translate("Form", "□"))
        self.pushButton_6.setText(_translate("Form", "-"))
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

