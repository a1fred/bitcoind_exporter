from pydantic import BaseModel, Field
from decimal import Decimal
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class GetblockchaininfoResponse(BaseModel):
    chain: str
    blocks: int
    headers: int
    bestblockhash: str
    difficulty: Decimal
    mediantime: int
    verificationprogress: float
    initialblockdownload: bool
    chainwork: str
    size_on_disk: int
    pruned: bool = False
    pruneheight: int = 0
    prune_target_size: int = 0
    softforks: dict = Field(default_factory=dict)
    warnings: str


async def getblockchaininfo(connection_string: str) -> GetblockchaininfoResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getblockchaininfo()
        return GetblockchaininfoResponse(**data)
