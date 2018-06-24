from  selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.implicitly_wait(20)
#登录海盗商城后台
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
#验证码输入
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_css_selector(".Btn").submit()
#选择商品管理模块
driver.find_element_by_link_text("商品管理").click()

#点击添加商品连接
driver.find_element_by_link_text("添加商品").click()
#driver.find_element_by_css_selector(".text_input Validform_error").send_keys("冰箱")
#输入商品名称
#操作子框架中的元素,首先要进行frame切换
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("冰箱")
#选择商品分类(双击 或者点击选择当前分类)
#在下拉框中选择商品品牌
#点击提交按钮