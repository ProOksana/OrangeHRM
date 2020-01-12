from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_login(self):
        success = True
        wd = self.wd
        wd.get("https://mvisionsapi.azurewebsites.net/Home/Login")
        wd.find_element_by_name("FUserName").click()
        wd.find_element_by_name("FUserName").clear()
        wd.find_element_by_name("FUserName").send_keys("Oksi")
        wd.find_element_by_name("FPassword").click()
        wd.find_element_by_name("FPassword").clear()
        wd.find_element_by_name("FPassword").send_keys("test")
        wd.find_element_by_name("LoginAs").send_keys("Visions User")
        wd.find_element_by_id("loginBtn").click()
        self.assertTrue(success)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()