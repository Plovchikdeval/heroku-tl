"""
   __  __                __             ________
   / / / /__  _________  / /____  __    /_  __/ /
  / /_/ / _ \/ ___/ __ \/ //_/ / / /_____/ / / /
 / __  /  __/ /  / /_/ / ,< / /_/ /_____/ / / /___
/_/ /_/\___/_/   \____/_/|_|\__,_/     /_/ /_____/

(C) 2025-2026 https://github.com/Plovchikdeval/Heroku-tl
Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

"""

from .. import types, alltlobjects
from ..custom.message import Message as _Message

class MessageEmpty(_Message, types.MessageEmpty):
    pass

types.MessageEmpty = MessageEmpty
alltlobjects.tlobjects[MessageEmpty.CONSTRUCTOR_ID] = MessageEmpty

class MessageService(_Message, types.MessageService):
    pass

types.MessageService = MessageService
alltlobjects.tlobjects[MessageService.CONSTRUCTOR_ID] = MessageService

class Message(_Message, types.Message):
    pass

types.Message = Message
alltlobjects.tlobjects[Message.CONSTRUCTOR_ID] = Message
