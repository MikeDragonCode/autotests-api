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


update_headers = {"Authorization": f'Bearer {login_response_data['token']["accessToken"]}'}

"""Обновляем юзера и убеждаемся, что его данные - сменились"""
update_user_payload = {
  "email": get_random_email(),
  "lastName": "Retestov",
  "firstName": "Retest",
  "middleName": "Retestovich"
}
update_user_response = httpx.patch(f'http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}',
                                   headers=update_headers, json=update_user_payload)
update_user_response_data = update_user_response.json()
"""Реализация визуального сравнения смены мейлом как доп фича"""
print("OLD email: ", create_user_response_data['user']['email'], "NEW email: ", update_user_response_data['user']['email'],
      "New user's data: ", update_user_response_data,)

