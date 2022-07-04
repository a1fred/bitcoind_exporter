import pytest
from bitcoind_exporter.bitcoind_rpc.getmemoryinfo import getmemoryinfo, GetMemoryInfoResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getmemoryinfo(settings.BITCOIND)
    assert isinstance(resp, GetMemoryInfoResponse)
