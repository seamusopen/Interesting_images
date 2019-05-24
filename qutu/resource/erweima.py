# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erweima.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 706)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"/*background-image: url(:/shouyexuanze/image/full.png);\n"
"border-image: url(:/shouyexuanze/image/background.png);*/\n"
"    background-color: rgb(38, 38, 38);\n"
"    border-style:outset; \n"
"        border-width:1px;\n"
"        border-color:balck;\n"
"        border-radius:30px;\n"
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
"        border-radius:15px;\n"
"        \n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(150, 150, 150);\n"
"    background-color: rgb(138, 138, 138);\n"
"    color: rgb(38, 38, 38);\n"
"}\n"
"QLabel#label{\n"
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
"        border-radius:15px;\n"
"color:rgb(150, 150, 150);\n"
"    background-color: rgb(138, 138, 138);\n"
"    color: rgb(38, 38, 38);\n"
"        \n"
"}\n"
"/*QLabel:hover{\n"
"color:rgb(150, 150, 150);\n"
"    background-color: rgb(138, 138, 138);\n"
"    color: rgb(38, 38, 38);\n"
"}*/")
        self.yuanzetupian = QtWidgets.QPushButton(Form)
        self.yuanzetupian.setGeometry(QtCore.QRect(150, 630, 121, 41))
        self.yuanzetupian.setStyleSheet("/*font: 15pt \"微软雅黑\";\n"
"color: rgb(52, 27, 54);\n"
"border-color: rgb(85, 52, 82);\n"
"\n"
"border:2px solid;\n"
"background-color: rgb(173, 147, 185);\n"
"border-color: rgb(85, 52, 82);\n"
"border-left-radius:10px;\n"
" \n"
"\n"
"border-top-left-radius:4px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:4px;\n"
"    border-right: transparent;\n"
"\n"
"hover-background:#501658;\n"
"*/")
        self.yuanzetupian.setObjectName("yuanzetupian")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(220, 80, 711, 61))
        self.textEdit.setStyleSheet("background-color: rgb(166, 166, 166);\n"
"font:22px;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 80, 161, 41))
        self.label.setStyleSheet("\n"
"font: 20pt \"方正舒体\";")
        self.label.setObjectName("label")
        self.yuan_image = QtWidgets.QLabel(Form)
        self.yuan_image.setGeometry(QtCore.QRect(30, 160, 411, 451))
        self.yuan_image.setStyleSheet("font: 48pt \"方正舒体\";\n"
"color:rgb(50, 11, 51);\n"
"border:1px solid;\n"
"border-color:bule;\n"
"border-radius:30px;\n"
"border:2px solid;\n"
"border-color: rgb(127, 188, 248);\n"
"color:white;")
        self.yuan_image.setObjectName("yuan_image")
        self.yuan_image_2 = QtWidgets.QLabel(Form)
        self.yuan_image_2.setGeometry(QtCore.QRect(480, 150, 451, 471))
        self.yuan_image_2.setStyleSheet("font: 48pt \"方正舒体\";\n"
"color:rgb(50, 11, 51);\n"
"border:1px solid;\n"
"border-color:bule;\n"
"border-radius:30px;\n"
"border:2px solid;\n"
"border-color: rgb(127, 188, 248);\n"
"color:white;\n"
"border:none;")
        self.yuan_image_2.setObjectName("yuan_image_2")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 30, 21, 21))
        self.pushButton_6.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font:26px \"微软雅黑\";\n"
"font-weight:600;\n"
"padding-top:-4px;\n"
"}\n"
"QPushButton:hover{background:green;}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 30, 21, 21))
        self.pushButton_7.setStyleSheet("QPushButton{background:#F7D674;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font-weight:bolder;\n"
"padding-top:-5px;\n"
"font: 20px\"微软雅黑\";\n"
"}\n"
"QPushButton:hover{background:yellow;}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 30, 21, 21))
        self.pushButton_8.setStyleSheet("QPushButton{background:#F76677;border-radius:5px;\n"
"color: rgb(166, 166, 166);\n"
"font-weight:bolder;\n"
"font:18px;\n"
"font-weight:bolder;\n"
"}\n"
"QPushButton:hover{background:red;}")
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Form)
        self.yuanzetupian.clicked.connect(Form.erxuantu)
        self.textEdit.textChanged.connect(Form.erhuodewenben)
        self.pushButton_6.clicked.connect(Form.zuixiaohua)
        self.pushButton_7.clicked.connect(Form.judahua)
        self.pushButton_8.clicked.connect(Form.guanbi)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yuanzetupian.setText(_translate("Form", "选择图片"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:22px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", " 网址或文本"))
        self.yuan_image.setText(_translate("Form", "   原 图 片"))
        self.yuan_image_2.setText(_translate("Form", "      新 图 片"))
        self.pushButton_6.setText(_translate("Form", "-"))
        self.pushButton_7.setText(_translate("Form", "□"))
        self.pushButton_8.setText(_translate("Form", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

