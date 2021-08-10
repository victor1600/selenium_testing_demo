from selenium.webdriver.common.by import By


class MainPageLocators(object):
    # Locators for main page
    # 1. How we want to access it, 2. The value
    perform_search_btn = (By.ID, "nav-search-submit-button")


class SearchResultsPageLocators(object):
    main_container = (By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
    first_row = (By.XPATH, "//div[@data-index='0']")
    first_item_span = (By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal")
    # iphone_link = (By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal")
