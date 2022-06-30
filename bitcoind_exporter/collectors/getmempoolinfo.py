from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getmempoolinfo import getmempoolinfo
from aioprometheus import Gauge


class Collector(BaseCollector):
    size = Gauge("getmempoolinfo_size", doc="Current tx count")
    bytes = Gauge(
        "getmempoolinfo_bytes",
        doc="Sum of all virtual transaction sizes as defined in BIP 141"
    )
    usage = Gauge("getmempoolinfo_usage", doc="Total memory usage for the mempool")
    maxmempool = Gauge("getmempoolinfo_maxmempool", doc="Maximum memory usage for the mempool")
    mempoolminfee = Gauge(
        "getmempoolinfo_mempoolminfee",
        doc="Minimum fee rate in BTC/kB for tx to be accepted. Is the maximum of minrelaytxfee and minimum mempool fee"
    )

    async def update(self):
        getmempoolinfo_resp = await getmempoolinfo(self.connection_string)
        self.size.set(value=getmempoolinfo_resp.size, labels={})
        self.bytes.set(value=getmempoolinfo_resp.bytes, labels={})
        self.usage.set(value=getmempoolinfo_resp.usage, labels={})
        self.maxmempool.set(value=getmempoolinfo_resp.maxmempool, labels={})
        self.mempoolminfee.set(value=getmempoolinfo_resp.mempoolminfee, labels={})
