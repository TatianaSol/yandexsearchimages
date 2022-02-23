from YandexSearch import SearchHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.suggest_list()
    yandex_main_page.click_search_button()
    suggested_links = yandex_main_page.get_links()
    assert "tensor.ru" in suggested_links, 'В первых 5 результатах нет ссылки на tensor.ru'
