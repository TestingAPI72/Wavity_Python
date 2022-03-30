from Driver_Config.webdriver_initalizer import WebDriverClass
import pytest
import os
from lib.selenium_keywords import keywords_custom
from Utilities.logger_log import customLogger
from Utilities.Data_readers import Data_readers
from Utilities.database_connective import database_connective

log = customLogger()


@pytest.fixture(scope='class')
def start_driver(request):
    session = WebDriverClass()
    driver = session.chrome_driver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def deleting_logs():
    try:
        if os.path.exists('/home/alethea/PycharmProjects/Web_Automation_2.0/Tests/Logfile.log'):
            os.remove('/home/alethea/PycharmProjects/Web_Automation_2.0/Tests/Logfile.log')
    except FileNotFoundError as e:
        log.error("file not found {}".format(e))


@pytest.fixture(scope='session')
def close_all_actions():
    dr = Data_readers()
    db = database_connective()
    yield
    dr.data_readers_teardown()
    del dr
    db.data_base_teardown()
    del db


