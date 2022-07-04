import typing
from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.collectors import (
    bestblock,
    estimaterawfee,
    estimatesmartfee,
    getblockchaininfo,
    getmemoryinfo,
    getmempoolinfo,
    getmininginfo,
    getnettotals,
    getnetworkinfo,
    uptime,
)

collectors: typing.Dict[str, typing.Type[BaseCollector]] = {
    "bestblock": bestblock.Collector,
    "estimaterawfee": estimaterawfee.Collector,
    "estimatesmartfee": estimatesmartfee.Collector,
    "getblockchaininfo": getblockchaininfo.Collector,
    "getmemoryinfo": getmemoryinfo.Collector,
    "getmempoolinfo": getmempoolinfo.Collector,
    "getmininginfo": getmininginfo.Collector,
    "getnettotals": getnettotals.Collector,
    "getnetworkinfo": getnetworkinfo.Collector,
    "uptime": uptime.Collector,
}
