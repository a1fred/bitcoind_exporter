from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getblockchaininfo import getblockchaininfo
from aioprometheus import Gauge


class Collector(BaseCollector):
    blocks = Gauge("getblockchaininfo_blocks", doc="the height of the most-work fully-validated chain. The genesis block has height 0")
    headers = Gauge("getblockchaininfo_headers", doc="the current number of headers we have validated")
    difficulty = Gauge("getblockchaininfo_difficulty", doc="the current difficulty")
    mediantime = Gauge("getblockchaininfo_mediantime", doc="median time for the current best block")
    verificationprogress = Gauge("getblockchaininfo_verificationprogress", doc="estimate of verification progress [0..1]")
    initialblockdownload = Gauge(
        "getblockchaininfo_initialblockdownload",
        doc="estimate of whether this node is in Initial Block Download mode"
    )

    async def update(self):
        resp = await getblockchaininfo(self.connection_string)

        self.blocks.set(value=resp.blocks, labels={})
        self.headers.set(value=resp.headers, labels={})
        self.difficulty.set(value=resp.difficulty, labels={})
        self.mediantime.set(value=resp.mediantime, labels={})
        self.verificationprogress.set(value=resp.verificationprogress, labels={})
        self.initialblockdownload.set(value=1 if resp.initialblockdownload else 0, labels={})
