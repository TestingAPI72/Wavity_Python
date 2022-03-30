import unittest
import pytest
from pathlib import Path
from Pages.Wave_login_page import wave_login_page
from Pages.Wave_Create_app import wave_create_app

# from pytest_bdd import given, when, then, scenario
#
# featurefiledir = 'wavity_features'
# featurefilename = 'wavity_login.feature'
# BASEDIR = Path(__file__).resolve().parent
# FEATURE_FILE =BASEDIR.joinpath(featurefiledir)
@pytest.mark.Sanity
@pytest.mark.usefixtures("start_driver","deleting_logs","close_all_actions")
class create_app(unittest.TestCase):

    @pytest.fixture(autouse=True)
    #@scenario(features_base_dir=FEATURE_FILE,feature_name='wavity_login.feature', scenario_name='Object Initiator')
    def class_objects(self):
        self.login = wave_login_page(self.driver)
        self.create_app_wave = wave_create_app(self.driver)

    #@given("Creating_application")
    def test_wave_app_creation(self):
        self.login.wave_login_screen()
        self.create_app_wave.wave_create_app()
