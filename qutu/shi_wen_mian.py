import threading

from PyQt5.Qt import *
from resource.shi_wen import Ui_Form
import cv2
import time
from PyQt5 import QtCore, QtGui, QtWidgets

charSet = "'.,`^[]/\<>-=+ocvedaslzxBGHWNM*%$"
#M = []
flag = -20


class Window(QWidget, Ui_Form):
   # M = []
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 影藏边框
        self.setWindowOpacity(0.95)  # 设置窗口透明度


    def shi_wen(self):
        print("1")
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开视频", "", "*All Files(*)")
        print(imgName)
        self.cap = cv2.VideoCapture(imgName)
        print("3")

        threading.Thread(target=self.shuchu).start()
            # if(threada.join()):

        cv2.waitKey(10000)
        print("9")
    def shuchu(self):
        if (self.cap.isOpened()):
            print("4")
            self.height = (int)(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print("5")
            self.ret, self.frame = self.cap.read()
            print("6")
        while self.ret:
            print("7")
            src = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

            # scale = 1/20
            # 最终单个字符画的高度为命令行显示的最多行数(50)，这样连续输出可以保证基本流畅
            self.scale = 50 / self.height  # 命令行高度
            # 缩放图像，用一个字符代替1/scale * 1/scale个像素点
            self.dst = cv2.resize(src, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_CUBIC)
            h = self.dst.shape[0]
            w = self.dst.shape[1]
            self.M = ""
            for row in range(h):
                line = ""
                for col in range(w):
                    pix = self.dst[row, col]
                    # 将像素值映射到字符集，后接' '规范格式(默认输出有行间距没有字间距)
                    i = (int)(pix / 256 * len(charSet))
                    line += charSet[i] + " "
                    # print(charSet[i],end = ' ')
                # print(line)
                #self.M.append(line)
                self.M+=line
                self.M+='\n'
            print("1")
            #for i in self.M:
            #   print("2")
            self.dudu.append(self.M)
            print("3")
            time.sleep(0.01)
            #self.dudu.setText("2")
            print("8")
            self.ret, self.frame = self.cap.read()
            self.dudu.moveCursor(self.dudu.textCursor().End)

            flag = 1
        self.cap.release()

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
        if self.isMaximized() == 0:
            self.showMaximized()
        else:
            self.showNormal()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    win = Window()
    win.show()
    sys.exit(app.exec_())