import pytest
from bitcoind_exporter.bitcoind_rpc.getnetworkinfo import getnetworkinfo, GetNetworkInfoResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getnetworkinfo(settings.BITCOIND)
    assert isinstance(resp, GetNetworkInfoResponse)
