import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)

message = "Привет серверу!"
client_socket.send(message.encode())

response = client_socket.recv(1234).decode()
print(f"Ответ от сервера: {response}")

client_socket.close()

