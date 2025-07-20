from discord import Message
from logging import getLogger

from versecbot_interface import Watcher, INTERFACE_VERSION

from .settings import SmileBackSettings

logger = getLogger("versecbot.plugins.smile_back.smile")


def contains_smile(message_contents: str, recognized_smiles: list[str]) -> bool:
    return any(
        recognized_smile in message_contents for recognized_smile in recognized_smiles
    )


class SmileBack(Watcher):
    smile_to_send: str
    recognized_smiles: list[str]
    only_recognized_smiles: bool

    interface_version = INTERFACE_VERSION
    name = "watcher_smile_back"

    def __init__(self, settings: SmileBackSettings):
        super().__init__(settings, logger=logger)
        self.smile_to_send = settings.smile.smile_to_send
        self.recognized_smiles = settings.smile.recognized_smiles
        self.only_recognized_smiles = settings.smile.only_recognized_smiles

    def initialize(self, settings: SmileBackSettings, *args):
        super().initialize(settings, *args)
        logger.info("SmileBack initialized with smile: %s", self.smile_to_send)

    def should_act(self, message: Message) -> bool:
        if not super().should_act(message):
            return False

        return contains_smile(message.content, recognized_smiles=self.recognized_smiles)

    async def act(self, message: Message):
        logger.info(
            "Smiling back at %s <%s>",
            message.author.name,
            message.author.id,
        )
        await message.reply(self.smile_to_send)
