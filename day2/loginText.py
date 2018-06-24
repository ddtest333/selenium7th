
from selenium   import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#1/打开浏览器
driver =webdriver.Chrome()
#2/打开海盗商城网站
driver.get("http://localhost")
#3/删除登录连接的属性
#在python中字符串可以用单引号,页可以用双引号
#如果字符串本身包含双引号,那么我们就在两边使用单引号
driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
#4/点击登录按钮,跳转到登录页面
driver.find_element_by_link_text("登录").click()
#输入用户名
driver.find_element_by_id("username").send_keys("yushanshan")
#输入密码
#ActionChains 需要导包,导包快捷键alt+enter
#action 动作行为的意思,chaine是连表的意思,链表类似与数组
#所以ActionChains 是一组动作和行为的意思
#下面这句话的作用是实例化一个ActionChains 这个类的对象,这个对象可以用来执行和java的区别就是去掉
actions = ActionChains(driver)
#如果你向使用键盘上的任意控件,直接在Keys这个类中找就可以了
#所有Action中的方法都必须以perform()结尾才会被执行
actions.send_keys(Keys.TAB).send_keys("123456").perform()
#7/点击登录按钮
#actions.send_keys(Keys.ENTER).perform()
#加入不支持回车登录,我们可以直接点击登录按钮
#加入也很难定位登录按钮,我还可以用submit()
#submit是提交的意思,用于提交表单
#想向一下,用户名和密码等信息是不是同时发送给后端服务器?
#开发通过form 表单把这些信息同时提交到服务器
#可以用任何一个元素执行submit()来提交表单中的所有数据
#比如,我们可以使用户名来提交表单数据
driver.find_element_by_id("username").submit()