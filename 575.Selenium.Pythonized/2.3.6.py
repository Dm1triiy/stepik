from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # time.sleep(1)
    wname = browser.window_handles[1]
    browser.switch_to.window(wname)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
 
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()