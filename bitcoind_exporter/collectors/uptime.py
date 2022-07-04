from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.uptime import uptime
from aioprometheus import Gauge


class Collector(BaseCollector):
    uptime = Gauge("bitcoind_uptime", doc="The number of seconds that the server has been running")

    async def update(self):
        resp = await uptime(self.connection_string)
        self.uptime.set(value=resp, labels={})
