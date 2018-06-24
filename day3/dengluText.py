#seleniu  执行javascript 中的两个关键字:return(返回值)和 arguments(参数)
import time
from  selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/")
#点击登录链接
#用javascript找登录链接(document.getElementsByClassName("site-nav-right fr")[0].childNodes[1])
#用selenium的方法找
#driver.get_element_by_link_test("")
#某些元素,用selenium 的方法找元素比javascript 更容易
#虽然selenium不支持 removeAttribute 的方法
# 但是 selenium找到登录链接和 javascript 找到的是同一个元素
#我们可不可以用selenium 找到元素后,转换成javascript的元素?
#这样以后写javascript 就容易很多,不需要childnodes 这个方法了
login_link =driver.find_element_by_link_text("登录")
#把原来的 javascript 看成一个无参数无返回的方法,现在直接从外面传入一个压页面元素
#把selenium 找到的这个元素,传入到javascript方法里
#arguments 参数的复数形式,[0]表示第一个参数,值的是js后面的login_link
#所以下面的这句代码,相当于把driver.finf_elemient_by_link_test()带入到javascript中
#argument是参数数组,值的是js侯爱民的参数
driver.execute_script('arguments[0].removeAttribute("target")',login_link)
login_link.click()
#登录
driver.find_element_by_name("username").send_keys("yushanshan")

ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()


#返回商城首页
driver.find_element_by_link_text("返回商城首页").click()
#搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()

#点击商品(用这种方法,在实现一次)
#body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a > img
#因为img没有target属性 所以我们要找父节点a标签
#赋值出来人css比较长,我们可以适当的缩写长度
#我们定位元素的目标节点是最后一个节点,最后一个节点
#大于号>的前面是父节点,后面是子节点
#每个几点的第一个的单词是标签名,比a,div,body
#小数点后面表示class属性
#:nth-child(2),nth 表示第几个 4th/5th,nth表示第N个,child 表示子节点
#所以:nth-child(2)表示当前标签是他的父节点的第二个子节点
product_link_css=" div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a"

#通过xpath 定位元素
iphone=driver.find_element_by_css_selector(product_link_css)
#删除元素target属性

#使用javascript 删除a标签属性
driver.execute_script('arguments[0].removeAttribute("target")',iphone)
iphone.click()
#在相拼详情页界面点击加入购物车
driver.find_element_by_id("joinCarButton").click()

driver.find_element_by_css_selector(".shopCar_T_span3").click()
#在每个class前面都加一个小数点,并且去掉中间的空格,我们就可以用两个class 定位了
#点击结算按钮
driver.find_element_by_css_selector(".shopCar_btn_03").click()
#点击添加新地址
driver.find_element_by_css_selector(".add-address").click()
#输入是收货人等信息(选择地区)
driver.find_element_by_name("address[address_name]").send_keys("多里")
driver.find_element_by_name("address[mobile]").send_keys("13566666666")
##
dropdow1=   driver.find_element_by_id("add-new-area-select")
#下拉框是一种特殊的网页元素,对下拉框的操作和网页普通元素不太一样
#selenium 为这种特殊的元素专门创建一个类select
#dropdown1 的类型是一个普通的网页元素,下面这句代码的意思是
#把一个普通的网页元素,装换成一个下拉框的特殊网页元素
print(type(dropdow1))#dropdow  是webElement 类型
#webElement 这个类中,没有选择下拉狂选择的方法
select1 = Select(dropdow1)

print(type(select1))#select1 是Select 方法

select1.select_by_value("320000")#页可以通过选项的值来定位
time.sleep(2)
select1.select_by_visible_text("辽宁省")#页可以 通过文本信息来定位
#选择沈阳市
#因为是动态ID所以不能通过DI定位
#因为class重复 ,所以我们不能直接用class定位
#但是 我们可用find_element  的方法,先找到页面中所有class=add-new-area-select 的元素
#然后通过下标的方式选择第N个页面元素
#这种方法类似与javascript
#
dropdow2 = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdow2).select_by_visible_text("沈阳市")
#dropdow3 = driver.find_elements_by_class_name("add-new-area-select")[2]

#Select(dropdow3).select_by_visible_text("铁西区")
#tag_name() 方法大多数情况可以找到一堆元素,
#所以 find_elemenr_tag_name () 这个方法很少用
#但是find_elemenr_tag_name ()[] 这个方法比较常用
dropdow3= driver.find_elements_by_tag_name("select")[2]
Select(dropdow3).select_by_visible_text("铁西区")
#填写详细地址
driver.find_element_by_css_selector(".add-new-name-span-2").send_keys("铁丝南路")
#填写邮编
driver.find_element_by_css_selector(".add-new-name-span-3").send_keys("1099999")
#点击确定 ,保存收货人信息
driver.find_element_by_class_name("aui_state_highlight").click()