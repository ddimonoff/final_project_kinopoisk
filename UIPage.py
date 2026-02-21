from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
# from time import sleep

# from webdriver_manager.core import driver

# import json

base_url = "https://www.kinopoisk.ru"

class UIPage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step(f"Открыть сайт {base_url}")
    def open(self):
        self.driver.get(base_url)

    @allure.step("Открытие сайта и активность строки поиска")
    def test_ui_search(self):
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".kinopoisk-header-search-form-input__input"))
        )
        search_input.click()
        with (allure.step("Выбор фильма по названию")):
            search_input.send_keys("Инсургент")
            search_input.send_keys(Keys.RETURN)
        with (allure.step("Проверяем наличие в списке фильма 'Дивергент, глава 2: Инсургент'")):
            first_result = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".most_wanted"))
            )
            assert "Дивергент, глава 2: Инсургент" in first_result.text


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
