from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time
from itertools import groupby
from collections import Counter

class StoreSeacrhLocators:
    LOCATOR_STORE_SEARCH_HEAD = (By.XPATH, "//head")
    LOCATOR_STORE_SEARCH_TOP_BREND = (By.XPATH, "//a[@class='navbar-brand']")
    LOCATOR_STORE_SEARCH_TOP_BAR = (By.XPATH, "//*[@id='navbar']/ul/li")
    LOCATOR_STORE_PUBLESHER = (By.XPATH, "//*[@id='navbar']/ul/li[1]/a")
    LOCATOR_STORE_BOOKS = (By.XPATH, "//*[@id='navbar']/ul/li[2]/a")
    LOCATOR_STORE_CONTACT = (By.XPATH, "//*[@id='navbar']/ul/li[3]/a")
    LOCATOR_STORE_MY_CART = (By.XPATH, "//*[@id='navbar']/ul/li[4]/a")
    LOCATOR_STORE_WELCOME_CONTAINER = (By.XPATH, "//div[@class='jumbotron']")
    LOCATOR_STORE_BOOK_START_LIST = (By.XPATH, "//div[@class='col-md-3']")
    LOCATOR_STORE_START_LIST_BOOK_TEXT = (By.XPATH, "//*[@id='main']/p")
    LOCATOR_STORE_ADMIN_LOG = (By.XPATH, "//div[@class ='text-muted pull-right']")
    LOCATOR_STORE_PROJECT = (By.XPATH, "//div[@class ='text-muted pull-left']")
    LOCATOR_STORE_CONTAINER = (By.XPATH, "//*[@id='main']")



class SearchHelper(BasePage):

    def brand(self):
        return self.find_element(StoreSeacrhLocators.LOCATOR_STORE_SEARCH_TOP_BREND).click()

    def check_list(self):
        all_list = self.find_elements(StoreSeacrhLocators.LOCATOR_STORE_BOOK_START_LIST)
        assert len(all_list) == 4

    def check_bar(self):
        all_list = self.find_elements(StoreSeacrhLocators.LOCATOR_STORE_SEARCH_TOP_BAR)
        text_brand = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_SEARCH_TOP_BREND).text
        text_publisher = all_list[0].find_element_by_xpath(".//a").text
        text_books = all_list[1].find_element_by_xpath(".//a").text
        text_contact = all_list[2].find_element_by_xpath(".//a").text
        text_my_cart = all_list[3].find_element_by_xpath(".//a").text
        assert text_publisher == '  Publisher'
        assert text_books == '  Books'
        assert text_contact == '  Contact'
        assert text_my_cart == '  My Cart'
        assert text_brand == 'CSE Bookstore'

    def check_welcome(self):
        welcome = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_WELCOME_CONTAINER)
        text1 = welcome.find_element_by_xpath('.//h1').text
        text2 = welcome.find_element_by_xpath('.//p[@class="lead"]').text
        text3 = welcome.find_element_by_xpath('.//p[2]').text
        assert text1 == 'Welcome to online CSE bookstore'
        assert text2 == 'This site has been made using PHP with MYSQL (procedure functions)!'
        assert text3 == "The layout use Bootstrap to make it more responsive. It's just a simple web!"

    def check_latest(self):
        text_latest = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_START_LIST_BOOK_TEXT).text
        assert text_latest == 'Latest books'

    def text_footer(self):
        admin_text = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_ADMIN_LOG).text
        project_text = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PROJECT).text
        assert admin_text == 'Admin Login 2017'
        assert project_text == 'projectworlds'

    def check_publisher_text(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        publisher_text = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        text = publisher_text.find_element_by_xpath(".//p[@class='lead']").text
        text_list = publisher_text.find_elements_by_xpath(".//ul/li")
        text_wrox = text_list[0].find_element_by_xpath(".//a").text
        text_wiley = text_list[1].find_element_by_xpath(".//a").text
        text_oreilly_media = text_list[2].find_element_by_xpath(".//a").text
        text_apress = text_list[3].find_element_by_xpath(".//a").text
        text_packt_publishing = text_list[4].find_element_by_xpath(".//a").text
        text_addison_wesley = text_list[5].find_element_by_xpath(".//a").text
        text_list_full_of_books = text_list[6].find_element_by_xpath(".//a").text
        assert text == 'List of Publisher'
        assert text_wrox == 'Wrox'
        assert text_wiley == 'Wiley'
        assert text_oreilly_media == "O'Reilly Media"
        assert text_apress == 'Apress'
        assert text_packt_publishing == 'Packt Publishing'
        assert text_addison_wesley == 'Addison-Wesley'
        assert text_list_full_of_books == 'List full of books'

    def check_publisher_list(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT publisherid FROM books "
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["publisherid"])
                list_db_text = Counter(list_db)

            publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
            publisher_list = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_site = publisher_list.find_elements_by_xpath(".//ul/li")
            number_list_wrox = list_site[0].find_element_by_xpath(".//span").text
            number_list_wiley = list_site[1].find_element_by_xpath(".//span").text
            number_list_oreilly_media = list_site[2].find_element_by_xpath(".//span").text
            number_list_apress = list_site[3].find_element_by_xpath(".//span").text
            number_list_oreilly_packt_publishing = list_site[4].find_element_by_xpath(".//span").text
            number_list_oreilly_addison_wesley = list_site[5].find_element_by_xpath(".//span").text
            assert str(list_db_text[1]) == str(number_list_wrox)
            assert str(list_db_text[2]) == str(number_list_wiley)
            assert str(list_db_text[3]) == str(number_list_oreilly_media)
            assert str(list_db_text[4]) == str(number_list_apress)
            assert str(list_db_text[5]) == str(number_list_oreilly_packt_publishing)
            assert str(list_db_text[6]) == str(number_list_oreilly_addison_wesley)
        finally:
            connection.close()

    def check_book_title_wrox(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE publisherid = 1"
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["book_title"])
            publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            wrox = container.find_element_by_xpath(".//ul/li[1]/a").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book_title_site = container.find_elements_by_xpath(".//h4")
            list_site = []
            for row in list_book_title_site:
                list_site.append(row.text)
            assert list_db == list_site
        finally:
            connection.close()

    def check_wrox_text(self):
        publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wrox = container.find_element_by_xpath(".//ul/li[1]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wrox_text = container.find_element_by_xpath(".//p[@class='lead']").text
        assert wrox_text == 'Publishers > Wrox'

    def check_link_publisher_wrox(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wrox = container.find_element_by_xpath(".//ul/li[1]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        publisher_link = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        assert self.driver.title == "List Of Publishers"

    def check_book_title_wiley(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE publisherid = 2"
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["book_title"])
            publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            wiley = container.find_element_by_xpath(".//ul/li[2]/a").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book_title_site = container.find_elements_by_xpath(".//h4")
            list_site = []
            for row in list_book_title_site:
                list_site.append(row.text)
            assert list_db == list_site
        finally:
            connection.close()

    def check_wiley_text(self):
        publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wiley = container.find_element_by_xpath(".//ul/li[2]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wiley_text = container.find_element_by_xpath(".//p[@class='lead']").text
        assert wiley_text == 'Publishers > Wiley'

    def check_link_publisher_wiley(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wiley = container.find_element_by_xpath(".//ul/li[2]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        publisher_link = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        assert self.driver.title == "List Of Publishers"

    def check_book_title_reilli_media(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE publisherid = 3"
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["book_title"])
            publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            reilli_media = container.find_element_by_xpath(".//ul/li[3]/a").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book_title_site = container.find_elements_by_xpath(".//h4")
            list_site = []
            for row in list_book_title_site:
                list_site.append(row.text)
            assert list_db == list_site
        finally:
            connection.close()

    def check_reilli_media_text(self):
        publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        reilli_media = container.find_element_by_xpath(".//ul/li[3]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        reilli_media_text = container.find_element_by_xpath(".//p[@class='lead']").text
        assert reilli_media_text == "Publishers > O'Reilly Media"

    def check_link_publisher_reilli_media(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        reilli_media = container.find_element_by_xpath(".//ul/li[3]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        publisher_link = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        assert self.driver.title == "List Of Publishers"

    def check_book_title_apress(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE publisherid = 4"
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["book_title"])
            publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            apress = container.find_element_by_xpath(".//ul/li[4]/a").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book_title_site = container.find_elements_by_xpath(".//h4")
            list_site = []
            for row in list_book_title_site:
                list_site.append(row.text)
            assert list_db == list_site
        finally:
            connection.close()

    def check_apress_text(self):
        publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        apress = container.find_element_by_xpath(".//ul/li[4]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        apress_text = container.find_element_by_xpath(".//p[@class='lead']").text
        assert apress_text == "Publishers > Apress"

    def check_link_publisher_apress(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        apress = container.find_element_by_xpath(".//ul/li[4]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        publisher_link = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        assert self.driver.title == "List Of Publishers"

    def check_book_title_addison_wesley(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE publisherid = 6"
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["book_title"])
            publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            apress = container.find_element_by_xpath(".//ul/li[6]/a").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book_title_site = container.find_elements_by_xpath(".//h4")
            list_site = []
            for row in list_book_title_site:
                list_site.append(row.text)
            assert list_db == list_site
        finally:
            connection.close()

    def check_addison_wesley_text(self):
        publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        addison_wesley = container.find_element_by_xpath(".//ul/li[6]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        addison_wesley_text = container.find_element_by_xpath(".//p[@class='lead']").text
        assert addison_wesley_text == "Publishers > Addison-Wesley"

    def check_link_publisher_addison_wesley(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        addison_wesley = container.find_element_by_xpath(".//ul/li[6]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        publisher_link = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        assert self.driver.title == "List Of Publishers"

    def check_link_publisher_books(self):
        publisher= self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        list_full_books = container.find_element_by_xpath(".//ul/li[7]/a").click()
        assert self.driver.title == "Full Catalogs of Books"

    def check_books_all_list(self):
        connection = self.go_to_bd()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books "
                result_bd = cursor.execute(sql)
            books = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_BOOKS).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            books_list = container.find_elements_by_xpath(".//div[@class='col-md-3']")
            result_site = len(books_list)
            assert str(result_bd) == str(result_site)
        finally:
            connection.close()