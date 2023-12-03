###########################################################
## Выжевский Евгений
## Код Автотест для программы обучения QA тестировщик
## Версия 1.0
## Name = Selenium_AutoTest
##
## Test_object=radiokot.ru
##
## переменная среды windows path должна быть установлена
##              для chromedriver.exe
###########################################################

## ВНИМАНИЕ !!! ТЕСТИРУЕТСЯ БОЕВОЙ САЙТ. НА САЙТЕ ПРИСУТСТВУЕТ DDOS защита. Скрипт может не выполнятся из-за КАПЧИ !

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import random
import time
import os
import os.path
import sys

#################################################################################################################
## Selenium_AutoTest CLASS ######################################################################################
#################################################################################################################

class Selenium_AutoTest:
    ## Класс Автотеста ориентированый на проведение GET запросов в Автотестах
    ## Основные элементы исследования Menu, TextBox, Button

    def __init__(self,Service_Option,Main_web_url):
        Service_path=self.Get_Enveronment_Path()
        self.local_option=Options()
        self.local_option.add_experimental_option(Service_Option[0],Service_Option[1])
        self.local_services=Service(Service_path)
        self.local_driver=webdriver.Chrome(options=self.local_option,service=self.local_services)
        self.local_url=Main_web_url
        self.average_delay=1000

    def Start(self):
        try:
            self.local_driver.get(self.local_url)
        except Exception as e:
            self.StateMessage("error","Не верный URL (ошибка с доступом к странице)")
            sys.exit()

    def StateMessage(self,state,text):
        # helper вывод сообщений статуса.
        if state=="error":
            print('\033[31m',"ERROR: ",text)
        elif state=="success":
            print("\033[32m","SUCCESS: ",text)
        elif state=="info":
            print("\033[34m","Information: ",text)
        else:
            raise Exception('НЕВЕРНЫЙ ФОРМАТ СООБЩЕНИЙ ОБ ОШИБКЕ !!! state->',state)

    def Info(self,message_str):
        # нешний хелпер для инфо сообщений
        driver.StateMessage("info",message_str)

    def Delay(self):
        # использовать среднюю задержку (Set_Average_delay)
        time.sleep(self.average_delay+(random.randrange(-150,150)/1000))


    def Set_Average_delay(self,mils_int):
        # установить среднюю задержку
        mils_int = int(mils_int)

        if (mils_int < 300 or mils_int > 10000):
            raise Exception('Формат от 300 до 10000 миллисекунд var->', mils_int)
        mils_int = (mils_int+random.randrange(-100,100)) / 1000
        self.average_delay=mils_int
        self.StateMessage("info","Установлен промежуток задержки времяни ->"+str(mils_int)+"сек DDOS protection")

    def Make_delay(self,mils_int):
        # дополнительная функция произвольной задержки

        mils_int=int(mils_int)
        if (mils_int<1 or mils_int>10000):
            raise Exception('Формат от 1 до 10000 миллисекунд var->', mils_int)
        mils_int=mils_int/1000
        time.sleep(mils_int)

    def Click_By_ID(self,id_name_string,comment_string,make_delay: bool):
        try:
            self.local_driver.find_element(By.ID,id_name_string).click()
        except Exception as e:
            self.StateMessage("error", "Не верный ID или его не существует ->"+comment_string+": ->"+id_name_string)
            ##sys.exit()
        else:
            self.StateMessage("success", "Тест Пройден ID_Click ->" + comment_string + ": ->" + id_name_string)

    def Click_By_XPATH(self,FULL_XPATH_name_string,comment_string,make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.XPATH, FULL_XPATH_name_string).click()
        except Exception as e:
            self.StateMessage("error", "Не верный FULL XPATH или его не существует ->"+comment_string+": ->"+FULL_XPATH_name_string)
            ##sys.exit()
        else:
            self.StateMessage("success","Тест Пройден XPAHT_Click ->"+comment_string+": ->"+FULL_XPATH_name_string)

    def Clear_and_Type_by_ID(self,id_name_string,text_string,make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.ID, id_name_string).clear()
            self.local_driver.find_element(By.ID, id_name_string).send_keys(text_string)
        except Exception as e:
            self.StateMessage("error", "Не верный ID или его не существует ->" + text_string + ": ->" + id_name_string)
        else:
            self.StateMessage("success","Тест Пройден Clear_and_Type_by_ID ->" + text_string + ": ->" + id_name_string)

    def Clear_and_Type_by_Name(self,name_string,text_string,make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.NAME, name_string).clear()
            self.local_driver.find_element(By.NAME, name_string).send_keys(text_string)
        except Exception as e:
            self.StateMessage("error", "Не верное Name или его не существует ->" + text_string + ": ->" + name_string)
        else:
            self.StateMessage("success","Тест Пройден Clear_and_Type_by_Name ->" + text_string + ": ->" + name_string)

    def Clear_and_Type_by_XPATH(self,FULL_XPATH_name_string,text_string,make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.XPATH, FULL_XPATH_name_string).clear()
            self.local_driver.find_element(By.XPATH, FULL_XPATH_name_string).send_keys(text_string)
        except Exception as e:
            self.StateMessage("error", "Не верное Name или его не существует ->" + text_string + ": ->" + FULL_XPATH_name_string)
        else:
            self.StateMessage("success","Тест Пройден Clear_and_Type_by_Name ->" + text_string + ": ->" + FULL_XPATH_name_string)

    def Press_Enter_by_XPATH(self,FULL_XPATH_name_string,make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.XPATH, FULL_XPATH_name_string).send_keys(Keys.RETURN)
        except Exception as e:
            self.StateMessage("error", "Не верный FULL XPATH или его не существует ->" + FULL_XPATH_name_string)
        else:
            self.StateMessage("success","Тест Пройден Press_Enter_by_XPATH ->" + FULL_XPATH_name_string)

    def Press_Enter_by_ID(self, id_name_string, make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.ID, id_name_string).send_keys(Keys.RETURN)
        except Exception as e:
            self.StateMessage("error",
                              "Не верный ID или его не существует ->" + id_name_string)
        else:
            self.StateMessage("success",
                              "Тест Пройден Press_Enter_by_ID ->" + id_name_string)

    def Press_Enter_by_Name(self, name_string, make_delay: bool):
        if (make_delay):
            self.Delay()
        try:
            self.local_driver.find_element(By.NAME, name_string).send_keys(Keys.RETURN)
        except Exception as e:
            self.StateMessage("error",
                              "Не верный ID или его не существует ->" + name_string)
        else:
            self.StateMessage("success",
                              "Тест Пройден Press_Enter_by_ID ->" + name_string)


    def Get_Enveronment_Path(self):
        # поиск файла chromedriver.exe в переменных среды для Servise_path
        var_env_path = os.environ.get("path")
        var_env_split_path = var_env_path.split(";")
        for val in var_env_split_path:
            file = os.path.exists(val + "\\chromedriver.exe")
            if file == True:
                return (val + "\\chromedriver.exe")



#################################################################################################################
## MAIN PROGRAMM ################################################################################################
#################################################################################################################


WebSite_NAME="https://www.google.com/"


driver=Selenium_AutoTest(["detach",True],WebSite_NAME)


driver.Set_Average_delay(500)
driver.Start()

driver.Clear_and_Type_by_ID("APjFqb","Herb der",True)
driver.Press_Enter_by_ID("APjFqb",True)
driver.Clear_and_Type_by_ID("APjFqb","Herb der Var",True)
driver.Press_Enter_by_ID("APjFqb",True)