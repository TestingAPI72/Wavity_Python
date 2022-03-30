import time
from lib.selenium_keywords import keywords_custom
from Utilities.Data_readers import Data_readers
from Utilities.database_connective import database_connective


class wave_create_app(keywords_custom):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.xpath = Data_readers()
        self.data_base = database_connective()

    def wave_create_app(self):
        self.create_application(app_type='company')
        self.adding_controls_to_created_app(controls_type='date', maximum=3)
        self.submit_app()
