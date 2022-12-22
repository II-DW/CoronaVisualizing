import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap
import config as config 

from PyQt5.QtWidgets import *
from PyQt5 import uic

New = uic.loadUiType(r"./ui/UI2.ui")[0] #두 번째창 ui
class window_4(QDialog,QWidget,New):
    def __init__(self):
        super(window_4,self).__init__()
        self.initUI()
        self.btn_4()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_4)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,1000,500)
        self.label.move(-10,-60)
        
    def Home(self):
        self.close() #창 닫기

    def btn_4 (self) :
        plt.figure(figsize=(11, 5.5))
        self.label.clear()
        start_day = '20220720'
        decoding_key = config.decoding_key4
        day = datetime.today().strftime('%Y%m%d') #오늘 날짜
        params ={'serviceKey' : decoding_key, 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : start_day , 'endCreateDt' : day }
        xml = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson', params=params)
        xml_dict = xmltodict.parse(xml.text)    
        data = xml_dict['response']['body']['items']['item']
        df = pd.DataFrame(data)
        df_list = []
        a_list = ['제주','경남','경북','전남','전북','충남','충북','강원','경기','세종','울산','대전','광주','인천','대구','부산','서울']
        for y in a_list :
            df_list.append(df[df['gubun']==y])
        df4 = pd.DataFrame()
        for df2 in df_list :
            df2 = df2.astype({'qurRate' : 'float', 'gubun' : 'str'})
            df2['date'] = pd.to_datetime(df2['createDt'])
            df3 = df2[['gubun','qurRate','date']]
            df4 = pd.concat((df4,df3.iloc[[0],:]),sort=False)
        plt.rcParams['font.family'] = 'Malgun Gothic'
        sns.barplot(x='gubun',y='qurRate', data = df4, color = 'blue')
        plt.savefig('./img/IMG4.png')

        pixmap = QPixmap('./img/IMG4.png')
        self.label.setPixmap(pixmap)


