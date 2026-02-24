import requests
import allure

class CinemaPage:
    def __init__(self, base_url, my_headers):
        self.base_url = base_url
        self.my_headers = my_headers

    def get_kino(self, id, ref_name):
        with allure.step("Запрос фильма по id " + str(id)):
            try:
                resp = requests.get(f'{self.base_url}v1.4/movie/{id}', headers=self.my_headers)
                with allure.step(f"Проверка статус кода {resp.status_code}"):
                    if resp.status_code == 200:
                        data = resp.json()
                        with allure.step(f"Проверка названия фильма"):
                            cinema_name = data.get('name')
                            if cinema_name and cinema_name == str(ref_name):
                                with allure.step(f"Название фильма = {cinema_name}"):
                                    return cinema_name
                            else:
                                print(f"Название фильма '{cinema_name}' не соответствует ожидаемому '{ref_name}'")
                                return None
                    elif resp.status_code == 404:
                        print("По этому id ничего не найдено!")
                        return None
                    else:
                        print(f"Ошибка API: {resp.status_code}")
                        return None
            except requests.exceptions.RequestException as e:
                print(f"Ошибка запроса: {e}")
                return None
            except KeyError as e:
                print(f"Ошибка в структуре ответа: отсутствует ключ {e}")
                return None
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")
                return None


    def get_cinema(self, cinema_name, ref_id):
        with (allure.step(f"Запрос фильма по названию - {cinema_name}")):
            params = {
                "page": 1,
                "limit": 10,
                "query": cinema_name
            }
            try:
                resp = requests.get(f'{self.base_url}v1.4/movie/search',headers=self.my_headers, params=params)
                with allure.step(f"Проверка статус кода {resp.status_code}"):
                    if resp.status_code == 200:
                        with allure.step(f"Проверка ID фильма {cinema_name}"):
                            cinema_id = resp.json()
                            list_id = []
                        for movie in cinema_id.get("docs", []):
                            list_id += [movie.get('id')]
                        for a in list_id:
                            if a == int(ref_id):
                                with allure.step(f"ID фильма = {a}"):
                                    return a  # сразу возвращаем
                        return None  # если ничего не нашли
                    elif resp.status_code == 404:
                        print("По этому названию ничего не найдено!")
                        return None
                    else:
                        print(f"Ошибка API: {resp.status_code}")
            except requests.exceptions.RequestException:
                pass


    def get_person(self, id):
        with allure.step("Поиск персоны по ID " + id):
            try:
                resp = requests.get(f'{self.base_url}v1.4/person/{id}', headers=self.my_headers)
                with allure.step(f"Проверка статус кода {resp.status_code}"):
                    if resp.status_code == 200:
                        with allure.step(f"Проверка фамилии {resp.json()["name"]}"):
                            return resp.json()["name"]
                    elif resp.status_code == 404:
                        print("По этому id ничего не найдено!")
                        return None
                    else:
                        print(f"Ошибка API: {resp.status_code}")
            except requests.exceptions.RequestException:
                pass

