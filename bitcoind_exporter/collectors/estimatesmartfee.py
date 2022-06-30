from bitcoind_exporter.collectors.base import BaseCollector
from bitcoind_exporter.bitcoind_rpc.estimatesmartfee import estimatesmartfee
from aioprometheus import Gauge


class Collector(BaseCollector):
    feerate = Gauge("estimatesmartfee_feerate", doc="estimate fee rate in BTC/kB (only present if no errors were encountered)")
    blocks = Gauge("estimatesmartfee_blocks", doc="block number where estimate was found")

    async def update(self):
        conf_targets = [1, 2, 3, 4, 5, 6]
        estimate_modes = ["CONSERVATIVE", "ECONOMICAL"]

        for conf_target in conf_targets:
            for estimate_mode in estimate_modes:
                estimatesmartfee_resp = await estimatesmartfee(self.connection_string, conf_target=conf_target, estimate_mode=estimate_mode)
                self.feerate.set(
                    value=estimatesmartfee_resp.feerate or 0,
                    labels={"conf_target": str(conf_target), "estimate_mode": estimate_mode},
                )
                self.blocks.set(
                    value=estimatesmartfee_resp.blocks,
                    labels={"conf_target": str(conf_target), "estimate_mode": estimate_mode},
                )
