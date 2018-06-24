#通过ddt 代码库实现数据驱动
#1/导包
import  ddt
import unittest
import time
from  selenium import  webdriver
#2/为类增加一个装饰器.装饰器类似于java中的注解,
#@ddt.ddt  表示这个类实现数据驱动测试
from selenium.webdriver.common.by import By
from  day5.csvFileManager4 import  CsvFileManager4


@ddt.ddt
class RegisterTest2(unittest.TestCase):
    #3/声明一个变量 ,读取csv文件的测试数据
    data_table =  CsvFileManager4().read('test_data.csv')
    @classmethod
    def setUpClass(cls):
        cls.driver =webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    #为test_register  方法 添加装饰器 @ddt.data,指定测试数据
    #data_table  是一个list 类型,包含很多元素
    #在data_table 前面加一个* 号表示调用 ddt.data()方法时
    #我们传入的不是列表,而是单独传的列表中的每一个元素
    #所以*号的作用就是 把列表中的每个元素 都单独看成一个参数
    #假如 一个方法需要的参数数点不固定,我们可以用这种方法
    @ddt.data(*data_table)
    #5/给方法添加一个参数, row
    #如果想取第一列数据,那么应该是row([1])
    def test_register(self,ros):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            # find_elemrnt()
            # driver.find_element_by_name("username")=driver.find_element(By.NAME,"username")
            # 这两种方法没有任何区别,但是后面这中方法扩展性更好,便于框架封装
        driver.find_element(By.NAME, "username").send_keys(ros[0])
        driver.find_element(By.NAME, "password").send_keys(ros[1])
        driver.find_element(By.NAME, "userpassword2").send_keys(ros[2])
        driver.find_element(By.NAME, "mobile_phone").send_keys(ros[3])
        driver.find_element(By.NAME, "email").send_keys(ros[4])



        check_tip = driver.find_element(By.CSS_SELECTOR," body > div.w1180 > div > div.reg_main > div.reg_left.fl > form > ul > li:nth-child(1) > div > span").text
        self.assertEqual("用户名不低于三位，使用中文、数字、字母皆可！", check_tip)




if __name__ == '__main__':
    unittest.main()