from selector_store import SearchHelper
import time
import allure

@allure.title('Результат')


def test_brand (browser):
    with allure.step('Проверяем ссылку brend'):
        main_page = SearchHelper(browser)
        main_page.go_to_site()
        main_page.brand()

def test_list (browser):
    with allure.step('Проверяем наличие книг на стартовой странице'):
        main_page = SearchHelper(browser)
        main_page.check_list()

def test_bar (browser):
    with allure.step('Проверяем текст элементов в топ баре'):
        main_page = SearchHelper(browser)
        main_page.check_bar()

def test_text_welcome (browser):
    with allure.step('Проверяем текс Welcom на начальной странице'):
        main_page = SearchHelper(browser)
        main_page.check_welcome()

def test_text_latest (browser):
    with allure.step('Проверяем текс Latest books на начальной странице'):
        main_page = SearchHelper(browser)
        main_page.check_latest()

def test_text_footer (browser):
    with allure.step('Проверяем текс футера'):
        main_page = SearchHelper(browser)
        main_page.text_footer()

def test_publisher_text (browser):
    with allure.step('Проверяем текст не странице Publisher'):
        main_page = SearchHelper(browser)
        main_page.check_publisher_text()

def test_publisher_list (browser):
    with allure.step('Cверяем колличество publisher с бд в Publisher'):
        main_page = SearchHelper(browser)
        main_page.check_publisher_list()

def test_publisher_wrox (browser):
    with allure.step('Cверяем book title Publisher>Wrox с бд'):
        main_page = SearchHelper(browser)
        main_page.check_book_title_wrox()

def test_publisher_wrox_text (browser):
    with allure.step('Проверяем текст Publisher>Wrox'):
        main_page = SearchHelper(browser)
        main_page.check_wrox_text()

def test_publisher_wrox_link (browser):
    with allure.step('Ссылка перехода обратно в Publisher  Publisher>Wrox'):
        main_page = SearchHelper(browser)
        main_page.check_link_publisher_wrox()

def test_publisher_wiley (browser):
    with allure.step('Cверяем book title Publisher>Wiley с бд'):
        main_page = SearchHelper(browser)
        main_page.check_book_title_wiley()

def test_publisher_wiley_text (browser):
    with allure.step('Проверяем текст Publisher>Wiley'):
        main_page = SearchHelper(browser)
        main_page.check_wiley_text()

def test_publisher_wiley_link (browser):
    with allure.step('Ссылка перехода обратно в Publisher  Publisher>Wrox'):
        main_page = SearchHelper(browser)
        main_page.check_link_publisher_wiley()

def test_publisher_reilli_media (browser):
    with allure.step("Cверяем book title Publisher> O'Reilly Media с бд"):
        main_page = SearchHelper(browser)
        main_page.check_book_title_reilli_media()

def test_publisher_reilli_media_text (browser):
    with allure.step("Проверяем текст Publisher>O'Reilly Media"):
        main_page = SearchHelper(browser)
        main_page.check_reilli_media_text()

def test_publisher_reilli_media_link (browser):
    with allure.step("Ссылка перехода обратно в Publisher  O'Reilly Media"):
        main_page = SearchHelper(browser)
        main_page.check_link_publisher_reilli_media()

def test_publisher_apress (browser):
    with allure.step('Cверяем book title Publisher> Apress с бд'):
        main_page = SearchHelper(browser)
        main_page.check_book_title_apress()

def test_publisher_apress_text (browser):
    with allure.step('Проверяем текст Publisher>Apress'):
        main_page = SearchHelper(browser)
        main_page.check_apress_text()

def test_publisher_apress_link (browser):
    with allure.step('Ссылка перехода обратно в Publisher  Apress'):
        main_page = SearchHelper(browser)
        main_page.check_link_publisher_apress()

def test_publisher_addison_wesley (browser):
    with allure.step('Cверяем book title Publisher> Addison-Wesley с бд'):
        main_page = SearchHelper(browser)
        main_page.check_book_title_addison_wesley()

def test_publisher_addison_wesley_text (browser):
    with allure.step('Проверяем текст Publisher>Addison-Wesley'):
        main_page = SearchHelper(browser)
        main_page.check_addison_wesley_text()

def test_publisher_addison_wesley_link (browser):
    with allure.step('Ссылка перехода обратно в Publisher  Addison-Wesley'):
        main_page = SearchHelper(browser)
        main_page.check_link_publisher_addison_wesley()

def test_publisher_addison_wesley_link_books (browser):
    with allure.step('Publisher, cсылка перехода List full of books в Books'):
        main_page = SearchHelper(browser)
        main_page.check_link_publisher_books()

def test_books_all_list (browser):
    with allure.step('Сверяем колличество книг в Books с бд '):
        main_page = SearchHelper(browser)
        main_page.check_books_all_list()