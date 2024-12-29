import asyncio
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from telentfy import Notifier, default_settings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    DEBUG: bool = False


settings = Settings()


# setup logging
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

# setup notifier
notifier = Notifier(default_settings)


async def main() -> None:
    logger.info("executing")


if __name__ == "__main__":
    asyncio.run(main())
