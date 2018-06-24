
from selenium.webdriver.support import expected_conditions as EC
from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3,打开登录页面
driver.find_element_by_id("username").send_keys("yushanshan")
driver.find_element_by_name("password").send_keys("123456")
#4.输入用户名和密码
driver.find_element_by_class_name("login_btn ").click()
#以为中间存在一个""登录成功页面,所以不能直接点击连接
#显示等待代码
WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))
driver.find_element_by_link_text("进入商城购物").click()
