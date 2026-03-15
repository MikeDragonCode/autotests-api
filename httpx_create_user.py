import httpx
from tools.fakers import get_random_email


"""Создание пользователя"""

create_user_payload = {
  "email": get_random_email(),
  "password": "password!1",
  "lastName": "Testov",
  "firstName": "Test",
  "middleName": "Testovich"
}

user_create_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
print(user_create_response.status_code)
print(user_create_response.json())



