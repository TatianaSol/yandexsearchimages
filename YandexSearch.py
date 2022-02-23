from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.XPATH, '//*[contains(@class, "input__control")]')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SUGGEST_LIST = (By.XPATH, '//*[contains(@id, "suggest-list")]')
    LOCATOR_YANDEX_LINKS = (By.CSS_SELECTOR, '#search-result > .serp-item a.link > b')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def suggest_list(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=5)

    def click_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=5).click()

    def get_links(self):
        links = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_LINKS, time=5)
        items = [elem.text.strip() for elem in links[:5]]
        return items
