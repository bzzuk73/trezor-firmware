# Automatically generated by pb2py
from micropython import const

import protobuf as p

class IdentityType(p.MessageType):
    FIELDS = {
        1: ('proto', p.UnicodeType, 0),
        2: ('user', p.UnicodeType, 0),
        3: ('host', p.UnicodeType, 0),
        4: ('port', p.UnicodeType, 0),
        5: ('path', p.UnicodeType, 0),
        6: ('index', p.UVarintType, 0), # default=0
    }
