from elarian import Elarian, Customer
import asyncio

client = Elarian(org_id='el_org_eu_CCi7AV', app_id='el_app_ad5gdI',
                 api_key='el_k_test_02e469b043d66490e22b6774babc68b238b4ef7e7e5e83fbc907d11bfa2b96dd')


async def start():
    client.set_on_connection_error(lambda err: print(f"Connection error: {err}"))
    client.set_on_connected(lambda: print("App is running!"))
    await client.connect()


loop = asyncio.get_event_loop()
loop.create_task(start())
loop.run_forever()
