import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)

async def main_users():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main_users())