# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import time, unittest

class testcase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.browser.get("http://192.168.0.100:8090/zentaopms/www/index.html")
        print("start chandao_test_01")

#----------------------------登录------------------------------
    def test01(self):
        a = self.browser
        try:
            a.find_element_by_id("account").send_keys("yanjinzhu")
            a.find_element_by_name("password").send_keys("123456")
            a.find_element_by_id("submit").click()
        except Exception as e:
            print(e)
        else:
            print("login success!")
#-----------------------------点击测试--------------------
        try:
            elem = a.find_element_by_id("menuqa")
        except Exception as e:
            print(e)
        else:
            elem.click()

#---------------------点击提Bug---------------------------------

        try:
            t = a.find_element_by_xpath('//*[@id="featurebar"]/div[1]/div[2]/a[2]')
        except Exception as e:
            print(e)
        else:
            t.click()

#---------选择版本-----------
        try:
            a.find_element_by_id("buildBox").click()
            a.find_element_by_xpath('//*[@id="openedBuild_chosen"]/div/ul/li').click()
        except Exception as e:
            print(e)
        else:
            print("OK,choose version sucess!")


#----------输入标题-------------
        try:
            a.find_element_by_id("title").clear()
            a.find_element_by_id("title").send_keys("哈哈")
        except Exception as e:
            print(e)
        else:
            print("OK,input title success!")

#-----------保存------------------------------
        try:
            a.find_element_by_xpath("//form[@id='dataform']/table/tbody/tr[14]/td[2]/button").submit()
        except Exception as e:
            print(e)
        else:
            print("OK,submit bug success!")


#--------------------搜索框输入Bug编号-----------------------
        try:
            elem = a.find_element_by_id("searchQuery")
        except Exception as e:
            print(e)
        else:
            elem.send_keys("016")

#-------------------点击"GO"查询Bug---------------------------
        try:
            a.find_element_by_xpath('//*[@id="objectSwitcher"]/a').click()
        except Exception as e:
            print(e)

        try:
            a.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[2]/div[1]/div/fieldset[1]/legend')
            msg = True
        except:
            msg = False

        if msg == True:
            print("search bug success!")
        else:
            print("search bug failed!")

#------------------关闭浏览器------------------------------
    def tearDown(self):
		print("end test chandao OK!")
        self.browser.close()

if __name__ == "__main__":
    unittest.main()




