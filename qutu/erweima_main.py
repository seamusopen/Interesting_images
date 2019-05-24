
from PyQt5 import QtWidgets, QtCore, QtGui
from resource.erweima import Ui_Form
from PyQt5.Qt import *

from PyQt5.QtGui import QMovie
from MyQR import myqr

class Window(QWidget,Ui_Form):
    def __init__(self):
        self.txt="2333"
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 影藏边框
        self.setWindowOpacity(0.95)  # 设置窗口透明度

    def erxuantu(self):
        #print(self.txt)
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.yuan_image.width(), self.yuan_image.height())
        self.yuan_image.setPixmap(jpg)
        qq,ww,ee=myqr.run(
        words = self.txt,
        picture = imgName,
        colorized=True,
        save_name = 'artistic.gif',
        version=5,
        level='H',
        )
        # jpg1 = QtGui.QPixmap(ee).scaled(self.yuan_image_2.width()+40, self.yuan_image_2.height())
        # self.yuan_image_2.setPixmap(jpg1)
        self.gif = QMovie(ee)
        self.yuan_image_2.setMovie(self.gif)
        self.gif.start()

    def erhuodewenben(self):
        self.txt=self.textEdit.toPlainText()
        a,b,c,=myqr.run(self.txt)
        #print(a,b,c)
        #print(self.txt)
        jpg=QtGui.QPixmap(c).scaled(self.yuan_image_2.width(), self.yuan_image_2.height())
        self.yuan_image_2.setPixmap(jpg)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))



    def guanbi(self):
        self.close()
    def zuixiaohua(self):
        self.showMinimized()
    def judahua(self):
        if self.isMaximized()==0:
            self.showMaximized()
        else:
            self.showNormal()

if __name__ =='__main__':
    import sys

    app = QApplication(sys.argv)

    win = Window()
    win.show()


    sys.exit(app.exec_())