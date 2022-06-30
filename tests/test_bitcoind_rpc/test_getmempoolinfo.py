import pytest
from bitcoind_exporter.bitcoind_rpc.getmempoolinfo import getmempoolinfo, GetMempoolInfoResponse


@pytest.mark.asyncio
async def test_rpc(settings):
    resp = await getmempoolinfo(settings.BITCOIND)
    assert isinstance(resp, GetMempoolInfoResponse)
