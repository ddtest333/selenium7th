#用unittest 写一个后台登录的测试用例
#导包
import  unittest
#键类,并且继承unittest.TestClass
import time


from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    #重写setUp tearDownClass
    @classmethod
    def setUpClass(self):
        #做web 自动化测试是不是所有的测试用例都要先打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #窗口最大化代码,要求驱动版本和浏览器精准匹配


    @classmethod
    def tearDownClass(self):

        time.sleep(30)
        #每次执行完测试用例,应该把打开的浏览器关闭.释放内存,清除cookie 和 缓存 为下次测试用例做准备\
        #这里调用的driver 是声明在setUp 方法中的一个局部变量,局部变量是不允许被其他方法访问的,所以我们应该把setUp方法中声明的driver 改写成一个全局变量
        #因为self表示类本身,所以我们只要在变量前加self.,就表示这个变量数属于类的
        self.driver.quit()
    def test_login(self):
        #为了简化代码可以把成员变量self.drver,改写赋值给局部变量 driver
        driver =self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        #有些常用的键也可以用转义字符代替,其中\t 表示Tab 键 ,\n 表示enter
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()
        #
    def test_prpduct_adding(self):
        driver =self.driver
        #添加商品
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #除了用name 属性切换 frame 也可以
        iframe=driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        #等于driver.switch_frame(frame的名字)
        driver.find_element_by_name("name").send_keys("电视机")
        #选择分类
        #变量名文件名的起名规则:数字/大写字母/下划线/一般要求以字母开头
        #如果id 是纯数字,用#号的方式不能定位,
        # 可以用[]方式定位,所有属性都可以用[]定位
        driver.find_element_by_css_selector("[id=1]").click()
        driver.find_element_by_id('2').click()
        #driver.find_element_by_id('7').click()
        ActionChains(driver).double_click(driver.find_element_by_id('7')).perform()
        select = Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_sarch").click()




#如果第二个方法重新打开一个浏览器,登录就无效了,
if __name__ == '__main__':
         unittest.main()