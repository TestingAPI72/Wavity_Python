import time
from lib.selenium_keywords import keywords_custom
from Utilities.Data_readers import Data_readers
from Utilities.logger_log import *
from Utilities.database_connective import database_connective

log = customLogger()


class wave_login_page(keywords_custom):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.xpath = Data_readers()
        self.data_base = database_connective()

    def wave_login_screen(self):
        xpaths = self.xpath.bring_locator("Login_Page")
        credientals = self.data_base.accessing_database(values='credientals')
        username = credientals[0]
        password = credientals[1]
        self.open_browser("https://tenant2.wavity.info/wavity/auth/signin/")
        start_time = 0
        element_status = False
        # while not element_status:
        #     if self.is_element_present(locator=xpaths[0]["email_user_field"]):
        #         start_time += 1
        #         element_status = True
        #         if start_time > 30:
        #             assert start_time > 30, "Shouldn't be more than 30 seconds for login screen, Time taken {}".format(start_time)
        #     continue
        # log.info("{}s Milli seconds have been taken to for login screen ".format(str(start_time)))
        self.window_maximize()
        self.input(xpaths[0]["email_user_field"], data=username)
        self.click(xpaths[0]["submit_button"])
        self.input(xpaths[0]["password_field"], data=password)
        self.click(xpaths[0]["submit_button"])
