import httpx

login_payload = {
  "email": "miketest@test.ru",
  "password": "test!!11"
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login',json=login_payload)
login_response_data = login_response.json()

refresh_payload = {
    "refreshToken": login_response_data['token']['refreshToken']}
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh',json=refresh_payload)
refresh_response_data = refresh_response.json()

headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}


get_me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
get_me_response_data = get_me_response.json()

print("Get 'me' response:", get_me_response_data)
print("Status code:", get_me_response.status_code)