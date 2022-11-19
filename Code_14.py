import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5 import uic

New = uic.loadUiType(r"C:\Users\dowon\OneDrive\PYTHON\pyqt\UI2.ui")[0] #두 번째창 ui
class window_14(QDialog,QWidget,New):
    def __init__(self):
        super(window_14,self).__init__()
        self.initUI()
        self.btn_14()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_14)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,1000,500)
        self.label.move(-10,0)
        
    def Home(self):
        self.close() #창 닫기

    def btn_14 (self) :
        plt.figure(figsize=(11, 6))
        self.label.clear()
        plt.rcParams['font.family'] = 'Malgun Gothic'

        decoding_key = 'hScrax2XxNGjs1gcynNRpIldiQEi3nYDi7f4B+KV05FDXh/OBvy1/6VtD0KzgfkkVKMdBkeKwyVTitQMaopiPw=='
        params ={'serviceKey' : decoding_key }
        json = requests.get('http://apis.data.go.kr/1790387/covid19CurrentStatusHospitalizations/covid19CurrentStatusHospitalizationsJson', params=params).json()
        data = json['response']['result']
        L = ['cnt1','cnt2','cnt3','cnt4','cnt5','cnt6','cnt7']
        b=0
        dict_a = {}
        for a in L :
            key = str(6-b) + '일 전'
            if b == 6 :
                key = '오늘'
            dict_a[key] = int(data[0][a])
            b+=1
        dict_a = [dict_a]
        df = pd.DataFrame(dict_a)
        df.index = ['value']
        df=df.transpose()
        df.index.name = "index"
        print(df)
        sns.relplot(x='index',y='value', data = df, kind='line', aspect=2)
        plt.savefig('IMG14.png')

        pixmap = QPixmap('IMG14.png')
        self.label.setPixmap(pixmap)


