# Automatically generated by pb2py
from micropython import const

import protobuf as p

class DebugLinkMemoryRead(p.MessageType):
    FIELDS = {
        1: ('address', p.UVarintType, 0),
        2: ('length', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 110
