"""
   __  __                __             ________
   / / / /__  _________  / /____  __    /_  __/ /
  / /_/ / _ \/ ___/ __ \/ //_/ / / /_____/ / / /
 / __  /  __/ /  / /_/ / ,< / /_/ /_____/ / / /___
/_/ /_/\___/_/   \____/_/|_|\__,_/     /_/ /_____/

(C) 2025-2026 https://github.com/Plovchikdeval/Heroku-tl
Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

"""

from .client.telegramclient import TelegramClient
from .network import connection
from .tl.custom import Button
from .tl import patched as _  # import for its side-effects
from . import version, events, utils, errors, types, functions, custom

__version__ = version.__version__

__all__ = [
    'TelegramClient', 'Button',
    'types', 'functions', 'custom', 'errors',
    'events', 'utils', 'connection'
]
