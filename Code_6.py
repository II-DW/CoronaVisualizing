import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5 import uic

New = uic.loadUiType(r"C:\Users\dowon\OneDrive\PYTHON\pyqt\UI1.ui")[0] #두 번째창 ui
class window_6(QDialog,QWidget,New):
    def __init__(self):
        super(window_6,self).__init__()
        self.initUI()
        self.btn_6()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_6)
        self.label = QLabel(self)
        self.label.move(10,10)
        
    def Home(self):
        self.close() #창 닫기

    def btn_6 (self) :
        self.label.clear()
        start_day = self.year.text() + self.month.text() + self.day.text()
        if start_day == "" :
            start_day = '20220720'
        decoding_key = 'hScrax2XxNGjs1gcynNRpIldiQEi3nYDi7f4B+KV05FDXh/OBvy1/6VtD0KzgfkkVKMdBkeKwyVTitQMaopiPw=='
        day = datetime.today().strftime('%Y%m%d') #오늘 날짜
        params ={'serviceKey' : decoding_key, 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : start_day , 'endCreateDt' : day }
        xml = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson', params=params)
        xml_dict = xmltodict.parse(xml.text)    
        data = xml_dict['response']['body']['items']['item']
        df = pd.DataFrame(data)
        df.head(10)
        df = df.astype({'deathCnt' : 'int','decideCnt' : 'int'})
        df['date'] = pd.to_datetime(df['createDt'])
        df3 = df[['date','deathCnt','decideCnt','updateDt']]
        df3 = df3.sort_values(by='date')
        df3['daily_natDefCnt'] = df3['deathCnt'].diff()

        temp = df3[df3['daily_natDefCnt']<=0].index

        df3 = df3.drop(temp)
        sns.relplot(x='date',y='daily_natDefCnt', data = df3, kind='line', aspect=2)
        plt.savefig('IMG6.png')

        pixmap = QPixmap('IMG6.png')
        self.label.setPixmap(pixmap)

