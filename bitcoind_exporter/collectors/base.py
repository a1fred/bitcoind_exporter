import typing


class BaseCollector:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    async def update(self):
        pass


class CollectorRegistry:
    def __init__(self, connection_string: str, collectors: typing.List[typing.Type[BaseCollector]]):
        self.collectors = [x(connection_string) for x in collectors]

    async def update(self):
        for collector in self.collectors:
            await collector.update()
