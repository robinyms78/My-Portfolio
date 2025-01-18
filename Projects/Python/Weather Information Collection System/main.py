import asyncio
import websockets
from information.weather import weather_supplicant
from information.place import Place


# Read zipcode from text file
#place = Place("102-0093, jp")


async def listen(websocket, path):
    query = await websocket.recv()
    print(f"<<< Received query: {query}")

    if query == "weather":
        # Get weather information from zip code
        weather_supplicant.get_weather_data()
        # Parse weather information to JSON
        weather_information = weather_supplicant.get_json_csv()
        # Send weather information in JSON to event handler
        await websocket.send(weather_information)
        print(f">>> Send weather information: {weather_information}")

if __name__ == "__main__":
    start_server = websockets.serve(listen, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
