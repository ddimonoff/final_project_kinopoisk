import requests
import allure

from CinemaPage import CinemaPage

base_url = "https://api.poiskkino.dev/"
my_headers = {
"Content-Type": "application/json; charset=utf-8",
"X-API-KEY": "6C7465Q-EQ1427W-ME47ZBZ-T1Q0XW7"
}
kino = CinemaPage(base_url, my_headers)

#  final_project_kinopoisk
#  ./run.sh
@allure.title("Поиск")
@allure.severity("blocker")
@allure.feature("READ")
@allure.description("Тест проверяет работу окна поиска")
@allure.epic("Кинопоиск")
def test_API() -> None:
    id1 = "1091"
    ref_name1 = "Люди в чёрном"
    with (allure.step("Запрос фильма по ID")):
        actual_name =kino.get_kino(id1)
    assert actual_name == ref_name1
    id2 = "533128"
    ref_name2 = "Побег"
    with (allure.step("Запрос фильма по названию на кириллице")):
        actual_id2 = kino.get_cinema(ref_name2, id2)
    assert actual_id2 == int(id2)
    id3 = "1722"
    ref_name3 = "Twister"
    with (allure.step("Запрос фильма по названию на латинице")):
        actual_id3 = kino.get_cinema(ref_name3, id3)
    assert actual_id3 == int(id3)
    id4 = "840744"
    ref_name4 = "Тихий Дон"
    with (allure.step("Запрос фильма по названию с пробелом")):
        actual_id4 = kino.get_cinema(ref_name4, id4)
    assert actual_id4 == int(id4)
    id5 = "43949"
    ref_name5 = "Спортлото-82"
    with (allure.step("Запрос фильма по названию с цифрами")):
        actual_id5 = kino.get_cinema(ref_name5, id5)
    assert actual_id5 == int(id5)
    id6 = "22260"
    ref_name6 = "Стивен Спилберг"
    with (allure.step("Запрос актёров/режиссеров по ID")):
        actual_name = kino.get_person(id6)
    assert actual_name == ref_name6
