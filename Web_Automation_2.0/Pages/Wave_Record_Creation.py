import time
from lib.selenium_keywords import keywords_custom
from Utilities.Data_readers import Data_readers
from Utilities.database_connective import database_connective


class wave_Record_Creation(keywords_custom):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wave_record_creation(self):
        self.Activate_created_application()
        self.app_status()
