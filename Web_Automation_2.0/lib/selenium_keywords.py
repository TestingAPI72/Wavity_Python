import subprocess
import sys

import pytest

from Driver_Config import webdriver_initalizer
from selenium.common.exceptions import *
from Utilities.logger_log import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from Utilities.Data_readers import Data_readers
import time

log = customLogger()
from Utilities.Data_readers import *


class keywords_custom:
    appname = ''

    def __init__(self, driver):
        self.action_obj = ActionChains(driver)
        self.obj_alert = Alert(driver)
        self.driver = driver
        self.xpath = Data_readers()

    def click(self, locator):
        time.sleep(3)
        try:
            self.wait_until_element_loaded(locator)
            element_status = self.is_element_present(locator=locator)
            if not element_status:
                raise Exception("Given element is not found in the page {}".format(locator))
            element_status.click()
        except ElementClickInterceptedException as e:
            log.error("Cannot click the element: {}".format(sys.exc_info()))
            raise AssertionError("Cannot click the element {}".format(sys.exc_info()))

    def open_browser(self, url):
        try:
            self.driver.get(url=url)
        except:
            log.error("Cannot open the url : {}".format(sys.exc_info()))
            raise Exception

    def reload_page(self):
        try:
            self.driver.refresh()
        except:
            log.error("cannot refresh the page {}".format(sys.exc_info()))
            raise AssertionError

    def input(self, locator, data):
        time.sleep(3)
        try:
            self.wait_until_element_loaded(locator)
            element_status = self.is_element_present(locator)
            if not element_status:
                raise Exception("Given element is not found in the page {}".format(locator))
            element_status.send_keys(data)
        except:
            log.error("Cannot send the data {}".format(sys.exc_info()))
            raise Exception

    def is_element_present(self, locator, duration=1):
        global Element_Status
        try:
            self.wait_until_element_loaded(locator)
            Element_Status = self.driver.find_element_by_xpath(locator)
            original_style = Element_Status.get_attribute('style')
            self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", Element_Status,
                                       "background:white;color:Red;border:4px dotted red;")
            if duration > 0:
                time.sleep(duration)
                self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", Element_Status,
                                           "style", original_style)
                return Element_Status
        except NoSuchElementException as e:
            log.error("Element is present in given page {}".format(sys.exc_info()))
            return False

    def get_window_title_text(self):
        try:
            return self.driver.title
        except:
            log.error("Can't able to get window's title {}".format(sys.exc_info()))
            raise Exception

    def switch_to_another_tab(self, locator):
        time.sleep(3)
        try:
            current_window = self.driver.current_window_handle
            all_window_handler = self.driver.window_handles
            for window in all_window_handler:
                if current_window != window:
                    self.driver.switch_to.window(window)
                    self.is_element_present(locator=locator)
                    break
        except:
            log.error("Can't switch to another tab {}".format(sys.exc_info()))
            raise AssertionError

    def accept_alert(self):
        try:
            self.obj_alert.accept()
        except NoAlertPresentException as e:
            log.error("no alert is present {}".format(e))
            raise e

    def dismiss_alert(self):
        try:
            self.obj_alert.dismiss()
        except NoAlertPresentException as e:
            log.error("can't dismiss alert {}".format(e))

    def close_tab(self):
        try:
            all_window_handler = self.driver.window_handles
            for window in all_window_handler:
                self.driver.switch_to.window(window)
                if self.is_element_present(locator="//div[@class='wavity-branding-icon']"):
                    current_window = self.driver.current_window_handle
                    if current_window== window:
                        break
                else:
                    self.driver.close()

        except:
            log.error("Can't able to close tab {}".format(sys.exc_info()))
            raise AssertionError

    def drag_and_drop_element(self, source, target=None):
        time.sleep(3)
        try:
            source_element = self.is_element_present(locator=source)
            target_element = self.is_element_present(locator=target)
            self.action_obj.click_and_hold(source_element).move_to_element(target_element).release().perform()
        except:
            raise AssertionError(sys.exc_info())

    def window_maximize(self):
        try:
            self.driver.maximize_window()
        except:
            log.error("can't maximize window {}".format(sys.exc_info()))

    def wait_until_element_loaded(self, locator):
        try:
            WebDriverWait(self.driver, 30, poll_frequency=1).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except NoSuchElementException as e:
            log.error("element is not loaded in given time {}".format(sys.exc_info()))
            assert e

    def get_text(self, locator):
        try:
            return self.driver.find_element_by_xpath(locator).text()
        except:
            log.error("Can't able to get text {}".format(sys.exc_info()))

    def select_by_visible_text(self, text, locator):
        try:
            select_obj = Select(self.driver.find_element_by_xpath(str(locator)))
            select_obj.select_by_visible_text(text=text)
        except:
            log.error("select_by_visible_text failed {}".format(sys.exc_info()))
            raise AssertionError

    def wait_until_pop_visible(func):

        def inner(self):
            func(self)
            self.wait_until_element_loaded(
                locator="//div[@class='modal-content']//div//p[contains(text(),'Application design has updated successfully')]")
            self.is_element_present(
                locator="//div[@class='modal-content']//div//p[contains(text(),'Application design has updated successfully')]")
            time.sleep(5)
            self.close_tab()
            self.switch_to_another_tab(locator="//div[@class='wavity-branding-icon']")
            time.sleep(5)

        return inner

    @staticmethod
    def random_string():
        return "wav_" + str(random.randint(999, 99999))

    @staticmethod
    def building_xpath(path, data1, data2='undefined'):
        try:
            log.info("Building_xpath started")
            if '{0}' in path:
                _xpath_quote = str(path).replace('{0}', data1)
                return _xpath_quote
            elif '{1}' in path:
                _xpath_quote = str(path).replace('{1}', data1)
                return _xpath_quote
            elif '{0}' and '{1}' in path:
                _xpath_quote = str(path).replace('{0}', data1)
                _final_xpath = str(_xpath_quote).replace('{1}', data2)
                return _final_xpath
        except TypeError:
            log.error("building_xpath failed {} ".format(sys.exc_info()))

    def create_application(self, app_type):
        xpath = self.xpath.bring_locator('App_Creation_Page', 'Login_Page')
        try:
            self.is_element_present(locator=xpath[1]['sign_toast'])
            self.is_element_present(locator=xpath[1]['wavity_brand_logo'])
            self.click(locator=xpath[0]['app_toaster_page'])
            self.click(locator=xpath[0]['app_button'])
            self.is_element_present(locator=xpath[0]['app_create_button'])
            self.click(locator=xpath[0]['app_down_arrow'])
            self.click(locator=xpath[0]['app_new_app'])
            window_title = self.get_window_title_text()
            if not window_title:
                raise Exception("Can't able to get window title")
            # start_time = 0
            # element_status = False
            # while not element_status:
            #     if self.is_element_present(locator=xpath[0]['app_name']):
            #         start_time += 1
            #         element_status = True
            #         if start_time > 30:
            #             assert start_time > 30, "Shouldn't be more than 30 seconds for app creation page, Time taken {}".format(
            #                 start_time)
            #     continue
            # log.info("{}s Milli seconds have been taken to for login screen ".format(str(start_time)))
            self.switch_to_another_tab(locator=xpath[0]['app_create_application_message'])
            keywords_custom.appname = self.random_string()
            self.input(locator=xpath[0]['app_name'], data=keywords_custom.appname)
            self.click(locator=xpath[0]['app_type'])
            user_app = self.building_xpath(path=xpath[0]['custom_app_type'], data1=str(app_type))
            log.info(user_app)
            self.click(locator=user_app)
            time.sleep(5)
            self.click(locator=xpath[0]['continue_button'])
            time.sleep(5)
        except:
            log.error("Problem in creating apptype \n {}".format(sys.exc_info()))
            raise Exception

    def adding_controls_to_created_app(self, controls_type, maximum=3):
        xpath = self.xpath.bring_locator('App_Creation_Page', 'Main_Control', 'App_Controls_All')
        assert len(xpath) == 3, "Length is not equal user input"
        try:
            log.debug(xpath)
            assert maximum == 3, "Max controls should be 3"
            sub_controls_with_controls = self.building_xpath(path=xpath[2]["all_controls"],
                                                             data1=str(controls_type).capitalize())
            for _ in range(maximum):
                self.click(locator=self.building_xpath(path=xpath[1]['main_controls'], data1=controls_type))
                _ += 1
                sub_controls_with_controls_path = sub_controls_with_controls.replace('{1}', str(_))
                self.drag_and_drop_element(source=sub_controls_with_controls_path,
                                           target=xpath[0]["controls_drop_area"])
                control_xpath = xpath[0]['controls_labels']
                controls_label = control_xpath.replace('{1}', str(_))
                self.input(locator=controls_label, data=self.random_string())
        except:
            log.error("adding_controls_to_created_app failed {}".format(sys.exc_info()))
            raise Exception

    @wait_until_pop_visible
    def submit_app(self):
        xpath = self.xpath.bring_locator('App_Designer_Page', 'App_Creation_Page')
        assert len(xpath) == 2, "length not equal two"
        try:
            self.click(locator=xpath[0]['record_title_dropdown'])
            self.click(locator=xpath[0]['record_title'])
            self.click(locator=xpath[0]['Save_button'])
            time.sleep(5)
        except:
            log.error('can''\t submit the app {}'.format(sys.exc_info()))

    def Activate_created_application(self):
        xpath = self.xpath.bring_locator('App_Home')
        try:
            time.sleep(5)
            self.input(locator=xpath[0]['search_bar'], data=keywords_custom.appname)
            self.click(locator=xpath[0]['dots_menu'])
            self.click(locator=xpath[0]['Activate_button'])
            self.wait_until_element_loaded(locator=xpath[0]['No_apps'])
            self.reload_page()
        except:
            log.error("Cannot able to activate app {}".format(sys.exc_info()))
            raise Exception

    def app_status(self):
        try:
            xpath = self.xpath.bring_locator('App_Home')
            self.input(locator=xpath[0]['search_bar'], data=keywords_custom.appname)
            app_status = self.get_text(locator=xpath[0]['app_active_status'])
            assert app_status == 'Active'
            self.reload_page()
        except:
            log.error("can't able to get app status {}".format(sys.exc_info()))

    def delete_created_apps(self, appname='wav'):
        xpath = self.xpath.bring_locator('App_Home')
        try:
            self.input(locator=xpath[0]['search_bar'], data=appname)
            try:
                elements = self.driver.find_elements_by_xpath(xpath[0]['created_apps'])
            except NoSuchElementException as e:
                log.error("Elements not founded")
                assert False
            for _ in elements:
                self.is_element_present(locator=str(xpath[0]['created_apps_custom']).replace('{0}', str(_)))
        except:
            pass

    @staticmethod
    def kill_any_specific_process_thru_shell(**process):

        """
        kill_all_specific_process function is used to kill any linux process given by user
        Eg: to kill excel, format : soffice.bin(process name)
        :param process: dict format(eg : excel='soffice.bin')
        :return: None
        """

        global stderr
        for key, value in process.items():
            try:
                p1 = subprocess.Popen(['ps', '-e'], stdout=PIPE, stderr=PIPE, text=True)
                stdout, stderr = p1.communicate()
                for x in str(stdout).splitlines():
                    if re.search('^(.*\d*\s{})'.format(value), x):
                        output = re.search('^(.*\d*\s{})'.format(value), x).group().strip()
                        if re.search('(..\d+ \W)', output):
                            pid_no = re.search('(..\d+ \W)', output).group().strip('?').strip()
                            p2 = subprocess.Popen(['kill', '{}'.format(pid_no)], stderr=PIPE, stdout=PIPE, text=True)
                            stdout, stderr = p2.communicate()
                            log.info(stdout)
                        log.info("No process id for {}".format(value))
                    log.info("No process with name {} is running".format(value))
            except AttributeError:
                log.error(stderr)
                log.error(sys.exc_info())
                raise AssertionError
