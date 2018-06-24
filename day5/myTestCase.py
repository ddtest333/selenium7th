#在mytestCase .中封装setUp和teat Dowm  达到一劳永逸的效果
import  unittest
from  selenium import  webdriver
import  time


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        #time.sleep(30)
        cls.driver.quit()
