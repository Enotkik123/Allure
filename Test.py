import allure
import pytest
import requests

@allure.feature("User API")
class TestUserAPI:

    @allure.story("Create User")
    def test_create_user(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        with allure.step("Sending POST request to create user"):
            response = requests.post(url, json=data)
            assert response.status_code == 201
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
            user_data = response.json()
            assert "id" in user_data
            assert "name" in user_data
            assert "job" in user_data
            assert "createdAt" in user_data
            assert user_data["name"] == "morpheus"

    @allure.story("Retrieve Single User")
    def test_single_user(self):
        url = "https://reqres.in/api/users/2"
        with allure.step("Sending GET request to retrieve single user"):
            response = requests.get(url)
            assert response.status_code == 200
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
            user_data = response.json()["data"]
            assert "id" in user_data
            assert "email" in user_data
            assert "first_name" in user_data
            assert "last_name" in user_data
            assert "avatar" in user_data
            assert len(user_data) == 5

    @allure.story("Update User")
    def test_update_user(self):
        url = "https://reqres.in/api/users/2"
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        with allure.step("Sending PUT request to update user"):
            response = requests.put(url, json=data)
            assert response.status_code == 200
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
            user_data = response.json()
            assert "name" in user_data
            assert "job" in user_data
            assert "updatedAt" in user_data
            assert user_data["job"] == "zion resident"

    @allure.story("Delete User")
    def test_delete_user(self):
        url = "https://reqres.in/api/users/2"
        with allure.step("Sending DELETE request to delete user"):
            response = requests.delete(url)
            assert response.status_code == 204
