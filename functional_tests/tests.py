from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class RegistrationTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
