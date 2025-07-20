from discord import Intents
from versecbot_interface import Plugin

from .settings import SmileBackSettings
from .main import SmileBack
from .logging import logger


class SmileBackPlugin(Plugin):
    name: str = "smile_back"
    settings = SmileBackSettings
    intents = [Intents.guild_messages]

    on_message = list

    def __init__(self):
        self.on_message = []

    def initialize(self, settings: SmileBackSettings, *args):
        logger.info("Initializing SmileBack plugin...")

        if not settings.enabled:
            return

        try:
            smile_handler = SmileBack(settings)
        except Exception:
            logger.exception("Failed to initialize SmileBack")
        else:
            self.on_message.append(smile_handler)
            logger.info("Ready to start smiling back!")

        logger.debug("SmileBack initialized")


plugin = SmileBackPlugin()
