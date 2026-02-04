import unittest
from selenium import webdriver
from Base_framework import Funciones


class Examen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.f = Funciones(self.driver)

    def test_form(self):
        self.f.Navigate("https://demoqa.com/automation-practice-form", .6)
        self.f.text_mixto()
        
        self.f.Time(2)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

