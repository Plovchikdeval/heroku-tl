"""
   __  __                __             ________
   / / / /__  _________  / /____  __    /_  __/ /
  / /_/ / _ \/ ___/ __ \/ //_/ / / /_____/ / / /
 / __  /  __/ /  / /_/ / ,< / /_/ /_____/ / / /___
/_/ /_/\___/_/   \____/_/|_|\__,_/     /_/ /_____/

(C) 2025-2026 https://github.com/Plovchikdeval/Heroku-tl
Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

"""

from .. import TLObject


class TLMessage(TLObject):
    """
    https://core.telegram.org/mtproto/service_messages#simple-container.

    Messages are what's ultimately sent to Telegram:
        message msg_id:long seqno:int bytes:int body:bytes = Message;

    Each message has its own unique identifier, and the body is simply
    the serialized request that should be executed on the server, or
    the response object from Telegram. Since the body is always a valid
    object, it makes sense to store the object and not the bytes to
    ease working with them.

    There is no need to add serializing logic here since that can be
    inlined and is unlikely to change. Thus these are only needed to
    encapsulate responses.
    """
    SIZE_OVERHEAD = 12

    def __init__(self, msg_id, seq_no, obj):
        self.msg_id = msg_id
        self.seq_no = seq_no
        self.obj = obj

    def to_dict(self):
        return {
            '_': 'TLMessage',
            'msg_id': self.msg_id,
            'seq_no': self.seq_no,
            'obj': self.obj
        }
