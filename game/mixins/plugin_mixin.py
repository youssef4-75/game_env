from ..plugin import Plugin

class PluginMixin: 
    def __init__(self, *__, **_) -> None:
        super().__init__(*__, **_)
        self.plugins: list[Plugin] = []

    # plugin
    def add_plugin(self, *plugins: Plugin):
        for plugin in plugins:
            plugin.init(self)
            self.plugins.append(plugin)

    # plugin
    def activate_plugins(self):
        for plug in self.plugins:
            plug.activate(self)