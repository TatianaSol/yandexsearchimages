from YandexPictures import PicturesHelper


def test_yandex_pictures(browser):
    yandex_pictures_page = PicturesHelper(browser)
    yandex_pictures_page.go_to_site()
    yandex_pictures_page.open_pictures()
    browser.switch_to.window(browser.window_handles[1])
    assert "https://yandex.ru/images/" in browser.current_url, 'Страница "Картинки" не открылась'
    yandex_pictures_page.open_first_category()
    first_category_name = yandex_pictures_page.get_category_name().lower()
    current_category = yandex_pictures_page.get_page_description().lower()
    assert current_category == first_category_name, 'Открытая категория не соответствует первой в списке'
    yandex_pictures_page.open_first_picture()
    first_picture_id = yandex_pictures_page.get_picture_id()
    yandex_pictures_page.click_next_button()
    second_picture_id = yandex_pictures_page.get_picture_id()
    assert second_picture_id != first_picture_id, 'Картинка не перелистнулась'
    yandex_pictures_page.click_prev_button()
    third_picture_id = yandex_pictures_page.get_picture_id()
    assert third_picture_id == first_picture_id, 'Картинка не соответствует первой'
