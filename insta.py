from selenium import webdriver
from config import INSTA_PASS, INSTA_USER
import time

browser = webdriver.Chrome()

url = 'https://www.instagram.com'

browser.get(url)
time.sleep(2)
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
submit_button = browser.find_element_by_css_selector('button[type = "submit"]')

time.sleep(2)
username.send_keys(INSTA_USER)
password.send_keys(INSTA_PASS)
submit_button.click()


my_follow_btn_xpath = "//button[text()='Follow']"
follow_btn_elements = browser.find_elements_by_xpath(my_follow_btn_xpath)

for btn in follow_btn_elements:
    time.sleep(1)
    try:
        btn.click()
    except:
        pass

