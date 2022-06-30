import logging
from envvarconf import BaseSettings  # type: ignore
from envvarconf.mixins import logger, sentry  # type: ignore
from envvarconf.loaders import environ  # type: ignore
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

from bitcoind_exporter.collectors import collectors


class Settings(logger.LoggingMixin, sentry.SentryMixin, BaseSettings):
    # ----- Server api parameters section
    HOST: str = 'localhost'    # Server listen address
    PORT: int = 8064           # Server listen port

    # ----- Bitcoind parameters section
    BITCOIND: str = "http://bitcoind:bitcoind@localhost:8335"  # Bitcoind connection string

    COLLECTORS: str = ",".join(collectors.keys())

    def get_collectors(self):
        return [collectors[x] for x in self.COLLECTORS.split(",")]


def get_settings() -> Settings:
    settings = Settings()
    settings.load(loaders=[environ.Loader(), ])
    settings.print_detailed_settings()

    settings.initialize_logging()
    logging.getLogger('hpack.hpack').setLevel(logging.FATAL)

    settings.initialize_sentry(
        default_integrations=False,
        integrations=[AioHttpIntegration()],
        release="bitcoind_exporter@0.1.0",
    )
    return settings
