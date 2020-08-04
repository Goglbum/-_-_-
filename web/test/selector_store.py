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
    LOCATOR_STORE_HTML = (By.XPATH, "//html")



class SearchHelper(BasePage):

    def brand(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_SEARCH_TOP_BREND).click()

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
        connection = self.go_to_db()
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
        connection = self.go_to_db()
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
        connection = self.go_to_db()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE publisherid = 2"
                cursor.execute(sql)
                result = cursor.fetchall()
                list_db = []
                for row in result:
                    list_db.append(row["book_title"])
        finally:
            connection.close()
        publisher = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_PUBLESHER).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        wiley = container.find_element_by_xpath(".//ul/li[2]/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        list_book_title_site = container.find_elements_by_xpath(".//h4")
        list_site = []
        for row in list_book_title_site:
            list_site.append(row.text)
        assert list_db == list_site

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
        connection = self.go_to_db()
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
        connection = self.go_to_db()
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
        connection = self.go_to_db()
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
        connection = self.go_to_db()
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

    def check_books_text(self):
        books = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_BOOKS).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        books_text = container.find_element_by_xpath(".//p").text
        assert books_text == "Full Catalogs of Books"

    def check_books_db(self):
        connection = self.go_to_db()
        try:
            books = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_BOOKS).click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book = container.find_elements_by_xpath(".//div[@class='col-md-3']/a")
            for i in range(0, len(list_book), 1):
                container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
                list_book = container.find_elements_by_xpath(".//div[@class='col-md-3']/a")
                list_book[i].click()
                with connection.cursor() as cursor:
                    container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
                    isbn_book = container.find_element_by_xpath(".//tbody/tr[1]/td[2]").text
                    sql = "SELECT * FROM books WHERE book_isbn= '%s'" %(isbn_book)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                book_title_site = container.find_element_by_xpath(".//p[@class='lead']").text
                book_author_site = container.find_element_by_xpath(".//tr[2]/td[2]").text
                book_descr_site = container.find_element_by_xpath(".//div/div[2]/p").text
                book_price_site = container.find_element_by_xpath(".//tr[3]/td[2]").text
                for row in result:
                    book_title_db = row["book_title"]
                    book_author_db = row["book_author"]
                    #book_descr_db = row["book_descr"]
                    book_price_db = row["book_price"]
                    #book_descr_db = book_descr_db.replace('\n', ' ').replace('  ', ' ')
                assert book_title_site == "Books > %s" %(book_title_db)
                assert str(book_author_db).strip() == str(book_author_site).strip()
                #assert str(book_descr_db) == str(book_descr_site)
                assert str(book_price_db) == str(book_price_site)
                self.driver.back()
        finally:
            connection.close()

    def check_contact_text(self):
        contact = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTACT).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        books_text_contact = container.find_element_by_xpath(".//legend").text
        books_text_container = container.find_element_by_xpath(".//p").text
        books_text_name = container.find_element_by_xpath(".//label[@for='inputName']").text
        books_text_email = container.find_element_by_xpath(".//label[@for='inputEmail']").text
        books_text_textarea = container.find_element_by_xpath(".//label[@for='textArea']").text
        books_text_help_block = container.find_element_by_xpath(".//span[@class='help-block']").text
        input_name = container.find_element_by_xpath(".//*[@id='inputName']").get_attribute("placeholder")
        input_email = container.find_element_by_xpath(".//*[@id='inputEmail']").get_attribute("placeholder")
        input_textarea = container.find_element_by_xpath(".//*[@id='textArea']").get_attribute("placeholder")
        assert books_text_contact == 'Contact'
        assert books_text_container == "I’d love to hear from you! Complete the form to send me an email."
        assert books_text_name == 'Name'
        assert books_text_email == 'Email'
        assert books_text_textarea == 'Textarea'
        assert books_text_help_block == 'A longer block of help text that breaks onto a new line and may extend beyond one line.'
        assert input_name == 'Name'
        assert input_email == 'Email'
        assert input_textarea == ''

    def check_send_message(self):
        contact = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTACT).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_name = container.find_element_by_xpath(".//*[@id='inputName']")
        input_email = container.find_element_by_xpath(".//*[@id='inputEmail']")
        input_textarea = container.find_element_by_xpath(".//*[@id='textArea']")
        input_name.send_keys('Petr')
        input_email.send_keys('Petr@gmail.com')
        input_textarea.send_keys('I like your books!')
        button = container.find_element_by_xpath(".//button[@type='submit']").click()

    def check_send_message_cancel(self):
        contact = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTACT).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_name = container.find_element_by_xpath(".//*[@id='inputName']")
        input_email = container.find_element_by_xpath(".//*[@id='inputEmail']")
        input_textarea = container.find_element_by_xpath(".//*[@id='textArea']")
        input_name.send_keys('Petr')
        input_email.send_keys('Petr@gmail.com')
        input_textarea.send_keys('I like your books!')
        text_name = input_name.get_attribute("value")
        assert text_name == 'Petr'
        button = container.find_element_by_xpath(".//button[@type='reset']").click()
        text_name = input_name.get_attribute("value")
        text_email = input_email.get_attribute("value")
        text_textarea = input_textarea.get_attribute("value")
        assert text_name == ''
        assert text_email == ''
        assert text_textarea == ''

    def check_my_cart_zero(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_MY_CART).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        my_cart_text = container.find_element_by_xpath(".//p").text
        assert my_cart_text == 'Your cart is empty! Please make sure you add some books in it!'

    def check_add_book(self):
        books = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_BOOKS).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        list_book = container.find_elements_by_xpath(".//div[@class='col-md-3']/a")
        list_title_and_author_db = []
        list_price_db = []
        for i in range(0, 3, 1):
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            list_book = container.find_elements_by_xpath(".//div[@class='col-md-3']/a")
            list_book[i].click()
            try:
                connection = self.go_to_db()
                with connection.cursor() as cursor:
                    container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
                    isbn_book = container.find_element_by_xpath(".//tbody/tr[1]/td[2]").text
                    sql = "SELECT * FROM books WHERE book_isbn= '%s'" % (isbn_book)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                for row in result:
                    book_title_db = row["book_title"]
                    book_author_db = row["book_author"]
                    book_price_db = row["book_price"]
                    list_price_db.append('$' + str(book_price_db))
                    list_title_and_author_db.append(book_title_db + ' by ' + str(book_author_db).strip())
            finally:
                connection.close()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            book_add = container.find_element_by_xpath(".//input[@type='submit']").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            book_add_save = container.find_element_by_xpath(".//input[@type='submit']").click()
            container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
            continue_shopp = container.find_element_by_xpath(".//a[2]").click()
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_MY_CART).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        list_title_site = container.find_elements_by_xpath(".//tr/td[1]")
        list_title_site_text = []
        for row in list_title_site:
            list_title_site_text.append(row.text)
        list_price_site = container.find_elements_by_xpath(".//tr/td[2]")
        list_price_site_text = []
        for row in list_price_site:
            list_price_site_text.append(row.text)
        assert str(list_title_site_text) == str(list_title_and_author_db)
        assert str(list_price_site_text) == str(list_price_db)

    def check_my_cart_quantity(self):
        my_cart = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_MY_CART).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        list_quantity = container.find_elements_by_xpath(".//tr/td[3]/input")
        list_quantity[0].clear()
        list_quantity[0].send_keys(2)
        list_quantity[1].clear()
        list_quantity[1].send_keys(3)
        list_quantity[2].clear()
        list_quantity[2].send_keys(4)
        book_add_save = container.find_element_by_xpath(".//input[@type='submit']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        list_quantity = container.find_elements_by_xpath(".//tr/td[3]/input")
        list_price = container.find_elements_by_xpath(".//tr/td[2]")
        list_total = container.find_elements_by_xpath(".//tr/td[4]")
        quantity_rasch = 0
        total_summ_rasch = 0
        for i in range(0, len(list_quantity)):
            quantity_rasch = quantity_rasch + int(list_quantity[i].get_attribute("value"))
            price = list_price[i].text.replace('$', '')
            price = float(price)
            total = list_total[i].text.replace('$', '')
            total = float(total)
            quantity = float(list_quantity[i].get_attribute("value"))
            price_rasch = price * quantity
            total_summ_rasch = total_summ_rasch + total
            assert price_rasch == total
        quantity_site = container.find_element_by_xpath(".//tr[5]/th[3]").text
        total_summ_site = container.find_element_by_xpath(".//tr[5]/th[4]").text
        total_summ_site = total_summ_site.replace('$', '')
        assert str(quantity_rasch) == str(quantity_site)
        assert float(total_summ_rasch) == float(total_summ_site)

    def check_checkout(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_MY_CART).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        my_cart_text = container.find_element_by_xpath(".//a[1]").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_name = container.find_element_by_xpath(".//input[@name='name']")
        input_addres = container.find_element_by_xpath(".//input[@name='address']")
        input_city = container.find_element_by_xpath(".//input[@name='city']")
        input_zip_code = container.find_element_by_xpath(".//input[@name='zip_code']")
        input_country = container.find_element_by_xpath(".//input[@name='country']")
        check_text = container.find_element_by_xpath(".//p[@class='lead']").text
        assert check_text == 'Please press Purchase to confirm your purchase, or Continue Shopping to add or remove items.'
        input_name.send_keys('Peter')
        input_addres.send_keys('ul. Svobody')
        input_city.send_keys('Moscow')
        input_zip_code.send_keys('143650')
        input_country.send_keys('Russia')
        purchase = container.find_element_by_xpath(".//input[@name='submit']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_number = container.find_element_by_xpath(".//input[@name='card_number']")
        input_card_pid = container.find_element_by_xpath(".//input[@name='card_PID']")
        input_card_expire = container.find_element_by_xpath(".//input[@name='card_expire']")
        input_card_owner = container.find_element_by_xpath(".//input[@name='card_owner']")
        input_number.send_keys('9999 9999 9999 9999')
        input_card_pid.send_keys('999')
        input_card_expire.send_keys('11.11.2020')
        input_card_owner.send_keys('Petr')
        purchase = container.find_element_by_xpath(".//button[@type='submit']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        final_purchase_text = container.find_element_by_xpath(".//p").text
        assert final_purchase_text == 'Your order has been processed sucessfully. Please check your email to get your order confirmation and shipping detail!. Your cart has been empty.'
        connection = self.go_to_db()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT orderid FROM orders"
                cursor.execute(sql)
                result = cursor.fetchall()
                result = result[-1]['orderid']
                sql = "SELECT * FROM orders WHERE orderid = '%s'" %(result)
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    customerid = row['customerid']
                    amount = row['amount']
                    date = row['date']
                    ship_name = row['ship_name']
                    ship_address = row['ship_address']
                    ship_city = row['ship_city']
                    ship_zip_code = row['ship_zip_code']
                    ship_country = row['ship_country']
                    orderid = row['orderid']
                sql = "SELECT * FROM customers WHERE customerid = '%s'" %(customerid)
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    name = row["name"]
                    address = row["address"]
                    city = row["city"]
                    zip_code = row["zip_code"]
                    country = row["country"]
                sql = "DELETE FROM orders WHERE orderid = '%s'" % (orderid)
                cursor.execute(sql)
                sql = "DELETE FROM order_items WHERE orderid = '%s'" % (orderid)
                cursor.execute(sql)
                connection.commit()
        finally:
            connection.close()
        assert ship_name == name == 'Peter'
        assert ship_address == address == 'ul. Svobody'
        assert ship_city == city == 'Moscow'
        assert ship_zip_code == zip_code == '143650'
        assert ship_country == country == 'Russia'

    def check_admin_log(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_ADMIN_LOG).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_name = container.find_element_by_xpath(".//input[@name='name']")
        input_pass = container.find_element_by_xpath(".//input[@name='pass']")
        input_name.send_keys('admin@admin.com')
        input_pass.send_keys('admin')
        button = container.find_element_by_xpath(".//input[@name='submit']").click()
        assert self.driver.title == "List book"

    def check_admin_incorrect_pass(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_ADMIN_LOG).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_name = container.find_element_by_xpath(".//input[@name='name']")
        input_pass = container.find_element_by_xpath(".//input[@name='pass']")
        input_name.send_keys('admin@admin.com')
        input_pass.send_keys('root')
        button = container.find_element_by_xpath(".//input[@name='submit']").click()
        result = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_HTML).text
        assert result == "Name or pass is wrong. Check again!"

    def check_admin_empty_pass(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_ADMIN_LOG).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_name = container.find_element_by_xpath(".//input[@name='name']")
        input_name.send_keys('admin@admin.com')
        button = container.find_element_by_xpath(".//input[@name='submit']").click()
        result = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_HTML).text
        assert result == "Name or Pass is empty!"

    def check_admin_empty_login(self):
        self.find_element(StoreSeacrhLocators.LOCATOR_STORE_ADMIN_LOG).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_pass = container.find_element_by_xpath(".//input[@name='pass']")
        input_pass.send_keys('admin')
        button = container.find_element_by_xpath(".//input[@name='submit']").click()
        result = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_HTML).text
        assert result == "Name or Pass is empty!"

    def check_admin_book_add(self):
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        add_book = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_isbn = container.find_element_by_xpath(".//input[@name='isbn']")
        input_title = container.find_element_by_xpath(".//input[@name='title']")
        input_author = container.find_element_by_xpath(".//input[@name='author']")
        input_description = container.find_element_by_xpath(".//textarea[@name='descr']")
        input_price = container.find_element_by_xpath(".//input[@name='price']")
        input_publisher = container.find_element_by_xpath(".//input[@name='publisher']")
        isbn_text = '978-1-49192-7076-771'
        title_text = 'New Book'
        author_text = 'Peter'
        description_text = 'This is a new good book.'
        price_text = '40'
        publisher_text = 'Wrox'
        input_isbn.send_keys(isbn_text)
        input_title.send_keys(title_text)
        input_author.send_keys(author_text)
        input_description.send_keys(description_text)
        input_price.send_keys(price_text)
        input_publisher.send_keys(publisher_text)
        button = container.find_element_by_xpath(".//input[@name='add']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        isbn_list = container.find_elements_by_xpath(".//tr/td[1]")
        isbn_list_text = []
        for row in isbn_list:
            isbn_list_text.append(row.text)
        index = isbn_list_text.index(isbn_text) + 2
        book_info_list = container.find_element_by_xpath(".//tr[%s]" %(index))
        title = book_info_list.find_element_by_xpath(".//td[2]").text
        author = book_info_list.find_element_by_xpath(".//td[3]").text
        description = book_info_list.find_element_by_xpath(".//td[5]").text
        price = book_info_list.find_element_by_xpath(".//td[6]").text
        publisher = book_info_list.find_element_by_xpath(".//td[7]").text
        assert title_text == title
        assert author_text == author
        assert description_text == description
        assert float(price_text) == float(price)
        assert publisher_text == publisher

    def check_long_isbn_book_add(self):
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        add_book = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_isbn = container.find_element_by_xpath(".//input[@name='isbn']")
        input_title = container.find_element_by_xpath(".//input[@name='title']")
        input_author = container.find_element_by_xpath(".//input[@name='author']")
        input_description = container.find_element_by_xpath(".//textarea[@name='descr']")
        input_price = container.find_element_by_xpath(".//input[@name='price']")
        input_publisher = container.find_element_by_xpath(".//input[@name='publisher']")
        isbn_text = '978999-1-49192-7076-771'
        title_text = 'New Book'
        author_text = 'Peter'
        description_text = 'This is a new good book.'
        price_text = '40'
        publisher_text = 'Wrox'
        input_isbn.send_keys(isbn_text)
        input_title.send_keys(title_text)
        input_author.send_keys(author_text)
        input_description.send_keys(description_text)
        input_price.send_keys(price_text)
        input_publisher.send_keys(publisher_text)
        button = container.find_element_by_xpath(".//input[@name='add']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER).text
        assert container == "Can't add new data Data too long for column 'book_isbn' at row 1"

    def check_repetitive_book_add(self):
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        add_book = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_isbn = container.find_element_by_xpath(".//input[@name='isbn']")
        input_title = container.find_element_by_xpath(".//input[@name='title']")
        input_author = container.find_element_by_xpath(".//input[@name='author']")
        input_description = container.find_element_by_xpath(".//textarea[@name='descr']")
        input_price = container.find_element_by_xpath(".//input[@name='price']")
        input_publisher = container.find_element_by_xpath(".//input[@name='publisher']")
        isbn_text = '978-1-49192-7076-771'
        title_text = 'New Book'
        author_text = 'Peter'
        description_text = 'This is a new good book.'
        price_text = '40'
        publisher_text = 'Wrox'
        input_isbn.send_keys(isbn_text)
        input_title.send_keys(title_text)
        input_author.send_keys(author_text)
        input_description.send_keys(description_text)
        input_price.send_keys(price_text)
        input_publisher.send_keys(publisher_text)
        button = container.find_element_by_xpath(".//input[@name='add']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER).text
        assert container == "Can't add new data Duplicate entry '" + isbn_text + "' for key 'books.PRIMARY'"

    def check_non_existent_publisher_book_add(self):
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        add_book = container.find_element_by_xpath(".//p[@class='lead']/a").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_isbn = container.find_element_by_xpath(".//input[@name='isbn']")
        input_title = container.find_element_by_xpath(".//input[@name='title']")
        input_author = container.find_element_by_xpath(".//input[@name='author']")
        input_description = container.find_element_by_xpath(".//textarea[@name='descr']")
        input_price = container.find_element_by_xpath(".//input[@name='price']")
        input_publisher = container.find_element_by_xpath(".//input[@name='publisher']")
        isbn_text = '978-1-49192-7076-779'
        title_text = 'New Book'
        author_text = 'Peter'
        description_text = 'This is a new good book.'
        price_text = '40'
        publisher_text = 'Wroxi'
        input_isbn.send_keys(isbn_text)
        input_title.send_keys(title_text)
        input_author.send_keys(author_text)
        input_description.send_keys(description_text)
        input_price.send_keys(price_text)
        input_publisher.send_keys(publisher_text)
        button = container.find_element_by_xpath(".//input[@name='add']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER).text
        assert container == "Can't add new data Incorrect integer value: '' for column 'publisherid' at row 1"

    def check_edit_book(self):
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        isbn_text = '978-1-49192-7076-771'
        isbn_list = container.find_elements_by_xpath(".//tr/td[1]")
        isbn_list_text = []
        for row in isbn_list:
            isbn_list_text.append(row.text)
        index = isbn_list_text.index(isbn_text) + 2
        book_edit = container.find_element_by_xpath(".//tr[%s]/td[8]/a" % (index)).click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_title = container.find_element_by_xpath(".//input[@name='title']")
        input_author = container.find_element_by_xpath(".//input[@name='author']")
        input_description = container.find_element_by_xpath(".//textarea[@name='descr']")
        input_price = container.find_element_by_xpath(".//input[@name='price']")
        input_publisher = container.find_element_by_xpath(".//input[@name='publisher']")
        title_text = 'Book New Book'
        author_text = 'Peter Peter'
        description_text = 'This is a new good book!!!!!!'
        price_text = '4000'
        publisher_text = 'Apress'
        input_title.clear()
        input_title.send_keys(title_text)
        input_author.clear()
        input_author.send_keys(author_text)
        input_description.clear()
        input_description.send_keys(description_text)
        input_price.clear()
        input_price.send_keys(price_text)
        input_change = container.find_element_by_xpath(".//input[@name='save_change']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        input_confirm = container.find_element_by_xpath(".//a[@class ='btn btn-success']").click()
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        isbn_list = container.find_elements_by_xpath(".//tr/td[1]")
        isbn_list_text = []
        for row in isbn_list:
            isbn_list_text.append(row.text)
        index = isbn_list_text.index(isbn_text) + 2
        book_info_list = container.find_element_by_xpath(".//tr[%s]" % (index))
        title = book_info_list.find_element_by_xpath(".//td[2]").text
        author = book_info_list.find_element_by_xpath(".//td[3]").text
        description = book_info_list.find_element_by_xpath(".//td[5]").text
        price = book_info_list.find_element_by_xpath(".//td[6]").text
        publisher = book_info_list.find_element_by_xpath(".//td[7]").text
        assert title_text == title
        assert author_text == author
        assert description_text == description
        assert float(price_text) == float(price)

    def check_delete_book(self):
        container = self.find_element(StoreSeacrhLocators.LOCATOR_STORE_CONTAINER)
        isbn_text = '978-1-49192-7076-771'
        isbn_list = container.find_elements_by_xpath(".//tr/td[1]")
        isbn_list_text = []
        for row in isbn_list:
            isbn_list_text.append(row.text)
        index = isbn_list_text.index(isbn_text) + 2
        book_delete = container.find_element_by_xpath(".//tr[%s]/td[9]/a" % (index)).click()
