from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getmemoryinfo import getmemoryinfo
from aioprometheus import Gauge


class Collector(BaseCollector):
    locked_used = Gauge("getmemoryinfo_used", doc="Number of bytes used")
    locked_free = Gauge("getmemoryinfo_free", doc="Number of bytes available in current arenas")
    locked_total = Gauge("getmemoryinfo_total", doc="Total number of bytes managed")
    locked_locked = Gauge("getmemoryinfo_locked", doc="Amount of bytes that succeeded locking.")
    locked_chunks_used = Gauge("getmemoryinfo_chunks_used", doc="Number allocated chunks")
    locked_chunks_free = Gauge("getmemoryinfo_chunks_free", doc="Number unused chunks")

    async def update(self):
        resp = await getmemoryinfo(self.connection_string)
        self.locked_used.set(value=resp.locked.used, labels={})
        self.locked_free.set(value=resp.locked.free, labels={})
        self.locked_total.set(value=resp.locked.total, labels={})
        self.locked_locked.set(value=resp.locked.locked, labels={})
        self.locked_chunks_used.set(value=resp.locked.chunks_used, labels={})
        self.locked_chunks_free.set(value=resp.locked.chunks_free, labels={})
