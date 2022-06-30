from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getnettotals import getnettotals
from aioprometheus import Gauge


class Collector(BaseCollector):
    totalbytesrecv = Gauge("getnettotals_totalbytesrecv", doc="Total bytes received")
    totalbytessent = Gauge("getnettotals_totalbytessent", doc="Total bytes sent")

    async def update(self):
        resp = await getnettotals(self.connection_string)
        self.totalbytesrecv.set(value=resp.totalbytesrecv, labels={})
        self.totalbytessent.set(value=resp.totalbytessent, labels={})
