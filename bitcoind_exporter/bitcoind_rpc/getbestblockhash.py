from bitcoind_exporter.bitcoind_rpc.json_rpc import JsonRPCServer


async def getbestblockhash(connection_string: str) -> str:
    async with JsonRPCServer(connection_string) as server:
        return await server.getbestblockhash()
