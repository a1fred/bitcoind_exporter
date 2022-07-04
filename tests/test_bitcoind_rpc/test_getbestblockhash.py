import pytest
from bitcoind_exporter.bitcoind_rpc.getbestblockhash import getbestblockhash


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getbestblockhash(settings.BITCOIND)
    assert isinstance(resp, str)
