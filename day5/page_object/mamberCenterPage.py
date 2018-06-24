from selenium.webdriver.common.by import By


class MemberCenterPage:
    def __init__(self,driver):
        self.driver =driver
        self.url ="http://localhost/index.php?m=user&c=index&a=index"
    welcome_link_loc =(By.PARTIAL_LINK_TEXT,"您好")
    #get_welcome_link_text()  用户返回"你好连接的所有文本内容,这是页面上的实际结果

    def get_welcome_link_text(self):
        return self.driver.find_element(*self.welcome_link_loc).text
    #如果当前累中 赋值driver时,没有先用driver = webdriver.chrome(),后面写代码想用selenium 放发时,因为IDE 不知道driver的类型,就不会给出提示信息
    #比如在输入self.driver 时,后面 不会 自动提示 find_element() 这个方法