import requests
import allure

from CinemaPage import CinemaPage

base_url = "https://api.poiskkino.dev/"
my_headers = {
"Content-Type": "application/json; charset=utf-8",
"X-API-KEY": "6C7465Q-EQ1427W-ME47ZBZ-T1Q0XW7"
}
kino = CinemaPage(base_url, my_headers)


@allure.title("Расширенный поиск фильмов")
@allure.severity("blocker")
@allure.feature("READ")
@allure.description("Тест проверяет работу "
                    "расширенного поиска")
@allure.epic("Кинопоиск")
def test_API() -> None:
    id = "533128"  # 1091
    kino.get_kino(id)
    id1 = "1091"
    list_id = kino.get_cinema("Люди в чёрном")
    assert list_id[0] == int(id1)
    id2 = "1722"
    list_id = kino.get_cinema("Twister")
    assert list_id[0] == int(id2)