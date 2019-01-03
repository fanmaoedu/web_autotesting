
import unittest
from selenium import webdriver

class WeiboLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    
    def setUp(self):
        driver = self.driver
        driver.maximize_window()



    def test_post_topic(self):
        pass



    def tearDown(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.save_screenshot('./topic.png')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
    