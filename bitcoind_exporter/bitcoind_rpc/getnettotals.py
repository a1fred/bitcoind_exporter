from pydantic import BaseModel
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class GetNetTotalsResponseUploadTarget(BaseModel):
    timeframe: int
    target: int
    target_reached: bool
    serve_historical_blocks: bool
    bytes_left_in_cycle: int
    time_left_in_cycle: int


class GetNetTotalsResponse(BaseModel):
    totalbytesrecv: int
    totalbytessent: int
    timemillis: int
    uploadtarget: GetNetTotalsResponseUploadTarget


async def getnettotals(connection_string: str) -> GetNetTotalsResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getnettotals()
        return GetNetTotalsResponse(**data)
