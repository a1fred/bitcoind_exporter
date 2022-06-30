from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getmininginfo import getmininginfo
from aioprometheus import Gauge


class Collector(BaseCollector):
    blocks = Gauge("getmininginfo_blocks", doc="The current block")
    currentblockweight = Gauge("getmininginfo_currentblockweight", doc="The block weight of the last assembled block")
    currentblocktx = Gauge("getmininginfo_currentblocktx", doc="The number of block transactions of the last assembled block")
    difficulty = Gauge("getmininginfo_difficulty", doc="The current difficulty")
    networkhashps = Gauge("getmininginfo_networkhashps", doc="The network hashes per second")
    pooledtx = Gauge("getmininginfo_pooledtx", doc="The size of the mempool")

    async def update(self):
        resp = await getmininginfo(self.connection_string)
        self.blocks.set(value=resp.blocks, labels={})
        self.currentblockweight.set(value=resp.currentblockweight or 0, labels={})
        self.currentblocktx.set(value=resp.currentblocktx or 0, labels={})
        self.difficulty.set(value=resp.difficulty, labels={})
        self.networkhashps.set(value=resp.networkhashps, labels={})
        self.pooledtx.set(value=resp.pooledtx, labels={})
