import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5 import uic


New = uic.loadUiType(r"./ui/UI2.ui")[0] #두 번째창 ui
class window_15(QDialog,QWidget,New):
    def __init__(self):
        super(window_15,self).__init__()
        self.initUI()
        self.btn_15()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_15)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,1000,500)
        self.label.move(-10,0)
        
    def Home(self):
        self.close() #창 닫기

    def btn_15 (self) :
        self.label.clear()
        plt.figure(figsize=(11, 6))
        plt.rcParams['font.family'] = 'Malgun Gothic'

        xml = requests.get('https://nip.kdca.go.kr/irgd/cov19stats.do?list=all')
        xml_dict = xmltodict.parse(xml.text)    
        data = xml_dict['response']['body']['items']['item']
        df = pd.DataFrame(data)
        df.set_index("tpcd", inplace=True)
        df=df.transpose()
        L = []
        try :
            df['당일실적(A)']=df['당일실적(A)'].astype(float)
            df['전일누적(B)']=df['전일누적(B)'].astype(float)
            df['전체건수(C): (A)+(B)']=df['전체건수(C): (A)+(B)'].astype(float)
            df['60세이상 접종률']=df['60세이상 접종률'].astype(float)
        except :
            df['당일실적(A)']= 0
            df['전일누적(B)']= 0
            df['전체건수(C): (A)+(B)']=0
            df['60세이상 접종률']=0
        for y in range (1, len(df.index)+1):
            L.append(str(y) + '차 접종')
        df['N'] = L
        fig, ax = plt.subplots(ncols=4, nrows=1,figsize=(11, 5))
        sns.barplot(data= df, ax=ax[0], x="N", y="당일실적(A)")
        sns.barplot(data= df, ax=ax[1], x="N", y="전일누적(B)")
        sns.barplot(data= df, ax=ax[2], x="N", y="전체건수(C): (A)+(B)")
        sns.barplot(data= df, ax=ax[3], x="N", y="60세이상 접종률")
        plt.savefig('./img/IMG15.png')

        pixmap = QPixmap('./img/IMG15.png')
        self.label.setPixmap(pixmap)


