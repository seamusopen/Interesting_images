import time

from PyQt5.Qt import *
from resource.masaike import Ui_Form
from PyQt5 import QtWidgets, QtCore, QtGui
import os

class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 影藏边框
        self.setWindowOpacity(0.95)  # 设置窗口透明度

    def xuanze_tu(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(self.imgName).scaled(self.yuan_image.width(), self.yuan_image.height())
        self.yuan_image.setPixmap(jpg)

    def xuanze_tuku(self):
        directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")  # 起始路径
        print(directory1)

    def shengcheng(self): #暂时伪实现
        #m="python puzzle.py -i "+ self.imgName + " -d database/full/ -o output/"
        #print(m)
        #result=os.popen(m)
        #print(result.read())
        m=''
        lujin=''
        new_lujin=''
        sum=0
        for i in self.imgName[::-1]:
            if i=='/':
                break
            m+=i
            if i=='.':
                m+='2'
        wenjianming=m[::-1]
        print(wenjianming)
        cd=len(wenjianming)
        print(len(self.imgName))
        for i in self.imgName:
            sum+=1
            if(sum>len(self.imgName)-cd+1):
                break
            lujin+=i
        print(lujin)
        for i in lujin[-4:]:
            new_lujin+=i
        print(new_lujin)
        time.sleep(5)
        if new_lujin == '马赛克/':
            jpg = QtGui.QPixmap(lujin+'out/'+wenjianming).scaled(self.yuan_image.width(), self.yuan_image.height())
            self.yuan_image_2.setPixmap(jpg)
        else:
            jpg = QtGui.QPixmap('./a样例/马赛克/out/error.png').scaled(self.yuan_image.width(), self.yuan_image.height())
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