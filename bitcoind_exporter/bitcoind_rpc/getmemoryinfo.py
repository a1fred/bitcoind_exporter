from pydantic import BaseModel
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class GetMemoryInfoResponseLocked(BaseModel):
    used: int
    free: int
    total: int
    locked: int
    chunks_used: int
    chunks_free: int


class GetMemoryInfoResponse(BaseModel):
    locked: GetMemoryInfoResponseLocked


async def getmemoryinfo(connection_string: str) -> GetMemoryInfoResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getmemoryinfo()
        return GetMemoryInfoResponse(**data)
