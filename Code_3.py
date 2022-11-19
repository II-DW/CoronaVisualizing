import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5 import uic

New = uic.loadUiType(r"C:\Users\dowon\OneDrive\PYTHON\pyqt\UI3.ui")[0] #두 번째창 ui
class window_3(QDialog,QWidget,New):
    def __init__(self):
        super(window_3,self).__init__()
        self.initUI()
        self.btn_3()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_3)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,1000,500)
        self.label.move(-10,-60)
        
    def Home(self):
        self.close() #창 닫기

    def btn_3 (self) :
        plt.figure(figsize=(11, 5.5))
        self.label.clear()
        start_day = self.year.text() + self.month.text() + self.day.text()
        if start_day == "" :
            start_day = '20220720'
        decoding_key = 'hScrax2XxNGjs1gcynNRpIldiQEi3nYDi7f4B+KV05FDXh/OBvy1/6VtD0KzgfkkVKMdBkeKwyVTitQMaopiPw=='
        day = datetime.today().strftime('%Y%m%d') #오늘 날짜
        params ={'serviceKey' : decoding_key, 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : start_day , 'endCreateDt' : day }
        xml = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson', params=params)
        xml_dict = xmltodict.parse(xml.text)    
        data = xml_dict['response']['body']['items']['item']
        df = pd.DataFrame(data)
        df2 = df[df['gubun']=='여성']
        df1 = df[df['gubun']=='남성']

        df2 = df2.astype({'confCase' : 'float'})
        df2['date'] = pd.to_datetime(df2['createDt'])
        df3 = df2[['date','confCase']]
        df3 = df3.sort_values(by='date')
        df3['daily_natDefCnt'] = df3['confCase'].diff()

        temp = df3[df3['daily_natDefCnt']<=0].index
        df3 = df3.drop(temp)
        sns.lineplot(x='date',y='daily_natDefCnt', data = df3, color = 'red',label = 'woman')

        df1 = df1.astype({'confCase' : 'float'})
        df1['date'] = pd.to_datetime(df1['createDt'])
        df4 = df1[['date','confCase']]
        df4 = df4.sort_values(by='date')
        df4['daily_natDefCnt'] = df4['confCase'].diff()

        temp = df4[df4['daily_natDefCnt']<=0].index
        df4 = df4.drop(temp)
        sns.lineplot(x='date',y='daily_natDefCnt', data = df4, label = 'man')
        plt.xticks(rotation = 30)
        plt.savefig('IMG3.png')

        pixmap = QPixmap('IMG3.png')
        self.label.setPixmap(pixmap)


