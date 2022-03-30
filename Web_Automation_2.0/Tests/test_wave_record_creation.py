import unittest
import pytest
from pathlib import Path
from Pages.Wave_login_page import wave_login_page
from Pages.Wave_Create_app import wave_create_app
from Pages.Wave_Record_Creation import wave_Record_Creation

# from pytest_bdd import given, when, then, scenario
#
# featurefiledir = 'wavity_features'
# featurefilename = 'wavity_login.feature'
# BASEDIR = Path(__file__).resolve().parent
# FEATURE_FILE =BASEDIR.joinpath(featurefiledir)
@pytest.mark.Regression
@pytest.mark.usefixtures("start_driver","deleting_logs","close_all_actions")
class create_record(unittest.TestCase):

    @pytest.fixture(autouse=True)
    #@scenario(features_base_dir=FEATURE_FILE,feature_name='wavity_login.feature', scenario_name='Object Initiator')
    def class_objects(self):
        self.login = wave_login_page(self.driver)
        self.create_app_wave = wave_create_app(self.driver)
        self.create_record = wave_Record_Creation(self.driver)

    #@given("Creating_application")
    def test_wave_record_creation(self):
        self.login.wave_login_screen()
        self.create_app_wave.wave_create_app()
        self.create_record.wave_record_creation()

