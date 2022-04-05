
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:5000"
    async with websockets.connect(uri) as websocket:
        client = 'Client'
        bot = 'Bot'
        # first conversetion
        respn = await websocket.recv()
        print(f"{bot}    : {respn}")

        while True:
            msg = input(f"{client} : ")
            # main confersetion
            await websocket.send(msg)
            
            respn = await websocket.recv()
            tag = await websocket.recv()
            
            print(f"{bot}    : {respn}")

            if tag == 'goodbye':
                break

        # end conversetion
        respn = await websocket.recv()
        print(f"{bot}    : {respn}")
        await websocket.close()

if __name__ == "__main__":
    asyncio.run(hello())