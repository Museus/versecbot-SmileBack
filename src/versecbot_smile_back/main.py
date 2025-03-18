from discord import Message

from versecbot.jobs import Watcher

from .settings import SmileBackSettings
from .logging import logger
from .util import contains_smile


class SmileBack(Watcher):
    enabled: bool
    smile_to_send: str

    def __init__(self, settings: SmileBackSettings):
        super().__init__(settings, logger=logger)
        self.smile_to_send = settings.smile_to_send

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
