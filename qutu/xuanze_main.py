import time

from PyQt5.Qt import *
from resource.xuanze import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import tu_wen_mian as t
import erweima_main as e
import ciyun_main as ci
import shi_wen_mian as shi
import masai_main as ma


class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

        self.animation_targets=[self.set_menue_btn,self.example_menue_btn,self.about_menue_btn]
        self.animation_targets_pos=[target.pos() for target in self.animation_targets]

        # _________________________________________________________________美化测试
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)#影藏边框
        self.setWindowOpacity(0.95)  # 设置窗口透明度
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        QThread.sleep(2)

    def show_hide_menue(self):
        pass
    def set_qt(self):
        pass
    def example_qt(self):
        pass
    def about_qt(self):
        pass
    # def show_
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


    def show_hide_menue(self,checked):
        print("xianshi",checked)


        if not checked:
            animation_group =QSequentialAnimationGroup(self)

            for idX,target in enumerate(self.animation_targets):

                animation = QPropertyAnimation()

                animation.setTargetObject(target)
                animation.setPropertyName(b"pos")
                animation.setStartValue(self.main_menue_btn.pos())
                animation.setEndValue(self.animation_targets_pos[idX])
                animation.setDuration(200)
                animation_group.addAnimation(animation)

            animation_group.start(QAbstractAnimation.DeleteWhenStopped)

        else:
            animation_group = QSequentialAnimationGroup(self)

            for idX, target in enumerate(self.animation_targets):

                animation = QPropertyAnimation()

                animation.setTargetObject(target)

                animation.setPropertyName(b"pos")

                animation.setEndValue(self.main_menue_btn.pos())

                animation.setStartValue(self.animation_targets_pos[idX])

                animation.setDuration(200)

                animation_group.addAnimation(animation)


            animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def show_tu_wen(self):
        wint.show()

    def show_erweima(self):
        wine.show()
    def show_ciyun(self):
        winci.show()
    def show_shi_wen(self):
        winshi.show()
    def show_masai(self):
        winma.show()


#下面是左上角三个标的实现
    def xuanze_guanbi(self):
        self.close()
    def xuanze_yincang(self):
        self.showMinimized()
    def xuanze_fangda(self):
        if self.isMaximized()==0:
            self.showMaximized()
        else:
            self.showNormal()

#下面是确认关闭界面
   # def closeEvent(self, QCloseEvent):
        #QMessageBox.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 影藏边框
        #QMessageBox.setWindowOpacity(0.95)  # 设置窗口透明度
        #  使用QMessageBox提示
       # reply = QMessageBox.warning(self, "温馨提示", "即将退出, 确定？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
       # if (reply == QMessageBox.Yes):
       #    QCloseEvent.accept()
        #if (reply == QMessageBox.No):
        #    QCloseEvent.ignore()


if __name__ =='__main__':
    import sys

    app = QApplication(sys.argv)


    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("qidong3.png"))
    # 设置画面中的文字的字体
    splash.setFont(QFont('Microsoft YaHei UI', 12))
    #透明度
    splash.setWindowOpacity(0.89)
    # 显示画面
    splash.show()
    # 显示信息



    win = Window()
    wint = t.Window()
    wine = e.Window()
    winci= ci.Window()
    winshi=shi.Window()
    winma = ma.Window()
    win.show()
    splash.finish(win)



    sys.exit(app.exec_())