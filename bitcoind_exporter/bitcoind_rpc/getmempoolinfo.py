from decimal import Decimal
from pydantic import BaseModel
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class GetMempoolInfoResponse(BaseModel):
    loaded: bool
    size: int
    bytes: int
    usage: Decimal
    maxmempool: Decimal
    mempoolminfee: Decimal
    minrelaytxfee: Decimal


async def getmempoolinfo(connection_string: str) -> GetMempoolInfoResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getmempoolinfo()
        return GetMempoolInfoResponse(**data)
