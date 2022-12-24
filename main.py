import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from UI_code.Code_1 import window_1 
from UI_code.Code_2 import window_2
from UI_code.Code_3 import window_3
from UI_code.Code_4 import window_4
from UI_code.Code_5 import window_5
from UI_code.Code_6 import window_6
from UI_code.Code_7 import window_7
from UI_code.Code_8 import window_8
from UI_code.Code_9 import window_9
from UI_code.Code_10 import window_10

form_class = uic.loadUiType(r"./ui/pyqt.ui")[0]

  
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
        self.push_7.clicked.connect(self.btn_clicked_7)
        self.push_8.clicked.connect(self.btn_clicked_8)
        self.push_9.clicked.connect(self.btn_clicked_9)
        self.push_10.clicked.connect(self.btn_clicked_10)
        self.IMG_11 = QPixmap('./img/IM11.jpg')

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
    def btn_clicked_7(self): #병상현황
        self.hide() #메인 윈도우 숨김
        self.second = window_7()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_8(self): #신규 입원자 현황
        self.hide() #메인 윈도우 숨김
        self.second = window_8()
        self.second.exec() # 두번째창 닫을때까지 기다림65696369
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_9(self): #예방접종
        self.hide() #메인 윈도우 숨김
        self.second = window_9()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐
    def btn_clicked_10(self):
        self.hide() #메인 윈도우 숨김
        self.second = window_10()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()  #두번째창 닫으면 다시 첫 번째 창 보여 짐

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()