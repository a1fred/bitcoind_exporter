from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getbestblockhash import getbestblockhash
from bitcoind_exporter.bitcoind_rpc.getblock import getblock_v1
from aioprometheus import Gauge


class Collector(BaseCollector):
    size = Gauge("bestblock_size", doc="The block size")
    strippedsize = Gauge("bestblock_strippedsize", doc="The block size excluding witness data")
    weight = Gauge("bestblock_weight", doc="The block weight as defined in BIP 141")
    height = Gauge("bestblock_height", doc="The block height or index")
    version = Gauge("bestblock_version", doc="The block version")
    time = Gauge("bestblock_time", doc="The block time expressed in UNIX epoch time")
    mediantime = Gauge("bestblock_mediantime", doc="The median block time expressed in UNIX epoch time")
    nonce = Gauge("bestblock_nonce", doc="The nonce")
    difficulty = Gauge("bestblock_difficulty", doc="The difficulty")
    tx_count = Gauge("bestblock_tx_count", doc="The number of transactions in the block")

    async def update(self):
        bestblockhash = await getbestblockhash(self.connection_string)
        block = await getblock_v1(self.connection_string, bestblockhash)

        self.size.set(value=block.size, labels={})

        self.strippedsize.set(value=block.strippedsize, labels={})
        self.weight.set(value=block.weight, labels={})
        self.height.set(value=block.height, labels={})
        self.version.set(value=block.version, labels={})
        self.time.set(value=block.time, labels={})
        self.mediantime.set(value=block.mediantime, labels={})
        self.nonce.set(value=block.nonce, labels={})
        self.difficulty.set(value=block.difficulty, labels={})
        self.tx_count.set(value=block.nTx, labels={})
