from locator1 import *
from element import BasePageElement
from selenium.webdriver.common.keys import Keys


class SearchTextElement(BasePageElement):
    locator = "field-keywords"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def click_submit_btn(self):
        element = self.driver.find_element(*MainPageLocators.perform_search_btn)
        element.click()


class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source

    def enter_first_result(self):
        container = self.driver.find_element(*SearchResultsPageLocators.main_container)
        row = container.find_element(*SearchResultsPageLocators.first_row)
        first_item_span = row.find_element(*SearchResultsPageLocators.first_item_span)
        first_item_link = first_item_span.find_element(By.XPATH, "./..")
        first_item_link.click()


class SingleItemPage(BasePage):
    def check_if_first_item_is_available(self):
        return "In Stock." in self.driver.page_source
