from selenium import webdriver
import time,unittest

class testcase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()
        self.browser.get("http://192.168.0.139:8080")
        print("start test_01")

    def test01(self):
        browser = self.browser
        browser.find_element_by_name("username").send_keys("lucy")
        browser.find_element_by_name("password").send_keys("123456")
        try:
           browser.find_element_by_xpath("/html/body/div/form/div/div[3]/button").click()
        except Exception as e:
            print(e)
        else:
            elem = browser.find_element_by_xpath("/html/body/div/div/h1").text
            print("login success!")
            print(elem)


        try:
            browser.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul[1]/li[3]/a").click()
        except Exception as e:
            print(e)
        else:
            text = browser.find_element_by_xpath("/html/body/div/div/h4[1]/li[2]/a").text
            print("找到：",text)


        try:
            browser.find_element_by_xpath("/html/body/div/div/h4[1]/li[2]/a").click()
        except Exception as e:
            print(e)
        else:
            text = browser.find_element_by_tag_name("body").text
            if text == "权限不足！":
                print(text)
                print("测试OK")
            else:
                print("username is wrong!")


    def tearDown(self):
        print("end test_01")
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
