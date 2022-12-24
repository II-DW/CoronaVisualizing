import requests
import xmltodict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap
import UI_code.config as config

from PyQt5.QtWidgets import *
from PyQt5 import uic

New = uic.loadUiType(r"./ui/UI4.ui")[0] #두 번째창 ui
class window_10(QDialog,QWidget,New):
    def __init__(self):
        super(window_10,self).__init__()
        self.initUI()
        self.btn_33()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_33)
        self.label = QLabel(self)
        self.label.move(10,10)
        
    def Home(self):
        self.close() #창 닫기

    def btn_33 (self) :
        self.label.clear()
        start_day = self.year.text() + self.month.text() + self.day.text()
        print(start_day)
        if start_day == "" :
            start_day = '20220720'
        Nation_NM = self.nation.text()
        print(Nation_NM)
        if Nation_NM == "" :
            Nation_NM = "일본"
        
        decoding_key = config.decoding_key32
        day = datetime.today().strftime('%Y%m%d') #오늘 날짜
        params ={'serviceKey' : decoding_key, 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : start_day , 'endCreateDt' : day }
        xml = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson', params=params)
        xml_dict = xmltodict.parse(xml.text)    
        data = xml_dict['response']['body']['items']['item']
        df = pd.DataFrame(data)
        df.head(10)    
        df_Nation = df[df['nationNm']==Nation_NM]

        df_Nation = df_Nation.astype({'natDeathCnt' : 'int','natDefCnt' : 'int'})
        df_Nation['date'] = pd.to_datetime(df_Nation['createDt'])
        df_Nation2 = df_Nation[['date','natDeathCnt','natDefCnt','nationNmEn','stdDay']]
        df_Nation2 = df_Nation2.sort_values(by='date')
        df_Nation2['daily_natDefCnt'] = df_Nation2['natDefCnt'].diff()

        temp = df_Nation2[df_Nation2['daily_natDefCnt']<=0].index

        df_Nation2 = df_Nation2.drop(temp)
        sns.relplot(x='date',y='daily_natDefCnt', data = df_Nation2, kind='line', aspect=2)
        plt.savefig('./img/IMG10.png')

        pixmap = QPixmap('./img/IMG10.png')
        self.label.setPixmap(pixmap)

