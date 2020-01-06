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
        wd.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        wd.find_element_by_name("txtUsername").click()
        wd.find_element_by_name("txtUsername").clear()
        wd.find_element_by_name("txtUsername").send_keys("Admin")
        wd.find_element_by_name("txtPassword").click()
        wd.find_element_by_name("txtPassword").clear()
        wd.find_element_by_name("txtPassword").send_keys("admin123")
        wd.find_element_by_id("btnLogin").click()
        wd.implicitly_wait(20)
        wd.find_element_by_id("welcome").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
