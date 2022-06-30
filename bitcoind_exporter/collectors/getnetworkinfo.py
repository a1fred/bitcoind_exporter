from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.getnetworkinfo import getnetworkinfo
from aioprometheus import Gauge


class Collector(BaseCollector):
    version = Gauge("getnetworkinfo_version", doc="the server version")
    protocolversion = Gauge("getnetworkinfo_protocolversion", doc="the protocol version")
    timeoffset = Gauge("getnetworkinfo_timeoffset", doc="the time offset")
    connections = Gauge("getnetworkinfo_connections", doc="the total number of connections")
    connections_in = Gauge("getnetworkinfo_connections_in", doc="the number of inbound connections")
    connections_out = Gauge("getnetworkinfo_connections_out", doc="the number of outbound connections")
    networkactive = Gauge("getnetworkinfo_networkactive", doc="whether p2p networking is enabled")
    relayfee = Gauge("getnetworkinfo_relayfee", doc="minimum relay fee for transactions in BTC/kB")
    incrementalfee = Gauge(
        "getnetworkinfo_incrementalfee",
        doc="minimum fee increment for mempool limiting or BIP 125 replacement in BTC/kB"
    )

    async def update(self):
        resp = await getnetworkinfo(self.connection_string)
        self.version.set(value=resp.version, labels={})
        self.protocolversion.set(value=resp.protocolversion, labels={})
        self.timeoffset.set(value=resp.timeoffset, labels={})
        self.connections.set(value=resp.connections, labels={})
        self.connections_in.set(value=resp.connections_in, labels={})
        self.connections_out.set(value=resp.connections_out, labels={})
        self.networkactive.set(value=1 if resp.networkactive else 0, labels={})
        self.relayfee.set(value=resp.relayfee, labels={})
        self.incrementalfee.set(value=resp.incrementalfee, labels={})
