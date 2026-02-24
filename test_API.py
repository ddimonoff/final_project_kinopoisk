import allure
from dotenv import load_dotenv
import os

from CinemaPage import CinemaPage

load_dotenv()
key = os.getenv("X-API-KEY")


base_url = "https://api.poiskkino.dev/"
my_headers = {
"Content-Type": "application/json; charset=utf-8",
"X-API-KEY": key,
}
kino = CinemaPage(base_url, my_headers)

#  final_project_kinopoisk
#  ./run.sh
@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.title("Строка поиска на главной странице")
@allure.severity("Critical")
def test_API_1() -> None:
    id1 = "840744"
    ref_name1 = "Тихий Дон"
    with allure.step("Запрос фильма по ID"):
        actual_name = kino.get_kino(id1, ref_name1)
    assert actual_name == ref_name1

@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.title("Строка поиска на главной странице")
@allure.severity("Critical")
def test_API_2() -> None:
    id2 = "533128"
    ref_name2 = "Побег"
    with allure.step("Запрос фильма по названию на кириллице"):
        actual_id2 = kino.get_cinema(ref_name2, id2)
    assert actual_id2 == int(id2)

@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.title("Строка поиска на главной странице")
@allure.severity("Critical")
def test_API_3() -> None:
    id3 = "1722"
    ref_name3 = "Twister"
    with allure.step("Запрос фильма по названию на латинице"):
        actual_id3 = kino.get_cinema(ref_name3, id3)
    assert actual_id3 == int(id3)

@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.title("Строка поиска на главной странице")
@allure.severity("Critical")
def test_API_4() -> None:
    id4 = "1091"
    ref_name4 = "Люди в чёрном"
    with allure.step("Запрос фильма по названию с пробелом"):
        actual_id4 = kino.get_cinema(ref_name4, id4)
    assert actual_id4 == int(id4)

@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.title("Строка поиска на главной странице")
@allure.severity("Critical")
def test_API_5() -> None:
    id5 = "43949"
    ref_name5 = "Спортлото-82"
    with allure.step("Запрос фильма по названию с цифрами"):
        actual_id5 = kino.get_cinema(ref_name5, id5)
    assert actual_id5 == int(id5)

@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.title("Строка поиска на главной странице")
@allure.severity("Critical")
def test_API_6() -> None:
    id6 = "22260"
    ref_name6 = "Стивен Спилберг"
    with allure.step("Запрос актёров/режиссеров по ID"):
        actual_name = kino.get_person(id6)
    assert actual_name == ref_name6
