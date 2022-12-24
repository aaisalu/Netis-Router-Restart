from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service

browser = webdriver.Firefox()

# NOTE using service to map driver
# browser = webdriver.Firefox(service=Service('./geckodriver'))
# NOTE If router page got login enabled then uncomment and fill your router credentials
# browser.get("login_username:login_password@ip_of_router")

browser.get("http://192.168.2.1/")
sleep(2)

# advanced btn
advanced_btn = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/a/img')
advanced_btn.click()
sleep(2)

# system tools
sys_tools = browser.find_element(
    By.ID, "p_menu_misc")
sys_tools.click()

# restart_menu
restart_menu = browser.find_element(By.ID, 'c_menu_reboot')
restart_menu.click()

# reboot_btn
reboot_btn = browser.find_element(By.XPATH, '//*[@id="reboot"]')
reboot_btn.click()

# brower_alert-accept
browser.switch_to.alert.accept()
