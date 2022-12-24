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

New = uic.loadUiType(r"./ui/UI2.ui")[0] #두 번째창 ui
class window_7(QDialog,QWidget,New):
    def __init__(self):
        super(window_7,self).__init__()
        self.initUI()
        self.btn_13()
        self.show() # 두번째창 실행


    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)
        self.reset.clicked.connect(self.btn_13)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,1000,500)
        self.label.move(-10,0)
        
    def Home(self):
        self.close() #창 닫기

    def btn_13 (self) :
        plt.figure(figsize=(11, 5))
        self.label.clear()
        plt.rcParams['font.family'] = 'Malgun Gothic'

        decoding_key = config.decoding_key13
        params ={'serviceKey' : decoding_key}
        json = requests.get('http://apis.data.go.kr/1790387/covid19HospitalBedStatus/covid19HospitalBedStatusJson', params=params).json()
        data = json['response']['result']
        a = {'a' : ['중환자병상','중환자병상','일반병상','일반병상'] ,'legendd' : ['보유병상수','가용병상수','보유병상수','가용병상수'],'b' : [int(data[0]['itsv_bed_rtn']),int(data[0]['itsv_bed_avlb']),int(data[0]['nm_bed_rtn']),int(data[0]['nm_bed_avlb'])]}
        df = pd.DataFrame(a)
        sns.barplot(x = 'a', y = 'b',data = df,hue = "legendd")
        plt.legend()
        plt.savefig('./img/IMG7.png')

        pixmap = QPixmap('./img/IMG7.png')
        self.label.setPixmap(pixmap)


