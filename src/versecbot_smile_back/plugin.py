from discord import Intents
from logging import getLogger
from versecbot_interface import Plugin

from .settings import SmileBackSettings
from .jobs import SmileBack


logger = getLogger("versecbot.plugins.smile_back")


class SmileBackPlugin(Plugin):
    name: str = "smile_back"
    intents = [Intents.guild_messages]

    def __init__(self):
        super().__init__()

    def initialize(self, settings: SmileBackSettings, *args):
        logger.info("Initializing SmileBack plugin...")

        if not settings.enabled:
            return

        try:
            smile_handler = SmileBack(settings.smile)
        except Exception:
            logger.exception("Failed to initialize SmileBack")
        else:
            self.assign_job(smile_handler)
            logger.info("Ready to start smiling back!")

        logger.debug("SmileBack initialized")
