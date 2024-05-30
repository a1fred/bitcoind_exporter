from pydantic import BaseModel

from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer
import typing
from decimal import Decimal


class EstimateSmartFeeResponse(BaseModel):
    feerate: typing.Optional[Decimal] = None
    errors: typing.List[str] = []
    blocks: int


async def estimatesmartfee(
    connection_string: str, conf_target: int, estimate_mode: str
) -> EstimateSmartFeeResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.estimatesmartfee(conf_target, estimate_mode)
        return EstimateSmartFeeResponse(**data)
