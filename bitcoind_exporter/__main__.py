import asyncio

from bitcoind_exporter import config
from bitcoind_exporter.webapp import run_app


async def main():
    service = await run_app(config.get_settings())

    try:
        while True:
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        await service.stop()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
