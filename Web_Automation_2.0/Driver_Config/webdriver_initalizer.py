import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utilities.logger_log import *
import sys

log = customLogger()


class WebDriverClass:

    def chrome_driver(self):
        try:
            options = Options()
            options.headless = False
            options.page_load_strategy = 'normal'
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(time_to_wait=30000)
            return driver
        except:
            log.error("Session is not created {}".format(sys.exc_info()))

# if __name__ =='__main__':
#     d1 =driver_start()
#     d1.chrome_driver()
