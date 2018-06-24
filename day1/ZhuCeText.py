#在这个python文件中,实现注册功能的自动化

#从 谷歌公司的一个项目名  导入 网络驱动,用代码来操作浏览器的
from selenium  import webdriver
#打开网页
driver =webdriver.Chrome
#访问地址
driver.get("http://localhost/")
#进入注册页面
driver.find_element_by_class_name("reg")
#填写注册信息
driver.find_element_by_name("username").send_keys("shanshan")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("13666666666")
driver.find_element_by_name("email").send_keys("ssyu@rxhui.com")
driver.find_element_by_class_name("reg_btn").click()

