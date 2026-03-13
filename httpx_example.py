import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())

data = {
    "userId": 1,
    "title": "Тестовая задача Майк",
    "completed": False
}
response = httpx.post('https://jsonplaceholder.typicode.com/todos/', json=data)
print(response.status_code)
print(response.json())

data = {
    "username" : "mike_user",
    "password" : "pass1234!"
}
response = httpx.post('https://httpbin.org/post',data=data)
print(response.status_code)
print(response.json())

headers = {"Authorization": "Bearer my_server_token"}
response = httpx.get('https://httpbin.org/get', headers=headers)
print(response.status_code)
print(response.request.headers)
print(response.json())

params = {"userId":1}
response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response.url)
print(response.json())

files = {'file': ("example.txt", open("example.txt", "rb"))}
response = httpx.post('https://httpbin.org/post',files=files)
print(response.status_code)
print(response.json())

with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_server_token"})
response = client.get('https://httpbin.org/get')
print(response.json())

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/todos/fake-url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошиька запроса!!! {e}")

try:
    response = httpx.post('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")


