import asyncio
import websockets


async def query():
    async with websockets.connect(
            "ws://localhost:8765") as websocket:
        # Event handler send request to information collector
        print("Welcome to Omotenashi Weather Information Collector!")
        query = input("Enter the information (weather | event): ")

        await websocket.send(query)
        print(f">>> Send query: {query}")

        weather_information = await websocket.recv()
        print(f"<<< Received weather information: {weather_information}")

asyncio.get_event_loop().run_until_complete(query())




