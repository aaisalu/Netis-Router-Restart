from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from plyer import notification

# for firefox browser
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# NOTE for chrome browser
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# NOTE If the router page is secured, then fill up your credentials by using the below format:
# router_ip= "login_username:login_password@ip_of_router"
router_ip = "http://192.168.2.1/"

# to debug set level to debug
logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {name:<5} - {levelname:<8} - {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)


class web_driver():
    options = Options()
    options.headless = True  # set false when debugging
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # for firefox browser
    browser = webdriver.Firefox(options=options,
                                service=FirefoxService(GeckoDriverManager().install(), log_path='/dev/null'))
    # NOTE for chrome browser
    # browser = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))


def reboot_it(ip_adr):
    sucess_msg = "Router has been successfully restarted."
    failed_msg = "Router could not be restarted."
    try:
        logging.info("Accessing the router login page")
        web_driver.browser.get(ip_adr)
        sleep(2)

        # advanced btn
        logging.info("Navigating to the advanced menu")
        advanced_btn = web_driver.browser.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/a/img')
        advanced_btn.click()
        sleep(2)

        # system tools
        sys_tools = web_driver.browser.find_element(
            By.ID, "p_menu_misc")
        sys_tools.click()

        # restart_menu
        restart_menu = web_driver.browser.find_element(By.ID, 'c_menu_reboot')
        restart_menu.click()

        # reboot_btn
        reboot_btn = web_driver.browser.find_element(
            By.XPATH, '//*[@id="reboot"]')
        reboot_btn.click()
        logging.info("Please wait while the router restarts")

        # accept browser_alert
        web_driver.browser.switch_to.alert.accept()

        # close browser and logs the result
        quit_driver()
        logging.info(f"{sucess_msg}\n")

        # sends user notification
        ping("⏳  Restarting the router! ", sucess_msg)

    except Exception as e:
        logging.critical(f'{failed_msg} because of the following error {e}\n')
        ping("⚠️  Restarting the router failed!",
             f'{failed_msg} due to an error {e}')
        quit_driver()


def quit_driver():
    web_driver.browser.quit()


def ping(header, msg):
    notification.notify(
        title=header,
        message=msg,
        timeout=10,
    )


def main():
    try:
        reboot_it(router_ip)
    except KeyboardInterrupt:
        quit_driver()


if __name__ == "__main__":
    main()
