import httpx
from tools.fakers import get_random_email

create_new_user_payload = {
  "email": get_random_email(),
  "password": "password!1",
  "lastName": "Testov",
  "firstName": "Test",
  "middleName": "Testovich"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_new_user_payload)
create_user_response_data = create_user_response.json()

print(f"New user data: {create_user_response_data}")

login_payload = {
  "email": create_new_user_payload['email'],
  "password": create_new_user_payload['password']
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login',json=login_payload)
login_response_data = login_response.json()
print(f"Login data: {login_response_data}")

"""Получили юзера и убеждаемся, что его данные ОК"""
login_headers = {"Authorization": f'Bearer {login_response_data['token']["accessToken"]}'}
get_user_response = httpx.get(f'http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}',
                              headers=login_headers)
get_user_response_data = get_user_response.json()
print("User's data: ", get_user_response_data)

"""Удадли юзера и убеждаемся, что его данные - ОТСУТСТВУЮТ"""
delete_user_response = httpx.delete(f'http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}',
                              headers=login_headers)
delete_user_response_data = delete_user_response.json()
print("Delete user: ", delete_user_response.status_code)


