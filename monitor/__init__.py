import os.path
CANMONITOR_NAME = 'CANopen Monitor'
CANMONITOR_AUTHOR = "Portland State Aerospace Society"
CANMONITOR_WEBSITE = "https://psas.pdx.edu"
CANMONITOR_LICENSE = 'GPL-3.0'
CANMONITOR_VERSION = 'v2.6.0a'

CANMONITOR_CONFIG_DIR = os.path.expanduser('~/.config/canmonitor/')
CANMONITOR_DEVICES_CONFIG = CANMONITOR_CONFIG_DIR + 'devices.json'
CANMONITOR_LAYOUT_CONFIG = CANMONITOR_CONFIG_DIR + 'layout.json'
CANMONITOR_NODES_CONFIG = CANMONITOR_CONFIG_DIR + 'nodes.json'

DEBUG = False
TIMEOUT = 0.1