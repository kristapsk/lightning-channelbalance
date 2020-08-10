#!/usr/bin/env python3
"""This plugin for c-lightning emulates `lncli channelbalance` command of LND.

Returns the sum of the total available channel balance across all open channels.

Active the plugin with:
`lightningd --plugin=PATH_TO_PLUGIN/channelbalance.py`

Call the plugin with:
`lightning-cli channelbalance`

Author: Kristaps Kaupe (https://github.com/kristapsk)
"""

from lightning import LightningRpc, Plugin
from os.path import join

rpc = None
plugin = Plugin(autopatch=True)

@plugin.method("channelbalance")
def channelbalance(plugin=None):
    """Returns the sum of the total available channel balance across all open channels."""
    balance = 0
    pending_open_balance = 0
    channels = rpc.listfunds()["channels"]
    for channel in channels:
        if channel["state"] == "CHANNELD_NORMAL":
            balance += channel["channel_sat"]
        elif channel["state"] == "CHANNELD_AWAITING_LOCKIN":
            pending_open_balance += channel["channel_sat"]
    return {
        "balance": str(balance),
        "pending_open_balance": str(pending_open_balance)
    }

@plugin.init()
def init(options, configuration, plugin):
    global rpc
    plugin.log("channelbalance init")
    path = join(configuration["lightning-dir"], configuration["rpc-file"])
    rpc = LightningRpc(path)

plugin.run()
