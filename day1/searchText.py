#打开主页
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#点击"登录"按钮

driver.find_element_by_class_name("login_btn ").click()
#在搜索中输入iphone
#driver.find_element_by_name("keyword").send_keys("iphone")
#如果我们向在新的标签页上操作页面元素
#需要进行窗口切换
#driver.switch_to.window(第二个窗口的名字)
#接下来的问题就是,如何获取第二个窗口的名字了
#selenium 提供了浏览器中所有窗口名字的集合
#handle 是句并的意思,把句并理解为名字就可以了
#driver.window_handles可以理解为一个数组,我要求第二个窗口子的明名字怎么做
#[1]表示数据的第二个元素
#driver.window_handles[1]
#所以,第二个窗口的名字及是  driver.window_handles[]1
#所以,窗口切换语句是
driver.swith.window(driver.window_handles[1])
#这时再试一下,iphine  会被输入哪个窗口中
driver.find_element_by_name("keyword").send_keys("iphone")
#这就是窗口切换的方法
#[1]表示第二个元素,[-1]表示最后一个元素
#在python中元祖和数列表可以正这从0开始数
#可以-这从-1开始数,倒数第一个-1,倒数第二个-2
#所以上面的代码可以改成什么? 把1改成-1 试一试
#如果这端代码能理解了,在回到logtest.点击加入购物车