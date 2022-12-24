from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# NOTE for firefox browser
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# NOTE for chrome browser
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# NOTE for firefox browser
browser = webdriver.Firefox(options=options,
                            service=FirefoxService(GeckoDriverManager().install()))
# NOTE for chrome browser
# browser = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

# NOTE If the router page is secured then fill up your credential by using below format
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

browser.quit()
