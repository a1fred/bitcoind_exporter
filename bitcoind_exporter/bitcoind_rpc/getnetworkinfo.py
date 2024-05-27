import typing
from decimal import Decimal
from pydantic import BaseModel
from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


class GetNetworkInfoResponseNetworks(BaseModel):
    name: str
    limited: bool
    reachable: bool
    proxy: str
    proxy_randomize_credentials: bool


class GetNetworkInfoResponseLocalAddresses(BaseModel):
    address: str
    port: int
    score: int


class GetNetworkInfoResponse(BaseModel):
    version: float
    subversion: str
    protocolversion: int
    localservices: str
    localservicesnames: typing.List[str]
    localrelay: bool
    timeoffset: int
    connections: int
    connections_in: int = 0
    connections_out: int = 0
    networkactive: bool
    networks: typing.List[GetNetworkInfoResponseNetworks]
    relayfee: Decimal
    incrementalfee: Decimal
    localaddresses: typing.List[GetNetworkInfoResponseLocalAddresses]
    warnings: str


async def getnetworkinfo(connection_string: str) -> GetNetworkInfoResponse:
    async with JsonRPCServer(connection_string) as server:
        data = await server.getnetworkinfo()
        return GetNetworkInfoResponse(**data)
