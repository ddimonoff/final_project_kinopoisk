# План тестирование
 # 1. Вход и регистрация
 # 2. Проверка переходов на Главной странице
 # 3. Строка поиска на главной странице
 # 4. Функциональное тестирование медиаплеера
 # 5. Кросс-браузерное тестирование
# from UIPage import UIPage
# import allure
# from time import sleep   # задержка

import pytest
import allure
from selenium import webdriver
from UIPage import UIPage as uip

base_url = "https://www.kinopoisk.ru"
login = ""
password = ""

@pytest.fixture(scope="session")
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.maximize_window()
    uip(browser).open()
    yield browser
    browser.quit()


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Функциональное тестирование")
@allure.title("Тестирование меню главной страницы сайта")
@allure.severity("Critical")
def test_1_ui(driver):
    uip(driver).test_films_ui()
    uip(driver).test_serials_ui()
    uip(driver).test_media_ui()


@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("Функциональное тестирование")
@allure.title("Выбор фильма в окне поиска")
@allure.severity("Critical")
def test_2_ui(driver):
    uip(driver).test_ui_search()

