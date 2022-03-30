import unittest
import pytest
from Pages.Wave_login_page import wave_login_page


@pytest.mark.Smoke
@pytest.mark.usefixtures("start_driver")
class login_page(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.login = wave_login_page(self.driver)

    def test_login_page(self):
        self.login.wave_login_screen()
