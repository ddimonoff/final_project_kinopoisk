import pytest
import allure
from UIPage import UIPage as uip

base_url = "https://www.kinopoisk.ru"


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Тестирование навигационного меню сайта")
@allure.severity("Critical")
@allure.description("Проверка перехода в разделы Фильмы, Сериалы, Медиа и наличия ожидаемых элементов")
def test_navigation_menu(driver):
    page = uip(driver)

    with allure.step("Проверка раздела 'Фильмы'"):
        page.go_to_films_section()
        page.verify_section_element_text("250 лучших фильмов", "Фильмы")

    with allure.step("Проверка раздела 'Сериалы'"):
        page.go_to_serials_section()
        page.verify_section_element_text("Все сериалы онлайн", "Сериалы")
        page.return_to_main_page_via_logo()

    with allure.step("Проверка раздела 'Медиа'"):
        page.go_to_media_section()
        page.verify_section_element_text("Рубрики", "Медиа")
        page.return_to_main_page_via_home_button()


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Поиск фильма по названию")
@allure.severity("Critical")
@allure.description("Проверка работы поиска: ввод названия фильма и проверка результатов")
@pytest.mark.parametrize("movie_title", ["Пятый элемент", "Аватар", "Матрица"])
def test_movie_search(driver, movie_title):
    page = uip(driver)

    page.search_movie_by_title(movie_title)
    page.verify_movie_in_search_results(movie_title)
    page.open_main_page()


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Тестирование функций видеоплеера")
@allure.severity("Critical")
@allure.description("Проверка основных элементов управления видеоплеера")
def test_video_player(driver):
    page = uip(driver)
    movie_title = "Дивергент"
    phone_number = "9372058064"

    with allure.step(f"Поиск фильма '{movie_title}'"):
        page.search_movie_by_title(movie_title)
        film_url = page.get_first_search_result_link()

    with allure.step("Переход на страницу фильма"):
        page.go_to_film_page(film_url)
        page.wait_for_film_page_load()

    with allure.step("Запуск плеера"):
        page.click_watch_button()

    with allure.step("Авторизация по номеру телефона"): # не будет проходить
        page.enter_phone_number(phone_number)

    player_actions = [
        ("Смотреть", ".styles_button__3MsZF"),
        ("Пауза", ".styles_pause__Wnh0_"),
        ("Назад 10 секунд", ".styles_backward__4hsAy"),
        ("Смотреть", ".styles_play__W5EMB"),
        ("Вперед 10 секунд", ".styles_forward__iN7hT"),
        ("Полноэкранный режим", ".styles_root__8VlBL"),
        ("Обычный режим", ".styles_fullScreen__ryrjs"),
        ("Выключить звук", ".styles_volumeIcon__gSpC_"),
        ("Включить звук", ".styles_volumeIcon__gSpC_"),
        ("Закрыть", ".styles_closeButton__UldPY")
    ]

    page.execute_player_actions(player_actions)
    page.open_main_page()


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Кросс-браузерное тестирование")
@allure.severity("Critical")
@allure.description("Проверка открытия главной страницы в разных браузерах")
def test_cross_browser(cross):
    page = uip(cross)

    with allure.step("Открытие главной страницы"):
        page.open_main_page()

    with allure.step("Проверка доступности поля поиска"):
        page.focus_search_input()


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Расширенный поиск фильма по параметрам")
@allure.severity("Critical")
@allure.description("Проверка расширенного поиска с указанием названия и жанра")
@pytest.mark.parametrize("movie_title, genre", [
    ("Я, робот", "фантастика"),
    ("Титаник", "драма"),
    ("Хатико", "драма")
])
def test_advanced_movie_search(driver, movie_title, genre):
    page = uip(driver)

    page.perform_advanced_search(movie_title, genre)
    page.verify_movie_in_search_results(movie_title)