
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from resource.tu_wen import Ui_Form
from PIL import Image


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 影藏边框
        self.setWindowOpacity(0.95)  # 设置窗口透明度
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.yuan_image.width(), self.yuan_image.height())
        self.yuan_image.setPixmap(jpg)
        if not imgName == '':
            IMG = imgName
            WIDTH = 100
            HEIGHT = 57
            print(IMG)
            im = Image.open(IMG)
            im = im.resize((WIDTH, HEIGHT))
            txt = ""
            print(HEIGHT, WIDTH)
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    txt += self.get_char(*im.getpixel((j, i)))
                txt += '\n'
        self.wuzi.setText(txt)



    def get_char(self,r,g,b,alpha = 256):

        if alpha == 0:
            return ' '

        length = len(ascii_char)

        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1)/length

        return ascii_char[int(gray/unit)]

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