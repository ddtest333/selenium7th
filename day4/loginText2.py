
#1.导包
import time
import unittest
from selenium import webdriver



#2.建类,并集成unittest.TestCase
from selenium.webdriver import ActionChains



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    #    4个空格,在pycharm中可以用tab键代替
    #   对于初学者,或者找工作来讲,格式是最重要
    #   算法是程序的灵魂, 个人认为,格式是程序的外表
    @classmethod
    def tearDownClass(self):
#         为了保证可以看清测试结果,可以在tearDown方法中加一个30秒的延时等待
        time.sleep(30)
#
        self.driver.quit()

    def test_login(self):

        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")

        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

    def test_product_adding(self):
        driver = self.driver
#       添加商品的代码
#       如果第二个方法重新打开一个浏览器,登录就无效了,怎么办?



if __name__ == '__main__':
    unittest.main()
