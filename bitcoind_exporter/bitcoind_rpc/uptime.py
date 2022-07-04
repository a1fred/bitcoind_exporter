from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


async def uptime(connection_string: str) -> int:
    async with JsonRPCServer(connection_string) as server:
        return await server.uptime()
