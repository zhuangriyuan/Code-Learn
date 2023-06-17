from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#导入动作链
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

#如果标签是存在于iframe标签之中的，则必须通过如下方法定位
driver.switch_to.frame("iframeResult")
dragable_button = driver.find_element(By.CLASS_NAME,"ui-draggable")
print(dragable_button)

#滑块拖动
action = ActionChains(driver)
action.click_and_hold(dragable_button).perform()

for i in range(5):
	action.move_by_offset(37,0).perform()
	time.sleep(0.2)
action.release().perform()