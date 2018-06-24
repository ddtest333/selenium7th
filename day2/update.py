from selenium import webdriver

# 文件名.类名,包名,变量名,所有的命名都该以字母开口,可以有数据和下划线
# 但是不能有空格和中文
from day2.UpdateMenberInfo import Login

driver =webdriver.Chrome()
#每次创建浏览器时,implicitly_wait固定写一次,对在这个浏览器上执行的所有代码都生效
#implicitly_wait主页检测页面的加载时间,检测什么时候页面加载完,什么时候执行后续操作
driver .implicitly_wait(20)
#实例化对象会占用内存,pycharm会自动帮我们释放内存
#代码运行完,检测到Lofin()这个对象,不在被使用,系统会自动释放
#把driver浏览器传入到登录方法中
#让登录方法和下面的点击账号设置使用一个浏览器
#我们现在已经创建号一个空白的浏览器了,后续的所有操作都该在这个浏览器中执行
Login().loginWithDefaultUser(driver)
#点击"账号分析
#本来要点击"账号设置,需要使用 driver这个变量,但现在文件中没有driver这个变量了 怎么办?
#可以重新声明一个driver么

# 2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
# 3.点击个人资料
#partial_link_text可以使用连接的一部分进行元素定位
#当连接文本过程时,推荐使用partial
#使用partial_link_text方法时,可以用连接中的任意部分,只要在网页中唯一即可
driver.find_element_by_class_name("ico_nav8").click()
#xpath的方法比较通用,作为一种么有办法时使用
#但是不推荐使用,作为
#driver.find_element_by_xpath();

#driver.find_element_by_partial_link_text("")
# 4.修改真实姓名
#r如果输入框中原本有内容,那么我们修改内容时,往往需要先清空
#实际上一个良好的变成习惯是在每次sendkes之前,都先做clear()操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("姜小白")
# 5.修改性别
#通过观察,可以发现,保密/男/女 唯一的区别就是value属性
#实际上我们可以通过任何属性来定位
#要想通过value属性定位有两种方法 :xpath/css_selector
#通过css-selectot定位元素,只要在唯一属性两边加一一个[]
#driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中//表示采用相对路径定位元素,
#/单斜巷表示绝对路径,一般都是从/html节点开始定位元素
#相对路径一般通过元素的特殊属性查找元素
#绝对路径一般通过元素的位置,层级关系查找元素
#绝对路径写起来比较长,涉及到节点比较多,当开发人员修改页面布局时,收影响的可能性比较大
#相对路径,查询速度比较慢,因为肯呢过需要遍历更多的节点
#工作中一般用绝对还是相对? 工作中推荐用css_seletor
#css_selector的查询速度比xpath快一些
#css跟xpath的可读性比较
#xpath在某些浏览器上支持的不太好.比如ＩＥ
#css_selector 所有前段开发都在用
# *号便是任意节点
#[@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]')
#javascript 的 getElementByClassName()方法可以找到符合条件的所有元素
#然后通过下标选取第N个元素也可以定位
#selenium可不可以用这中思路做?
driver.find_elements_by_id("xb")[2].click()
# 6.修改生日
#一下一下点年/月/日是可以实现的
#但是稳定性比较差,很容易点错
#并且 很难修改日期,
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("2019-01-01")
# 7.修改QQ
# 8.点击确定.保存成功