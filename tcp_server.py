import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print('TCP Сервер ВКЛ и ждет подключений на 12345')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от: {client_address}")

        try:
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Было получено сообщение: {data}")
                response = f"Сервер получил {data}"
                client_socket.send(response.encode())
        finally:
            client_socket.close()


if __name__ == '__main__':
    server()