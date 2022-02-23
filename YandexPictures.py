from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexPicturesLocators:
    LOCATOR_YANDEX_PICTURES = (By.XPATH, '//*[contains(@data-id, "images")]')
    LOCATOR_YANDEX_PICTURES_FIRST_CATEGORY = (By.XPATH, '//*[contains(@class, "PopularRequestList-Item_pos_0")]')
    LOCATOR_YANDEX_PICTURES_DESCRIPTION = (By.XPATH, '//*[contains(@id, "suggest-item")]')
    LOCATOR_YANDEX_PICTURES_FIRST_PICTURE = (By.XPATH, '//*[contains(@class, "serp-item_pos_0")]')
    LOCATOR_YANDEX_PICTURES_NEXT_BUTTON = (By.XPATH, '//*[contains(@class, "CircleButton_type_next")]')
    LOCATOR_YANDEX_PICTURES_PREV_BUTTON = (By.XPATH, '//*[contains(@class, "CircleButton_type_prev")]')
    LOCATOR_YANDEX_PICTURES_PICTURE_ID = (By.XPATH, '//*[contains(@class, "MMImage-Preview")]')


class PicturesHelper(BasePage):

    def open_pictures(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES, time=5).click()

    def open_first_category(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_FIRST_CATEGORY, time=5).click()

    def get_category_name(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_FIRST_CATEGORY, time=5)\
            .get_attribute('data-grid-text')

    def get_page_description(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_DESCRIPTION, time=5)\
            .get_attribute('data-text')

    def open_first_picture(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_FIRST_PICTURE, time=5).click()

    def click_next_button(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_NEXT_BUTTON, time=5).click()

    def click_prev_button(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_PREV_BUTTON, time=5).click()

    def get_picture_id(self):
        return self.find_element(YandexPicturesLocators.LOCATOR_YANDEX_PICTURES_PICTURE_ID).get_attribute('src')
