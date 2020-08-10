# lightning-channelbalance

[![tippin.me](https://badgen.net/badge/%E2%9A%A1%EF%B8%8Ftippin.me/@kristapsk/F0918E)](https://tippin.me/@kristapsk)

channelbalance plugin for c-lightning

This plugin for c-lightning emulates `lncli channelbalance` command of LND.

Returns the sum of the total available channel balance across all open channels.

Active the plugin with:
`lightningd --plugin=PATH_TO_PLUGIN/channelbalance.py`

Call the plugin with:
`lightning-cli channelbalance`
