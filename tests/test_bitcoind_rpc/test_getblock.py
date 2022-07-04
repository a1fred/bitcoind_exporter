import pytest
from bitcoind_exporter.bitcoind_rpc.getbestblockhash import getbestblockhash
from bitcoind_exporter.bitcoind_rpc.getblock import getblock_v1, BlockV1


@pytest.mark.asyncio
async def test_rpc_getblock_v1(settings):
    blockhash = await getbestblockhash(settings.BITCOIND)
    resp = await getblock_v1(settings.BITCOIND, blockhash)
    assert isinstance(resp, BlockV1)
