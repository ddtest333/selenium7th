#
# 因为大部分测试用例都会用到登录功能,那么我们可不可
# 把登录功能单独封装成一个方法,每次直接调用这个方法
# 就可以了,这样以后每次登录就还需要一行方法调用的代码
# 如何把这个文件封装成一个登录方法
# python中类的关键字和java一样,是

# 1.登录海盗商城
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# python中使用冒号代替java中的大括号
# 在冒号后面敲回车,会自动缩进4个空格
# 所有数据类中语句,都必须空4个空格
#注释方法:全选 按 ctrl+/   加3个单/双引号
#
class Login:
    # def是方法的关键字,表示这是一个方法
    # loginWithDefaultUser,这是我们随意起的方法名,意思是 使用默认账户登录
    # 方法后面必须要有括号,可以用来声明参数
    # 括号中默认有一个参数(self),self表示类本身,类似于java中的this关键字
    # self参数后面在详细将,暂时用不到
    # 方法的声明后面也有一个冒号,下面所有语句还要在缩进4个空格
    # 这样登录功能的代码,就被封装到loginWithDefaultUser()方法中了
    # 以后只需要写一句话,调用这个方法,即可登录网站了

    def loginWithDefaultUser(self,driver):
        driver.get("http://localhost/")
        driver.execute_script( 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_id("username").send_keys("yushanshan")
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()

        #  2.点击账号设置
        # driver.find_element_by_link_text("账号设置").click()
        #  3.点击个人资料
        # driver.find_element_by_class_name("hover")
        #  4.修改真实姓名
        #  5.修改性别
        #  6.修改生日
        #  7.修改QQ
        #  8.点击确定.保存成功
