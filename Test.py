import requests
import pytest
import allure

@allure.feature("Тести API користувача")
@allure.epic("Тестування API")
class TestApi:
    @allure.story("Отримання одного користувача")
    @allure.description("Цей тест перевіряє можливість отримання інформації про одного користувача.")
    def test_single_user(self):
        url = "https://reqres.in/api/users/2"
        with allure.step("Відправлення GET-запиту для отримання даних користувача"):
            response = requests.get(url)
        assert response.status_code == 200
        
        with allure.step("Перевірка заголовка Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        user_data = response.json()["data"]
        with allure.step("Перевірка атрибутів даних користувача"):
            assert "id" in user_data
            assert "email" in user_data
            assert "first_name" in user_data
            assert "last_name" in user_data
            assert "avatar" in user_data

    @allure.story("Створення користувача")
    @allure.description("Цей тест перевіряє можливість створення нового користувача.")
    def test_create_user(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        with allure.step("Відправлення POST-запиту для створення нового користувача"):
            response = requests.post(url, json=data)
        assert response.status_code == 201
        
        with allure.step("Перевірка заголовка Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        user_data = response.json()
        with allure.step("Перевірка атрибутів даних користувача"):
            assert "id" in user_data
            assert "name" in user_data
            assert "job" in user_data
            assert "createdAt" in user_data

    @allure.story("Оновлення користувача")
    @allure.description("Цей тест перевіряє можливість оновлення даних користувача.")
    def test_update_user(self):
        url = "https://reqres.in/api/users/2"
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        with allure.step("Відправлення PUT-запиту для оновлення даних користувача"):
            response = requests.put(url, json=data)
        assert response.status_code == 200
        
        with allure.step("Перевірка заголовка Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        user_data = response.json()
        with allure.step("Перевірка оновлених атрибутів даних користувача"):
            assert "name" in user_data
            assert "job" in user_data
            assert "updatedAt" in user_data

    @allure.story("Видалення користувача")
    @allure.description("Цей тест перевіряє можливість видалення користувача.")
    def test_delete_user(self):
        url = "https://reqres.in/api/users/2"
        with allure.step("Відправлення DELETE-запиту для видалення користувача"):
            response = requests.delete(url)
        assert response.status_code == 204

