from aiohttp.web_request import Request
from aiohttp.web_response import Response

from aioprometheus.service import Service

from bitcoind_exporter.config import Settings
from bitcoind_exporter.collectors.base import CollectorRegistry


class SyncService(Service):
    def __init__(self, collectorRegistry: CollectorRegistry):
        self.collectorRegistry = collectorRegistry
        super().__init__()

    async def handle_metrics(self, request: Request) -> Response:
        await self.collectorRegistry.update()
        return await super().handle_metrics(request)


async def run_app(settings: Settings) -> SyncService:
    collectorRegistry = CollectorRegistry(settings.BITCOIND, collectors=settings.get_collectors())

    service = SyncService(collectorRegistry)
    await service.start(addr=settings.HOST, port=settings.PORT)
    return service
