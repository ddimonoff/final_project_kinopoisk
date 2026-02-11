import requests
import allure

class CinemaPage:
    def __init__(self, base_url, my_headers):
        self.base_url = base_url
        self.my_headers = my_headers

    def get_kino(self, id):
        with allure.step("Запрос фильма по id " + id):
            try:
                resp = requests.get(f'{self.base_url}v1.4/movie/{id}', headers=self.my_headers)
                with allure.step(f"Проверка статус кода {resp.status_code}"):
                    if resp.status_code == 200:
                        with allure.step("Проверка названия фильма"):
                            var = resp.json()["name"]
                            assert var == "Побег"
                    elif resp.status_code == 404:
                        print("По этому id ничего не найдено!")
                        return None
                    else:
                        print(f"Ошибка API: {resp.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Другая ошибка: {e}")


    def get_cinema(self, cinema_name):
        with allure.step(f"Запрос фильма по названию - {cinema_name}"):
            params = {
                "page": 1,
                "limit": 10,
                "query": cinema_name
            }
            resp = requests.get(f'{self.base_url}v1.4/movie/search',headers=self.my_headers, params=params)
        with allure.step("Проверка статус кода 200"):
            assert resp.status_code == 200
        with allure.step(f"Проверка ID фильма {cinema_name}"):
            cinema_id = resp.json()
            list_id = []
            for movie in cinema_id.get("docs", []):
                list_id += [movie.get('id')]
                return list_id