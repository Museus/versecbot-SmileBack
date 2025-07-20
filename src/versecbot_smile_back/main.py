from discord import Message
from versecbot_interface import Watcher, INTERFACE_VERSION

from .settings import SmileBackSettings
from .logging import logger


def contains_smile(message_contents: str) -> bool:
    return ":)" in message_contents


class SmileBack(Watcher):
    smile_to_send: str
    interface_version = INTERFACE_VERSION
    name = "watcher_smile_back"

    def __init__(self, settings: SmileBackSettings):
        super().__init__(settings, logger=logger)
        self.smile_to_send = settings.smile_to_send

    def initialize(self, settings: SmileBackSettings, *args):
        super().initialize(settings, *args)
        logger.info("SmileBack initialized with smile: %s", self.smile_to_send)

    def should_act(self, message: Message) -> bool:
        if not super().should_act(message):
            return False

        return contains_smile(message.content)

    async def act(self, message: Message):
        logger.info(
            "Smiling back at %s <%s>",
            message.author.name,
            message.author.id,
        )
        await message.reply(self.smile_to_send)
