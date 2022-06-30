import pytest
from bitcoind_exporter.bitcoind_rpc.estimatesmartfee import estimatesmartfee, EstimateSmartFeeResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await estimatesmartfee(settings.BITCOIND, 1, "CONSERVATIVE")
    assert isinstance(resp, EstimateSmartFeeResponse)
