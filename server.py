import asyncio
import websockets
from bot import Bot,firstConv,endConv

async def chat(websocket):
    # global times
    # firs conversetion 
    respn = firstConv()
    await websocket.send(respn)

    while True:
        try:
            # main conversetion
            msg = await websocket.recv()
            
            respn,tag = Bot(msg)
        
            # print(respn, tag)
    
            await websocket.send(respn)
            # await websocket.send(tag)

            # end conversetion 
            if tag == 'goodbye':
                respn = endConv()
                await websocket.send(respn)

        except websockets.ConnectionClosedOK:
            break
        # print(respn)
    


async def main():
    async with websockets.serve(chat, "localhost", 5000):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())