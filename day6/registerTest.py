import  unittest

import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.DBconnection import BDConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        #数据库验证,测试的正常情况
        self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver =self.driver
        driver.find_element(By.NAME, "username").send_keys("yushanshan0011")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        driver.find_element(By.NAME, "mobile_phone").send_keys("13600000020")
        driver.find_element(By.NAME, "email").send_keys("ssy1u@163.com")
        driver.find_element(By.CLASS_NAME,"reg_btn").click()
        time.sleep(2)
        sql = "SELECT * FROM hd_user order by id desc "
        new_record =BDConnection().execute_sql_command()
        self.assertEqual("yushanshan0011",new_record[1])
        self.assertEqual("ssy1u@163.com",new_record[2])
        print(new_record)
