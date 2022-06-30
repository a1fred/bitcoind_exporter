import pytest
from bitcoind_exporter.bitcoind_rpc.estimaterawfee import estimaterawfee, EstimateRawFeeResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await estimaterawfee(settings.BITCOIND, 1, 0.95)
    assert isinstance(resp, EstimateRawFeeResponse)
