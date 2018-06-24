#这种框架的设计思想叫做 page-object 设计模式,是一种高级的框架设计思想
#这种思想的主旨是把业务逻辑和代码技术分离开
#测试用例的类,专门负责业务逻辑
#元素定位和操作交给,网页对象
#在 object 这个类中,把每个网页看成一个类
#网页中的每个元素看成类中的一个属性
#针对这个元素的操作,看成类中的一个方法
#元素的信息,定位是名词性,所以可以看成属性(成员变量)
#元素的操作是动词性的,所以可以看成是方法
#下面我们封装一下,登录这个网页

#这个类主要做的就是把元素定位 改一个易于理解的名字


from selenium import webdriver
from selenium.webdriver.common.by import By


class LogigPage:
    #为这个网页创建一个构造函数
    #在python中构造函数固定名字 __init__()
    def __init__(self,driver):
        #因为setup 中已经创建了一个浏览器,
        # 所以这里不需要新建浏览器,直接用setUp 建好的浏览器
        self.driver = driver
        self.url ="http://localhost/index.php?m=user&c=public&a=login"
#声明一个变量,保存元素的定位方式
        #python 的元祖,类似于数组
        #这句化的意识是,声明了一个数组叫 username_input_loc
        #这个数组中有两个元素,分别是 By.ID/  username
        #*号表示find_element() 这个方法 传入的不是一个元祖,而是把元祖中的每个元素都分别传入find_element() 这个方法 作为单独的参数
    username_input_loc =(By.ID,"username")
    password_input_loc =(By.ID,"password")
    login_button_loc =(By.CLASS_NAME,"login_btn")


    def open(self):
        self.driver.get(self.url)
        #给参数设置默认值,如果调用方法时,传入一个新的用户名,那么使用新的
        #如果调用方式时,不传参,使用默认自
        #这类中涉及到三个元素定位,因为元素定位不太稳定,经常修改所以应该把定位方式 声明成 类中的一个属性
    def input_username(self,username="yushanshan" ):
     #   self.find_element_(By.ID,"username").send_keys(username)
     self.find_element_(*self.username_input_loc).send_keys(username)
    def input_password(self,password="123456"):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def clice_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

