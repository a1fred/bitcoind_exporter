import pytest
from bitcoind_exporter.bitcoind_rpc.getblockchaininfo import getblockchaininfo, GetblockchaininfoResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getblockchaininfo(settings.BITCOIND)
    assert isinstance(resp, GetblockchaininfoResponse)
