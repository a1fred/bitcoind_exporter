import pytest
from bitcoind_exporter.bitcoind_rpc.getmininginfo import getmininginfo, MiningInfoResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getmininginfo(settings.BITCOIND)
    assert isinstance(resp, MiningInfoResponse)
