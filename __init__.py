from __future__ import absolute_import

import octoprint.plugin
from . import client


class USBoN(octoprint.plugin.StartupPlugin,
            octoprint.plugin.TemplatePlugin,
            octoprint.plugin.SettingsPlugin,
            octoprint.plugin.AssetPlugin):

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    client.usbid = client.usb_waiter()
    client.writer()


__plugin_name__ = "USBoN"
__plugin_implementation__ = USBoN()
