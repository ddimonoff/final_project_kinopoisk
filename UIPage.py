from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
from time import sleep

# from webdriver_manager.core import driver

# import json

base_url = "https://www.kinopoisk.ru"

class UIPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = base_url

    @allure.step(f"Открыть сайт {base_url}")
    def open(self):
        self.driver.get(self.url)

    @allure.step(f"Открыть сайт {base_url}")
    def open_cross(self):
        self.driver.get(self.url)
        with allure.step("Открытие главной страницы сайта и проверка кликабельности окна Поиск"):
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".kinopoisk-header-search-form-input__input"))
            )

    @allure.step("Открытие сайта и выбор фильма по названию")
    def test_ui_search(self):
        with allure.step("Открытие главной страницы сайта и окна Поиск"):
            search_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".kinopoisk-header-search-form-input__input"))
            )
            search_input.click()
            search_input.clear()
        with allure.step("Выбор фильма по названию"):
            search_input.send_keys("Пятый элемент")
            search_input.send_keys(Keys.RETURN)
        with allure.step("Проверяем наличие в списке фильма 'Пятый элемент'"):
            first_result = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located ((By.CSS_SELECTOR, ".most_wanted"))
            )
            assert "Пятый элемент" in first_result.text
        self.driver.get(base_url)


    @allure.step("Переход на страницу Медиа")
    def test_media_ui(self):
        search_menu = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/media/']"))
        )
        search_menu.click()
        with (allure.step("Проверяем, что на странице есть кнопка Рубрики")):
            res = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".media-rubrics-navigation__button"))
            ).text
            assert res == "Рубрики"
        with (allure.step("Возврат на главную страницу")):
            search_menu_before = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".uW96Br00hFkFKc_Vc7HM"))
            )
            search_menu_before.click()


    @allure.step("Переход на страницу Фильмы")
    def test_films_ui(self):
        search_menu = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/lists/categories/movies/1/']"))
        )
        search_menu.click()
        with (allure.step("Проверяем, что на странице есть ссылка на 250 лучших фильмов")):
            res = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_name__7luvu"))
            ).text
            assert res == "250 лучших фильмов"
        with (allure.step("Возврат на главную страницу")):
            search_menu_before = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_logo__hEJCv"))
            )
            search_menu_before.click()


    @allure.step("Переход на страницу Сериалы")
    def test_serials_ui(self):
        search_menu = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/lists/categories/movies/3/']"))
        )
        search_menu.click()
        with (allure.step("Проверяем, что на странице есть ссылка на Все сериалы онлайн")):
            res = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_name__7luvu"))
            ).text
            assert res == "Все сериалы онлайн"
        with (allure.step("Возврат на главную страницу")):
            search_menu_before = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_logo__hEJCv"))
            )
            search_menu_before.click()


    @allure.step("Проверка работы плеера")
    def test_ui_player(self):
        with allure.step("Открытие главной страницы сайта и окна Поиск"):
            search_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".kinopoisk-header-search-form-input__input"))
            )
            search_input.clear()
            search_input.click()

        with allure.step("Выбор фильма по названию"):
            search_input.send_keys("Дивергент")

        with allure.step("Находим ссылку на фильм 'Дивергент'"):
            first_result = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_mainLink__gC1Ce"))
            )
            film_url = first_result.get_attribute("href")
            self.driver.get(film_url)

        with allure.step("Переход на страницу фильма"):
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_button__3MsZF"))
            )

        with allure.step("Нажатие кнопки Смотреть"):
            watch_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_button__3MsZF"))
            )
            watch_button.click()

        with allure.step("Авторизация по номеру телефона"):
            phone_input = WebDriverWait(self.driver, 90).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="phone"]'))
            )
            phone_input.send_keys("9372058064")

        # Словарь с действиями и селекторами
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

        for action_name, selector in player_actions:
            with allure.step(action_name):
                element = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                # Небольшая пауза для визуального подтверждения (опционально)
                sleep(1)

        self.driver.get(self.url)


    def test_advanced_movie_search(self):
        try:
            search_but = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_advancedSearch__gn_09"))
            )
            search_but.click()

            movie_search = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "find_film"))
            )
            movie_search.send_keys("Я, робот")

            genre_search = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".__genreSB__"))
            )
            genre_search.send_keys("фантастика")
            genre_search.send_keys(Keys.RETURN)

            button_search = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".nice_button"))  # исправлено
            )
            button_search.click()
            with (allure.step("Проверяем наличие в списке фильма 'Я, робот'")):
                first_result = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".most_wanted"))
                )
                assert "Я, робот" in first_result.text

        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
            raise

