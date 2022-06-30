import typing
from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.collectors import (
    estimaterawfee,
    estimatesmartfee,
    getblockchaininfo,
    getmempoolinfo,
    getmininginfo,
    getnettotals,
    getnetworkinfo,
)

collectors: typing.Dict[str, typing.Type[BaseCollector]] = {
    "estimaterawfee": estimaterawfee.Collector,
    "estimatesmartfee": estimatesmartfee.Collector,
    "getblockchaininfo": getblockchaininfo.Collector,
    "getmempoolinfo": getmempoolinfo.Collector,
    "getmininginfo": getmininginfo.Collector,
    "getnettotals": getnettotals.Collector,
    "getnetworkinfo": getnetworkinfo.Collector,
}
