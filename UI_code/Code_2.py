import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap
import UI_code.config  as config

from PyQt5.QtWidgets import *
from PyQt5 import uic

New = uic.loadUiType(r"./ui/UI2.ui")[0] #두 번째창 ui
class window_2(QDialog,QWidget,New):
    def __init__(self):
        super(window_2,self).__init__()
        self.initUI()
        self.btn_2()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_2)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,1000,500)
        self.label.move(-10,-65)
        
    def Home(self):
        self.close() #창 닫기

    def btn_2 (self) :
        plt.figure(figsize=(11, 6))
        self.label.clear()
        decoding_key = config.decoding_key2
        day = datetime.today().strftime('%Y%m%d') #오늘 날짜
        start_day = '20220720'
        params ={'serviceKey' : decoding_key, 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : start_day , 'endCreateDt' : day }
        xml = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson', params=params)
        xml_dict = xmltodict.parse(xml.text)    
        data = xml_dict['response']['body']['items']['item']
        df = pd.DataFrame(data)
        df.head(10)
        df_list = []
        a_list = ['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80 이상']
        for y in a_list :
            df_list.append(df[df['gubun']==y])
        df4 = pd.DataFrame()
        for df2 in df_list :
            df2 = df2.astype({'confCase' : 'float', 'gubun' : 'str'})
            df2['date'] = pd.to_datetime(df2['createDt'])
            df3 = df2[['gubun','confCase','date']]
            df4 = pd.concat((df4,df3.iloc[[0],:]),sort=False)
        plt.rcParams['font.family'] = 'Malgun Gothic'
        sns.barplot(x='gubun',y='confCase', data = df4, color = 'red')
        plt.xticks(rotation = 30)
        plt.savefig('./img/IMG2.png')

        pixmap = QPixmap('./img/IMG2.png')
        self.label.setPixmap(pixmap)


