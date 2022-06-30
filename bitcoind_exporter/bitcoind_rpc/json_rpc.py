import typing
import aiohttp
import asyncio
import logging
from json.decoder import JSONDecodeError

from jsonrpc_async import Server  # type: ignore
from jsonrpc_base import Message  # type: ignore
from jsonrpc_base import TransportError


logger = logging.getLogger(__name__)


class TransportDataError(TransportError):
    def __init__(self, exception_text, message, data, *args):
        """Create the transport error with information about the attempted message."""
        self.data = data
        if message:
            super().__init__('%s: %s: %s' % (message.transport_error_text, exception_text, data), *args)


class RpcServer(Server):
    async def send_message(self, message: Message) -> typing.Optional[dict]:
        if not message.params:
            message.params = []

        serialized_message = message.serialize()
        logger.debug(f"RPC request: {serialized_message}")

        try:
            response = await self._request(data=serialized_message)
        except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
            raise TransportError('Transport Error', message, exc)

        logger.debug(f"RPC response {response.status}: {await response.text()}")

        if response.status != 200:
            try:
                data = await response.json()
            except JSONDecodeError:
                raise TransportError('HTTP %d %s' % (response.status, response.reason), message)

            raise TransportDataError('HTTP %d %s' % (response.status, response.reason), message, data)

        if message.response_id is None:
            # Message is notification, so no response is expcted.
            return None

        try:
            response_data = await response.json(**self._json_args)
        except ValueError as value_error:
            raise TransportError('Cannot deserialize response body', message, value_error)

        return message.parse_response(response_data)


class JsonRPCServer:
    def __init__(self, addr: str):
        self.addr = addr

    async def __aenter__(self):
        self.server = RpcServer(self.addr, timeout=15)
        return self.server

    # noinspection PyShadowingBuiltins
    async def __aexit__(self, type, value, traceback):
        await self.server.session.close()
