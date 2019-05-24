from PyQt5.Qt import *
from resource.yiyun import Ui_Form
from PyQt5 import QtWidgets, QtCore, QtGui
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba



class Window(QWidget,Ui_Form):
    txt1 = "2333"
    txt2 = "2333"
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 影藏边框
        self.setWindowOpacity(0.95)  # 设置窗口透明度

    def ci_xuanzetupian(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        self.txt1=imgName
        jpg = QtGui.QPixmap(self.txt1).scaled(self.yuan_image.width(), self.yuan_image.height())
        self.yuan_image.setPixmap(jpg)

    def ci_xuanzewenben(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开文本", "", "All Files(*)")
        self.txt2=imgName
        fd=open(imgName)
        txt=fd.read()
        self.ci_wen.setText(txt)
        fd.close()


    def ci_zuihou(self):
        abel_mask = np.array(Image.open(self.txt1))

        # 读取要生成词云的文件
        text_from_file_with_apath = open(self.txt2).read()

        # 通过jieba分词进行分词并通过空格分隔
        wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
        wl_space_split = " ".join(wordlist_after_jieba)
        # my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
        my_wordcloud = WordCloud(
            background_color='white',  # 设置背景颜色
            mask=abel_mask,  # 设置背景图片
            max_words=200,  # 设置最大现实的字数
            stopwords=STOPWORDS,  # 设置停用词
            font_path='./DroidSansFallbackFull.ttf',  # 设置字体格式，如不设置显示不了中文
            max_font_size=50,  # 设置字体最大值
            random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
            scale=1.5
        ).generate(wl_space_split)

        # 根据图片生成词云颜色
        image_colors = ImageColorGenerator(abel_mask)
        # my_wordcloud.recolor(color_func=image_colors)

        # 以下代码显示图片
        #plt.imshow(my_wordcloud)
        #print(my_wordcloud)
        #plt.axis("off")
        #plt.show()
        my_wordcloud.to_file('ciyun.jpg')
        print(self.txt1)
        self.txt1='./ciyun.jpg'
        jpg = QtGui.QPixmap(self.txt1).scaled(self.yuan_image_2.width(), self.yuan_image_2.height())
        self.yuan_image_2.setPixmap(jpg)
    # def ci_zuihou(self):
    #     print("1")
    #     font = "./resource/DroidSansFallbackFull.ttf"
    #     print("2")
    #     print(self.txt1)
    #     mask = np.array(Image.open(self.txt1))
    #     text = open(self.txt2, 'r', encoding='gbk').read()
    #     # preprocessing the text a little bit
    #     text = text.replace("程心说", "程心")
    #     text = text.replace("程心和", "程心")
    #     text = text.replace("程心问", "程心")
    #
    #     # adding movie script specific stopwords
    #     stopwords = set(STOPWORDS)
    #     stopwords.add("int")
    #     stopwords.add("ext")
    #     print("3")
    #     wc = WordCloud(font_path=font, max_words=2000, mask=mask, stopwords=stopwords, margin=10,
    #                    random_state=1).generate(text)
    #     # store default colored image
    #     print("4")
    #     default_colors = wc.to_array()
    #     print("5")
    #     plt.title("Custom colors")
    #     print("6")
    #     plt.imshow( wc.recolor(color_func=self.grey_color_func, random_state=3))
    #     print("7")
    #     wc.to_file("a_new_hope.png")
    #     print("8")
    #     plt.axis("off")
    #     plt.figure()
    #     plt.title("三体-词频统计")
    #     plt.imshow(default_colors)
    #     plt.axis("off")
    #     plt.show()
    #
    # def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    #         return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
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

    def exit(self):
        self.close()
    def zxh(self):
        self.showMinimized()
    def fd(self):
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