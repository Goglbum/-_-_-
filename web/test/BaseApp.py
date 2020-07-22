from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql.cursors

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://192.168.220.1:81"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator), message="Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator), message="Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_db(self):
        self = pymysql.connect(host='192.168.220.1',
                                     user='root',
                                     password='password',
                                    db='www_project',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        return self