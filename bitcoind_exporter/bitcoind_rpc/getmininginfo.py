import typing
from decimal import Decimal
from pydantic import BaseModel
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class MiningInfoResponse(BaseModel):
    blocks: int
    currentblockweight: typing.Optional[int]
    currentblocktx: typing.Optional[int]
    difficulty: Decimal
    networkhashps: Decimal
    pooledtx: Decimal
    chain: str
    warnings: str


async def getmininginfo(connection_string: str) -> MiningInfoResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getmininginfo()
        return MiningInfoResponse(**data)
