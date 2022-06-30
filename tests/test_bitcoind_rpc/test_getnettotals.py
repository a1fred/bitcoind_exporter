import pytest
from bitcoind_exporter.bitcoind_rpc.getnettotals import getnettotals, GetNetTotalsResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getnettotals(settings.BITCOIND)
    assert isinstance(resp, GetNetTotalsResponse)
