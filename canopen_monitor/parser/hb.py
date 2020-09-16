from canopen_monitor.parser.eds import EDS
"""
Parse Heartbeat message

@:param: data: a byte string containing the heartbeat message
@:returns: string describing the message
"""


def parse(eds_config: EDS, data: bytes):
    states = {
        0x00: "Boot-up",
        0x04: "Stopped",
        0x05: "Operational",
        0x7F: "Pre-operational"
    }

    hex_data = int(str(data[0]), 16)
    state = states.get(hex_data)
    name = eds_config.device_info.product_name

    if(state is None):
        return "{}{}".format(name.ljust(20, ' '),
                             'Invalid State')
    else:
        if int.from_bytes(data, "big") in states:
            return "{}{}".format(name.ljust(20, ' '),
                                 state)
        else:
            raise ValueError("Invalid heartbeat state detected")
