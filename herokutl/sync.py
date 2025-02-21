"""
   __  __                __             ________
   / / / /__  _________  / /____  __    /_  __/ /
  / /_/ / _ \/ ___/ __ \/ //_/ / / /_____/ / / /
 / __  /  __/ /  / /_/ / ,< / /_/ /_____/ / / /___
/_/ /_/\___/_/   \____/_/|_|\__,_/     /_/ /_____/

(C) 2025-2026 https://github.com/Plovchikdeval/Heroku-tl
Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

"""

import asyncio
import functools
import inspect

from . import events, errors, utils, connection, helpers
from .client.account import _TakeoutClient
from .client.telegramclient import TelegramClient
from .tl import types, functions, custom
from .tl.custom import (
    Draft, Dialog, MessageButton, Forward, Button,
    Message, InlineResult, Conversation
)
from .tl.custom.chatgetter import ChatGetter
from .tl.custom.sendergetter import SenderGetter


def _syncify_wrap(t, method_name):
    method = getattr(t, method_name)

    @functools.wraps(method)
    def syncified(*args, **kwargs):
        coro = method(*args, **kwargs)
        loop = helpers.get_running_loop()
        if loop.is_running():
            return coro
        else:
            return loop.run_until_complete(coro)

    # Save an accessible reference to the original method
    setattr(syncified, '__tl.sync', method)
    setattr(t, method_name, syncified)


def syncify(*types):
    """
    Converts all the methods in the given types (class definitions)
    into synchronous, which return either the coroutine or the result
    based on whether ``asyncio's`` event loop is running.
    """
    # Our asynchronous generators all are `RequestIter`, which already
    # provide a synchronous iterator variant, so we don't need to worry
    # about asyncgenfunction's here.
    for t in types:
        for name in dir(t):
            if not name.startswith('_') or name == '__call__':
                if inspect.iscoroutinefunction(getattr(t, name)):
                    _syncify_wrap(t, name)


syncify(TelegramClient, _TakeoutClient, Draft, Dialog, MessageButton,
        ChatGetter, SenderGetter, Forward, Message, InlineResult, Conversation)


# Private special case, since a conversation's methods return
# futures (but the public function themselves are synchronous).
_syncify_wrap(Conversation, '_get_result')

__all__ = [
    'TelegramClient', 'Button',
    'types', 'functions', 'custom', 'errors',
    'events', 'utils', 'connection'
]
