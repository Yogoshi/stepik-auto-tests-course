from selenium import webdriver
import time
import math
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn.btn-primary").click()
    conf = browser.switch_to.alert
    conf.accept()
    number =browser.find_element_by_id("input_value").text
    conv_num1 = str(math.log(abs(12*math.sin(int(number)))))
    browser.find_element_by_class_name("form-control").send_keys(conv_num1)
    browser.find_element_by_class_name("btn.btn-primary").click()
        
finally:
    time.sleep(5)
    browser.quit()