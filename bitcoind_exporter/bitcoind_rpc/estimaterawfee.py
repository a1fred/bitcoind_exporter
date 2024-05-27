from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer
import typing
from decimal import Decimal

from pydantic import BaseModel, Field


class EstimateRawFeeResponseHorizonPass(BaseModel):
    startrange: Decimal
    endrange: Decimal
    withintarget: Decimal
    totalconfirmed: Decimal
    inmempool: Decimal
    leftmempool: Decimal


class EstimateRawFeeResponseHorizon(BaseModel):
    feerate: typing.Optional[Decimal] = None
    decay: Decimal
    scale: Decimal
    horizon_pass: EstimateRawFeeResponseHorizonPass = Field(None, alias="pass")
    horizon_fail: EstimateRawFeeResponseHorizonPass = Field(None, alias="fail")
    errors: typing.List[str] = []


class EstimateRawFeeResponse(BaseModel):
    short: EstimateRawFeeResponseHorizon
    medium: EstimateRawFeeResponseHorizon
    long: EstimateRawFeeResponseHorizon


async def estimaterawfee(
    connection_string: str, conf_target: int, threshold: float
) -> EstimateRawFeeResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.estimaterawfee(conf_target, threshold)
        return EstimateRawFeeResponse(**data)
