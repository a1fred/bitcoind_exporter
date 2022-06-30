from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.estimaterawfee import estimaterawfee
from aioprometheus import Gauge


class Collector(BaseCollector):
    short_feerate = Gauge("estimaterawfee_short_feerate", doc="estimate fee rate in BTC/kB")

    medium_feerate = Gauge("estimaterawfee_medium_feerate", doc="estimate fee rate in BTC/kB")

    long_feerate = Gauge("estimaterawfee_long_feerate", doc="estimate fee rate in BTC/kB")

    async def update(self):
        conf_targets = [1, 2, 3, 4, 5, 6]
        thresholds = [0.99, 0.95, 0.90]

        for conf_target in conf_targets:
            for threshold in thresholds:
                resp = await estimaterawfee(self.connection_string, conf_target=conf_target, threshold=threshold)
                self.short_feerate.set(
                    value=resp.short.feerate or 0,
                    labels={"conf_target": str(conf_target), "threshold": str(threshold)}
                )
                self.medium_feerate.set(
                    value=resp.medium.feerate or 0,
                    labels={"conf_target": str(conf_target), "threshold": str(threshold)}
                )
                self.long_feerate.set(
                    value=resp.long.feerate or 0,
                    labels={"conf_target": str(conf_target), "threshold": str(threshold)}
                )
