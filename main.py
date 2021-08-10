import unittest
from selenium import webdriver
import page
from time import sleep


class AmazonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/usr/bin/chromedriver")
        self.driver.get("https://www.amazon.com/")

    def test_google_colab_existance(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "iphone 12"
        main_page.click_submit_btn()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        search_result_page.enter_first_result()
        single_item_page = page.SingleItemPage(self.driver)
        assert single_item_page.check_if_first_item_is_available()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
