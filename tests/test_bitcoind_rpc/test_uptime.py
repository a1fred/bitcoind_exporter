import pytest
from bitcoind_exporter.bitcoind_rpc.uptime import uptime


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await uptime(settings.BITCOIND)
    assert isinstance(resp, int)
