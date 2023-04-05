import os
os.system('cls')

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel,QListWidget

from datetime import datetime

import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'oq_tepa',
    user = 'root',
    password = 'sanjarbek2006'
)

mycursor = mydb.cursor()

class Kefsi(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.count_strp = 0

        self.count_strp3 = 0

        self.count_bayts = 0

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,700)
        self.btn_buy.setFixedSize(110,50)

        self.acceptDrops()

        self.setWindowTitle('CEFSI')

        self.setFixedSize(1200, 780)

        self.setStyleSheet('background-color: white')

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.logo_cefsi = QLabel(self)

        self.btn_joja_box = QPushButton(self)
        self.btn_joja_box.setText('Добавить')
        
        self.btn_strips = QPushButton(self)
        self.btn_strips.setText('Добавить')

        self.btn_strips_3 = QPushButton(self)
        self.btn_strips_3.setText('Добавить')

        self.btn_bayts = QPushButton(self)
        self.btn_bayts.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)

        self.initUi()

        self.btn_joja_box.clicked.connect(self.press_btn_joja)

    
    def initUi(self):


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)
    


        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)




        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)
    


        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.count_label = QLabel(self)
        self.count_label.setText('1')

        self.count_label.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)


        self.btn_plus = QPushButton(self)
        self.btn_plus.setText('+')

        self.btn_minus = QPushButton(self)
        self.btn_minus.setText('-')


        self.btn_minus.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus.setFixedSize(50,50)


        self.galochka_pixmax = QPixmap('D:Oqtepa/label_kefsi.png')

        self.galochka.setPixmap(self.galochka_pixmax)

        self.galochka.resize(self.galochka_pixmax.width(),self.galochka_pixmax.height())

        self.galochka_pixmax = QPixmap()

        # LOGO KEFSI
        self.logo_kefsi_pixmax = QPixmap('D:Oqtepa/logo_cefsi.png')

        self.logo_cefsi.setPixmap(self.logo_kefsi_pixmax)

        self.logo_cefsi.resize(self.logo_kefsi_pixmax.width(),self.logo_kefsi_pixmax.height())

        self.logo_kefsi_pixmax = QPixmap()

        #1

        self.pixmap1 = QPixmap('D:Oqtepa/joja_box.png')

        self.label1.setPixmap(self.pixmap1)

        self.label1.resize(self.pixmap1.width(),self.pixmap1.height())

        self.pixmap1 = QPixmap()

        self.btn_joja_box.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_joja_box.setFixedSize(110,50)
    

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/strips.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_strips.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_strips.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/strips_3.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_strips_3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_strips_3.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/bayts.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_bayts.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_bayts.setFixedSize(110,50)

        self.btn_plus.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus.setFixedSize(50,50)
        


        self.btn_joja_box.move(178,512)
        self.btn_strips.move(460,515)
        self.btn_oq2.move(458,151515)
        self.btn_strips_3.move(740,512)
        self.btn_bayts.move(1025,512)

        self.btn_minus.move(10000,100854)
        self.btn_plus.move(1000,1000)
        self.btn_minus2.move(10000,100854)
        self.btn_plus2.move(1000,1000)


        self.btn_plus3.move(10000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_oq1.move(10000,10000)
        self.btn_oq3.move(10000,10000)
        self.count_label3.move(100000,10000)


        self.btn_plus4.move(100000,184855)
        self.btn_minus4.move(100000,100000)
        self.btn_oq4.move(100000,100000)
        self.count_label4.move(10000,10000)



        self.label1.move(40,  250)
        self.label2.move(320,250)
        self.label3.move(600,250)
        self.label4.move(890,250)
        self.count_label2.move(100000,10000)
        self.count_label.move(10000,1000)

        self.logo_cefsi.move(380, 20)
        self.galochka.move(40, 200)
        self.btn_back.move(30,700)
    
        self.show()
    
        self.btn_back.clicked.connect(self.press_btn_back)
        self.btn_plus.clicked.connect(self.press_btn_plus)
        self.btn_minus.clicked.connect(self.press_btn_minus)
        

        self.btn_strips.clicked.connect(self.press_btn_strips)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        

        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_strips_3.clicked.connect(self.press_btn_strips3)


        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)
        self.btn_bayts.clicked.connect(self.press_btn_bayts)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count > 0:
            try:
                name_product = "JOJA BOX"
                num_of_product = f'{self.count}'
                price = 23_000 * int(self.count)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

        if self.count_strp > 0:
            try:
                name_product = "STRIPS 5 DONA"
                num_of_product = f'{self.count_strp}'
                price = 18000 * int(self.count_strp)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count_strp3 > 0:
            try:
                name_product = "STRIPS 3 DONA"
                num_of_product = f'{self.count_strp3}'
                price = 15000 * int(self.count_strp3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count_bayts > 0:
            try:
                name_product = "BAYTS"
                num_of_product = f'{self.count_bayts}'
                price = 13000 * int(self.count_bayts)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        


    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()

    
    def press_btn_joja(self):
        if self.count != -1:
            self.count+=1
            self.btn_joja_box.move(10000,10000)
            self.btn_oq1.move(178,514)
            self.btn_plus.move(230,512)
            self.btn_minus.move(170,512)
            self.count_label.move(220,555)
            self.count_label.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_strips(self):
        if self.count_strp != -1:
            self.count_strp+=1
            self.btn_strips.move(100000,10000)
            self.btn_oq2.move(458,515)
            self.btn_plus2.move(510,515)
            self.btn_minus2.move(450,515)
            self.count_label2.move(502,556)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_strips3(self):
        if self.count_strp3 != -1:
            self.count_strp3 += 1
            self.btn_strips_3.move(100000,10000)
            self.btn_oq3.move(740,512)
            self.btn_plus3.move(792,515)
            self.btn_minus3.move(732,515)
            self.count_label3.move(783,553)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_bayts(self):
        if self.count_bayts != -1:
            self.count_bayts+=1
            self.btn_bayts.move(100000,10000)
            self.btn_oq4.move(1025,512)
            self.btn_plus4.move(1077,515)
            self.btn_minus4.move(1017,515)
            self.count_label4.move(1068,556)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )



    def press_btn_plus2(self):
        self.count_strp += 1
        self.count_label2.setText(f'{self.count_strp}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus2(self):
        if self.count_strp == 1:
            self.count_strp -= 1
            self.btn_strips.move(460,515)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_strp != 0:
            self.count_strp -= 1
            self.count_label2.setText(f'{self.count_strp}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
            

    
    def press_btn_plus(self):
        self.count += 1
        self.count_label.setText(f'{self.count}')
        self.count_label.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    
    def press_btn_minus(self):
        if self.count == 1:
            self.count -= 1
            self.btn_joja_box.move(178,515)
            self.btn_plus.move(100000,10000)
            self.btn_minus.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label.move(1000,1000)
            self.count_label.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count != 0:
            self.count -= 1
            self.count_label.setText(f'{self.count}')
            self.count_label.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    def press_btn_plus3(self):
        self.count_strp3 += 1
        self.count_label3.setText(f'{self.count_strp3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus3(self):
        if self.count_strp3 == 1:
            self.count_strp3 -= 1
            self.btn_strips_3.move(740,515)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_strp3 != 0:
            self.count_strp3 -= 1
            self.count_label3.setText(f'{self.count_strp3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_plus4(self):
        self.count_bayts += 1
        self.count_label4.setText(f'{self.count_bayts}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus4(self):
        if self.count_bayts == 1:
            self.count_bayts -= 1
            self.btn_bayts.move(1025,515)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_bayts != 0:
            self.count_bayts -= 1
            self.count_label4.setText(f'{self.count_bayts}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    




class set(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count_baraka = 0

        self.count_juftlik = 0
        
        self.count_oqtepa1 = 0

        self.count_oqtepa2 = 0

        self.acceptDrops()

        self.setWindowTitle('SET')

        self.setFixedSize(1200, 780)

        self.setStyleSheet('background-color: white')   

        self.label1 = QLabel(self)

        self.galochka = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.logo_set = QLabel(self)

        self.btn_baraka = QPushButton(self)
        self.btn_baraka.setText('Добавить')
        
        self.btn_juftlik = QPushButton(self)
        self.btn_juftlik.setText('Добавить')

        self.btn_oqtepa_2 = QPushButton(self)
        self.btn_oqtepa_2.setText('Добавить')

        self.btn_oqtepa_1 = QPushButton(self)
        self.btn_oqtepa_1.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,700)

        self.initUi()

    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,700)
        self.btn_buy.setFixedSize(110,50)


        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)



        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')



        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')



        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')


        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')


        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')


        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)


        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)


        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)



        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)


        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)


        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)


        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        # LOGO KEFSI
        self.pixmax = QPixmap('D:Oqtepa/label_set.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/Baraka.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_baraka.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_baraka.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/Juftlik.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_juftlik.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_juftlik.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/oqtepa_2.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_oqtepa_2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oqtepa_2.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/oqtepa_1.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_oqtepa_1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oqtepa_1.setFixedSize(110,50)


        self.btn_baraka.move(178,512)
        self.btn_juftlik.move(458,515)
        self.btn_oqtepa_2.move(738,512)
        self.btn_oqtepa_1.move(1025,512)

        self.label1.move(40,  250)
        self.label2.move(320,250)
        self.label3.move(600,250)
        self.label4.move(890,250)

        # self.logo_set.move(380, 20)
        self.galochka.move(40, 200)


        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)

        self.btn_baraka.clicked.connect(self.press_btn_baraka)
        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_minus1.clicked.connect(self.press_btn_minus1)

        self.btn_juftlik.clicked.connect(self.press_btn_juftlik)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)

        self.btn_oqtepa_2.clicked.connect(self.press_btn_oqtepa1)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)

        self.btn_oqtepa_1.clicked.connect(self.press_btn_oqtepa2)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)

        self.count_label1.move(10000,10000)
        self.count_label2.move(10000,10000)
        self.count_label3.move(10000,10000)
        self.count_label4.move(10000,10000)

        self.btn_plus1.move(10000,10000)
        self.btn_plus2.move(10000,10000)
        self.btn_plus3.move(10000,10000)
        self.btn_plus4.move(10000,10000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)



        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count_baraka > 0:
            try:
                name_product = "SET BARAKA"
                num_of_product = f'{self.count_baraka}'
                price = 114_000 * int(self.count_baraka)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
    
        if self.count_juftlik > 0:
            try:
                name_product = "SET JUFTLIK"
                num_of_product = f'{self.count_juftlik}'
                price = 50_000 * int(self.count_juftlik)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count_oqtepa2 > 0:
            try:
                name_product = "SET OQTEPA #1"
                num_of_product = f'{self.count_oqtepa2}'
                price = 16_000 * int(self.count_oqtepa2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count_oqtepa1 > 0:
            try:
                name_product = "SET OQTEPA #2"
                num_of_product = f'{self.count_oqtepa1}'
                price = 16_000 * int(self.count_oqtepa1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()



    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()


    def press_btn_baraka(self):
        if self.count_baraka != -1:
            self.count_baraka += 1
            self.btn_baraka.move(10000,10000)
            self.btn_oq1.move(178,512)
            self.btn_plus1.move(230,512)
            self.btn_minus1.move(170,512)
            self.count_label1.move(220,555)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_juftlik(self):
        if self.count_juftlik != -1:
            self.count_juftlik += 1
            self.btn_juftlik.move(10000,10000)
            self.btn_oq2.move(458,515)
            self.btn_plus2.move(510,515)
            self.btn_minus2.move(450,515)
            self.count_label2.move(502,556)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_oqtepa1(self):
        if self.count_oqtepa1 != -1:
            self.count_oqtepa1 += 1
            self.btn_oqtepa_2.move(10000,10000)
            self.btn_oq3.move(738,515)
            self.btn_plus3.move(790,512)
            self.btn_minus3.move(730,512)
            self.count_label3.move(781,553)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    
    def press_btn_oqtepa2(self):
        if self.count_oqtepa2 != -1:
            self.count_oqtepa2 += 1
            self.btn_oqtepa_1.move(10000,10000)
            self.btn_oq4.move(1025,512)
            self.btn_plus4.move(1077,512)
            self.btn_minus4.move(1017,512)
            self.count_label4.move(1068,556)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_plus1(self):
        self.count_baraka += 1
        self.count_label1.setText(f'{self.count_baraka}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count_juftlik += 1
        self.count_label2.setText(f'{self.count_juftlik}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_plus3(self):
        self.count_oqtepa1 += 1
        self.count_label3.setText(f'{self.count_oqtepa1}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus4(self):
        self.count_oqtepa2 += 1
        self.count_label4.setText(f'{self.count_oqtepa2}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    


    def press_btn_minus1(self):
        if self.count_baraka == 1:
            self.count_baraka -= 1
            self.btn_baraka.move(178,512)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_baraka != 0:
            self.count_baraka -= 1
            self.count_label1.setText(f'{self.count_baraka}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count_juftlik == 1:
            self.count_juftlik -= 1
            self.btn_juftlik.move(458,512)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_juftlik != 0:
            self.count_juftlik -= 1
            self.count_label2.setText(f'{self.count_juftlik}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus3(self):
        if self.count_oqtepa1 == 1:
            self.count_oqtepa1 -= 1
            self.btn_oqtepa_2.move(738,512)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_oqtepa1 != 0:
            self.count_oqtepa1 -= 1
            self.count_label3.setText(f'{self.count_oqtepa1}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        
    

    def press_btn_minus4(self):
        if self.count_oqtepa2 == 1:
            self.count_oqtepa2 -= 1
            self.btn_oqtepa_1.move(1025,512)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(10000,10000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count_oqtepa2 != 0:
            self.count_oqtepa2 -= 1
            self.count_label4.setText(f'{self.count_oqtepa2}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


class lavash(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0 

        self.count5 = 0 

        self.count6 = 0 

        self.count7 = 0 


        self.acceptDrops()

        self.setWindowTitle('LAVASH')

        self.setFixedSize(1200, 900)

        self.setStyleSheet('background-color: white')

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.label5 = QLabel(self)

        self.label6 = QLabel(self)

        self.label7 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_tandir_sir = QPushButton(self)
        self.btn_tandir_sir.setText('Добавить')
        
        self.btn_sir = QPushButton(self)
        self.btn_sir.setText('Добавить')

        self.btn_tandir = QPushButton(self)
        self.btn_tandir.setText('Добавить')

        self.btn_xalapen = QPushButton(self)
        self.btn_xalapen.setText('Добавить')

        self.btn_original = QPushButton(self)
        self.btn_original.setText('Добавить')

        self.btn_mini = QPushButton(self)
        self.btn_mini.setText('Добавить')

        self.btn_original_mini = QPushButton(self)
        self.btn_original_mini.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(35,810)


        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,815)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.btn_oq5 = QPushButton(self)
        self.btn_oq5.setText('')
        self.btn_oq5.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq5.setFixedSize(110,50)


        self.btn_oq6 = QPushButton(self)
        self.btn_oq6.setText('')
        self.btn_oq6.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq6.setFixedSize(110,50)


        self.btn_oq7 = QPushButton(self)
        self.btn_oq7.setText('')
        self.btn_oq7.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq7.setFixedSize(110,50)



        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label5 = QLabel(self)
        self.count_label5.setText('1')

        self.count_label6 = QLabel(self)
        self.count_label6.setText('1')

        self.count_label7 = QLabel(self)
        self.count_label7.setText('1')


        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')

        self.btn_plus5 = QPushButton(self)
        self.btn_plus5.setText('+')

        self.btn_plus6 = QPushButton(self)
        self.btn_plus6.setText('+')

        self.btn_plus7 = QPushButton(self)
        self.btn_plus7.setText('+')

        

        self.btn_minus7 = QPushButton(self)
        self.btn_minus7.setText('-')

        self.btn_minus6 = QPushButton(self)
        self.btn_minus6.setText('-')

        self.btn_minus5 = QPushButton(self)
        self.btn_minus5.setText('-')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')

        self.btn_minus7.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus7.setFixedSize(50,50)

        self.btn_minus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus6.setFixedSize(50,50)

        self.btn_minus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus5.setFixedSize(50,50)

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)



        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)


        self.btn_plus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus5.setFixedSize(50,50)


        self.btn_plus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus6.setFixedSize(50,50)



        self.btn_plus7.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus7.setFixedSize(50,50)


        # LOGO LAVASH
        self.pixmax = QPixmap('D:Oqtepa/logo_lavash.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/tandir_sir.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_tandir_sir.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_tandir_sir.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/sir.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_sir.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_sir.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/tandir.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_tandir.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_tandir.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/xalapen.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_xalapen.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_xalapen.setFixedSize(110,50)


        self.pixmap5 = QPixmap('D:Oqtepa/original.png')

        self.label5.setPixmap(self.pixmap5)

        self.label5.resize(self.pixmap5.width(), self.pixmap5.height())
      
        self.pixmap5 = QPixmap()

        self.btn_original.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_original.setFixedSize(110,50)


        self.pixmap6 = QPixmap('D:Oqtepa/mini_sir.png')

        self.label6.setPixmap(self.pixmap6)

        self.label6.resize(self.pixmap6.width(), self.pixmap6.height())
      
        self.pixmap6 = QPixmap()

        self.btn_mini.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_mini.setFixedSize(110,50)


        self.pixmap7 = QPixmap('D:Oqtepa/original_mini.png')

        self.label7.setPixmap(self.pixmap7)

        self.label7.resize(self.pixmap7.width(), self.pixmap7.height())
      
        self.pixmap7 = QPixmap()

        self.btn_original_mini.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_original_mini.setFixedSize(110,50)




        self.btn_tandir_sir.move(178,350)
        self.btn_sir.move(458,350)
        self.btn_tandir.move(738,350)
        self.btn_xalapen.move(1025,347)
        self.btn_original.move(178,714)
        self.btn_mini.move(458,714)
        self.btn_original_mini.move(738,714)

        self.label1.move(40,  85)
        self.label2.move(320,85)
        self.label3.move(600,85)
        self.label4.move(890,85)
        self.label5.move(40,450)
        self.label6.move(320,450)
        self.label7.move(600,450)

        # self.logo_lavash.move(380, 20)
        self.galochka.move(38, 30)


        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)


        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)
        self.count_label5.move(100000,10000)
        self.count_label6.move(100000,10000)
        self.count_label7.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)
        self.btn_plus5.move(10000,100000)
        self.btn_plus6.move(10000,100000)
        self.btn_plus7.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)
        self.btn_minus5.move(100000,10000)
        self.btn_minus6.move(100000,10000)
        self.btn_minus7.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)
        self.btn_oq5.move(1000000,10000)
        self.btn_oq6.move(1000000,10000)
        self.btn_oq7.move(1000000,10000)

        self.btn_tandir_sir.clicked.connect(self.press_btn_tandir_sir)
        self.btn_sir.clicked.connect(self.press_btn_sir)
        self.btn_tandir.clicked.connect(self.press_btn_tandir)
        self.btn_xalapen.clicked.connect(self.press_btn_xalapen)
        self.btn_original.clicked.connect(self.press_btn_original)
        self.btn_mini.clicked.connect(self.press_btn_mini)
        self.btn_original_mini.clicked.connect(self.press_btn_original_mini)

        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_plus5.clicked.connect(self.press_btn_plus5)
        self.btn_plus6.clicked.connect(self.press_btn_plus6)
        self.btn_plus7.clicked.connect(self.press_btn_plus7)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)
        self.btn_minus5.clicked.connect(self.press_btn_minus5)
        self.btn_minus6.clicked.connect(self.press_btn_minus6)
        self.btn_minus7.clicked.connect(self.press_btn_minus7)


        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "TANDIR SIRLI LAVASH"
                num_of_product = f'{self.count1}'
                price = 30_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "SIRLI LAVASH"
                num_of_product = f'{self.count2}'
                price = 29_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count3 > 0:
            try:
                name_product = "TANDIR LAVASH"
                num_of_product = f'{self.count3}'
                price = 27_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count4 > 0:
            try:
                name_product = "XALAPENO LAVASH"
                num_of_product = f'{self.count4}'
                price = 27_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

        if self.count5 > 0:
            try:
                name_product = "ORIGINAL LAVASH"
                num_of_product = f'{self.count5}'
                price = 26_000 * int(self.count5)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count6 > 0:
            try:
                name_product = "MINI LAVASH SIRLI"
                num_of_product = f'{self.count6}'
                price = 25_000 * int(self.count6)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count7 > 0:
            try:
                name_product = "ORIGINAL MINI LAVASH"
                num_of_product = f'{self.count7}'
                price = 22_000 * int(self.count7)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
            self.close()
            self.menu = MenuPage()
            self.menu.show()

    
    def press_btn_tandir_sir(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_tandir_sir.move(10000,100000)
            self.btn_oq1.move(180,350)
            self.btn_plus1.move(230,350)
            self.btn_minus1.move(170,350)
            self.count_label1.move(220,388)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_sir(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_sir.move(10000,100000)
            self.btn_oq2.move(458,350)
            self.btn_plus2.move(510,350)
            self.btn_minus2.move(450,350)
            self.count_label2.move(502,388)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_tandir(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_tandir.move(10000,100000)
            self.btn_oq3.move(738,350)
            self.btn_plus3.move(790,350)
            self.btn_minus3.move(730,350)
            self.count_label3.move(781,388)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_xalapen(self):
        if self.count4 != -1:
            self.count4 += 1
            self.btn_xalapen.move(10000,100000)
            self.btn_oq4.move(1025,346)
            self.btn_plus4.move(1077,350)
            self.btn_minus4.move(1017,350)
            self.count_label4.move(1068,388)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    def press_btn_original(self):
        if self.count5 != -1:
            self.count5 += 1
            self.btn_original.move(10000,100000)
            self.btn_oq5.move(178,714)
            self.btn_plus5.move(230,714)
            self.btn_minus5.move(170,714)
            self.count_label5.move(220,752)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_mini(self):
        if self.count6 != -1:
            self.count6 += 1
            self.btn_mini.move(10000,100000)
            self.btn_oq6.move(458,714)
            self.btn_plus6.move(510,714)
            self.btn_minus6.move(450,714)
            self.count_label6.move(502,752)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_original_mini(self):
        if self.count7 != -1:
            self.count7 += 1
            self.btn_original_mini.move(10000,100000)
            self.btn_oq7.move(738,714)
            self.btn_plus7.move(790,714)
            self.btn_minus7.move(730,714)
            self.count_label7.move(781,752)
            self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
  
    def press_btn_plus5(self):
        self.count5 += 1
        self.count_label5.setText(f'{self.count5}')
        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus6(self):
        self.count6 += 1
        self.count_label6.setText(f'{self.count6}')
        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus7(self):
        self.count7 += 1
        self.count_label7.setText(f'{self.count7}')
        self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    


    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1  -= 1
            self.btn_tandir_sir.move(178,350)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1  != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2  -= 1
            self.btn_sir.move(458,350)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2  != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3  -= 1
            self.btn_tandir.move(738,350)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3  != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4  -= 1
            self.btn_xalapen.move(1025,347)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4  != 0:
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus5(self):
        if self.count5 == 1:
            self.count5  -= 1
            self.btn_original.move(178,714)
            self.btn_plus5.move(100000,10000)
            self.btn_minus5.move(100000,10000)
            self.btn_oq5.move(100000,10000)
            self.count_label5.move(1000,1000)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count5  != 0:
            self.count5 -= 1
            self.count_label5.setText(f'{self.count5}')
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus6(self):
        if self.count6 == 1:
            self.count6  -= 1
            self.btn_mini.move(458,714)
            self.btn_plus6.move(100000,10000)
            self.btn_minus6.move(100000,10000)
            self.btn_oq6.move(100000,10000)
            self.count_label6.move(1000,1000)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count6  != 0:
            self.count6 -= 1
            self.count_label6.setText(f'{self.count6}')
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus7(self):
        if self.count7 == 1:
            self.count7  -= 1
            self.btn_original_mini.move(738,714)
            self.btn_plus7.move(100000,10000)
            self.btn_minus7.move(100000,10000)
            self.btn_oq7.move(100000,10000)
            self.count_label7.move(1000,1000)
            self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count7  != 0:
            self.count7 -= 1
            self.count_label7.setText(f'{self.count7}')
            self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()

class clab_xaggi(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0

        self.acceptDrops()

        self.setWindowTitle('CLAB AND XAGGi')

        self.setFixedSize(750, 700)

        self.setStyleSheet('background-color: white')

        self.galochka = QLabel(self)

        self.galochka2 = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.logo_set = QLabel(self)

        self.btn_xaggi = QPushButton(self)
        self.btn_xaggi.setText('Добавить')
        
        self.btn_club = QPushButton(self)
        self.btn_club.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,610)

        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(600,610)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')


        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)


        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        
        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)


        # LOGO XAGGI AND CLUP
        self.pixmax = QPixmap('D:Oqtepa/logo_haggi.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()



        self.pixmax_clab = QPixmap('D:Oqtepa/clab_logo.png')

        self.galochka2.setPixmap(self.pixmax_clab)

        self.galochka2.resize(self.pixmax_clab.width(),self.pixmax_clab.height())

        self.pixmax_clab = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/xaggi.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_xaggi.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_xaggi.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/clab.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_club.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_club.setFixedSize(110,50)



        self.btn_xaggi.move(230,511)
        self.btn_club.move(540,513)

        self.label1.move(90,250)
        self.label2.move(400,250)

        self.galochka.move(90, 200)
        self.galochka2.move(400, 200)

        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)


        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)

        self.btn_xaggi.clicked.connect(self.press_btn_xaggi)
        self.btn_club.clicked.connect(self.press_btn_clab)

        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "XAGGI"
                num_of_product = f'{self.count1}'
                price = 29_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

        if self.count2 > 0:
            try:
                name_product = "CLAB SENDVICH"
                num_of_product = f'{self.count2}'
                price = 27_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
        
            self.close()
            self.menu = MenuPage()
            self.menu.show()



    def press_btn_xaggi(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_xaggi.move(10000,100000)
            self.btn_oq1.move(230,511)
            self.btn_plus1.move(280,511)
            self.btn_minus1.move(220,511)
            self.count_label1.move(270,549)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_clab(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_club.move(10000,100000)
            self.btn_oq2.move(540,513)
            self.btn_plus2.move(590,513)
            self.btn_minus2.move(530,513)
            self.count_label2.move(580,552)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_xaggi.move(230,511)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1 != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_club.move(540,513)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2 != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )




    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()


class hamburger(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0 

        self.count5 = 0 

        self.count6 = 0 


        self.acceptDrops()

        self.setWindowTitle('LAVASH')


        self.setFixedSize(1200, 900)

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.label5 = QLabel(self)

        self.label6 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_big_chizburger = QPushButton(self)
        self.btn_big_chizburger.setText('Добавить')
        
        self.btn_big_hamburger = QPushButton(self)
        self.btn_big_hamburger.setText('Добавить')

        self.btn_big_donar = QPushButton(self)
        self.btn_big_donar.setText('Добавить')

        self.btn_chizburger = QPushButton(self)
        self.btn_chizburger.setText('Добавить')

        self.btn_hamburger = QPushButton(self)
        self.btn_hamburger.setText('Добавить')

        self.btn_shaurma = QPushButton(self)
        self.btn_shaurma.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)

        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,800)
        self.btn_buy.setFixedSize(110,50)


        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.btn_oq5 = QPushButton(self)
        self.btn_oq5.setText('')
        self.btn_oq5.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq5.setFixedSize(110,50)


        self.btn_oq6 = QPushButton(self)
        self.btn_oq6.setText('')
        self.btn_oq6.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq6.setFixedSize(110,50)

        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label5 = QLabel(self)
        self.count_label5.setText('1')

        self.count_label6 = QLabel(self)
        self.count_label6.setText('1')



        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')

        self.btn_plus5 = QPushButton(self)
        self.btn_plus5.setText('+')

        self.btn_plus6 = QPushButton(self)
        self.btn_plus6.setText('+')


        self.btn_minus6 = QPushButton(self)
        self.btn_minus6.setText('-')

        self.btn_minus5 = QPushButton(self)
        self.btn_minus5.setText('-')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')



        self.btn_minus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus6.setFixedSize(50,50)

        self.btn_minus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus5.setFixedSize(50,50)

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)



        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)


        self.btn_plus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus5.setFixedSize(50,50)


        self.btn_plus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus6.setFixedSize(50,50)


        # LOGO HAMBURGER
        self.pixmax = QPixmap('D:Oqtepa/logo_hamburger.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/big_chizburger.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_big_chizburger.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_big_chizburger.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/big_burger.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_big_hamburger.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_big_hamburger.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/big_donar.png')

        self.setStyleSheet('background-color: white')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_big_donar.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_big_donar.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/chizburger.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_chizburger.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_chizburger.setFixedSize(110,50)


        self.pixmap5 = QPixmap('D:Oqtepa/gamburger.png')

        self.label5.setPixmap(self.pixmap5)

        self.label5.resize(self.pixmap5.width(), self.pixmap5.height())
      
        self.pixmap5 = QPixmap()

        self.btn_hamburger.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_hamburger.setFixedSize(110,50)


        self.pixmap6 = QPixmap('D:Oqtepa/shaurma.png')

        self.label6.setPixmap(self.pixmap6)

        self.label6.resize(self.pixmap6.width(), self.pixmap6.height())
      
        self.pixmap6 = QPixmap()

        self.btn_shaurma.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_shaurma.setFixedSize(110,50)


        self.btn_big_chizburger.move(178,350)
        self.btn_big_hamburger.move(458,350)
        self.btn_big_donar.move(738,350)
        self.btn_chizburger.move(1025,347)
        self.btn_hamburger.move(178,714)
        self.btn_shaurma.move(458,714)

        self.label1.move(40,  85)
        self.label2.move(320,85)
        self.label3.move(600,85)
        self.label4.move(890,85)
        self.label5.move(40,450)
        self.label6.move(320,450)

        # self.logo_lavash.move(380, 20)
        self.galochka.move(38, 30)


        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)


        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)
        self.count_label5.move(100000,10000)
        self.count_label6.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)
        self.btn_plus5.move(10000,100000)
        self.btn_plus6.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)
        self.btn_minus5.move(100000,10000)
        self.btn_minus6.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)
        self.btn_oq5.move(1000000,10000)
        self.btn_oq6.move(1000000,10000)


        self.btn_big_chizburger.clicked.connect(self.press_btn_big_chizburger)
        self.btn_big_hamburger.clicked.connect(self.press_btn_big_hamburger)
        self.btn_big_donar.clicked.connect(self.press_btn_big_donar)
        self.btn_chizburger.clicked.connect(self.press_btn_chizburger)
        self.btn_hamburger.clicked.connect(self.press_btn_hamburger)
        self.btn_shaurma.clicked.connect(self.press_btn_shaurma)



        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_plus5.clicked.connect(self.press_btn_plus5)
        self.btn_plus6.clicked.connect(self.press_btn_plus6)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)
        self.btn_minus5.clicked.connect(self.press_btn_minus5)
        self.btn_minus6.clicked.connect(self.press_btn_minus6)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "BIG CHIZBURGER"
                num_of_product = f'{self.count1}'
                price = 35_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        

        if self.count2 > 0:
            try:
                name_product = "BIG BURGER"
                num_of_product = f'{self.count2}'
                price = 31_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count3  > 0:
            try:
                name_product = "BIG DONAR"
                num_of_product = f'{self.count3 }'
                price = 25_000 * int(self.count3 )
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count4 > 0:
            try:
                name_product = "CHIZBURGER"
                num_of_product = f'{self.count4}'
                price = 23_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        

        if self.count5 > 0:
            try:
                name_product = "GAMBURGER"
                num_of_product = f'{self.count5}'
                price = 21_000 * int(self.count5)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count6 > 0:
            try:
                name_product = "SHAURMA"
                num_of_product = f'{self.count6}'
                price = 21_000 * int(self.count6)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()




    
    
    def press_btn_big_chizburger(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_big_chizburger.move(10000,100000)
            self.btn_oq1.move(178,350)
            self.btn_plus1.move(228,350)
            self.btn_minus1.move(168,350)
            self.count_label1.move(222,388)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_big_hamburger(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_big_hamburger.move(10000,100000)
            self.btn_oq2.move(458,350)
            self.btn_plus2.move(510,350)
            self.btn_minus2.move(450,350)
            self.count_label2.move(502,388)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_big_donar(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_big_donar.move(10000,100000)
            self.btn_oq3.move(738,350)
            self.btn_plus3.move(790,350)
            self.btn_minus3.move(730,350)
            self.count_label3.move(781,388)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_chizburger(self):
        if self.count4 != -1:
            self.count4 += 1
            self.btn_chizburger.move(10000,100000)
            self.btn_oq4.move(1025,346)
            self.btn_plus4.move(1077,350)
            self.btn_minus4.move(1017,350)
            self.count_label4.move(1068,388)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_hamburger(self):
        if self.count5 != -1:
            self.count5 += 1
            self.btn_hamburger.move(10000,100000)
            self.btn_oq5.move(178,714)
            self.btn_plus5.move(230,714)
            self.btn_minus5.move(170,714)
            self.count_label5.move(220,752)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_shaurma(self):
        if self.count6 != -1:
            self.count6 += 1
            self.btn_shaurma.move(10000,100000)
            self.btn_oq6.move(458,714)
            self.btn_plus6.move(510,714)
            self.btn_minus6.move(450,714)
            self.count_label6.move(502,752)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
  
    def press_btn_plus5(self):
        self.count5 += 1
        self.count_label5.setText(f'{self.count5}')
        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus6(self):
        self.count6 += 1
        self.count_label6.setText(f'{self.count6}')
        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    
    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_big_chizburger.move(178,350)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1 != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_big_hamburger.move(458,350)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2 != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3 -= 1
            self.btn_big_donar.move(738,350)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3 != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4 -= 1
            self.btn_chizburger.move(1025,347)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4 != 0:
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus5(self):
        if self.count5 == 1:
            self.count5 -= 1
            self.btn_hamburger.move(178,714)
            self.btn_plus5.move(100000,10000)
            self.btn_minus5.move(100000,10000)
            self.btn_oq5.move(100000,10000)
            self.count_label5.move(1000,1000)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count5 != 0:
            self.count5 -= 1
            self.count_label5.setText(f'{self.count5}')
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus6(self):
        if self.count6 == 1:
            self.count6 -= 1
            self.btn_shaurma.move(458,714)
            self.btn_plus6.move(100000,10000)
            self.btn_minus6.move(100000,10000)
            self.btn_oq6.move(100000,10000)
            self.count_label6.move(1000,1000)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count6 != 0:
            self.count6 -= 1
            self.count_label6.setText(f'{self.count6}')
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )





    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()


class pizza(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0 

        self.count5 = 0 

        self.count6 = 0 

        self.acceptDrops()

        self.setWindowTitle('PIZZA')

        self.setFixedSize(1200, 900)

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.label5 = QLabel(self)

        self.label6 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_kazi = QPushButton(self)
        self.btn_kazi.setText('Добавить')
        
        self.btn_asarti = QPushButton(self)
        self.btn_asarti.setText('Добавить')

        self.btn_gusht = QPushButton(self)
        self.btn_gusht.setText('Добавить')

        self.btn_pepperoni = QPushButton(self)
        self.btn_pepperoni.setText('Добавить')

        self.btn_gribnaya = QPushButton(self)
        self.btn_gribnaya.setText('Добавить')

        self.btn_tovuq = QPushButton(self)
        self.btn_tovuq.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)

        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,805)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.btn_oq5 = QPushButton(self)
        self.btn_oq5.setText('')
        self.btn_oq5.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq5.setFixedSize(110,50)


        self.btn_oq6 = QPushButton(self)
        self.btn_oq6.setText('')
        self.btn_oq6.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq6.setFixedSize(110,50)


        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label5 = QLabel(self)
        self.count_label5.setText('1')

        self.count_label6 = QLabel(self)
        self.count_label6.setText('1')



        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')

        self.btn_plus5 = QPushButton(self)
        self.btn_plus5.setText('+')

        self.btn_plus6 = QPushButton(self)
        self.btn_plus6.setText('+')


        self.btn_minus6 = QPushButton(self)
        self.btn_minus6.setText('-')

        self.btn_minus5 = QPushButton(self)
        self.btn_minus5.setText('-')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')



        self.btn_minus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus6.setFixedSize(50,50)

        self.btn_minus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus5.setFixedSize(50,50)

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)

        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)


        self.btn_plus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus5.setFixedSize(50,50)


        self.btn_plus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus6.setFixedSize(50,50)


        # LOGO PIZZA
        self.pixmax = QPixmap('D:Oqtepa/logo_pizza.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/qazi.png')

        self.setStyleSheet('background-color: white')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_kazi.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_kazi.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/asarti.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_asarti.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_asarti.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/gushtli.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_gusht.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_gusht.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/pepperoni.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_pepperoni.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_pepperoni.setFixedSize(110,50)


        self.pixmap5 = QPixmap('D:Oqtepa/gribnaya.png')

        self.label5.setPixmap(self.pixmap5)

        self.label5.resize(self.pixmap5.width(), self.pixmap5.height())
      
        self.pixmap5 = QPixmap()

        self.btn_gribnaya.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_gribnaya.setFixedSize(110,50)

        self.pixmap6 = QPixmap('D:Oqtepa/kurinnaya.png')

        self.label6.setPixmap(self.pixmap6)

        self.label6.resize(self.pixmap6.width(), self.pixmap6.height())
      
        self.pixmap6 = QPixmap()

        self.btn_tovuq.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_tovuq.setFixedSize(110,50)


        self.btn_kazi.move(178,350)
        self.btn_asarti.move(458,350)
        self.btn_gusht.move(738,350)
        self.btn_pepperoni.move(1025,347)
        self.btn_gribnaya.move(178,714)
        self.btn_tovuq.move(458,714)

        self.label1.move(40,  85)
        self.label2.move(320,85)
        self.label3.move(600,85)
        self.label4.move(890,85)
        self.label5.move(40,450)
        self.label6.move(320,450)

        # self.logo_lavash.move(380, 20)
        self.galochka.move(38, 30)

        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)


        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)
        self.count_label5.move(100000,10000)
        self.count_label6.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)
        self.btn_plus5.move(10000,100000)
        self.btn_plus6.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)
        self.btn_minus5.move(100000,10000)
        self.btn_minus6.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)
        self.btn_oq5.move(1000000,10000)
        self.btn_oq6.move(1000000,10000)


        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_plus5.clicked.connect(self.press_btn_plus5)
        self.btn_plus6.clicked.connect(self.press_btn_plus6)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)
        self.btn_minus5.clicked.connect(self.press_btn_minus5)
        self.btn_minus6.clicked.connect(self.press_btn_minus6)

        self.btn_kazi.clicked.connect(self.press_btn_kazi)
        self.btn_asarti.clicked.connect(self.press_btn_asarti)
        self.btn_gusht.clicked.connect(self.press_btn_gusht)
        self.btn_pepperoni.clicked.connect(self.press_btn_pepperoni)
        self.btn_gribnaya.clicked.connect(self.press_btn_gribnaya)
        self.btn_tovuq.clicked.connect(self.press_btn_tovuq)


        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "PIZZA KAZI"
                num_of_product = f'{self.count1}'
                price = 83_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "PIZZA ASARTI"
                num_of_product = f'{self.count2}'
                price = 78_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

        if self.count3 > 0:
            try:
                name_product = "PIZZA GO'SHTLI"
                num_of_product = f'{self.count3}'
                price = 78_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count4 > 0:
            try:
                name_product = "PIZZA PEPPERONI"
                num_of_product = f'{self.count4}'
                price = 69_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        

        if self.count5 > 0:
            try:
                name_product = "PIZZA GRIBNAYA"
                num_of_product = f'{self.count5}'
                price = 67_000 * int(self.count5)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count6  > 0:
            try:
                name_product = "PIZZA TOVUQLI"
                num_of_product = f'{self.count6 }'
                price = 67_000 * int(self.count6 )
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()




    def press_btn_kazi(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_kazi.move(10000,100000)
            self.btn_oq1.move(178,347)
            self.btn_plus1.move(228,350)
            self.btn_minus1.move(168,350)
            self.count_label1.move(222,388)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_asarti(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_asarti.move(10000,100000)
            self.btn_oq2.move(458,347)
            self.btn_plus2.move(510,350)
            self.btn_minus2.move(450,350)
            self.count_label2.move(502,388)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_gusht(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_gusht.move(10000,100000)
            self.btn_oq3.move(738,350)
            self.btn_plus3.move(790,350)
            self.btn_minus3.move(730,350)
            self.count_label3.move(781,388)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_pepperoni(self):
        if self.count4 != -1:
            self.count4 += 1
            self.btn_pepperoni.move(10000,100000)
            self.btn_oq4.move(1027,350)
            self.btn_plus4.move(1077,350)
            self.btn_minus4.move(1017,350)
            self.count_label4.move(1068,388)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_gribnaya(self):
        if self.count5 != -1:
            self.count5 += 1
            self.btn_gribnaya.move(10000,100000)
            self.btn_oq5.move(178,714)
            self.btn_plus5.move(230,714)
            self.btn_minus5.move(170,714)
            self.count_label5.move(220,752)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_tovuq(self):
        if self.count6 != -1:
            self.count6 += 1
            self.btn_tovuq.move(10000,100000)
            self.btn_oq6.move(458,714)
            self.btn_plus6.move(510,714)
            self.btn_minus6.move(450,714)
            self.count_label6.move(502,752)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
  
    def press_btn_plus5(self):
        self.count5 += 1
        self.count_label5.setText(f'{self.count5}')
        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus6(self):
        self.count6 += 1
        self.count_label6.setText(f'{self.count6}')
        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_kazi.move(178,350)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1 != 0 :
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_asarti.move(458,350)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2 != 0 :
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3 -= 1
            self.btn_gusht.move(738,350)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3 != 0 :
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4 -= 1
            self.btn_pepperoni.move(1025,347)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4 != 0 :
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus5(self):
        if self.count5 == 1:
            self.count5 -= 1
            self.btn_gribnaya.move(178,714)
            self.btn_plus5.move(100000,10000)
            self.btn_minus5.move(100000,10000)
            self.btn_oq5.move(100000,10000)
            self.count_label5.move(1000,1000)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count5 != 0 :
            self.count5 -= 1
            self.count_label5.setText(f'{self.count5}')
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus6(self):
        if self.count6 == 1:
            self.count6 -= 1
            self.btn_tovuq.move(458,714)
            self.btn_plus6.move(100000,10000)
            self.btn_minus6.move(100000,10000)
            self.btn_oq6.move(100000,10000)
            self.count_label6.move(1000,1000)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count6 != 0 :
            self.count6 -= 1
            self.count_label6.setText(f'{self.count6}')
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()


class xot_dog(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0 

        self.acceptDrops()

        self.setWindowTitle('PIZZA')

        # self.setStyleSheet('background-color: white')

        self.setFixedSize(1200, 900)

        self.galochka = QLabel(self)

        self.galochka2 = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_korol = QPushButton(self)
        self.btn_korol.setText('Добавить')
        
        self.btn_xalapen = QPushButton(self)
        self.btn_xalapen.setText('Добавить')

        self.btn_sirli = QPushButton(self)
        self.btn_sirli.setText('Добавить')

        self.btn_xot_dog = QPushButton(self)
        self.btn_xot_dog.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)


        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,805)
        self.btn_buy.setFixedSize(110,50)
        # LOGO PIZZA

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')


        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)

        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)



        self.pixmax0 = QPixmap('D:Oqtepa/logo_xot_dog.png')
        

        self.galochka2.setPixmap(self.pixmax0)

        self.galochka2.resize(self.pixmax0.width(),self.pixmax0.height())

        self.pixmax0 = QPixmap()



        self.pixmax = QPixmap('D:Oqtepa/logo_hot_dog.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/korol.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_korol.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_korol.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/xalapenli.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_xalapen.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_xalapen.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/sirli.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_sirli.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_sirli.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/xot_dog.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_xot_dog.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_xot_dog.setFixedSize(110,50)

        self.setStyleSheet('background-color: white')


        self.btn_korol.move(180,656)
        self.btn_xalapen.move(458,656)
        self.btn_sirli.move(738,656)
        self.btn_xot_dog.move(1025,656)

        self.label1.move(40,  390)
        self.label2.move(320,390)
        self.label3.move(600,390)
        self.label4.move(890,390)

        self.galochka2.move(380, 20)
        self.galochka.move(40, 345)


        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)

        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)


        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)


        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)


        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)


        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)


        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)

    
        self.btn_korol.clicked.connect(self.press_btn_korol)
        self.btn_xalapen.clicked.connect(self.press_btn_xalapen)
        self.btn_sirli.clicked.connect(self.press_btn_sirli)
        self.btn_xot_dog.clicked.connect(self.press_btn_xot_dog)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "XOT-DOG KOROLEVSKIE"
                num_of_product = f'{self.count1}'
                price = 20_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        

        if self.count2 > 0:
            try:
                name_product = "XOT-DOG XALAPENO"
                num_of_product = f'{self.count2}'
                price = 15_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        

        if self.count3 > 0:
            try:
                name_product = "XOT-DOG SIRLI"
                num_of_product = f'{self.count3}'
                price = 13_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

        if self.count4 > 0:
            try:
                name_product = "XOT-DOG"
                num_of_product = f'{self.count4}'
                price = 10_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

    
    def press_btn_korol(self):
        if self.count1 != -1:
            self.count1  += 1
            self.btn_korol.move(10000,100000)
            self.btn_oq1.move(180,656)
            self.btn_plus1.move(230,656)
            self.btn_minus1.move(170,656)
            self.count_label1.move(220,694)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_xalapen(self):
        if self.count2 != -1:
            self.count2  += 1
            self.btn_xalapen.move(10000,100000)
            self.btn_oq2.move(461,656)
            self.btn_plus2.move(510,656)
            self.btn_minus2.move(450,656)
            self.count_label2.move(502,694)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_sirli(self):
        if self.count3 != -1:
            self.count3  += 1
            self.btn_sirli.move(10000,100000)
            self.btn_oq3.move(738,656)
            self.btn_plus3.move(790,656)
            self.btn_minus3.move(730,656)
            self.count_label3.move(781,694)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_xot_dog(self):
        if self.count4 != -1:
            self.count4  += 1
            self.btn_xot_dog.move(10000,100000)
            self.btn_oq4.move(1030,656)
            self.btn_plus4.move(1077,656)
            self.btn_minus4.move(1017,656)
            self.count_label4.move(1068,694)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    



    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

    
    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_korol.move(180,656)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1  != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_xalapen.move(458,656)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2  != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3 -= 1
            self.btn_sirli.move(738,656)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3  != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4 -= 1
            self.btn_xot_dog.move(1025,656)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4  != 0:
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )



    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()

class snek(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0 

        self.count5 = 0 

        self.count6 = 0 

        self.acceptDrops()

        self.setWindowTitle('SNEK')

        self.setStyleSheet('background-color: white')

        self.setFixedSize(1200, 900)

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.label5 = QLabel(self)

        self.label6 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_katta = QPushButton(self)
        self.btn_katta.setText('Добавить')
        
        self.btn_derevenski = QPushButton(self)
        self.btn_derevenski.setText('Добавить')

        self.btn_urtacha = QPushButton(self)
        self.btn_urtacha.setText('Добавить')

        self.btn_maliy = QPushButton(self)
        self.btn_maliy.setText('Добавить')

        self.btn_xalapeno = QPushButton(self)
        self.btn_xalapeno.setText('Добавить')

        self.btn_non = QPushButton(self)
        self.btn_non.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)

        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,805)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.btn_oq5 = QPushButton(self)
        self.btn_oq5.setText('')
        self.btn_oq5.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq5.setFixedSize(110,50)


        self.btn_oq6 = QPushButton(self)
        self.btn_oq6.setText('')
        self.btn_oq6.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq6.setFixedSize(110,50)



        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label5 = QLabel(self)
        self.count_label5.setText('1')

        self.count_label6 = QLabel(self)
        self.count_label6.setText('1')



        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')

        self.btn_plus5 = QPushButton(self)
        self.btn_plus5.setText('+')

        self.btn_plus6 = QPushButton(self)
        self.btn_plus6.setText('+')

        
        self.btn_minus6 = QPushButton(self)
        self.btn_minus6.setText('-')

        self.btn_minus5 = QPushButton(self)
        self.btn_minus5.setText('-')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')


        self.btn_minus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus6.setFixedSize(50,50)

        self.btn_minus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus5.setFixedSize(50,50)

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)



        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)


        self.btn_plus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus5.setFixedSize(50,50)


        self.btn_plus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus6.setFixedSize(50,50)


        # LOGO PIZZA
        self.pixmax = QPixmap('D:Oqtepa/logo_snake.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/bolshoy.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_katta.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_katta.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/derevensi.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_urtacha.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_urtacha.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/urtacha.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_derevenski.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_derevenski.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/maliy.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_maliy.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_maliy.setFixedSize(110,50)


        self.pixmap5 = QPixmap('D:Oqtepa/xolopeno.png')

        self.label5.setPixmap(self.pixmap5)

        self.label5.resize(self.pixmap5.width(), self.pixmap5.height())
      
        self.pixmap5 = QPixmap()

        self.btn_xalapeno.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_xalapeno.setFixedSize(110,50)

        self.pixmap6 = QPixmap('D:Oqtepa/xleb.png')

        self.label6.setPixmap(self.pixmap6)

        self.label6.resize(self.pixmap6.width(), self.pixmap6.height())
      
        self.pixmap6 = QPixmap()

        self.btn_non.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_non.setFixedSize(110,50)


        self.btn_katta.move(178,311)
        self.btn_derevenski.move(458,312)
        self.btn_urtacha.move(738,311)
        self.btn_maliy.move(1025,311)
        self.btn_xalapeno.move(178,680)
        self.btn_non.move(458,680)

        self.label1.move(40,  85)
        self.label2.move(320,85)
        self.label3.move(600,85)
        self.label4.move(890,85)
        self.label5.move(40,450)
        self.label6.move(320,450)

        # self.logo_lavash.move(380, 20)
        self.galochka.move(38, 30)


        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)


        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)
        self.count_label5.move(100000,10000)
        self.count_label6.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)
        self.btn_plus5.move(10000,100000)
        self.btn_plus6.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)
        self.btn_minus5.move(100000,10000)
        self.btn_minus6.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)
        self.btn_oq5.move(1000000,10000)
        self.btn_oq6.move(1000000,10000)


        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_plus5.clicked.connect(self.press_btn_plus5)
        self.btn_plus6.clicked.connect(self.press_btn_plus6)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)
        self.btn_minus5.clicked.connect(self.press_btn_minus5)
        self.btn_minus6.clicked.connect(self.press_btn_minus6)

        self.btn_katta.clicked.connect(self.press_btn_katta)
        self.btn_derevenski.clicked.connect(self.press_btn_derevenski)
        self.btn_urtacha.clicked.connect(self.press_btn_urtacha)
        self.btn_xalapeno.clicked.connect(self.press_btn_xalapeno)
        self.btn_non.clicked.connect(self.press_btn_non)
        self.btn_maliy.clicked.connect(self.press_btn_maliy)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "KORTOFEL FRI BOLSHOY"
                num_of_product = f'{self.count1}'
                price = 16_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "KORTOFEL DEREVENSI"
                num_of_product = f'{self.count2}'
                price = 14_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count3 > 0:
            try:
                name_product = "KORTOFEL FRI SREDNIY"
                num_of_product = f'{self.count3}'
                price = 13_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count4 > 0:
            try:
                name_product = "KORTOFEL FRI MALIY"
                num_of_product = f'{self.count4}'
                price = 7_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count5 > 0:
            try:
                name_product = "XALAPENO"
                num_of_product = f'{self.count5}'
                price = 3_000 * int(self.count5)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count6 > 0:
            try:
                name_product = "NON"
                num_of_product = f'{self.count6}'
                price = 3_000 * int(self.count6)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()



    
    def press_btn_katta(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_katta.move(10000,100000)
            self.btn_oq1.move(178,311)
            self.btn_plus1.move(232,311)
            self.btn_minus1.move(168,311)
            self.count_label1.move(222,349)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_derevenski(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_derevenski.move(10000,100000)
            self.btn_oq2.move(458,312)
            self.btn_plus2.move(510,312)
            self.btn_minus2.move(450,312)
            self.count_label2.move(502,350)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_urtacha(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_urtacha.move(10000,100000)
            self.btn_oq3.move(738,312)
            self.btn_plus3.move(790,312)
            self.btn_minus3.move(730,312)
            self.count_label3.move(781,350)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_maliy(self):
        if self.count4 != -1:
            self.count4 += 1
            self.btn_maliy.move(10000,100000)
            self.btn_oq4.move(1028,312)
            self.btn_plus4.move(1077,312)
            self.btn_minus4.move(1017,312)
            self.count_label4.move(1068,350)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_xalapeno(self):
        if self.count5 != -1:
            self.count5 += 1
            self.btn_xalapeno.move(10000,100000)
            self.btn_oq5.move(178,677)
            self.btn_plus5.move(230,680)
            self.btn_minus5.move(170,680)
            self.count_label5.move(220,718)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_non(self):
        if self.count6 != -1:
            self.count6 += 1
            self.btn_non.move(10000,100000)
            self.btn_oq6.move(458,677)
            self.btn_plus6.move(510,680)
            self.btn_minus6.move(450,680)
            self.count_label6.move(502,718)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )




    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
  
    def press_btn_plus5(self):
        self.count5 += 1
        self.count_label5.setText(f'{self.count5}')
        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus6(self):
        self.count6 += 1
        self.count_label6.setText(f'{self.count6}')
        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_katta.move(178,311)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1  != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_derevenski.move(458,312)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2  != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3 -= 1
            self.btn_urtacha.move(738,311)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3  != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4 -= 1
            self.btn_maliy.move(1025,311)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4  != 0:
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus5(self):
        if self.count5 == 1:
            self.count5 -= 1
            self.btn_xalapeno.move(178,680)
            self.btn_plus5.move(100000,10000)
            self.btn_minus5.move(100000,10000)
            self.btn_oq5.move(100000,10000)
            self.count_label5.move(1000,1000)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count5  != 0:
            self.count5 -= 1
            self.count_label5.setText(f'{self.count5}')
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus6(self):
        if self.count6 == 1:
            self.count6 -= 1
            self.btn_non.move(458,680)
            self.btn_plus6.move(100000,10000)
            self.btn_minus6.move(100000,10000)
            self.btn_oq6.move(100000,10000)
            self.count_label6.move(1000,1000)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count6  != 0:
            self.count6 -= 1
            self.count_label6.setText(f'{self.count6}')
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )



    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()

class desert(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.acceptDrops()

        self.setWindowTitle('DESERT')

        self.setStyleSheet('background-color: white')

        self.setFixedSize(900, 900)

        self.galochka = QLabel(self)

        self.galochka_logo = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_medovik = QPushButton(self)
        self.btn_medovik.setText('Добавить')
        
        self.btn_vishnevoy_tort = QPushButton(self)
        self.btn_vishnevoy_tort.setText('Добавить')

        self.btn_chezkeyk = QPushButton(self)
        self.btn_chezkeyk.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)


        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(740,800)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)

        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)



        # LOGO PIZZA
        self.pixmax = QPixmap('D:Oqtepa/logo_desert.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()


        self.pixmax5 = QPixmap('D:Oqtepa/logo_desrts.png')

        self.galochka_logo.setPixmap(self.pixmax5)

        self.galochka_logo.resize(self.pixmax5.width(),self.pixmax5.height())

        self.pixmax5 = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/medovik.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_vishnevoy_tort.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_vishnevoy_tort.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/vishnevoy.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_medovik.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_medovik.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/chizkeyk.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_chezkeyk.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_chezkeyk.setFixedSize(110,50)


        self.btn_vishnevoy_tort.move(180,675)
        self.btn_medovik.move(458,675)
        self.btn_chezkeyk.move(738,675)

        self.label1.move(40,450)
        self.label2.move(320,450)
        self.label3.move(600,450)



        self.galochka_logo.move(245, 20)
        self.galochka.move(40, 400)

        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)

        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)

        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        
        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)

        self.btn_vishnevoy_tort.clicked.connect(self.press_btn_vishnevoy_tort)
        self.btn_medovik.clicked.connect(self.press_btn_medovik)
        self.btn_chezkeyk.clicked.connect(self.press_btn_chezkeyk)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "MEDOVIK TORT"
                num_of_product = f'{self.count1}'
                price = 15_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "VISHNEVIY TORT"
                num_of_product = f'{self.count2}'
                price = 15_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count3 > 0:
            try:
                name_product = "CHIZKEYK TORT"
                num_of_product = f'{self.count3}'
                price = 15_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()


    

    def press_btn_vishnevoy_tort(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_vishnevoy_tort.move(10000,100000)
            self.btn_oq1.move(180,675)
            self.btn_plus1.move(230,675)
            self.btn_minus1.move(170,675)
            self.count_label1.move(220,713)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_medovik(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_medovik.move(10000,100000)
            self.btn_oq2.move(458,675)
            self.btn_plus2.move(507,675)
            self.btn_minus2.move(447,675)
            self.count_label2.move(499,713)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_chezkeyk(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_chezkeyk.move(10000,100000)
            self.btn_oq3.move(738,675)
            self.btn_plus3.move(790,675)
            self.btn_minus3.move(730,675)
            self.count_label3.move(781,713) 
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    

    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_vishnevoy_tort.move(180,675)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1 != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_medovik.move(458,675)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2 != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3 -= 1
            self.btn_chezkeyk.move(738,675)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3 != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()

class drinks(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0 

        self.count5 = 0 

        self.count6 = 0 

        self.count7 = 0

        self.count8 = 0

        self.acceptDrops()

        self.setWindowTitle('LAVASH')

        self.setStyleSheet('background-color: white')

        self.setFixedSize(1200, 900)

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.label5 = QLabel(self)

        self.label6 = QLabel(self)
        
        self.label7 = QLabel(self)
        
        self.label8 = QLabel(self)


        self.logo_lavash = QLabel(self)

        self.btn_dolina_1 = QPushButton(self)
        self.btn_dolina_1.setText('Добавить')
        
        self.btn_pepsi = QPushButton(self)
        self.btn_pepsi.setText('Добавить')

        self.btn_mirinda = QPushButton(self)
        self.btn_mirinda.setText('Добавить')

        self.btn_cofe = QPushButton(self)
        self.btn_cofe.setText('Добавить')

        self.btn_rozliv = QPushButton(self)
        self.btn_rozliv.setText('Добавить')

        self.btn_lemon_choy = QPushButton(self)
        self.btn_lemon_choy.setText('Добавить')

        self.btn_dolina = QPushButton(self)
        self.btn_dolina.setText('Добавить')

        self.btn_choy= QPushButton(self)
        self.btn_choy.setText('Добавить')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)

        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,805)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.btn_oq5 = QPushButton(self)
        self.btn_oq5.setText('')
        self.btn_oq5.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq5.setFixedSize(110,50)


        self.btn_oq6 = QPushButton(self)
        self.btn_oq6.setText('')
        self.btn_oq6.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq6.setFixedSize(110,50)


        self.btn_oq7 = QPushButton(self)
        self.btn_oq7.setText('')
        self.btn_oq7.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq7.setFixedSize(110,50)


        self.btn_oq8 = QPushButton(self)
        self.btn_oq8.setText('')
        self.btn_oq8.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq8.setFixedSize(110,50)


        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label5 = QLabel(self)
        self.count_label5.setText('1')

        self.count_label6 = QLabel(self)
        self.count_label6.setText('1')

        self.count_label7 = QLabel(self)
        self.count_label7.setText('1')

        self.count_label8 = QLabel(self)
        self.count_label8.setText('1')


        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label8.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')

        self.btn_plus5 = QPushButton(self)
        self.btn_plus5.setText('+')

        self.btn_plus6 = QPushButton(self)
        self.btn_plus6.setText('+')

        self.btn_plus7 = QPushButton(self)
        self.btn_plus7.setText('+')

        self.btn_plus8 = QPushButton(self)
        self.btn_plus8.setText('+')


        
        self.btn_minus8 = QPushButton(self)
        self.btn_minus8.setText('-')

        self.btn_minus7 = QPushButton(self)
        self.btn_minus7.setText('-')

        self.btn_minus6 = QPushButton(self)
        self.btn_minus6.setText('-')

        self.btn_minus5 = QPushButton(self)
        self.btn_minus5.setText('-')

        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')



        self.btn_minus8.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus8.setFixedSize(50,50)

        self.btn_minus7.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus7.setFixedSize(50,50)

        self.btn_minus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus6.setFixedSize(50,50)

        self.btn_minus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus5.setFixedSize(50,50)

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)


        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)


        self.btn_plus5.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus5.setFixedSize(50,50)


        self.btn_plus6.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus6.setFixedSize(50,50)



        self.btn_plus7.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus7.setFixedSize(50,50)
        

        self.btn_plus8.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus8.setFixedSize(50,50)


        # LOGO DRINKS
        self.pixmax = QPixmap('D:Oqtepa/logo_drinks.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/dolina_1.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_dolina_1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_dolina_1.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/pepsi.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_pepsi.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_pepsi.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/mirinda.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_cofe.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_cofe.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/kofe.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_mirinda.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_mirinda.setFixedSize(110,50)


        self.pixmap5 = QPixmap('D:Oqtepa/rozliv.png')

        self.label5.setPixmap(self.pixmap5)

        self.label5.resize(self.pixmap5.width(), self.pixmap5.height())
      
        self.pixmap5 = QPixmap()

        self.btn_rozliv.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_rozliv.setFixedSize(110,50)

        self.pixmap6 = QPixmap('D:Oqtepa/lemon_choy.png')

        self.label6.setPixmap(self.pixmap6)

        self.label6.resize(self.pixmap6.width(), self.pixmap6.height())
      
        self.pixmap6 = QPixmap()

        self.btn_lemon_choy.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_lemon_choy.setFixedSize(110,50)


        self.pixmap7 = QPixmap('D:Oqtepa/dolina.png')

        self.label7.setPixmap(self.pixmap7)

        self.label7.resize(self.pixmap7.width(), self.pixmap7.height())
      
        self.pixmap7 = QPixmap()

        self.btn_dolina.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_dolina.setFixedSize(110,50)


        self.pixmap8 = QPixmap('D:Oqtepa/chay.png')

        self.label8.setPixmap(self.pixmap8)

        self.label8.resize(self.pixmap8.width(), self.pixmap8.height())
      
        self.pixmap8 = QPixmap()

        self.btn_choy.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_choy.setFixedSize(110,50)


        self.btn_dolina_1.move(178,311)
        self.btn_pepsi.move(458,312)
        self.btn_cofe.move(738,309)
        self.btn_mirinda.move(1025,311)
        self.btn_rozliv.move(178,680)
        self.btn_lemon_choy.move(458,680)
        self.btn_dolina.move(742,680)
        self.btn_choy.move(1026,678)

        self.label1.move(40,  85)
        self.label2.move(320,85)
        self.label3.move(600,85)
        self.label4.move(890,85)
        self.label5.move(40,450)
        self.label6.move(320,450)
        self.label7.move(605,450)
        self.label8.move(890,450)

        # self.logo_lavash.move(380, 20)
        self.galochka.move(38, 30)


        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)

        self.btn_dolina_1.clicked.connect(self.press_btn_dolina_1)
        self.btn_pepsi.clicked.connect(self.press_btn_pepsi)
        self.btn_cofe.clicked.connect(self.press_btn_cofe)
        self.btn_mirinda.clicked.connect(self.press_btn_mirinda)
        self.btn_rozliv.clicked.connect(self.press_btn_rozliv)
        self.btn_lemon_choy.clicked.connect(self.press_btn_lemon_choy)
        self.btn_dolina.clicked.connect(self.press_btn_dolina)
        self.btn_choy.clicked.connect(self.press_btn_choy)


        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)
        self.count_label5.move(100000,10000)
        self.count_label6.move(100000,10000)
        self.count_label7.move(100000,10000)
        self.count_label8.move(100000,10000)


        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)
        self.btn_plus5.move(10000,100000)
        self.btn_plus6.move(10000,100000)
        self.btn_plus7.move(10000,100000)
        self.btn_plus8.move(10000,100000)


        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)
        self.btn_minus5.move(100000,10000)
        self.btn_minus6.move(100000,10000)
        self.btn_minus7.move(100000,10000)
        self.btn_minus8.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)
        self.btn_oq5.move(1000000,10000)
        self.btn_oq6.move(1000000,10000)
        self.btn_oq7.move(1000000,10000)
        self.btn_oq8.move(1000000,10000)


        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)
        self.btn_plus5.clicked.connect(self.press_btn_plus5)
        self.btn_plus6.clicked.connect(self.press_btn_plus6)
        self.btn_plus7.clicked.connect(self.press_btn_plus7)
        self.btn_plus8.clicked.connect(self.press_btn_plus8)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)
        self.btn_minus5.clicked.connect(self.press_btn_minus5)
        self.btn_minus6.clicked.connect(self.press_btn_minus6)
        self.btn_minus7.clicked.connect(self.press_btn_minus7)
        self.btn_minus8.clicked.connect(self.press_btn_minus8)  


        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "SOCHNAYA DOLINA"
                num_of_product = f'{self.count1}'
                price = 15_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "PEPSI 0.5"
                num_of_product = f'{self.count2}'
                price = 7_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count3 > 0:
            try:
                name_product = "MIRINDA 0.4"
                num_of_product = f'{self.count3}'
                price = 7_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count4 > 0:
            try:
                name_product = "COFE"
                num_of_product = f'{self.count4}'
                price = 7_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count5 > 0:
            try:
                name_product = "ROZLIV 0.3"
                num_of_product = f'{self.count5}'
                price = 5_000 * int(self.count5)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()

        if self.count6 > 0:
            try:
                name_product = "CHOY + LIMON"
                num_of_product = f'{self.count6}'
                price = 5_000 * int(self.count6)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count7 > 0:
            try:
                name_product = "SOCHNAYA DOLINA 0.2"
                num_of_product = f'{self.count7}'
                price = 4_000 * int(self.count7)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        

        if self.count8 > 0:
            try:
                name_product = "CHOY"
                num_of_product = f'{self.count8}'
                price = 3_000 * int(self.count8)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()




    
    def press_btn_dolina_1(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_dolina_1.move(10000,100000)
            self.btn_oq1.move(178,311)
            self.btn_plus1.move(228,311)
            self.btn_minus1.move(168,311)
            self.count_label1.move(218,349)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_pepsi(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_pepsi.move(10000,100000)
            self.btn_oq2.move(458,312)
            self.btn_plus2.move(510,312)
            self.btn_minus2.move(450,312)
            self.count_label2.move(502,350)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_cofe(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_cofe.move(10000,100000)
            self.btn_oq3.move(748,311)
            self.btn_plus3.move(790,309)
            self.btn_minus3.move(730,309)
            self.count_label3.move(781,347)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_mirinda(self):
        if self.count4 != -1:
            self.count4 += 1
            self.btn_mirinda.move(10000,100000)
            self.btn_oq4.move(1025,311)
            self.btn_plus4.move(1077,311)
            self.btn_minus4.move(1017,311)
            self.count_label4.move(1068,349)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_rozliv(self):
        if self.count5 != -1:
            self.count5 += 1
            self.btn_rozliv.move(10000,100000)
            self.btn_oq5.move(178,676)
            self.btn_plus5.move(230,680)
            self.btn_minus5.move(170,680)
            self.count_label5.move(220,718)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_lemon_choy(self):
        if self.count6 != -1:
            self.count6 += 1
            self.btn_lemon_choy.move(10000,100000)
            self.btn_oq6.move(458,676)
            self.btn_plus6.move(510,680)
            self.btn_minus6.move(450,680)
            self.count_label6.move(502,718)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_dolina(self):
        if self.count7 != -1:
            self.count7 += 1
            self.btn_dolina.move(10000,100000)
            self.btn_oq7.move(742,676)
            self.btn_plus7.move(794,680)
            self.btn_minus7.move(734,680)
            self.count_label7.move(785,718)
            self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_choy(self):
        if self.count8 != -1:
            self.count8 += 1
            self.btn_choy.move(10000,100000)
            self.btn_oq8.move(1026,678)
            self.btn_plus8.move(1078,678)
            self.btn_minus8.move(1019,678)
            self.count_label8.move(1069,716)
            self.count_label8.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
  
    def press_btn_plus5(self):
        self.count5 += 1
        self.count_label5.setText(f'{self.count5}')
        self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus6(self):
        self.count6 += 1
        self.count_label6.setText(f'{self.count6}')
        self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus7(self):
        self.count7 += 1
        self.count_label7.setText(f'{self.count7}')
        self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus8(self):
        self.count8 += 1
        self.count_label8.setText(f'{self.count8}')
        self.count_label8.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1  -= 1
            self.btn_dolina_1.move(178,311)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1  != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2  -= 1
            self.btn_pepsi.move(458,312)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2  != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3  -= 1
            self.btn_cofe.move(738,309)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3  != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4  -= 1
            self.btn_mirinda.move(1025,311)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4  != 0:
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus5(self):
        if self.count5 == 1:
            self.count5  -= 1
            self.btn_rozliv.move(178,680)
            self.btn_plus5.move(100000,10000)
            self.btn_minus5.move(100000,10000)
            self.btn_oq5.move(100000,10000)
            self.count_label5.move(1000,1000)
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count5  != 0:
            self.count5 -= 1
            self.count_label5.setText(f'{self.count5}')
            self.count_label5.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus6(self):
        if self.count6 == 1:
            self.count6  -= 1
            self.btn_lemon_choy.move(458,680)
            self.btn_plus6.move(100000,10000)
            self.btn_minus6.move(100000,10000)
            self.btn_oq6.move(100000,10000)
            self.count_label6.move(1000,1000)
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count6  != 0:
            self.count6 -= 1
            self.count_label6.setText(f'{self.count6}')
            self.count_label6.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus7(self):
        if self.count7 == 1:
            self.count7  -= 1
            self.btn_dolina.move(742,680)
            self.btn_plus7.move(100000,10000)
            self.btn_minus7.move(100000,10000)
            self.btn_oq7.move(100000,10000)
            self.count_label7.move(1000,1000)
            self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count7  != 0:
            self.count7 -= 1
            self.count_label7.setText(f'{self.count7}')
            self.count_label7.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus8(self):
        if self.count8 == 1:
            self.count8  -= 1
            self.btn_choy.move(1026,678)
            self.btn_plus8.move(100000,10000)
            self.btn_minus8.move(100000,10000)
            self.btn_oq8.move(100000,10000)
            self.count_label8.move(1000,1000)
            self.count_label8.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count8  != 0:
            self.count8 -= 1
            self.count_label8.setText(f'{self.count8}')
            self.count_label8.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()

class salat(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.acceptDrops()

        self.setWindowTitle('Salat')

        self.setFixedSize(750, 700)

        self.setStyleSheet('background-color: white')

        self.galochka = QLabel(self)

        self.galochka2 = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.logo_set = QLabel(self)

        self.btn_murskoy = QPushButton(self)
        self.btn_murskoy.setText('Добавить')
        
        self.btn_sezar = QPushButton(self)
        self.btn_sezar.setText('Добавить')

        self.logo_salad = QLabel(self)

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,630)

        self.initUi()

    
    def initUi(self):
        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(605,625)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')


        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)


        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        
        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)


        # LOGO XAGGI AND CLUP
        self.pixmax = QPixmap('D:Oqtepa/logo_salat.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()


        self.pixmax1 = QPixmap('D:Oqtepa/mujskoy.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_murskoy.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_murskoy.setFixedSize(110,50)

        #2

        self.pixmax2 = QPixmap('D:Oqtepa/sezar.png')

        self.label2.setPixmap(self.pixmax2)

        self.label2.resize(self.pixmax2.width(),self.pixmax2.height())

        self.lopixmax2 = QPixmap()

        self.btn_sezar.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_sezar.setFixedSize(110,50)

        self.btn_murskoy.move(230,511)
        self.btn_sezar.move(540,513)

        self.label1.move(90,250)
        self.label2.move(400,250)

        self.galochka.move(90, 200)

        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)

        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)

        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)

        self.btn_murskoy.clicked.connect(self.press_btn_murskoy)
        self.btn_sezar.clicked.connect(self.press_btn_sezar)


        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "MUJSKOY KAPRIZ"
                num_of_product = f'{self.count1}'
                price = 21_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "SALAT SEZAR"
                num_of_product = f'{self.count2}'
                price = 20_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()


    def press_btn_murskoy(self):
        if self.count1 != -1:
            self.count1 +=1
            self.btn_murskoy.move(10000,100000)
            self.btn_oq1.move(230,511)
            self.btn_plus1.move(280,511)
            self.btn_minus1.move(220,511)
            self.count_label1.move(270,549)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_sezar(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_sezar.move(10000,100000)
            self.btn_oq2.move(540,513)
            self.btn_plus2.move(590,513)
            self.btn_minus2.move(530,513)
            self.count_label2.move(580,552)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    
    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1 -= 1
            self.btn_murskoy.move(230,511)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1 != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2 -= 1
            self.btn_sezar.move(540,513)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2 != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()



class sous(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.count1 = 0
        
        self.count2 = 0 

        self.count3 = 0 

        self.count4 = 0         

        self.acceptDrops()

        self.setWindowTitle('SOUS')

        self.setFixedSize(1200, 900)

        self.setStyleSheet('background-color: white')

        self.galochka = QLabel(self)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.label3 = QLabel(self)

        self.label4 = QLabel(self)

        self.logo_lavash = QLabel(self)

        self.btn_ketchup = QPushButton(self)
        self.btn_ketchup.setText('Добавить')
        
        self.btn_mayonez = QPushButton(self)
        self.btn_mayonez.setText('Добавить')

        self.btn_chili_sous = QPushButton(self)
        self.btn_chili_sous.setText('Добавить')

        self.btn_sirli = QPushButton(self)
        self.btn_sirli.setText('Добавить')

        self.logo_souse = QLabel(self)

        self.btn_back = QPushButton(self)
        self.btn_back.setText('Назад')
        self.btn_back.setStyleSheet(
            'background-color: #EEC900; '
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)
        self.btn_back.move(30,800)


        self.initUi()
    
    def initUi(self):

        self.btn_buy = QPushButton(self)
        self.btn_buy.setText("BUY")
        self.btn_buy.setStyleSheet(
            'background-color: #EEC900;'
            'font: 15px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_buy.move(1050,805)
        self.btn_buy.setFixedSize(110,50)

        self.btn_oq1 = QPushButton(self)
        self.btn_oq1.setText('')
        self.btn_oq1.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq1.setFixedSize(110,50)


        self.btn_oq2 = QPushButton(self)
        self.btn_oq2.setText('')
        self.btn_oq2.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq2.setFixedSize(110,50)


        self.btn_oq3 = QPushButton(self)
        self.btn_oq3.setText('')
        self.btn_oq3.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq3.setFixedSize(110,50)


        self.btn_oq4 = QPushButton(self)
        self.btn_oq4.setText('')
        self.btn_oq4.setStyleSheet(
            'background-color: white; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid white;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_oq4.setFixedSize(110,50)

        self.count_label1 = QLabel(self)
        self.count_label1.setText('1')

        self.count_label2 = QLabel(self)
        self.count_label2.setText('1')

        self.count_label3 = QLabel(self)
        self.count_label3.setText('1')

        self.count_label4 = QLabel(self)
        self.count_label4.setText('1')

        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )


        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        self.btn_plus1 = QPushButton(self)
        self.btn_plus1.setText('+')

        self.btn_plus2 = QPushButton(self)
        self.btn_plus2.setText('+')

        self.btn_plus3 = QPushButton(self)
        self.btn_plus3.setText('+')

        self.btn_plus4 = QPushButton(self)
        self.btn_plus4.setText('+')


        self.btn_minus4 = QPushButton(self)
        self.btn_minus4.setText('-')

        self.btn_minus3 = QPushButton(self)
        self.btn_minus3.setText('-')

        self.btn_minus2 = QPushButton(self)
        self.btn_minus2.setText('-')

        self.btn_minus1 = QPushButton(self)
        self.btn_minus1.setText('-')

        self.btn_minus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus4.setFixedSize(50,50)

        self.btn_minus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus3.setFixedSize(50,50)

        self.btn_minus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus2.setFixedSize(50,50)

        self.btn_minus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_minus1.setFixedSize(50,50)

        self.btn_plus1.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus1.setFixedSize(50,50)

        self.btn_plus2.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus2.setFixedSize(50,50)

        self.btn_plus3.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus3.setFixedSize(50,50)


        self.btn_plus4.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_plus4.setFixedSize(50,50)


        # LOGO PIZZA
        self.pixmax = QPixmap('D:Oqtepa/logo_souse.png')

        self.galochka.setPixmap(self.pixmax)

        self.galochka.resize(self.pixmax.width(),self.pixmax.height())

        self.pixmax = QPixmap()


        self.pixmax0 = QPixmap('D:Oqtepa/logo_sous.png')

        self.logo_souse.setPixmap(self.pixmax0)

        self.logo_souse.resize(self.pixmax0.width(),self.pixmax0.height())

        self.pixmax0 = QPixmap()

        #1

        self.pixmax1 = QPixmap('D:Oqtepa/ketchup.png')

        self.label1.setPixmap(self.pixmax1)

        self.label1.resize(self.pixmax1.width(),self.pixmax1.height())

        self.lopixmax1 = QPixmap()

        self.btn_ketchup.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )

        self.btn_ketchup.setFixedSize(110,50)

        #2

        self.pixmap2 = QPixmap('D:Oqtepa/mayonez.png')

        self.label2.setPixmap(self.pixmap2)

        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
      
        self.pixmap2 = QPixmap()

        self.btn_mayonez.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_mayonez.setFixedSize(110,50)

        #3

        self.pixmap3 = QPixmap('D:Oqtepa/chili.png')

        self.label3.setPixmap(self.pixmap3)

        self.label3.resize(self.pixmap3.width(), self.pixmap3.height())
      
        self.pixmap3 = QPixmap()

        self.btn_chili_sous.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_chili_sous.setFixedSize(110,50)


        self.pixmap4 = QPixmap('D:Oqtepa/sirli_sous.png')

        self.label4.setPixmap(self.pixmap4)

        self.label4.resize(self.pixmap4.width(), self.pixmap4.height())
      
        self.pixmap4 = QPixmap()

        self.btn_sirli.setStyleSheet(
            'background-color: red; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_sirli.setFixedSize(110,50)

        # self.setStyleSheet('background-color: white')


        self.btn_ketchup.move(180,630)
        self.btn_mayonez.move(458,630)
        self.btn_chili_sous.move(738,630)
        self.btn_sirli.move(1027,628)

        self.label1.move(40,400)
        self.label2.move(320,400)
        self.label3.move(600,400)
        self.label4.move(890,400)

        self.logo_souse.move(40, 360)
        self.galochka.move(360,20)



        self.show()

        self.btn_back.clicked.connect(self.press_btn_back)

        self.count_label1.move(100000,10000)
        self.count_label2.move(100000,10000)
        self.count_label3.move(100000,10000)
        self.count_label4.move(100000,10000)

        self.btn_plus1.move(10000,100000)
        self.btn_plus2.move(10000,100000)
        self.btn_plus3.move(10000,100000)
        self.btn_plus4.move(10000,100000)

        self.btn_minus1.move(100000,10000)
        self.btn_minus2.move(100000,10000)
        self.btn_minus3.move(100000,10000)
        self.btn_minus4.move(100000,10000)

        self.btn_oq1.move(1000000,10000)
        self.btn_oq2.move(1000000,10000)
        self.btn_oq3.move(1000000,10000)
        self.btn_oq4.move(1000000,10000)

        self.btn_plus1.clicked.connect(self.press_btn_plus1)
        self.btn_plus2.clicked.connect(self.press_btn_plus2)
        self.btn_plus3.clicked.connect(self.press_btn_plus3)
        self.btn_plus4.clicked.connect(self.press_btn_plus4)

        self.btn_minus1.clicked.connect(self.press_btn_minus1)
        self.btn_minus2.clicked.connect(self.press_btn_minus2)
        self.btn_minus3.clicked.connect(self.press_btn_minus3)
        self.btn_minus4.clicked.connect(self.press_btn_minus4)

        self.btn_ketchup.clicked.connect(self.press_btn_ketchup)
        self.btn_mayonez.clicked.connect(self.press_btn_mayonez)
        self.btn_chili_sous.clicked.connect(self.press_btn_chili_sous)
        self.btn_sirli.clicked.connect(self.press_btn_sirli)

        self.btn_buy.clicked.connect(self.press_btn_buy)
    
    def press_btn_buy(self):
        if self.count1 > 0:
            try:
                name_product = "KETCHUP"
                num_of_product = f'{self.count1}'
                price = 3_000 * int(self.count1)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count2 > 0:
            try:
                name_product = "MAYONEZ"
                num_of_product = f'{self.count2}'
                price = 2_000 * int(self.count2)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count3 > 0:
            try:
                name_product = "CHILI SOUS"
                num_of_product = f'{self.count3}'
                price = 2_000 * int(self.count3)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()
        
        if self.count4 > 0:
            try:
                name_product = "SIRLI SOUS"
                num_of_product = f'{self.count4}'
                price = 2_000 * int(self.count4)
                created_date = f'{datetime.now()}'[:-7]
                phone_number = '+998900074272'

                sql = """insert into zakaz (NAME_OF_PRODUCT,NUM_OF_PRODUCT,PRICE,CREATED_DATE,phone_number)
                    values (%s,%s,%s,%s,%s)
                """
                val = (name_product,num_of_product,price,created_date,phone_number)

                mycursor.execute(sql,val)

                mydb.commit()
            except Exception as err:
                print(err)
            self.close()
            self.menu = MenuPage()
            self.menu.show()



    
    def press_btn_ketchup(self):
        if self.count1 != -1:
            self.count1 += 1
            self.btn_ketchup.move(10000,100000)
            self.btn_oq1.move(180,628)
            self.btn_plus1.move(230,630)
            self.btn_minus1.move(170,630)
            self.count_label1.move(220,668)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_mayonez(self):
        if self.count2 != -1:
            self.count2 += 1
            self.btn_mayonez.move(10000,100000)
            self.btn_oq2.move(458,628)
            self.btn_plus2.move(507,630)
            self.btn_minus2.move(447,630)
            self.count_label2.move(499,668)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_chili_sous(self):
        if self.count3 != -1:
            self.count3 += 1
            self.btn_chili_sous.move(10000,100000)
            self.btn_oq3.move(738,630)
            self.btn_plus3.move(790,630)
            self.btn_minus3.move(730,630)
            self.count_label3.move(781,668)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_sirli(self):
        if self.count4 != -1:
            self.count4 += 1
            self.btn_sirli.move(10000,100000)
            self.btn_oq4.move(1027,628)
            self.btn_plus4.move(1074,628)
            self.btn_minus4.move(1014,628)
            self.count_label4.move(1064,666)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_plus1(self):
        self.count1 += 1
        self.count_label1.setText(f'{self.count1}')
        self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_plus2(self):
        self.count2 += 1
        self.count_label2.setText(f'{self.count2}')
        self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
 
    def press_btn_plus3(self):
        self.count3 += 1
        self.count_label3.setText(f'{self.count3}')
        self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
 
    def press_btn_plus4(self):
        self.count4 += 1
        self.count_label4.setText(f'{self.count4}')
        self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus1(self):
        if self.count1 == 1:
            self.count1  -= 1
            self.btn_ketchup.move(180,630)
            self.btn_plus1.move(100000,10000)
            self.btn_minus1.move(100000,10000)
            self.btn_oq1.move(100000,10000)
            self.count_label1.move(1000,1000)
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count1  != 0:
            self.count1 -= 1
            self.count_label1.setText(f'{self.count1}')
            self.count_label1.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    

    def press_btn_minus2(self):
        if self.count2 == 1:
            self.count2  -= 1
            self.btn_mayonez.move(458,630)
            self.btn_plus2.move(100000,10000)
            self.btn_minus2.move(100000,10000)
            self.btn_oq2.move(100000,10000)
            self.count_label2.move(1000,1000)
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count2  != 0:
            self.count2 -= 1
            self.count_label2.setText(f'{self.count2}')
            self.count_label2.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus3(self):
        if self.count3 == 1:
            self.count3  -= 1
            self.btn_chili_sous.move(738,630)
            self.btn_plus3.move(100000,10000)
            self.btn_minus3.move(100000,10000)
            self.btn_oq3.move(100000,10000)
            self.count_label3.move(1000,1000)
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count3  != 0:
            self.count3 -= 1
            self.count_label3.setText(f'{self.count3}')
            self.count_label3.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )
    
    def press_btn_minus4(self):
        if self.count4 == 1:
            self.count4  -= 1
            self.btn_sirli.move(1027,628)
            self.btn_plus4.move(100000,10000)
            self.btn_minus4.move(100000,10000)
            self.btn_oq4.move(100000,10000)
            self.count_label4.move(1000,1000)
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )

        elif self.count4  != 0:
            self.count4 -= 1
            self.count_label4.setText(f'{self.count4}')
            self.count_label4.setStyleSheet(
            'color: black;'
            'font-size: 15px;'
            'font-weight: bold;'   
        )



    def press_btn_back(self):
        self.back = MenuPage()
        self.close()
        self.back.show()


class MainWindow(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.logo_oqtepa = QLabel(self)

        self.setFixedSize(570, 800)

        self.setStyleSheet('background-color: white')

        self.initUi()

    
    def initUi(self):

        self.galochka_pixmax = QPixmap('D:Oqtepa/logo_oqtepa.png')

        self.logo_oqtepa.setPixmap(self.galochka_pixmax)

        self.logo_oqtepa.resize(self.galochka_pixmax.width(),self.galochka_pixmax.height())

        self.galochka_pixmax = QPixmap()

        self.logo_oqtepa.move(20,10)

        self.name_edit = QLineEdit(self)
        self.name_edit.setFixedSize(300,50)
        self.name_edit.setPlaceholderText('Write name📃')
        self.name_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'border: 2px solid red;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )

        self.phone_number_edit = QLineEdit(self)
        self.phone_number_edit.setFixedSize(300,50)
        self.phone_number_edit.setPlaceholderText('Write phone number☎️')
        self.phone_number_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'border: 2px solid 	#FFD700;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )
        
        self.email_edit = QLineEdit(self)
        self.email_edit.setFixedSize(300,50)
        self.email_edit.setPlaceholderText('Write email📨')
        self.email_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'border: 2px solid red;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )
        
        self.password_edit = QLineEdit(self)
        self.password_edit.setFixedSize(300,50)
        self.password_edit.setPlaceholderText('Write password🔐')
        self.password_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'border: 2px solid #FFD700;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )

        self.btn_enter = QPushButton('ENTER',self)
        self.btn_enter.setFixedSize(200,40)
        self.btn_enter.setStyleSheet(
            'background-color: #FFD700;'
            'color: red;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )
        
        self.btn_login = QPushButton('LOGIN',self)
        self.btn_login.setFixedSize(200,40)
        self.btn_login.setStyleSheet(
            'background-color: red;'
            'color: yellow;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )
        
        self.btn_info = QPushButton('INFO',self)
        self.btn_info.setFixedSize(200,40)
        self.btn_info.setStyleSheet(
            'background-color: red;'
            'color: yellow;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )
        
        self.name_edit.move(130,400)
        self.phone_number_edit.move(130,470)
        self.email_edit.move(130,540)
        self.password_edit.move(130,610)

        self.btn_enter.move(180,680)
        self.btn_info.move(310,750)
        self.btn_login.move(50,750)

        self.btn_enter.clicked.connect(self.press_btn_enter)
        self.btn_login.clicked.connect(self.press_btn_login)
        self.btn_info.clicked.connect(self.press_btn_info)



        self.show()
    
    def press_btn_enter(self):
        if self._check_label():
            try:
                name = self.name_edit.text()
                number = self.phone_number_edit.text()
                email = self.email_edit.text()
                password = self.password_edit.text()

                sql = """insert into oq_tepa (name,number,email,password)
                    values(%s,%s,%s,%s)
                """
                val = (name,number,email,password)

                mycursor.execute(sql,val)

                mydb.commit()

            except Exception as err:
                print(err)
            else:
                self.close()
                self.menu = MenuPage()
                self.menu.show()
        else:
            self.name_edit.clear()
            self.phone_number_edit.clear()
            self.email_edit.clear()
            self.password_edit.clear()
                
    
    def press_btn_login(self):
        self.close()
        self.loginpage = LoginPage()
        self.loginpage.show()
    
    def _check_label(self):
        if self.name_edit.text() == '':
            self.name_edit.setPlaceholderText('Invalid Name')
        if self.phone_number_edit.text() == '':
            self.phone_number_edit.setPlaceholderText('Invalid Phone Number')
        if self.email_edit.text() == '':
            self.email_edit.setPlaceholderText('Invalid Email')
        if self.password_edit.text() == '':
            self.password_edit.setPlaceholderText('Invalid Password')
        else:
            return True
    
    def number(self):
        self.number = self.password_edit.text()
        return self.number

    
    def press_btn_info(self):
        self.info = info()
        self.close()
        self.info.show()
            

class LoginPage(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.logo_oqtepa = QLabel(self)

        self.setFixedSize(570, 800)

        self.setStyleSheet('background-color: white')

        self.initUi()

    def initUi(self):

        self.galochka_pixmax = QPixmap('D:Oqtepa/oqtepa_logo.png')

        self.logo_oqtepa.setPixmap(self.galochka_pixmax)

        self.logo_oqtepa.resize(self.galochka_pixmax.width(),self.galochka_pixmax.height())

        self.galochka_pixmax = QPixmap()

        self.logo_oqtepa.move(45,10)

        self.email_edit = QLineEdit(self)
        self.email_edit.setFixedSize(350,50)
        self.email_edit.setPlaceholderText('Enter your email📧')
        self.email_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'border: 2px solid black;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )
        
        self.password_edit = QLineEdit(self)
        self.password_edit.setFixedSize(350,50)
        self.password_edit.setPlaceholderText('Enter your password🔒')
        self.password_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'border: 2px solid black;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        self.btn_enter = QPushButton('ENTER',self)
        self.btn_enter.setFixedSize(200,40)
        self.btn_enter.setStyleSheet(
            'background-color: #FFD700;'
            'color: red;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )
        
        self.btn_registration = QPushButton('REGISTRATION',self)
        self.btn_registration.setFixedSize(200,40)
        self.btn_registration.setStyleSheet(
            'background-color: red;'
            'color: yellow;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )
        
        self.btn_forget_password = QPushButton('FORGET PASSWORD',self)
        self.btn_forget_password.setFixedSize(200,40)
        self.btn_forget_password.setStyleSheet(
            'background-color: #FFD700;'
            'color: red;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )

        
        self.email_edit.move(100,450)
        self.password_edit.move(100,520)

        self.btn_enter.move(180,590)
        self.btn_registration.move(180,650)
        self.btn_forget_password.move(180,710)

        self.btn_registration.clicked.connect(self.press_btn_register)

        self.btn_enter.clicked.connect(self.press_btn_enter)

        self.btn_forget_password.clicked.connect(self.press_btn_forget_password)

        self.show()


    def press_btn_register(self):
        self.close()
        self.main = MainWindow()
        self.main.show()
    
    def press_btn_forget_password(self):
        self.close()
        self.forget = ForgetPassword()
        self.forget.show()
    
    def press_btn_enter(self):
        # if self._check_label():
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                    select email,password
                    from oq_tepa
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    if self.email_edit.text() == i[0] and self.password_edit.text() == i[1]:
                        
                        with mydb.cursor() as cursor:
                            sql = f"""
                            delete from zakaz where price = price;      
                            """
                            cursor.execute(sql)

                        self.menu = MenuPage()
                        self.close()
                        self.menu.show()
        except Exception as err:
            print(err)
        else:
            self.email_edit.setPlaceholderText('Error email')
            self.email_edit.setStyleSheet(
                'border-width: 2px;'
                'border-radius: 8px;'
                'border-style: solid;'
                'border: 2px solid red;'
                'background-color: #f4f4f4;'
                'color: #3d3d3d;'
                'font-weight: bold;'
                'font: 25px'
                )
            self.email_edit.clear()
            
            self.password_edit.setPlaceholderText('Error password')
            self.password_edit.setStyleSheet(
                'border-width: 2px;'
                'border-radius: 8px;'
                'border-style: solid;'
                'border: 2px solid red;'
                'background-color: #f4f4f4;'
                'color: #3d3d3d;'
                'font-weight: bold;'
                'font: 25px'
                )
            self.password_edit.clear()


class ForgetPassword(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText("BACK")
        self.btn_exit.setStyleSheet(
            'background-color: #FFC125; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_exit.setFixedSize(200,50)

        self.setFixedSize(570, 800)

        self.logo_oqtepa = QLabel(self)

        self.setStyleSheet('background-color: white')

        self.initUi()
    
    def initUi(self):

        self.galochka_pixmax = QPixmap('D:Oqtepa/oqtepa_logo.png')

        self.logo_oqtepa.setPixmap(self.galochka_pixmax)

        self.logo_oqtepa.resize(self.galochka_pixmax.width(),self.galochka_pixmax.height())

        self.galochka_pixmax = QPixmap()

        self.logo_oqtepa.move(45,10)

        self.email_edit = QLineEdit(self)
        self.email_edit.setFixedSize(325,50)
        self.email_edit.setPlaceholderText('Enter your email 🔍')
        self.email_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'border: 2px solid black;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 25px'
            )
        

        self.btn_find = QPushButton('FIND',self)
        self.btn_find.setFixedSize(200,40)
        self.btn_find.setStyleSheet(
            'background-color: #FFD700;'
            'color: red;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            'font: 20px;'
            )
        
        self.email_edit.move(130,400)
        self.btn_find.move(185,485)
        self.btn_exit.move(10,720)

        self.btn_find.clicked.connect(self.press_btn_find)
        self.btn_exit.clicked.connect(self.press_btn_exit)
    
    def press_btn_exit(self):
        self.close()
        self.login = LoginPage()
        self.login.show()
    
    def press_btn_find(self):
        if self.email_edit.text() != '':
            self.count = 0
            self.finner = str()

            try:
                with mydb.cursor() as cursor:

                    email = self.email_edit.text()

                    sql = f"""select email,password from oq_tepa                   
                    """
                    cursor.execute(sql)
                    result = cursor.fetchall()

                    for i in result:
                        i = list(i)
                        if email == i[0]:
                            self.count += 1
                            self.finner = i[1]

            except Exception as err:
                print(err)
        
        if self.count == 1:
            self.email_edit.setPlaceholderText(f'Password: {self.finner} ✅')
            self.email_edit.setStyleSheet(
                'border-width: 2px;'
                'border-radius: 8px;'
                'border-style: solid;'
                'border: 2px solid green;'
                'background-color: #f4f4f4;'
                'color: #3d3d3d;'
                'font-weight: bold;'
                'font: 25px'
                )
            self.email_edit.clear()
        else:
            self.email_edit.setPlaceholderText(f'Email Not Found ❌')
            self.email_edit.setStyleSheet(
                'border-width: 2px;'
                'border-radius: 8px;'
                'border-style: solid;'
                'border: 2px solid red;'
                'background-color: #f4f4f4;'
                'color: #3d3d3d;'
                'font-weight: bold;'
                'font: 25px'
                )
            self.email_edit.clear()


class MenuPage(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.logo_oqtepa = QLabel(self)

        self.setFixedSize(1200, 780)

        self.setStyleSheet('background-color: white')

        self.btn_total_amout = QPushButton(self)
        self.btn_total_amout.setText('TOTAL AMOUT')

        self.btn_kefsi = QPushButton(self)
        self.btn_kefsi.setText('KEFSI')

        self.btn_set = QPushButton(self)
        self.btn_set.setText('SET')

        self.btn_lavash = QPushButton(self)
        self.btn_lavash.setText('LAVASH')

        self.btn_xaggi_club = QPushButton(self)
        self.btn_xaggi_club.setText('XAGGI AND CLUB')

        self.btn_hamburger = QPushButton(self)
        self.btn_hamburger.setText('HAMBURGER')

        self.btn_pizza = QPushButton(self)
        self.btn_pizza.setText('PIZZA')

        self.btn_xot_dog = QPushButton(self)
        self.btn_xot_dog.setText('XOT DOG')

        self.btn_snek = QPushButton(self)
        self.btn_snek.setText('SNEK')

        self.btn_desert = QPushButton(self)
        self.btn_desert.setText('DESERT')

        self.btn_drinks = QPushButton(self)
        self.btn_drinks.setText('DRINKS')

        self.btn_salad = QPushButton(self)
        self.btn_salad.setText('SALAD')

        self.btn_sous = QPushButton(self)
        self.btn_sous.setText('SOUS')

        self.btn_logout = QPushButton(self)
        self.btn_logout.setText('LOG OUT')

        self.show()

        self.initUi()
    
    def initUi(self):

        self.galochka_pixmax = QPixmap('D:Oqtepa/logo_menu.png')

        self.logo_oqtepa.setPixmap(self.galochka_pixmax)

        self.logo_oqtepa.resize(self.galochka_pixmax.width(),self.galochka_pixmax.height())

        self.galochka_pixmax = QPixmap()

        self.logo_oqtepa.move(425,20)

        self.btn_total_amout.setStyleSheet(
            'background-color: 	#00FF00; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_total_amout.setFixedSize(300,80)


        self.btn_kefsi.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_kefsi.setFixedSize(300,80)

        self.btn_set.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_set.setFixedSize(300,80)

        self.btn_lavash.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_lavash.setFixedSize(300,80)


        self.btn_xaggi_club.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_xaggi_club.setFixedSize(300,80)


        self.btn_hamburger.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_hamburger.setFixedSize(300,80)


        self.btn_pizza.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_pizza.setFixedSize(300,80)


        self.btn_xot_dog.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_xot_dog.setFixedSize(300,80)


        self.btn_snek.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_snek.setFixedSize(300,80)



        self.btn_desert.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_desert.setFixedSize(300,80)


        self.btn_drinks.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_drinks.setFixedSize(300,80)


        self.btn_salad.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_salad.setFixedSize(300,80)


        self.btn_sous.setStyleSheet(
            'background-color: #FFB90F; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_sous.setFixedSize(300,80)


        self.btn_logout.setStyleSheet(
            'background-color: red; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid black;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_logout.setFixedSize(300,80)


        self.btn_kefsi.move(50,280)
        self.btn_set.move(450,280)
        self.btn_lavash.move(850,280)
        self.btn_xaggi_club.move(50,380)
        self.btn_hamburger.move(450,380)
        self.btn_pizza.move(850,380)

      
        self.btn_xot_dog.move(50,480)
        self.btn_snek.move(450,480)
        self.btn_desert.move(850,480)
        self.btn_drinks.move(50,580)
        self.btn_salad.move(450,580)
        self.btn_sous.move(850,580)
        self.btn_total_amout.move(630,680)
        self.btn_logout.move(280,680)


        self.btn_kefsi.clicked.connect(self.press_btn_kefsi)
        self.btn_set.clicked.connect(self.press_btn_set)
        self.btn_lavash.clicked.connect(self.press_btn_lavash)
        self.btn_xaggi_club.clicked.connect(self.press_btn_clab)
        self.btn_hamburger.clicked.connect(self.press_btn_hamburger)
        self.btn_pizza.clicked.connect(self.press_btn_pizza)
        self.btn_xot_dog.clicked.connect(self.press_btn_xot_dog)
        self.btn_snek.clicked.connect(self.press_btn_snek)
        self.btn_desert.clicked.connect(self.press_btn_desert)
        self.btn_drinks.clicked.connect(self.press_btn_drinks)
        self.btn_salad.clicked.connect(self.press_btn_salat)
        self.btn_sous.clicked.connect(self.press_btn_sous)
        self.btn_total_amout.clicked.connect(self.press_btn_total_amout)
        self.btn_logout.clicked.connect(self.press_btn_logout)

    def press_btn_kefsi(self):
        self.close()
        self.kefsi = Kefsi()
        self.kefsi.show()
    
    def press_btn_set(self):
        self.close()
        self.set = set()
        self.set.show()
    
    def press_btn_lavash(self):
        self.close()
        self.lavash = lavash()
        self.lavash.show()
    
    def press_btn_clab(self):
        self.close()
        self.clab = clab_xaggi()
        self.clab.show()
    
    def press_btn_hamburger(self):
        self.close()
        self.hamburger = hamburger()
        self.hamburger.show()
    
    def press_btn_pizza(self):
        self.close()
        self.pizza = pizza()
        self.pizza.show()
    
    def press_btn_xot_dog(self):
        self.close()
        self.xot_dog = xot_dog()
        self.xot_dog.show()
    
    def press_btn_snek(self):
        self.close()
        self.snek = snek()
        self.snek.show()
    
    def press_btn_desert(self):
        self.close()
        self.desert =desert()
        self.desert.show()

    def press_btn_drinks(self):
        self.close()
        self.drinks = drinks()
        self.drinks.show()
    
    def press_btn_salat(self):
        self.close()
        self.salat = salat()
        self.salat.show()
    
    def press_btn_sous(self):
        self.close()
        self.sous = sous()
        self.sous.show()
    
    def press_btn_total_amout(self):
        self.close()
        self.total = total()
        self.total.show()
    
    def press_btn_logout(self):
        self.close()
        self.login = LoginPage()
        self.login.show()

class total(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('background-color: white')

        self.sum = int()

        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select sum(price) from zakaz         
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    i = list(i)
                    i = i[0]
                    if i != None:
                        self.sum += i

        except Exception as err:
            print(err)

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText("BACK")
        self.btn_exit.setStyleSheet(
            'background-color: #FFC125; '
            'font: 15px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid red;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_exit.setFixedSize(200,50)

        
        self.v_box = QHBoxLayout()

        self.h_box = QVBoxLayout()

        self.label1 = QLabel(self)
        self.label1.setText('PRODUCT NAME')
        self.label1.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )

        self.label2 = QLabel(self)
        self.label2.setText('NUMBER')
        self.label2.move(406,8)
        self.label2.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )

        self.label3 = QLabel(self)
        self.label3.setText('PRICE')
        self.label3.move(800,8)
        self.label3.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
        
        self.qlw = QListWidget()
        self.qlw2 = QListWidget()
        self.qlw3 = QListWidget()

        self.v_box.addWidget(self.qlw)
        self.v_box.addWidget(self.qlw2)
        self.v_box.addWidget(self.qlw3)

        self.h_box.addWidget(self.label1)
        self.h_box.addLayout(self.v_box)
        self.h_box.addWidget(self.btn_exit)

        self.setLayout(self.h_box)
        

        self.setFixedSize(1200,900)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.label_total = QLabel(self)
        self.label_total.setText('TOTAL:')
        self.label_total.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )

        self.label_total2 = QLabel(self)
        self.label_total2.setText(f'{self.sum}')
        self.label_total2.setStyleSheet(
                    'color: green;'
                    'font-size: 20px;'
                    'font-weight: bold;'
                    )

        self.show()

        self.show_data()

        self.btn_exit.clicked.connect(self.press_exit)

        self.label_total.move(800,850)
        self.label_total2.move(880,850)


    def show_data(self):
        self.sum = int()
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select name_of_product from zakaz         
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'
                    )
                    self.i = str(i)
                    self.qlw.addItem(self.i[2:-3])
        except Exception as err:
            print(err)

        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select num_of_product from zakaz         
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw2.addItem(self.i[2:-3])
        except Exception as err:
            print(err)

        
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select price from zakaz         
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw3.addItem(self.i[1:-2])
        except Exception as err:
            print(err)


    def press_exit(self):
        self.two = MenuPage()
        self.close()
        self.two.show()
    
class info(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(650, 800)

        self.setStyleSheet('background-color: white')
        
        self.logo_oqtepa1 = QLabel(self)

        self.logo_oqtepa2 = QLabel(self)

        self.logo_oqtepa3 = QLabel(self)

        self.logo_oqtepa4 = QLabel(self)

        self.btn_instagram = QPushButton(self)
        self.btn_instagram.setText('INSTAGRAM')

        self.btn_telegram = QPushButton(self)
        self.btn_telegram.setText('TELEGRAM')

        self.btn_chrome = QPushButton(self)
        self.btn_chrome.setText('GOOGLE')

        self.btn_facebook = QPushButton(self)
        self.btn_facebook.setText('FACEBOOK')

        self.btn_back = QPushButton(self)
        self.btn_back.setText('BACK')

        self.initUi()

    def initUi(self):

        self.galochka_pixmax = QPixmap('D:Oqtepa/oqtepa_logo.png')

        self.logo_oqtepa1.setPixmap(self.galochka_pixmax)

        self.logo_oqtepa1.resize(self.galochka_pixmax.width(),self.galochka_pixmax.height())

        self.galochka_pixmax = QPixmap()

        self.logo_oqtepa1.move(70,0)

        self.btn_instagram.setIcon(QIcon('D:Oqtepa/instagram.png'))
        self.btn_instagram.setFixedSize(300,80)
        self.btn_instagram.setStyleSheet(
            'background-color: white; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_instagram.setIconSize(QSize(40,40))


        self.btn_telegram.setIcon(QIcon('D:Oqtepa/telegram.png'))
        self.btn_telegram.setFixedSize(300,80)
        self.btn_telegram.setStyleSheet(
            'background-color: white; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_telegram.setIconSize(QSize(40,40))


        self.btn_chrome.setIcon(QIcon('D:Oqtepa/chrome.png'))
        self.btn_chrome.setFixedSize(300,80)
        self.btn_chrome.setStyleSheet(
            'background-color: white; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_chrome.setIconSize(QSize(40,40))

        self.btn_facebook.setIcon(QIcon('D:Oqtepa/facebooc.png'))
        self.btn_facebook.setFixedSize(300,80)
        self.btn_facebook.setStyleSheet(
            'background-color: white; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.btn_facebook.setIconSize(QSize(40,40))

        self.btn_back.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : black;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 20'
        )
        self.btn_back.setFixedSize(110,50)

        self.btn_back.move(10,730)


        self.btn_telegram.move(160,350)

        self.btn_instagram.move(160,450)

        self.btn_chrome.move(160,550)

        self.btn_facebook.move(160,650)

        self.btn_facebook.clicked.connect(self.press_btn_facebook)

        self.btn_chrome.clicked.connect(self.press_btn_chrome)

        self.btn_instagram.clicked.connect(self.press_btn_instagram)

        self.btn_telegram.clicked.connect(self.press_btn_telegram)

        self.btn_back.clicked.connect(self.press_btn_back)

        self.show()
    
    def press_btn_facebook(self):
        os.system('start https://www.facebook.com/oqtepalavash.official')
    
    def press_btn_chrome(self):
        os.system('start https://oqtepalavash.uz/')
    
    def press_btn_instagram(self):
        os.system('start https://www.instagram.com/oqtepalavash.official/')
    
    def press_btn_telegram(self):
        os.system('start https://t.me/oqtepalavash_bot')
    
    def press_btn_back(self):
        self.MainWindow = MainWindow()
        self.close()
        self.MainWindow.show()
    

app = QApplication(sys.argv)

win = LoginPage()

sys.exit(app.exec_())




