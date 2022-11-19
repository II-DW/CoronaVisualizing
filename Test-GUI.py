import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from Code_32 import window_32 
from Code_1 import window_1 
from Code_2 import window_2
from Code_3 import window_3
from Code_4 import window_4
from Code_5 import window_5
from Code_6 import window_6
from Code_13 import window_13
from Code_14 import window_14
from Code_15 import window_15

form_class = uic.loadUiType(r"C:\Users\dowon\OneDrive\PYTHON\pyqt\pyqt.ui")[0]

  
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.push_1.clicked.connect(self.btn_clicked_1)
        self.push_2.clicked.connect(self.btn_clicked_2)
        self.push_3.clicked.connect(self.btn_clicked_3)
        self.push_4.clicked.connect(self.btn_clicked_4)
        self.push_5.clicked.connect(self.btn_clicked_5)
        self.push_6.clicked.connect(self.btn_clicked_6)
        self.push_13.clicked.connect(self.btn_clicked_13)
        self.push_14.clicked.connect(self.btn_clicked_14)
        self.push_15.clicked.connect(self.btn_clicked_15)
        self.push_32.clicked.connect(self.btn_clicked_32)
        self.IMG_33 = QPixmap('IMG33.jpg')

    def btn_clicked_1(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_1()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_2(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_2()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_3(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_3()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_4(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_4()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_5(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_5()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_6(self):
        self.hide() #메인 윈도우 숨김   
        self.second = window_6()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_13(self): #병상현황
        self.hide() #메인 윈도우 숨김
        self.second = window_13()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_14(self): #신규 입원자 현황
        self.hide() #메인 윈도우 숨김
        self.second = window_14()
        self.second.exec() # 두번째창 닫을때까지 기다림65696369
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_15(self): #예방접종
        self.hide() #메인 윈도우 숨김
        self.second = window_15()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_32(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_32()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()