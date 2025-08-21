from versecbot_interface import PluginSettings, WatcherSettings


class SmileSettings(WatcherSettings):
    recognized_smiles: list[str]
    smile_to_send: str


class SmileBackSettings(PluginSettings):
    """Nothing special to add"""

    smile: SmileSettings
