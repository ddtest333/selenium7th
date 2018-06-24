
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("http://localhost/")
driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
driver.find_element_by_link_text("登录").click()

driver.find_element_by_name("username").send_keys("yushanshan")
actions =ActionChains(driver)

actions.send_keys(Keys.TAB).send_keys("123456").perform()
actions.send_keys(Keys.ENTER).perform()

