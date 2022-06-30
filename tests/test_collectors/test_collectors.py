import pytest
from bitcoind_exporter.collectors import collectors


@pytest.mark.asyncio
@pytest.mark.parametrize("collector_name", collectors.keys())
async def test_collector(settings, collector_name):
    collector_klass = collectors[collector_name]
    collector_inst = collector_klass(settings.BITCOIND)
    await collector_inst.update()
