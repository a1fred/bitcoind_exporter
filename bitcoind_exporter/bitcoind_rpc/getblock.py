from decimal import Decimal
import typing
from pydantic import BaseModel
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class BlockV1(BaseModel):
    hash: str
    confirmations: int
    size: int
    strippedsize: int
    weight: int
    height: int
    version: int
    versionHex: str
    merkleroot: str
    tx: typing.List[str]
    time: int
    mediantime: int
    nonce: int
    bits: str
    difficulty: Decimal
    chainwork: str
    nTx: int
    previousblockhash: typing.Optional[str] = None
    nextblockhash: typing.Optional[str] = None


async def getblock_v1(connection_string: str, blockhash: str) -> BlockV1:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getblock(blockhash, 1)
        return BlockV1(**data)
