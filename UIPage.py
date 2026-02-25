from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
from time import sleep

base_url = "https://www.kinopoisk.ru"
"ddimonoff@yandex.ru"


class UIPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = base_url
        self.wait = WebDriverWait(self.driver, 20)


    @allure.step("Открыть главную страницу Кинопоиска")
    def open_main_page(self):
        self.driver.get(self.url)

    @allure.step("Вернуться на главную страницу через логотип")
    def return_to_main_page_via_logo(self):
        logo = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_logo__hEJCv"))
        )
        logo.click()

    @allure.step("Вернуться на главную страницу через кнопку 'На главную'")
    def return_to_main_page_via_home_button(self):
        home_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".uW96Br00hFkFKc_Vc7HM"))
        )
        home_button.click()


    @allure.step("Найти и активировать поле поиска")
    def focus_search_input(self):
        search_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".kinopoisk-header-search-form-input__input"))
        )
        search_input.click()
        return search_input

    @allure.step("Очистить поле поиска")
    def clear_search_input(self, search_input):
        search_input.clear()

    @allure.step("Ввести текст в поле поиска: {text}")
    def enter_search_text(self, search_input, text):
        search_input.send_keys(text)

    @allure.step("Нажать Enter для выполнения поиска")
    def press_enter_to_search(self, search_input):
        search_input.send_keys(Keys.RETURN)

    @allure.step("Выполнить поиск фильма по названию: {movie_title}")
    def search_movie_by_title(self, movie_title):
        search_input = self.focus_search_input()
        self.clear_search_input(search_input)
        self.enter_search_text(search_input, movie_title)
        self.press_enter_to_search(search_input)

    @allure.step("Получить текст первого результата поиска")
    def get_first_search_result_text(self):
        first_result = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".most_wanted"))
        )
        return first_result.text

    @allure.step("Проверить наличие фильма '{expected_title}' в результатах поиска")
    def verify_movie_in_search_results(self, expected_title):
        result_text = self.get_first_search_result_text()
        assert expected_title in result_text, f"Фильм '{expected_title}' не найден в результатах поиска"

    @allure.step("Получить ссылку на первый результат поиска")
    def get_first_search_result_link(self):
        first_result = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-id='582101' and contains(text(), 'Дивергент')]"))
        )
        return first_result.get_attribute("href")


    @allure.step("Перейти в раздел 'Фильмы'")
    def go_to_films_section(self):
        films_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/lists/categories/movies/1/']"))
        )
        films_link.click()

    @allure.step("Перейти в раздел 'Сериалы'")
    def go_to_serials_section(self):
        serials_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'movies/3')]"))
        )
        serials_link.click()

    @allure.step("Перейти в раздел 'Медиа'")
    def go_to_media_section(self):

        media_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/media/']"))
        )
        media_link.click()

    @allure.step("Получить текст первого элемента в разделе")
    def get_first_section_item_text(self):
        first_item = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_name__7luvu"))
        )
        return first_item.text

    @allure.step("Получить текст кнопки 'Рубрики' в разделе Медиа")
    def get_media_rubrics_button_text(self):
        rubrics_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".media-rubrics-navigation__button"))
        )
        return rubrics_button.text

    @allure.step("Проверить текст элемента в разделе '{section_name}'")
    def verify_section_element_text(self, expected_text, section_name):
        if section_name == "Медиа":
            actual_text = self.get_media_rubrics_button_text()
        else:
            actual_text = self.get_first_section_item_text()
        assert actual_text == expected_text, f"В разделе {section_name} ожидался текст '{expected_text}', получен '{actual_text}'"


    @allure.step("Перейти на страницу фильма по ссылке: {film_url}")
    def go_to_film_page(self, film_url):
        self.driver.get(film_url)

    @allure.step("Дождаться загрузки страницы фильма")
    def wait_for_film_page_load(self):
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_button__3MsZF"))
        )

    @allure.step("Нажать кнопку 'Смотреть' на странице фильма")
    def click_watch_button(self):
        watch_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_button__3MsZF"))
        )
        watch_button.click()

    @allure.step("Ввести номер телефона для авторизации: {phone_number}")
    def enter_phone_number(self, phone_number):
        phone_input = WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="phone"]'))
        )
        phone_input.send_keys(phone_number)

    @allure.step("Нажать кнопку управления плеером: {button_name}")
    def click_player_button(self, button_name, selector):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        element.click()
        sleep(1)

    @allure.step("Выполнить последовательность действий с плеером")
    def execute_player_actions(self, actions):
        for action_name, selector in actions:
            with allure.step(f"Действие: {action_name}"):
                self.click_player_button(action_name, selector)


    @allure.step("Нажать кнопку 'Расширенный поиск'")
    def click_advanced_search_button(self):
        search_but = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_advancedSearch__gn_09"))
        )
        search_but.click()

    @allure.step("Ввести название фильма в расширенном поиске: {movie_title}")
    def enter_movie_title_advanced(self, movie_title):
        movie_search = self.wait.until(
            EC.visibility_of_element_located((By.ID, "find_film"))
        )
        movie_search.send_keys(movie_title)

    @allure.step("Выбрать жанр в расширенном поиске: {genre}")
    def select_genre_advanced(self, genre):
        genre_search = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".__genreSB__"))
        )
        genre_search.send_keys(genre)
        genre_search.send_keys(Keys.RETURN)

    @allure.step("Нажать кнопку 'Поиск' в расширенном поиске")
    def submit_advanced_search(self):
        button_search = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".nice_button"))
        )
        button_search.click()

    @allure.step("Выполнить расширенный поиск фильма")
    def perform_advanced_search(self, movie_title, genre):
        self.click_advanced_search_button()
        self.enter_movie_title_advanced(movie_title)
        self.select_genre_advanced(genre)
        self.submit_advanced_search()


    @allure.step("Тестирование разделов меню: Фильмы, Сериалы, Медиа")
    def test_all_menu_sections(self):
        self.go_to_films_section()
        self.verify_section_element_text("250 лучших фильмов", "Фильмы")
        self.return_to_main_page_via_logo()

        self.go_to_serials_section()
        self.verify_section_element_text("Все сериалы онлайн", "Сериалы")
        self.return_to_main_page_via_logo()

        self.go_to_media_section()
        self.verify_section_element_text("Рубрики", "Медиа")
        self.return_to_main_page_via_home_button()

    @allure.step("Тестирование поиска фильма")
    def test_movie_search(self, movie_title="Пятый элемент"):
        self.search_movie_by_title(movie_title)
        self.verify_movie_in_search_results(movie_title)
        self.open_main_page()

    @allure.step("Тестирование плеера")
    def test_player_functionality(self, movie_title="Дивергент", phone_number="9372058064"):
        self.search_movie_by_title(movie_title)
        film_url = self.get_first_search_result_link()
        self.go_to_film_page(film_url)
        self.wait_for_film_page_load()
        self.click_watch_button()
        self.enter_phone_number(phone_number)

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

        self.execute_player_actions(player_actions)
        self.open_main_page()

    @allure.step("Тестирование расширенного поиска")
    def test_advanced_search(self, movie_title="Я, робот", genre="фантастика"):
        self.perform_advanced_search(movie_title, genre)
        self.verify_movie_in_search_results(movie_title)