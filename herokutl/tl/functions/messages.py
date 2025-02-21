"""
   __  __                __             ________
   / / / /__  _________  / /____  __    /_  __/ /
  / /_/ / _ \/ ___/ __ \/ //_/ / / /_____/ / / /
 / __  /  __/ /  / /_/ / ,< / /_/ /_____/ / / /___
/_/ /_/\___/_/   \____/_/|_|\__,_/     /_/ /_____/

(C) 2025-2026 https://github.com/Plovchikdeval/Heroku-tl
Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International

"""

from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeChatBannedRights, TypeChatReactions, TypeDataJSON, TypeDialogFilter, TypeInlineBotSwitchPM, TypeInlineBotWebView, TypeInputBotApp, TypeInputBotInlineMessageID, TypeInputBotInlineResult, TypeInputChatPhoto, TypeInputCheckPasswordSRP, TypeInputDialogPeer, TypeInputDocument, TypeInputEncryptedChat, TypeInputEncryptedFile, TypeInputFile, TypeInputGeoPoint, TypeInputMedia, TypeInputMessage, TypeInputPeer, TypeInputReplyTo, TypeInputSingleMedia, TypeInputStickerSet, TypeInputStickeredMedia, TypeInputUser, TypeInputWallPaper, TypeMessageEntity, TypeMessagesFilter, TypeReaction, TypeReplyMarkup, TypeReportReason, TypeSendMessageAction, TypeShippingOption, TypeTextWithEntities, TypeWallPaperSettings



class AcceptEncryptionRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3dbc0415
    SUBCLASS_OF_ID = 0x6d28a37a

    def __init__(self, peer: 'TypeInputEncryptedChat', g_b: bytes, key_fingerprint: int):
        """
        :returns EncryptedChat: Instance of either EncryptedChatEmpty, EncryptedChatWaiting, EncryptedChatRequested, EncryptedChat, EncryptedChatDiscarded.
        """
        self.peer = peer
        self.g_b = g_b
        self.key_fingerprint = key_fingerprint

    def to_dict(self):
        return {
            '_': 'AcceptEncryptionRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'g_b': self.g_b,
            'key_fingerprint': self.key_fingerprint
        }

    def _bytes(self):
        return b''.join((
            b'\x15\x04\xbc=',
            self.peer._bytes(),
            self.serialize_bytes(self.g_b),
            struct.pack('<q', self.key_fingerprint),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _g_b = reader.tgread_bytes()
        _key_fingerprint = reader.read_long()
        return cls(peer=_peer, g_b=_g_b, key_fingerprint=_key_fingerprint)


class AcceptUrlAuthRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb12c7125
    SUBCLASS_OF_ID = 0x7765cb1e

    def __init__(self, write_allowed: Optional[bool]=None, peer: Optional['TypeInputPeer']=None, msg_id: Optional[int]=None, button_id: Optional[int]=None, url: Optional[str]=None):
        """
        :returns UrlAuthResult: Instance of either UrlAuthResultRequest, UrlAuthResultAccepted, UrlAuthResultDefault.
        """
        self.write_allowed = write_allowed
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url

    async def resolve(self, client, utils):
        if self.peer:
            self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'AcceptUrlAuthRequest',
            'write_allowed': self.write_allowed,
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'button_id': self.button_id,
            'url': self.url
        }

    def _bytes(self):
        assert ((self.peer or self.peer is not None) and (self.msg_id or self.msg_id is not None) and (self.button_id or self.button_id is not None)) or ((self.peer is None or self.peer is False) and (self.msg_id is None or self.msg_id is False) and (self.button_id is None or self.button_id is False)), 'peer, msg_id, button_id parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'%q,\xb1',
            struct.pack('<I', (0 if self.write_allowed is None or self.write_allowed is False else 1) | (0 if self.peer is None or self.peer is False else 2) | (0 if self.msg_id is None or self.msg_id is False else 2) | (0 if self.button_id is None or self.button_id is False else 2) | (0 if self.url is None or self.url is False else 4)),
            b'' if self.peer is None or self.peer is False else (self.peer._bytes()),
            b'' if self.msg_id is None or self.msg_id is False else (struct.pack('<i', self.msg_id)),
            b'' if self.button_id is None or self.button_id is False else (struct.pack('<i', self.button_id)),
            b'' if self.url is None or self.url is False else (self.serialize_bytes(self.url)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _write_allowed = bool(flags & 1)
        if flags & 2:
            _peer = reader.tgread_object()
        else:
            _peer = None
        if flags & 2:
            _msg_id = reader.read_int()
        else:
            _msg_id = None
        if flags & 2:
            _button_id = reader.read_int()
        else:
            _button_id = None
        if flags & 4:
            _url = reader.tgread_string()
        else:
            _url = None
        return cls(write_allowed=_write_allowed, peer=_peer, msg_id=_msg_id, button_id=_button_id, url=_url)


class AddChatUserRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf24753e3
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, chat_id: int, user_id: 'TypeInputUser', fwd_limit: int):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.chat_id = chat_id
        self.user_id = user_id
        self.fwd_limit = fwd_limit

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'AddChatUserRequest',
            'chat_id': self.chat_id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'fwd_limit': self.fwd_limit
        }

    def _bytes(self):
        return b''.join((
            b'\xe3SG\xf2',
            struct.pack('<q', self.chat_id),
            self.user_id._bytes(),
            struct.pack('<i', self.fwd_limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        _user_id = reader.tgread_object()
        _fwd_limit = reader.read_int()
        return cls(chat_id=_chat_id, user_id=_user_id, fwd_limit=_fwd_limit)


class CheckChatInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3eadb1bb
    SUBCLASS_OF_ID = 0x4561736

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: str):
        """
        :returns ChatInvite: Instance of either ChatInviteAlready, ChatInvite, ChatInvitePeek.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'CheckChatInviteRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xbb\xb1\xad>',
            self.serialize_bytes(self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.tgread_string()
        return cls(hash=_hash)


class CheckHistoryImportRequest(TLRequest):
    CONSTRUCTOR_ID = 0x43fe19f3
    SUBCLASS_OF_ID = 0x5bb2720b

    def __init__(self, import_head: str):
        """
        :returns messages.HistoryImportParsed: Instance of HistoryImportParsed.
        """
        self.import_head = import_head

    def to_dict(self):
        return {
            '_': 'CheckHistoryImportRequest',
            'import_head': self.import_head
        }

    def _bytes(self):
        return b''.join((
            b'\xf3\x19\xfeC',
            self.serialize_bytes(self.import_head),
        ))

    @classmethod
    def from_reader(cls, reader):
        _import_head = reader.tgread_string()
        return cls(import_head=_import_head)


class CheckHistoryImportPeerRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5dc60f03
    SUBCLASS_OF_ID = 0xb84bb337

    def __init__(self, peer: 'TypeInputPeer'):
        """
        :returns messages.CheckedHistoryImportPeer: Instance of CheckedHistoryImportPeer.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'CheckHistoryImportPeerRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'\x03\x0f\xc6]',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class ClearAllDraftsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7e58ee9c
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'ClearAllDraftsRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\x9c\xeeX~',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class ClearRecentReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9dfeefb4
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'ClearRecentReactionsRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\xb4\xef\xfe\x9d',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class ClearRecentStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8999602d
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, attached: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.attached = attached

    def to_dict(self):
        return {
            '_': 'ClearRecentStickersRequest',
            'attached': self.attached
        }

    def _bytes(self):
        return b''.join((
            b'-`\x99\x89',
            struct.pack('<I', (0 if self.attached is None or self.attached is False else 1)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _attached = bool(flags & 1)
        return cls(attached=_attached)


class CreateChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0x34a818
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, users: List['TypeInputUser'], title: str, ttl_period: Optional[int]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.users = users
        self.title = title
        self.ttl_period = ttl_period

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.users:
            _tmp.append(utils.get_input_user(await client.get_input_entity(_x)))

        self.users = _tmp

    def to_dict(self):
        return {
            '_': 'CreateChatRequest',
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users],
            'title': self.title,
            'ttl_period': self.ttl_period
        }

    def _bytes(self):
        return b''.join((
            b'\x18\xa84\x00',
            struct.pack('<I', (0 if self.ttl_period is None or self.ttl_period is False else 1)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
            self.serialize_bytes(self.title),
            b'' if self.ttl_period is None or self.ttl_period is False else (struct.pack('<i', self.ttl_period)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        _title = reader.tgread_string()
        if flags & 1:
            _ttl_period = reader.read_int()
        else:
            _ttl_period = None
        return cls(users=_users, title=_title, ttl_period=_ttl_period)


class DeleteChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5bd0ee50
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, chat_id: int):
        """
        :returns Bool: This type has no constructors.
        """
        self.chat_id = chat_id

    def to_dict(self):
        return {
            '_': 'DeleteChatRequest',
            'chat_id': self.chat_id
        }

    def _bytes(self):
        return b''.join((
            b'P\xee\xd0[',
            struct.pack('<q', self.chat_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        return cls(chat_id=_chat_id)


class DeleteChatUserRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa2185cab
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, chat_id: int, user_id: 'TypeInputUser', revoke_history: Optional[bool]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.chat_id = chat_id
        self.user_id = user_id
        self.revoke_history = revoke_history

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'DeleteChatUserRequest',
            'chat_id': self.chat_id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'revoke_history': self.revoke_history
        }

    def _bytes(self):
        return b''.join((
            b'\xab\\\x18\xa2',
            struct.pack('<I', (0 if self.revoke_history is None or self.revoke_history is False else 1)),
            struct.pack('<q', self.chat_id),
            self.user_id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _revoke_history = bool(flags & 1)
        _chat_id = reader.read_long()
        _user_id = reader.tgread_object()
        return cls(chat_id=_chat_id, user_id=_user_id, revoke_history=_revoke_history)


class DeleteExportedChatInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd464a42b
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', link: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.link = link

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'DeleteExportedChatInviteRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'link': self.link
        }

    def _bytes(self):
        return b''.join((
            b'+\xa4d\xd4',
            self.peer._bytes(),
            self.serialize_bytes(self.link),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _link = reader.tgread_string()
        return cls(peer=_peer, link=_link)


class DeleteHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb08f922a
    SUBCLASS_OF_ID = 0x2c49c116

    def __init__(self, peer: 'TypeInputPeer', max_id: int, just_clear: Optional[bool]=None, revoke: Optional[bool]=None, min_date: Optional[datetime]=None, max_date: Optional[datetime]=None):
        """
        :returns messages.AffectedHistory: Instance of AffectedHistory.
        """
        self.peer = peer
        self.max_id = max_id
        self.just_clear = just_clear
        self.revoke = revoke
        self.min_date = min_date
        self.max_date = max_date

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'DeleteHistoryRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'max_id': self.max_id,
            'just_clear': self.just_clear,
            'revoke': self.revoke,
            'min_date': self.min_date,
            'max_date': self.max_date
        }

    def _bytes(self):
        return b''.join((
            b'*\x92\x8f\xb0',
            struct.pack('<I', (0 if self.just_clear is None or self.just_clear is False else 1) | (0 if self.revoke is None or self.revoke is False else 2) | (0 if self.min_date is None or self.min_date is False else 4) | (0 if self.max_date is None or self.max_date is False else 8)),
            self.peer._bytes(),
            struct.pack('<i', self.max_id),
            b'' if self.min_date is None or self.min_date is False else (self.serialize_datetime(self.min_date)),
            b'' if self.max_date is None or self.max_date is False else (self.serialize_datetime(self.max_date)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _just_clear = bool(flags & 1)
        _revoke = bool(flags & 2)
        _peer = reader.tgread_object()
        _max_id = reader.read_int()
        if flags & 4:
            _min_date = reader.tgread_date()
        else:
            _min_date = None
        if flags & 8:
            _max_date = reader.tgread_date()
        else:
            _max_date = None
        return cls(peer=_peer, max_id=_max_id, just_clear=_just_clear, revoke=_revoke, min_date=_min_date, max_date=_max_date)


class DeleteMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe58e95d2
    SUBCLASS_OF_ID = 0xced3c06e

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List[int], revoke: Optional[bool]=None):
        """
        :returns messages.AffectedMessages: Instance of AffectedMessages.
        """
        self.id = id
        self.revoke = revoke

    def to_dict(self):
        return {
            '_': 'DeleteMessagesRequest',
            'id': [] if self.id is None else self.id[:],
            'revoke': self.revoke
        }

    def _bytes(self):
        return b''.join((
            b'\xd2\x95\x8e\xe5',
            struct.pack('<I', (0 if self.revoke is None or self.revoke is False else 1)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _revoke = bool(flags & 1)
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(id=_id, revoke=_revoke)


class DeletePhoneCallHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf9cbe409
    SUBCLASS_OF_ID = 0xf817652e

    def __init__(self, revoke: Optional[bool]=None):
        """
        :returns messages.AffectedFoundMessages: Instance of AffectedFoundMessages.
        """
        self.revoke = revoke

    def to_dict(self):
        return {
            '_': 'DeletePhoneCallHistoryRequest',
            'revoke': self.revoke
        }

    def _bytes(self):
        return b''.join((
            b'\t\xe4\xcb\xf9',
            struct.pack('<I', (0 if self.revoke is None or self.revoke is False else 1)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _revoke = bool(flags & 1)
        return cls(revoke=_revoke)


class DeleteRevokedExportedChatInvitesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x56987bd5
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser'):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.admin_id = admin_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.admin_id = utils.get_input_user(await client.get_input_entity(self.admin_id))

    def to_dict(self):
        return {
            '_': 'DeleteRevokedExportedChatInvitesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'admin_id': self.admin_id.to_dict() if isinstance(self.admin_id, TLObject) else self.admin_id
        }

    def _bytes(self):
        return b''.join((
            b'\xd5{\x98V',
            self.peer._bytes(),
            self.admin_id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _admin_id = reader.tgread_object()
        return cls(peer=_peer, admin_id=_admin_id)


class DeleteScheduledMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x59ae2b16
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int]):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'DeleteScheduledMessagesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x16+\xaeY',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(peer=_peer, id=_id)


class DiscardEncryptionRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf393aea0
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, chat_id: int, delete_history: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.chat_id = chat_id
        self.delete_history = delete_history

    def to_dict(self):
        return {
            '_': 'DiscardEncryptionRequest',
            'chat_id': self.chat_id,
            'delete_history': self.delete_history
        }

    def _bytes(self):
        return b''.join((
            b'\xa0\xae\x93\xf3',
            struct.pack('<I', (0 if self.delete_history is None or self.delete_history is False else 1)),
            struct.pack('<i', self.chat_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _delete_history = bool(flags & 1)
        _chat_id = reader.read_int()
        return cls(chat_id=_chat_id, delete_history=_delete_history)


class EditChatAboutRequest(TLRequest):
    CONSTRUCTOR_ID = 0xdef60797
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', about: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.about = about

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'EditChatAboutRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'about': self.about
        }

    def _bytes(self):
        return b''.join((
            b'\x97\x07\xf6\xde',
            self.peer._bytes(),
            self.serialize_bytes(self.about),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _about = reader.tgread_string()
        return cls(peer=_peer, about=_about)


class EditChatAdminRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa85bd1c2
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, chat_id: int, user_id: 'TypeInputUser', is_admin: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'EditChatAdminRequest',
            'chat_id': self.chat_id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'is_admin': self.is_admin
        }

    def _bytes(self):
        return b''.join((
            b'\xc2\xd1[\xa8',
            struct.pack('<q', self.chat_id),
            self.user_id._bytes(),
            b'\xb5ur\x99' if self.is_admin else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        _user_id = reader.tgread_object()
        _is_admin = reader.tgread_bool()
        return cls(chat_id=_chat_id, user_id=_user_id, is_admin=_is_admin)


class EditChatDefaultBannedRightsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa5866b41
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights'):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.banned_rights = banned_rights

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'EditChatDefaultBannedRightsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'banned_rights': self.banned_rights.to_dict() if isinstance(self.banned_rights, TLObject) else self.banned_rights
        }

    def _bytes(self):
        return b''.join((
            b'Ak\x86\xa5',
            self.peer._bytes(),
            self.banned_rights._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _banned_rights = reader.tgread_object()
        return cls(peer=_peer, banned_rights=_banned_rights)


class EditChatPhotoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x35ddd674
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, chat_id: int, photo: 'TypeInputChatPhoto'):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.chat_id = chat_id
        self.photo = photo

    async def resolve(self, client, utils):
        self.photo = utils.get_input_chat_photo(self.photo)

    def to_dict(self):
        return {
            '_': 'EditChatPhotoRequest',
            'chat_id': self.chat_id,
            'photo': self.photo.to_dict() if isinstance(self.photo, TLObject) else self.photo
        }

    def _bytes(self):
        return b''.join((
            b't\xd6\xdd5',
            struct.pack('<q', self.chat_id),
            self.photo._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        _photo = reader.tgread_object()
        return cls(chat_id=_chat_id, photo=_photo)


class EditChatTitleRequest(TLRequest):
    CONSTRUCTOR_ID = 0x73783ffd
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, chat_id: int, title: str):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.chat_id = chat_id
        self.title = title

    def to_dict(self):
        return {
            '_': 'EditChatTitleRequest',
            'chat_id': self.chat_id,
            'title': self.title
        }

    def _bytes(self):
        return b''.join((
            b'\xfd?xs',
            struct.pack('<q', self.chat_id),
            self.serialize_bytes(self.title),
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        _title = reader.tgread_string()
        return cls(chat_id=_chat_id, title=_title)


class EditExportedChatInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0xbdca2f75
    SUBCLASS_OF_ID = 0x82dcd4ca

    def __init__(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool]=None, expire_date: Optional[datetime]=None, usage_limit: Optional[int]=None, request_needed: Optional[bool]=None, title: Optional[str]=None):
        """
        :returns messages.ExportedChatInvite: Instance of either ExportedChatInvite, ExportedChatInviteReplaced.
        """
        self.peer = peer
        self.link = link
        self.revoked = revoked
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.request_needed = request_needed
        self.title = title

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'EditExportedChatInviteRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'link': self.link,
            'revoked': self.revoked,
            'expire_date': self.expire_date,
            'usage_limit': self.usage_limit,
            'request_needed': self.request_needed,
            'title': self.title
        }

    def _bytes(self):
        return b''.join((
            b'u/\xca\xbd',
            struct.pack('<I', (0 if self.revoked is None or self.revoked is False else 4) | (0 if self.expire_date is None or self.expire_date is False else 1) | (0 if self.usage_limit is None or self.usage_limit is False else 2) | (0 if self.request_needed is None else 8) | (0 if self.title is None or self.title is False else 16)),
            self.peer._bytes(),
            self.serialize_bytes(self.link),
            b'' if self.expire_date is None or self.expire_date is False else (self.serialize_datetime(self.expire_date)),
            b'' if self.usage_limit is None or self.usage_limit is False else (struct.pack('<i', self.usage_limit)),
            b'' if self.request_needed is None else (b'\xb5ur\x99' if self.request_needed else b'7\x97y\xbc'),
            b'' if self.title is None or self.title is False else (self.serialize_bytes(self.title)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _revoked = bool(flags & 4)
        _peer = reader.tgread_object()
        _link = reader.tgread_string()
        if flags & 1:
            _expire_date = reader.tgread_date()
        else:
            _expire_date = None
        if flags & 2:
            _usage_limit = reader.read_int()
        else:
            _usage_limit = None
        if flags & 8:
            _request_needed = reader.tgread_bool()
        else:
            _request_needed = None
        if flags & 16:
            _title = reader.tgread_string()
        else:
            _title = None
        return cls(peer=_peer, link=_link, revoked=_revoked, expire_date=_expire_date, usage_limit=_usage_limit, request_needed=_request_needed, title=_title)


class EditInlineBotMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0x83557dba
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputBotInlineMessageID', no_webpage: Optional[bool]=None, invert_media: Optional[bool]=None, message: Optional[str]=None, media: Optional['TypeInputMedia']=None, reply_markup: Optional['TypeReplyMarkup']=None, entities: Optional[List['TypeMessageEntity']]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities

    async def resolve(self, client, utils):
        if self.media:
            self.media = utils.get_input_media(self.media)

    def to_dict(self):
        return {
            '_': 'EditInlineBotMessageRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'no_webpage': self.no_webpage,
            'invert_media': self.invert_media,
            'message': self.message,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media,
            'reply_markup': self.reply_markup.to_dict() if isinstance(self.reply_markup, TLObject) else self.reply_markup,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities]
        }

    def _bytes(self):
        return b''.join((
            b'\xba}U\x83',
            struct.pack('<I', (0 if self.no_webpage is None or self.no_webpage is False else 2) | (0 if self.invert_media is None or self.invert_media is False else 65536) | (0 if self.message is None or self.message is False else 2048) | (0 if self.media is None or self.media is False else 16384) | (0 if self.reply_markup is None or self.reply_markup is False else 4) | (0 if self.entities is None or self.entities is False else 8)),
            self.id._bytes(),
            b'' if self.message is None or self.message is False else (self.serialize_bytes(self.message)),
            b'' if self.media is None or self.media is False else (self.media._bytes()),
            b'' if self.reply_markup is None or self.reply_markup is False else (self.reply_markup._bytes()),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities))),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _no_webpage = bool(flags & 2)
        _invert_media = bool(flags & 65536)
        _id = reader.tgread_object()
        if flags & 2048:
            _message = reader.tgread_string()
        else:
            _message = None
        if flags & 16384:
            _media = reader.tgread_object()
        else:
            _media = None
        if flags & 4:
            _reply_markup = reader.tgread_object()
        else:
            _reply_markup = None
        if flags & 8:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        return cls(id=_id, no_webpage=_no_webpage, invert_media=_invert_media, message=_message, media=_media, reply_markup=_reply_markup, entities=_entities)


class EditMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0x48f71778
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, no_webpage: Optional[bool]=None, invert_media: Optional[bool]=None, message: Optional[str]=None, media: Optional['TypeInputMedia']=None, reply_markup: Optional['TypeReplyMarkup']=None, entities: Optional[List['TypeMessageEntity']]=None, schedule_date: Optional[datetime]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        if self.media:
            self.media = utils.get_input_media(self.media)

    def to_dict(self):
        return {
            '_': 'EditMessageRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'no_webpage': self.no_webpage,
            'invert_media': self.invert_media,
            'message': self.message,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media,
            'reply_markup': self.reply_markup.to_dict() if isinstance(self.reply_markup, TLObject) else self.reply_markup,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities],
            'schedule_date': self.schedule_date
        }

    def _bytes(self):
        return b''.join((
            b'x\x17\xf7H',
            struct.pack('<I', (0 if self.no_webpage is None or self.no_webpage is False else 2) | (0 if self.invert_media is None or self.invert_media is False else 65536) | (0 if self.message is None or self.message is False else 2048) | (0 if self.media is None or self.media is False else 16384) | (0 if self.reply_markup is None or self.reply_markup is False else 4) | (0 if self.entities is None or self.entities is False else 8) | (0 if self.schedule_date is None or self.schedule_date is False else 32768)),
            self.peer._bytes(),
            struct.pack('<i', self.id),
            b'' if self.message is None or self.message is False else (self.serialize_bytes(self.message)),
            b'' if self.media is None or self.media is False else (self.media._bytes()),
            b'' if self.reply_markup is None or self.reply_markup is False else (self.reply_markup._bytes()),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities))),
            b'' if self.schedule_date is None or self.schedule_date is False else (self.serialize_datetime(self.schedule_date)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _no_webpage = bool(flags & 2)
        _invert_media = bool(flags & 65536)
        _peer = reader.tgread_object()
        _id = reader.read_int()
        if flags & 2048:
            _message = reader.tgread_string()
        else:
            _message = None
        if flags & 16384:
            _media = reader.tgread_object()
        else:
            _media = None
        if flags & 4:
            _reply_markup = reader.tgread_object()
        else:
            _reply_markup = None
        if flags & 8:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        if flags & 32768:
            _schedule_date = reader.tgread_date()
        else:
            _schedule_date = None
        return cls(peer=_peer, id=_id, no_webpage=_no_webpage, invert_media=_invert_media, message=_message, media=_media, reply_markup=_reply_markup, entities=_entities, schedule_date=_schedule_date)


class ExportChatInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa02ce5d5
    SUBCLASS_OF_ID = 0xb4748a58

    def __init__(self, peer: 'TypeInputPeer', legacy_revoke_permanent: Optional[bool]=None, request_needed: Optional[bool]=None, expire_date: Optional[datetime]=None, usage_limit: Optional[int]=None, title: Optional[str]=None):
        """
        :returns ExportedChatInvite: Instance of either ChatInviteExported, ChatInvitePublicJoinRequests.
        """
        self.peer = peer
        self.legacy_revoke_permanent = legacy_revoke_permanent
        self.request_needed = request_needed
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.title = title

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ExportChatInviteRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'legacy_revoke_permanent': self.legacy_revoke_permanent,
            'request_needed': self.request_needed,
            'expire_date': self.expire_date,
            'usage_limit': self.usage_limit,
            'title': self.title
        }

    def _bytes(self):
        return b''.join((
            b'\xd5\xe5,\xa0',
            struct.pack('<I', (0 if self.legacy_revoke_permanent is None or self.legacy_revoke_permanent is False else 4) | (0 if self.request_needed is None or self.request_needed is False else 8) | (0 if self.expire_date is None or self.expire_date is False else 1) | (0 if self.usage_limit is None or self.usage_limit is False else 2) | (0 if self.title is None or self.title is False else 16)),
            self.peer._bytes(),
            b'' if self.expire_date is None or self.expire_date is False else (self.serialize_datetime(self.expire_date)),
            b'' if self.usage_limit is None or self.usage_limit is False else (struct.pack('<i', self.usage_limit)),
            b'' if self.title is None or self.title is False else (self.serialize_bytes(self.title)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _legacy_revoke_permanent = bool(flags & 4)
        _request_needed = bool(flags & 8)
        _peer = reader.tgread_object()
        if flags & 1:
            _expire_date = reader.tgread_date()
        else:
            _expire_date = None
        if flags & 2:
            _usage_limit = reader.read_int()
        else:
            _usage_limit = None
        if flags & 16:
            _title = reader.tgread_string()
        else:
            _title = None
        return cls(peer=_peer, legacy_revoke_permanent=_legacy_revoke_permanent, request_needed=_request_needed, expire_date=_expire_date, usage_limit=_usage_limit, title=_title)


class FaveStickerRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb9ffc55b
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputDocument', unfave: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.unfave = unfave

    async def resolve(self, client, utils):
        self.id = utils.get_input_document(self.id)

    def to_dict(self):
        return {
            '_': 'FaveStickerRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'unfave': self.unfave
        }

    def _bytes(self):
        return b''.join((
            b'[\xc5\xff\xb9',
            self.id._bytes(),
            b'\xb5ur\x99' if self.unfave else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.tgread_object()
        _unfave = reader.tgread_bool()
        return cls(id=_id, unfave=_unfave)


class ForwardMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc661bbc4
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, from_peer: 'TypeInputPeer', id: List[int], to_peer: 'TypeInputPeer', silent: Optional[bool]=None, background: Optional[bool]=None, with_my_score: Optional[bool]=None, drop_author: Optional[bool]=None, drop_media_captions: Optional[bool]=None, noforwards: Optional[bool]=None, random_id: List[int]=None, top_msg_id: Optional[int]=None, schedule_date: Optional[datetime]=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.from_peer = from_peer
        self.id = id
        self.to_peer = to_peer
        self.silent = silent
        self.background = background
        self.with_my_score = with_my_score
        self.drop_author = drop_author
        self.drop_media_captions = drop_media_captions
        self.noforwards = noforwards
        self.random_id = random_id if random_id is not None else [int.from_bytes(os.urandom(8), 'big', signed=True) for _ in range(len(id))]
        self.top_msg_id = top_msg_id
        self.schedule_date = schedule_date
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.from_peer = utils.get_input_peer(await client.get_input_entity(self.from_peer))
        self.to_peer = utils.get_input_peer(await client.get_input_entity(self.to_peer))
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'ForwardMessagesRequest',
            'from_peer': self.from_peer.to_dict() if isinstance(self.from_peer, TLObject) else self.from_peer,
            'id': [] if self.id is None else self.id[:],
            'to_peer': self.to_peer.to_dict() if isinstance(self.to_peer, TLObject) else self.to_peer,
            'silent': self.silent,
            'background': self.background,
            'with_my_score': self.with_my_score,
            'drop_author': self.drop_author,
            'drop_media_captions': self.drop_media_captions,
            'noforwards': self.noforwards,
            'random_id': [] if self.random_id is None else self.random_id[:],
            'top_msg_id': self.top_msg_id,
            'schedule_date': self.schedule_date,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'\xc4\xbba\xc6',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 32) | (0 if self.background is None or self.background is False else 64) | (0 if self.with_my_score is None or self.with_my_score is False else 256) | (0 if self.drop_author is None or self.drop_author is False else 2048) | (0 if self.drop_media_captions is None or self.drop_media_captions is False else 4096) | (0 if self.noforwards is None or self.noforwards is False else 16384) | (0 if self.top_msg_id is None or self.top_msg_id is False else 512) | (0 if self.schedule_date is None or self.schedule_date is False else 1024) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.from_peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.random_id)),b''.join(struct.pack('<q', x) for x in self.random_id),
            self.to_peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
            b'' if self.schedule_date is None or self.schedule_date is False else (self.serialize_datetime(self.schedule_date)),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 32)
        _background = bool(flags & 64)
        _with_my_score = bool(flags & 256)
        _drop_author = bool(flags & 2048)
        _drop_media_captions = bool(flags & 4096)
        _noforwards = bool(flags & 16384)
        _from_peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        reader.read_int()
        _random_id = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _random_id.append(_x)

        _to_peer = reader.tgread_object()
        if flags & 512:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        if flags & 1024:
            _schedule_date = reader.tgread_date()
        else:
            _schedule_date = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(from_peer=_from_peer, id=_id, to_peer=_to_peer, silent=_silent, background=_background, with_my_score=_with_my_score, drop_author=_drop_author, drop_media_captions=_drop_media_captions, noforwards=_noforwards, random_id=_random_id, top_msg_id=_top_msg_id, schedule_date=_schedule_date, send_as=_send_as)


class GetAdminsWithInvitesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3920e6ef
    SUBCLASS_OF_ID = 0x8f5bad2b

    def __init__(self, peer: 'TypeInputPeer'):
        """
        :returns messages.ChatAdminsWithInvites: Instance of ChatAdminsWithInvites.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetAdminsWithInvitesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'\xef\xe6 9',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class GetAllDraftsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x6a3f8d65
    SUBCLASS_OF_ID = 0x8af52aac

    def to_dict(self):
        return {
            '_': 'GetAllDraftsRequest'
        }

    def _bytes(self):
        return b''.join((
            b'e\x8d?j',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetAllStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb8a0a1a8
    SUBCLASS_OF_ID = 0x45834829

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.AllStickers: Instance of either AllStickersNotModified, AllStickers.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetAllStickersRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xa8\xa1\xa0\xb8',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetArchivedStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x57f17692
    SUBCLASS_OF_ID = 0x7296d771

    def __init__(self, offset_id: int, limit: int, masks: Optional[bool]=None, emojis: Optional[bool]=None):
        """
        :returns messages.ArchivedStickers: Instance of ArchivedStickers.
        """
        self.offset_id = offset_id
        self.limit = limit
        self.masks = masks
        self.emojis = emojis

    def to_dict(self):
        return {
            '_': 'GetArchivedStickersRequest',
            'offset_id': self.offset_id,
            'limit': self.limit,
            'masks': self.masks,
            'emojis': self.emojis
        }

    def _bytes(self):
        return b''.join((
            b'\x92v\xf1W',
            struct.pack('<I', (0 if self.masks is None or self.masks is False else 1) | (0 if self.emojis is None or self.emojis is False else 2)),
            struct.pack('<q', self.offset_id),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _masks = bool(flags & 1)
        _emojis = bool(flags & 2)
        _offset_id = reader.read_long()
        _limit = reader.read_int()
        return cls(offset_id=_offset_id, limit=_limit, masks=_masks, emojis=_emojis)


class GetAttachMenuBotRequest(TLRequest):
    CONSTRUCTOR_ID = 0x77216192
    SUBCLASS_OF_ID = 0xdb33883d

    def __init__(self, bot: 'TypeInputUser'):
        """
        :returns AttachMenuBotsBot: Instance of AttachMenuBotsBot.
        """
        self.bot = bot

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'GetAttachMenuBotRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot
        }

    def _bytes(self):
        return b''.join((
            b'\x92a!w',
            self.bot._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        return cls(bot=_bot)


class GetAttachMenuBotsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x16fcc2cb
    SUBCLASS_OF_ID = 0x842e23da

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns AttachMenuBots: Instance of either AttachMenuBotsNotModified, AttachMenuBots.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetAttachMenuBotsRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xcb\xc2\xfc\x16',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetAttachedStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xcc5b67cc
    SUBCLASS_OF_ID = 0xcc125f6b

    def __init__(self, media: 'TypeInputStickeredMedia'):
        """
        :returns Vector<StickerSetCovered>: This type has no constructors.
        """
        self.media = media

    def to_dict(self):
        return {
            '_': 'GetAttachedStickersRequest',
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media
        }

    def _bytes(self):
        return b''.join((
            b'\xccg[\xcc',
            self.media._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _media = reader.tgread_object()
        return cls(media=_media)


class GetAvailableReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x18dea0ac
    SUBCLASS_OF_ID = 0xe426ad82

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.AvailableReactions: Instance of either AvailableReactionsNotModified, AvailableReactions.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetAvailableReactionsRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xac\xa0\xde\x18',
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_int()
        return cls(hash=_hash)


class GetBotAppRequest(TLRequest):
    CONSTRUCTOR_ID = 0x34fdc5c3
    SUBCLASS_OF_ID = 0x8f7243a7

    # noinspection PyShadowingBuiltins
    def __init__(self, app: 'TypeInputBotApp', hash: int):
        """
        :returns messages.BotApp: Instance of BotApp.
        """
        self.app = app
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetBotAppRequest',
            'app': self.app.to_dict() if isinstance(self.app, TLObject) else self.app,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xc3\xc5\xfd4',
            self.app._bytes(),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _app = reader.tgread_object()
        _hash = reader.read_long()
        return cls(app=_app, hash=_hash)


class GetBotCallbackAnswerRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9342ca07
    SUBCLASS_OF_ID = 0x6c4dd18c

    def __init__(self, peer: 'TypeInputPeer', msg_id: int, game: Optional[bool]=None, data: Optional[bytes]=None, password: Optional['TypeInputCheckPasswordSRP']=None):
        """
        :returns messages.BotCallbackAnswer: Instance of BotCallbackAnswer.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.game = game
        self.data = data
        self.password = password

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetBotCallbackAnswerRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'game': self.game,
            'data': self.data,
            'password': self.password.to_dict() if isinstance(self.password, TLObject) else self.password
        }

    def _bytes(self):
        return b''.join((
            b'\x07\xcaB\x93',
            struct.pack('<I', (0 if self.game is None or self.game is False else 2) | (0 if self.data is None or self.data is False else 1) | (0 if self.password is None or self.password is False else 4)),
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            b'' if self.data is None or self.data is False else (self.serialize_bytes(self.data)),
            b'' if self.password is None or self.password is False else (self.password._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _game = bool(flags & 2)
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        if flags & 1:
            _data = reader.tgread_bytes()
        else:
            _data = None
        if flags & 4:
            _password = reader.tgread_object()
        else:
            _password = None
        return cls(peer=_peer, msg_id=_msg_id, game=_game, data=_data, password=_password)


class GetChatInviteImportersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xdf04dd4e
    SUBCLASS_OF_ID = 0xd9bc8aa6

    def __init__(self, peer: 'TypeInputPeer', offset_date: Optional[datetime], offset_user: 'TypeInputUser', limit: int, requested: Optional[bool]=None, link: Optional[str]=None, q: Optional[str]=None):
        """
        :returns messages.ChatInviteImporters: Instance of ChatInviteImporters.
        """
        self.peer = peer
        self.offset_date = offset_date
        self.offset_user = offset_user
        self.limit = limit
        self.requested = requested
        self.link = link
        self.q = q

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.offset_user = utils.get_input_user(await client.get_input_entity(self.offset_user))

    def to_dict(self):
        return {
            '_': 'GetChatInviteImportersRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'offset_date': self.offset_date,
            'offset_user': self.offset_user.to_dict() if isinstance(self.offset_user, TLObject) else self.offset_user,
            'limit': self.limit,
            'requested': self.requested,
            'link': self.link,
            'q': self.q
        }

    def _bytes(self):
        return b''.join((
            b'N\xdd\x04\xdf',
            struct.pack('<I', (0 if self.requested is None or self.requested is False else 1) | (0 if self.link is None or self.link is False else 2) | (0 if self.q is None or self.q is False else 4)),
            self.peer._bytes(),
            b'' if self.link is None or self.link is False else (self.serialize_bytes(self.link)),
            b'' if self.q is None or self.q is False else (self.serialize_bytes(self.q)),
            self.serialize_datetime(self.offset_date),
            self.offset_user._bytes(),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _requested = bool(flags & 1)
        _peer = reader.tgread_object()
        if flags & 2:
            _link = reader.tgread_string()
        else:
            _link = None
        if flags & 4:
            _q = reader.tgread_string()
        else:
            _q = None
        _offset_date = reader.tgread_date()
        _offset_user = reader.tgread_object()
        _limit = reader.read_int()
        return cls(peer=_peer, offset_date=_offset_date, offset_user=_offset_user, limit=_limit, requested=_requested, link=_link, q=_q)


class GetChatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x49e9528f
    SUBCLASS_OF_ID = 0x99d5cb14

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List[int]):
        """
        :returns messages.Chats: Instance of either Chats, ChatsSlice.
        """
        self.id = id

    def to_dict(self):
        return {
            '_': 'GetChatsRequest',
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x8fR\xe9I',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<q', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _id.append(_x)

        return cls(id=_id)


class GetCommonChatsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe40ca104
    SUBCLASS_OF_ID = 0x99d5cb14

    def __init__(self, user_id: 'TypeInputUser', max_id: int, limit: int):
        """
        :returns messages.Chats: Instance of either Chats, ChatsSlice.
        """
        self.user_id = user_id
        self.max_id = max_id
        self.limit = limit

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'GetCommonChatsRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'max_id': self.max_id,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\x04\xa1\x0c\xe4',
            self.user_id._bytes(),
            struct.pack('<q', self.max_id),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _user_id = reader.tgread_object()
        _max_id = reader.read_long()
        _limit = reader.read_int()
        return cls(user_id=_user_id, max_id=_max_id, limit=_limit)


class GetCustomEmojiDocumentsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd9ab0f54
    SUBCLASS_OF_ID = 0xcc590e08

    def __init__(self, document_id: List[int]):
        """
        :returns Vector<Document>: This type has no constructors.
        """
        self.document_id = document_id

    def to_dict(self):
        return {
            '_': 'GetCustomEmojiDocumentsRequest',
            'document_id': [] if self.document_id is None else self.document_id[:]
        }

    def _bytes(self):
        return b''.join((
            b'T\x0f\xab\xd9',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.document_id)),b''.join(struct.pack('<q', x) for x in self.document_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _document_id = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _document_id.append(_x)

        return cls(document_id=_document_id)


class GetDefaultHistoryTTLRequest(TLRequest):
    CONSTRUCTOR_ID = 0x658b7188
    SUBCLASS_OF_ID = 0xf00d3367

    def to_dict(self):
        return {
            '_': 'GetDefaultHistoryTTLRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\x88q\x8be',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetDhConfigRequest(TLRequest):
    CONSTRUCTOR_ID = 0x26cf8950
    SUBCLASS_OF_ID = 0xe488ed8b

    def __init__(self, version: int, random_length: int):
        """
        :returns messages.DhConfig: Instance of either DhConfigNotModified, DhConfig.
        """
        self.version = version
        self.random_length = random_length

    def to_dict(self):
        return {
            '_': 'GetDhConfigRequest',
            'version': self.version,
            'random_length': self.random_length
        }

    def _bytes(self):
        return b''.join((
            b'P\x89\xcf&',
            struct.pack('<i', self.version),
            struct.pack('<i', self.random_length),
        ))

    @classmethod
    def from_reader(cls, reader):
        _version = reader.read_int()
        _random_length = reader.read_int()
        return cls(version=_version, random_length=_random_length)


class GetDialogFiltersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf19ed96d
    SUBCLASS_OF_ID = 0x601ce94d

    def to_dict(self):
        return {
            '_': 'GetDialogFiltersRequest'
        }

    def _bytes(self):
        return b''.join((
            b'm\xd9\x9e\xf1',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetDialogUnreadMarksRequest(TLRequest):
    CONSTRUCTOR_ID = 0x22e24e22
    SUBCLASS_OF_ID = 0xbec64ad9

    def to_dict(self):
        return {
            '_': 'GetDialogUnreadMarksRequest'
        }

    def _bytes(self):
        return b''.join((
            b'"N\xe2"',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetDialogsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa0f4cb4f
    SUBCLASS_OF_ID = 0xe1b52ee

    # noinspection PyShadowingBuiltins
    def __init__(self, offset_date: Optional[datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool]=None, folder_id: Optional[int]=None):
        """
        :returns messages.Dialogs: Instance of either Dialogs, DialogsSlice, DialogsNotModified.
        """
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_peer = offset_peer
        self.limit = limit
        self.hash = hash
        self.exclude_pinned = exclude_pinned
        self.folder_id = folder_id

    async def resolve(self, client, utils):
        self.offset_peer = utils.get_input_peer(await client.get_input_entity(self.offset_peer))

    def to_dict(self):
        return {
            '_': 'GetDialogsRequest',
            'offset_date': self.offset_date,
            'offset_id': self.offset_id,
            'offset_peer': self.offset_peer.to_dict() if isinstance(self.offset_peer, TLObject) else self.offset_peer,
            'limit': self.limit,
            'hash': self.hash,
            'exclude_pinned': self.exclude_pinned,
            'folder_id': self.folder_id
        }

    def _bytes(self):
        return b''.join((
            b'O\xcb\xf4\xa0',
            struct.pack('<I', (0 if self.exclude_pinned is None or self.exclude_pinned is False else 1) | (0 if self.folder_id is None or self.folder_id is False else 2)),
            b'' if self.folder_id is None or self.folder_id is False else (struct.pack('<i', self.folder_id)),
            self.serialize_datetime(self.offset_date),
            struct.pack('<i', self.offset_id),
            self.offset_peer._bytes(),
            struct.pack('<i', self.limit),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _exclude_pinned = bool(flags & 1)
        if flags & 2:
            _folder_id = reader.read_int()
        else:
            _folder_id = None
        _offset_date = reader.tgread_date()
        _offset_id = reader.read_int()
        _offset_peer = reader.tgread_object()
        _limit = reader.read_int()
        _hash = reader.read_long()
        return cls(offset_date=_offset_date, offset_id=_offset_id, offset_peer=_offset_peer, limit=_limit, hash=_hash, exclude_pinned=_exclude_pinned, folder_id=_folder_id)


class GetDiscussionMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0x446972fd
    SUBCLASS_OF_ID = 0x53f8e3e8

    def __init__(self, peer: 'TypeInputPeer', msg_id: int):
        """
        :returns messages.DiscussionMessage: Instance of DiscussionMessage.
        """
        self.peer = peer
        self.msg_id = msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetDiscussionMessageRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id
        }

    def _bytes(self):
        return b''.join((
            b'\xfdriD',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        return cls(peer=_peer, msg_id=_msg_id)


class GetDocumentByHashRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb1f2061f
    SUBCLASS_OF_ID = 0x211fe820

    def __init__(self, sha256: bytes, size: int, mime_type: str):
        """
        :returns Document: Instance of either DocumentEmpty, Document.
        """
        self.sha256 = sha256
        self.size = size
        self.mime_type = mime_type

    def to_dict(self):
        return {
            '_': 'GetDocumentByHashRequest',
            'sha256': self.sha256,
            'size': self.size,
            'mime_type': self.mime_type
        }

    def _bytes(self):
        return b''.join((
            b'\x1f\x06\xf2\xb1',
            self.serialize_bytes(self.sha256),
            struct.pack('<q', self.size),
            self.serialize_bytes(self.mime_type),
        ))

    @classmethod
    def from_reader(cls, reader):
        _sha256 = reader.tgread_bytes()
        _size = reader.read_long()
        _mime_type = reader.tgread_string()
        return cls(sha256=_sha256, size=_size, mime_type=_mime_type)


class GetEmojiGroupsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7488ce5b
    SUBCLASS_OF_ID = 0x7eca55d9

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.EmojiGroups: Instance of either EmojiGroupsNotModified, EmojiGroups.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetEmojiGroupsRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'[\xce\x88t',
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_int()
        return cls(hash=_hash)


class GetEmojiKeywordsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x35a0e062
    SUBCLASS_OF_ID = 0xd279c672

    def __init__(self, lang_code: str):
        """
        :returns EmojiKeywordsDifference: Instance of EmojiKeywordsDifference.
        """
        self.lang_code = lang_code

    def to_dict(self):
        return {
            '_': 'GetEmojiKeywordsRequest',
            'lang_code': self.lang_code
        }

    def _bytes(self):
        return b''.join((
            b'b\xe0\xa05',
            self.serialize_bytes(self.lang_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _lang_code = reader.tgread_string()
        return cls(lang_code=_lang_code)


class GetEmojiKeywordsDifferenceRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1508b6af
    SUBCLASS_OF_ID = 0xd279c672

    def __init__(self, lang_code: str, from_version: int):
        """
        :returns EmojiKeywordsDifference: Instance of EmojiKeywordsDifference.
        """
        self.lang_code = lang_code
        self.from_version = from_version

    def to_dict(self):
        return {
            '_': 'GetEmojiKeywordsDifferenceRequest',
            'lang_code': self.lang_code,
            'from_version': self.from_version
        }

    def _bytes(self):
        return b''.join((
            b'\xaf\xb6\x08\x15',
            self.serialize_bytes(self.lang_code),
            struct.pack('<i', self.from_version),
        ))

    @classmethod
    def from_reader(cls, reader):
        _lang_code = reader.tgread_string()
        _from_version = reader.read_int()
        return cls(lang_code=_lang_code, from_version=_from_version)


class GetEmojiKeywordsLanguagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4e9963b2
    SUBCLASS_OF_ID = 0xe795d387

    def __init__(self, lang_codes: List[str]):
        """
        :returns Vector<EmojiLanguage>: This type has no constructors.
        """
        self.lang_codes = lang_codes

    def to_dict(self):
        return {
            '_': 'GetEmojiKeywordsLanguagesRequest',
            'lang_codes': [] if self.lang_codes is None else self.lang_codes[:]
        }

    def _bytes(self):
        return b''.join((
            b'\xb2c\x99N',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.lang_codes)),b''.join(self.serialize_bytes(x) for x in self.lang_codes),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _lang_codes = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_string()
            _lang_codes.append(_x)

        return cls(lang_codes=_lang_codes)


class GetEmojiProfilePhotoGroupsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x21a548f3
    SUBCLASS_OF_ID = 0x7eca55d9

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.EmojiGroups: Instance of either EmojiGroupsNotModified, EmojiGroups.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetEmojiProfilePhotoGroupsRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xf3H\xa5!',
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_int()
        return cls(hash=_hash)


class GetEmojiStatusGroupsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2ecd56cd
    SUBCLASS_OF_ID = 0x7eca55d9

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.EmojiGroups: Instance of either EmojiGroupsNotModified, EmojiGroups.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetEmojiStatusGroupsRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xcdV\xcd.',
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_int()
        return cls(hash=_hash)


class GetEmojiStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xfbfca18f
    SUBCLASS_OF_ID = 0x45834829

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.AllStickers: Instance of either AllStickersNotModified, AllStickers.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetEmojiStickersRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\x8f\xa1\xfc\xfb',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetEmojiURLRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd5b10c26
    SUBCLASS_OF_ID = 0x1fa08a19

    def __init__(self, lang_code: str):
        """
        :returns EmojiURL: Instance of EmojiURL.
        """
        self.lang_code = lang_code

    def to_dict(self):
        return {
            '_': 'GetEmojiURLRequest',
            'lang_code': self.lang_code
        }

    def _bytes(self):
        return b''.join((
            b'&\x0c\xb1\xd5',
            self.serialize_bytes(self.lang_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _lang_code = reader.tgread_string()
        return cls(lang_code=_lang_code)


class GetExportedChatInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0x73746f5c
    SUBCLASS_OF_ID = 0x82dcd4ca

    def __init__(self, peer: 'TypeInputPeer', link: str):
        """
        :returns messages.ExportedChatInvite: Instance of either ExportedChatInvite, ExportedChatInviteReplaced.
        """
        self.peer = peer
        self.link = link

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetExportedChatInviteRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'link': self.link
        }

    def _bytes(self):
        return b''.join((
            b'\\ots',
            self.peer._bytes(),
            self.serialize_bytes(self.link),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _link = reader.tgread_string()
        return cls(peer=_peer, link=_link)


class GetExportedChatInvitesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa2b5a3f6
    SUBCLASS_OF_ID = 0x603d3871

    def __init__(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser', limit: int, revoked: Optional[bool]=None, offset_date: Optional[datetime]=None, offset_link: Optional[str]=None):
        """
        :returns messages.ExportedChatInvites: Instance of ExportedChatInvites.
        """
        self.peer = peer
        self.admin_id = admin_id
        self.limit = limit
        self.revoked = revoked
        self.offset_date = offset_date
        self.offset_link = offset_link

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.admin_id = utils.get_input_user(await client.get_input_entity(self.admin_id))

    def to_dict(self):
        return {
            '_': 'GetExportedChatInvitesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'admin_id': self.admin_id.to_dict() if isinstance(self.admin_id, TLObject) else self.admin_id,
            'limit': self.limit,
            'revoked': self.revoked,
            'offset_date': self.offset_date,
            'offset_link': self.offset_link
        }

    def _bytes(self):
        assert ((self.offset_date or self.offset_date is not None) and (self.offset_link or self.offset_link is not None)) or ((self.offset_date is None or self.offset_date is False) and (self.offset_link is None or self.offset_link is False)), 'offset_date, offset_link parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\xf6\xa3\xb5\xa2',
            struct.pack('<I', (0 if self.revoked is None or self.revoked is False else 8) | (0 if self.offset_date is None or self.offset_date is False else 4) | (0 if self.offset_link is None or self.offset_link is False else 4)),
            self.peer._bytes(),
            self.admin_id._bytes(),
            b'' if self.offset_date is None or self.offset_date is False else (self.serialize_datetime(self.offset_date)),
            b'' if self.offset_link is None or self.offset_link is False else (self.serialize_bytes(self.offset_link)),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _revoked = bool(flags & 8)
        _peer = reader.tgread_object()
        _admin_id = reader.tgread_object()
        if flags & 4:
            _offset_date = reader.tgread_date()
        else:
            _offset_date = None
        if flags & 4:
            _offset_link = reader.tgread_string()
        else:
            _offset_link = None
        _limit = reader.read_int()
        return cls(peer=_peer, admin_id=_admin_id, limit=_limit, revoked=_revoked, offset_date=_offset_date, offset_link=_offset_link)


class GetExtendedMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x84f80814
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int]):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetExtendedMediaRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x14\x08\xf8\x84',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(peer=_peer, id=_id)


class GetFavedStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4f1aaa9
    SUBCLASS_OF_ID = 0x8e736fb9

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.FavedStickers: Instance of either FavedStickersNotModified, FavedStickers.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetFavedStickersRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xa9\xaa\xf1\x04',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetFeaturedEmojiStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xecf6736
    SUBCLASS_OF_ID = 0x2614b722

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.FeaturedStickers: Instance of either FeaturedStickersNotModified, FeaturedStickers.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetFeaturedEmojiStickersRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'6g\xcf\x0e',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetFeaturedStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x64780b14
    SUBCLASS_OF_ID = 0x2614b722

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.FeaturedStickers: Instance of either FeaturedStickersNotModified, FeaturedStickers.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetFeaturedStickersRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\x14\x0bxd',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetFullChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0xaeb00b34
    SUBCLASS_OF_ID = 0x225a5109

    def __init__(self, chat_id: int):
        """
        :returns messages.ChatFull: Instance of ChatFull.
        """
        self.chat_id = chat_id

    def to_dict(self):
        return {
            '_': 'GetFullChatRequest',
            'chat_id': self.chat_id
        }

    def _bytes(self):
        return b''.join((
            b'4\x0b\xb0\xae',
            struct.pack('<q', self.chat_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        return cls(chat_id=_chat_id)


class GetGameHighScoresRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe822649d
    SUBCLASS_OF_ID = 0x6ccd95fd

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser'):
        """
        :returns messages.HighScores: Instance of HighScores.
        """
        self.peer = peer
        self.id = id
        self.user_id = user_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'GetGameHighScoresRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id
        }

    def _bytes(self):
        return b''.join((
            b'\x9dd"\xe8',
            self.peer._bytes(),
            struct.pack('<i', self.id),
            self.user_id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _id = reader.read_int()
        _user_id = reader.tgread_object()
        return cls(peer=_peer, id=_id, user_id=_user_id)


class GetHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4423e6c5
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetHistoryRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'offset_id': self.offset_id,
            'offset_date': self.offset_date,
            'add_offset': self.add_offset,
            'limit': self.limit,
            'max_id': self.max_id,
            'min_id': self.min_id,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xc5\xe6#D',
            self.peer._bytes(),
            struct.pack('<i', self.offset_id),
            self.serialize_datetime(self.offset_date),
            struct.pack('<i', self.add_offset),
            struct.pack('<i', self.limit),
            struct.pack('<i', self.max_id),
            struct.pack('<i', self.min_id),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _offset_id = reader.read_int()
        _offset_date = reader.tgread_date()
        _add_offset = reader.read_int()
        _limit = reader.read_int()
        _max_id = reader.read_int()
        _min_id = reader.read_int()
        _hash = reader.read_long()
        return cls(peer=_peer, offset_id=_offset_id, offset_date=_offset_date, add_offset=_add_offset, limit=_limit, max_id=_max_id, min_id=_min_id, hash=_hash)


class GetInlineBotResultsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x514e999d
    SUBCLASS_OF_ID = 0x3ed4d9c9

    def __init__(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', query: str, offset: str, geo_point: Optional['TypeInputGeoPoint']=None):
        """
        :returns messages.BotResults: Instance of BotResults.
        """
        self.bot = bot
        self.peer = peer
        self.query = query
        self.offset = offset
        self.geo_point = geo_point

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetInlineBotResultsRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'query': self.query,
            'offset': self.offset,
            'geo_point': self.geo_point.to_dict() if isinstance(self.geo_point, TLObject) else self.geo_point
        }

    def _bytes(self):
        return b''.join((
            b'\x9d\x99NQ',
            struct.pack('<I', (0 if self.geo_point is None or self.geo_point is False else 1)),
            self.bot._bytes(),
            self.peer._bytes(),
            b'' if self.geo_point is None or self.geo_point is False else (self.geo_point._bytes()),
            self.serialize_bytes(self.query),
            self.serialize_bytes(self.offset),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _bot = reader.tgread_object()
        _peer = reader.tgread_object()
        if flags & 1:
            _geo_point = reader.tgread_object()
        else:
            _geo_point = None
        _query = reader.tgread_string()
        _offset = reader.tgread_string()
        return cls(bot=_bot, peer=_peer, query=_query, offset=_offset, geo_point=_geo_point)


class GetInlineGameHighScoresRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf635e1b
    SUBCLASS_OF_ID = 0x6ccd95fd

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser'):
        """
        :returns messages.HighScores: Instance of HighScores.
        """
        self.id = id
        self.user_id = user_id

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'GetInlineGameHighScoresRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id
        }

    def _bytes(self):
        return b''.join((
            b'\x1b^c\x0f',
            self.id._bytes(),
            self.user_id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.tgread_object()
        _user_id = reader.tgread_object()
        return cls(id=_id, user_id=_user_id)


class GetMaskStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x640f82b8
    SUBCLASS_OF_ID = 0x45834829

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.AllStickers: Instance of either AllStickersNotModified, AllStickers.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetMaskStickersRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xb8\x82\x0fd',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetMessageEditDataRequest(TLRequest):
    CONSTRUCTOR_ID = 0xfda68d36
    SUBCLASS_OF_ID = 0xfb47949d

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int):
        """
        :returns messages.MessageEditData: Instance of MessageEditData.
        """
        self.peer = peer
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetMessageEditDataRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id
        }

    def _bytes(self):
        return b''.join((
            b'6\x8d\xa6\xfd',
            self.peer._bytes(),
            struct.pack('<i', self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _id = reader.read_int()
        return cls(peer=_peer, id=_id)


class GetMessageReactionsListRequest(TLRequest):
    CONSTRUCTOR_ID = 0x461b3f48
    SUBCLASS_OF_ID = 0x60fce5e6

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, limit: int, reaction: Optional['TypeReaction']=None, offset: Optional[str]=None):
        """
        :returns messages.MessageReactionsList: Instance of MessageReactionsList.
        """
        self.peer = peer
        self.id = id
        self.limit = limit
        self.reaction = reaction
        self.offset = offset

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetMessageReactionsListRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'limit': self.limit,
            'reaction': self.reaction.to_dict() if isinstance(self.reaction, TLObject) else self.reaction,
            'offset': self.offset
        }

    def _bytes(self):
        return b''.join((
            b'H?\x1bF',
            struct.pack('<I', (0 if self.reaction is None or self.reaction is False else 1) | (0 if self.offset is None or self.offset is False else 2)),
            self.peer._bytes(),
            struct.pack('<i', self.id),
            b'' if self.reaction is None or self.reaction is False else (self.reaction._bytes()),
            b'' if self.offset is None or self.offset is False else (self.serialize_bytes(self.offset)),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        _id = reader.read_int()
        if flags & 1:
            _reaction = reader.tgread_object()
        else:
            _reaction = None
        if flags & 2:
            _offset = reader.tgread_string()
        else:
            _offset = None
        _limit = reader.read_int()
        return cls(peer=_peer, id=_id, limit=_limit, reaction=_reaction, offset=_offset)


class GetMessageReadParticipantsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x31c1c44f
    SUBCLASS_OF_ID = 0x21ca455b

    def __init__(self, peer: 'TypeInputPeer', msg_id: int):
        """
        :returns Vector<ReadParticipantDate>: This type has no constructors.
        """
        self.peer = peer
        self.msg_id = msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetMessageReadParticipantsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id
        }

    def _bytes(self):
        return b''.join((
            b'O\xc4\xc11',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        return cls(peer=_peer, msg_id=_msg_id)


class GetMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x63c66506
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List['TypeInputMessage']):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.id = id

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.id:
            _tmp.append(utils.get_input_message(_x))

        self.id = _tmp

    def to_dict(self):
        return {
            '_': 'GetMessagesRequest',
            'id': [] if self.id is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.id]
        }

    def _bytes(self):
        return b''.join((
            b'\x06e\xc6c',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(x._bytes() for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _id.append(_x)

        return cls(id=_id)


class GetMessagesReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8bba90e6
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int]):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetMessagesReactionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'\xe6\x90\xba\x8b',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(peer=_peer, id=_id)


class GetMessagesViewsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5784d3e1
    SUBCLASS_OF_ID = 0xafb5eb9c

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int], increment: bool):
        """
        :returns messages.MessageViews: Instance of MessageViews.
        """
        self.peer = peer
        self.id = id
        self.increment = increment

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetMessagesViewsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:],
            'increment': self.increment
        }

    def _bytes(self):
        return b''.join((
            b'\xe1\xd3\x84W',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
            b'\xb5ur\x99' if self.increment else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        _increment = reader.tgread_bool()
        return cls(peer=_peer, id=_id, increment=_increment)


class GetOldFeaturedStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7ed094a1
    SUBCLASS_OF_ID = 0x2614b722

    # noinspection PyShadowingBuiltins
    def __init__(self, offset: int, limit: int, hash: int):
        """
        :returns messages.FeaturedStickers: Instance of either FeaturedStickersNotModified, FeaturedStickers.
        """
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetOldFeaturedStickersRequest',
            'offset': self.offset,
            'limit': self.limit,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xa1\x94\xd0~',
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _offset = reader.read_int()
        _limit = reader.read_int()
        _hash = reader.read_long()
        return cls(offset=_offset, limit=_limit, hash=_hash)


class GetOnlinesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x6e2be050
    SUBCLASS_OF_ID = 0x8c81903a

    def __init__(self, peer: 'TypeInputPeer'):
        """
        :returns ChatOnlines: Instance of ChatOnlines.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetOnlinesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'P\xe0+n',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class GetPeerDialogsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe470bcfd
    SUBCLASS_OF_ID = 0x3ac70132

    def __init__(self, peers: List['TypeInputDialogPeer']):
        """
        :returns messages.PeerDialogs: Instance of PeerDialogs.
        """
        self.peers = peers

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.peers:
            _tmp.append(await client._get_input_dialog(_x))

        self.peers = _tmp

    def to_dict(self):
        return {
            '_': 'GetPeerDialogsRequest',
            'peers': [] if self.peers is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.peers]
        }

    def _bytes(self):
        return b''.join((
            b'\xfd\xbcp\xe4',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.peers)),b''.join(x._bytes() for x in self.peers),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _peers = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _peers.append(_x)

        return cls(peers=_peers)


class GetPeerSettingsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xefd9a6a2
    SUBCLASS_OF_ID = 0x65a2f7a1

    def __init__(self, peer: 'TypeInputPeer'):
        """
        :returns messages.PeerSettings: Instance of PeerSettings.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetPeerSettingsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'\xa2\xa6\xd9\xef',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class GetPinnedDialogsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd6b94df2
    SUBCLASS_OF_ID = 0x3ac70132

    def __init__(self, folder_id: int):
        """
        :returns messages.PeerDialogs: Instance of PeerDialogs.
        """
        self.folder_id = folder_id

    def to_dict(self):
        return {
            '_': 'GetPinnedDialogsRequest',
            'folder_id': self.folder_id
        }

    def _bytes(self):
        return b''.join((
            b'\xf2M\xb9\xd6',
            struct.pack('<i', self.folder_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _folder_id = reader.read_int()
        return cls(folder_id=_folder_id)


class GetPollResultsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x73bb643b
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', msg_id: int):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.msg_id = msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetPollResultsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id
        }

    def _bytes(self):
        return b''.join((
            b';d\xbbs',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        return cls(peer=_peer, msg_id=_msg_id)


class GetPollVotesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb86e380e
    SUBCLASS_OF_ID = 0xc2199885

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, limit: int, option: Optional[bytes]=None, offset: Optional[str]=None):
        """
        :returns messages.VotesList: Instance of VotesList.
        """
        self.peer = peer
        self.id = id
        self.limit = limit
        self.option = option
        self.offset = offset

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetPollVotesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'limit': self.limit,
            'option': self.option,
            'offset': self.offset
        }

    def _bytes(self):
        return b''.join((
            b'\x0e8n\xb8',
            struct.pack('<I', (0 if self.option is None or self.option is False else 1) | (0 if self.offset is None or self.offset is False else 2)),
            self.peer._bytes(),
            struct.pack('<i', self.id),
            b'' if self.option is None or self.option is False else (self.serialize_bytes(self.option)),
            b'' if self.offset is None or self.offset is False else (self.serialize_bytes(self.offset)),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        _id = reader.read_int()
        if flags & 1:
            _option = reader.tgread_bytes()
        else:
            _option = None
        if flags & 2:
            _offset = reader.tgread_string()
        else:
            _offset = None
        _limit = reader.read_int()
        return cls(peer=_peer, id=_id, limit=_limit, option=_option, offset=_offset)


class GetRecentLocationsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x702a40e0
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', limit: int, hash: int):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.limit = limit
        self.hash = hash

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetRecentLocationsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'limit': self.limit,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xe0@*p',
            self.peer._bytes(),
            struct.pack('<i', self.limit),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _limit = reader.read_int()
        _hash = reader.read_long()
        return cls(peer=_peer, limit=_limit, hash=_hash)


class GetRecentReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x39461db2
    SUBCLASS_OF_ID = 0xadc38324

    # noinspection PyShadowingBuiltins
    def __init__(self, limit: int, hash: int):
        """
        :returns messages.Reactions: Instance of either ReactionsNotModified, Reactions.
        """
        self.limit = limit
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetRecentReactionsRequest',
            'limit': self.limit,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xb2\x1dF9',
            struct.pack('<i', self.limit),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _limit = reader.read_int()
        _hash = reader.read_long()
        return cls(limit=_limit, hash=_hash)


class GetRecentStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9da9403b
    SUBCLASS_OF_ID = 0xf76f8683

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int, attached: Optional[bool]=None):
        """
        :returns messages.RecentStickers: Instance of either RecentStickersNotModified, RecentStickers.
        """
        self.hash = hash
        self.attached = attached

    def to_dict(self):
        return {
            '_': 'GetRecentStickersRequest',
            'hash': self.hash,
            'attached': self.attached
        }

    def _bytes(self):
        return b''.join((
            b';@\xa9\x9d',
            struct.pack('<I', (0 if self.attached is None or self.attached is False else 1)),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _attached = bool(flags & 1)
        _hash = reader.read_long()
        return cls(hash=_hash, attached=_attached)


class GetRepliesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x22ddd30c
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', msg_id: int, offset_id: int, offset_date: Optional[datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetRepliesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'offset_id': self.offset_id,
            'offset_date': self.offset_date,
            'add_offset': self.add_offset,
            'limit': self.limit,
            'max_id': self.max_id,
            'min_id': self.min_id,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\x0c\xd3\xdd"',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            struct.pack('<i', self.offset_id),
            self.serialize_datetime(self.offset_date),
            struct.pack('<i', self.add_offset),
            struct.pack('<i', self.limit),
            struct.pack('<i', self.max_id),
            struct.pack('<i', self.min_id),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        _offset_id = reader.read_int()
        _offset_date = reader.tgread_date()
        _add_offset = reader.read_int()
        _limit = reader.read_int()
        _max_id = reader.read_int()
        _min_id = reader.read_int()
        _hash = reader.read_long()
        return cls(peer=_peer, msg_id=_msg_id, offset_id=_offset_id, offset_date=_offset_date, add_offset=_add_offset, limit=_limit, max_id=_max_id, min_id=_min_id, hash=_hash)


class GetSavedGifsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5cf09635
    SUBCLASS_OF_ID = 0xa68b61f5

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: int):
        """
        :returns messages.SavedGifs: Instance of either SavedGifsNotModified, SavedGifs.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetSavedGifsRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'5\x96\xf0\\',
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.read_long()
        return cls(hash=_hash)


class GetScheduledHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf516760b
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', hash: int):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.hash = hash

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetScheduledHistoryRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\x0bv\x16\xf5',
            self.peer._bytes(),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _hash = reader.read_long()
        return cls(peer=_peer, hash=_hash)


class GetScheduledMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xbdbb0464
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int]):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetScheduledMessagesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'd\x04\xbb\xbd',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(peer=_peer, id=_id)


class GetSearchCountersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xae7cc1
    SUBCLASS_OF_ID = 0x6bde3c6e

    def __init__(self, peer: 'TypeInputPeer', filters: List['TypeMessagesFilter'], top_msg_id: Optional[int]=None):
        """
        :returns Vector<messages.SearchCounter>: This type has no constructors.
        """
        self.peer = peer
        self.filters = filters
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetSearchCountersRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'filters': [] if self.filters is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.filters],
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'\xc1|\xae\x00',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.filters)),b''.join(x._bytes() for x in self.filters),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        reader.read_int()
        _filters = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _filters.append(_x)

        return cls(peer=_peer, filters=_filters, top_msg_id=_top_msg_id)


class GetSearchResultsCalendarRequest(TLRequest):
    CONSTRUCTOR_ID = 0x49f0bde9
    SUBCLASS_OF_ID = 0x92c5640f

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, offset_date: Optional[datetime]):
        """
        :returns messages.SearchResultsCalendar: Instance of SearchResultsCalendar.
        """
        self.peer = peer
        self.filter = filter
        self.offset_id = offset_id
        self.offset_date = offset_date

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetSearchResultsCalendarRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'filter': self.filter.to_dict() if isinstance(self.filter, TLObject) else self.filter,
            'offset_id': self.offset_id,
            'offset_date': self.offset_date
        }

    def _bytes(self):
        return b''.join((
            b'\xe9\xbd\xf0I',
            self.peer._bytes(),
            self.filter._bytes(),
            struct.pack('<i', self.offset_id),
            self.serialize_datetime(self.offset_date),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _filter = reader.tgread_object()
        _offset_id = reader.read_int()
        _offset_date = reader.tgread_date()
        return cls(peer=_peer, filter=_filter, offset_id=_offset_id, offset_date=_offset_date)


class GetSearchResultsPositionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x6e9583a3
    SUBCLASS_OF_ID = 0xd963708d

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, limit: int):
        """
        :returns messages.SearchResultsPositions: Instance of SearchResultsPositions.
        """
        self.peer = peer
        self.filter = filter
        self.offset_id = offset_id
        self.limit = limit

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetSearchResultsPositionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'filter': self.filter.to_dict() if isinstance(self.filter, TLObject) else self.filter,
            'offset_id': self.offset_id,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\xa3\x83\x95n',
            self.peer._bytes(),
            self.filter._bytes(),
            struct.pack('<i', self.offset_id),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _filter = reader.tgread_object()
        _offset_id = reader.read_int()
        _limit = reader.read_int()
        return cls(peer=_peer, filter=_filter, offset_id=_offset_id, limit=_limit)


class GetSplitRangesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1cff7e08
    SUBCLASS_OF_ID = 0x5ba52504

    def to_dict(self):
        return {
            '_': 'GetSplitRangesRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\x08~\xff\x1c',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetStickerSetRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc8a0ec74
    SUBCLASS_OF_ID = 0x9b704a5a

    # noinspection PyShadowingBuiltins
    def __init__(self, stickerset: 'TypeInputStickerSet', hash: int):
        """
        :returns messages.StickerSet: Instance of either StickerSet, StickerSetNotModified.
        """
        self.stickerset = stickerset
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetStickerSetRequest',
            'stickerset': self.stickerset.to_dict() if isinstance(self.stickerset, TLObject) else self.stickerset,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b't\xec\xa0\xc8',
            self.stickerset._bytes(),
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _stickerset = reader.tgread_object()
        _hash = reader.read_int()
        return cls(stickerset=_stickerset, hash=_hash)


class GetStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd5a5d3a1
    SUBCLASS_OF_ID = 0xd73bb9de

    # noinspection PyShadowingBuiltins
    def __init__(self, emoticon: str, hash: int):
        """
        :returns messages.Stickers: Instance of either StickersNotModified, Stickers.
        """
        self.emoticon = emoticon
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetStickersRequest',
            'emoticon': self.emoticon,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xa1\xd3\xa5\xd5',
            self.serialize_bytes(self.emoticon),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _emoticon = reader.tgread_string()
        _hash = reader.read_long()
        return cls(emoticon=_emoticon, hash=_hash)


class GetSuggestedDialogFiltersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa29cd42c
    SUBCLASS_OF_ID = 0x7b296c39

    def to_dict(self):
        return {
            '_': 'GetSuggestedDialogFiltersRequest'
        }

    def _bytes(self):
        return b''.join((
            b',\xd4\x9c\xa2',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class GetTopReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xbb8125ba
    SUBCLASS_OF_ID = 0xadc38324

    # noinspection PyShadowingBuiltins
    def __init__(self, limit: int, hash: int):
        """
        :returns messages.Reactions: Instance of either ReactionsNotModified, Reactions.
        """
        self.limit = limit
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetTopReactionsRequest',
            'limit': self.limit,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xba%\x81\xbb',
            struct.pack('<i', self.limit),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _limit = reader.read_int()
        _hash = reader.read_long()
        return cls(limit=_limit, hash=_hash)


class GetUnreadMentionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf107e790
    SUBCLASS_OF_ID = 0xd4b40b5e

    def __init__(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int]=None):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetUnreadMentionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'offset_id': self.offset_id,
            'add_offset': self.add_offset,
            'limit': self.limit,
            'max_id': self.max_id,
            'min_id': self.min_id,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'\x90\xe7\x07\xf1',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
            struct.pack('<i', self.offset_id),
            struct.pack('<i', self.add_offset),
            struct.pack('<i', self.limit),
            struct.pack('<i', self.max_id),
            struct.pack('<i', self.min_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        _offset_id = reader.read_int()
        _add_offset = reader.read_int()
        _limit = reader.read_int()
        _max_id = reader.read_int()
        _min_id = reader.read_int()
        return cls(peer=_peer, offset_id=_offset_id, add_offset=_add_offset, limit=_limit, max_id=_max_id, min_id=_min_id, top_msg_id=_top_msg_id)


class GetUnreadReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3223495b
    SUBCLASS_OF_ID = 0xd4b40b5e

    def __init__(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int]=None):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'GetUnreadReactionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'offset_id': self.offset_id,
            'add_offset': self.add_offset,
            'limit': self.limit,
            'max_id': self.max_id,
            'min_id': self.min_id,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'[I#2',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
            struct.pack('<i', self.offset_id),
            struct.pack('<i', self.add_offset),
            struct.pack('<i', self.limit),
            struct.pack('<i', self.max_id),
            struct.pack('<i', self.min_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        _offset_id = reader.read_int()
        _add_offset = reader.read_int()
        _limit = reader.read_int()
        _max_id = reader.read_int()
        _min_id = reader.read_int()
        return cls(peer=_peer, offset_id=_offset_id, add_offset=_add_offset, limit=_limit, max_id=_max_id, min_id=_min_id, top_msg_id=_top_msg_id)


class GetWebPageRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8d9692a3
    SUBCLASS_OF_ID = 0x2cf8b154

    # noinspection PyShadowingBuiltins
    def __init__(self, url: str, hash: int):
        """
        :returns messages.WebPage: Instance of WebPage.
        """
        self.url = url
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetWebPageRequest',
            'url': self.url,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xa3\x92\x96\x8d',
            self.serialize_bytes(self.url),
            struct.pack('<i', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _url = reader.tgread_string()
        _hash = reader.read_int()
        return cls(url=_url, hash=_hash)


class GetWebPagePreviewRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8b68b0cc
    SUBCLASS_OF_ID = 0x476cbe32

    def __init__(self, message: str, entities: Optional[List['TypeMessageEntity']]=None):
        """
        :returns MessageMedia: Instance of either MessageMediaEmpty, MessageMediaPhoto, MessageMediaGeo, MessageMediaContact, MessageMediaUnsupported, MessageMediaDocument, MessageMediaWebPage, MessageMediaVenue, MessageMediaGame, MessageMediaInvoice, MessageMediaGeoLive, MessageMediaPoll, MessageMediaDice, MessageMediaStory, MessageMediaGiveaway.
        """
        self.message = message
        self.entities = entities

    def to_dict(self):
        return {
            '_': 'GetWebPagePreviewRequest',
            'message': self.message,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities]
        }

    def _bytes(self):
        return b''.join((
            b'\xcc\xb0h\x8b',
            struct.pack('<I', (0 if self.entities is None or self.entities is False else 8)),
            self.serialize_bytes(self.message),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities))),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _message = reader.tgread_string()
        if flags & 8:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        return cls(message=_message, entities=_entities)


class HideAllChatJoinRequestsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe085f4ea
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', approved: Optional[bool]=None, link: Optional[str]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.approved = approved
        self.link = link

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'HideAllChatJoinRequestsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'approved': self.approved,
            'link': self.link
        }

    def _bytes(self):
        return b''.join((
            b'\xea\xf4\x85\xe0',
            struct.pack('<I', (0 if self.approved is None or self.approved is False else 1) | (0 if self.link is None or self.link is False else 2)),
            self.peer._bytes(),
            b'' if self.link is None or self.link is False else (self.serialize_bytes(self.link)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _approved = bool(flags & 1)
        _peer = reader.tgread_object()
        if flags & 2:
            _link = reader.tgread_string()
        else:
            _link = None
        return cls(peer=_peer, approved=_approved, link=_link)


class HideChatJoinRequestRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7fe7e815
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', approved: Optional[bool]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.user_id = user_id
        self.approved = approved

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'HideChatJoinRequestRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'approved': self.approved
        }

    def _bytes(self):
        return b''.join((
            b'\x15\xe8\xe7\x7f',
            struct.pack('<I', (0 if self.approved is None or self.approved is False else 1)),
            self.peer._bytes(),
            self.user_id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _approved = bool(flags & 1)
        _peer = reader.tgread_object()
        _user_id = reader.tgread_object()
        return cls(peer=_peer, user_id=_user_id, approved=_approved)


class HidePeerSettingsBarRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4facb138
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer'):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'HidePeerSettingsBarRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'8\xb1\xacO',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class ImportChatInviteRequest(TLRequest):
    CONSTRUCTOR_ID = 0x6c50051c
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, hash: str):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'ImportChatInviteRequest',
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\x1c\x05Pl',
            self.serialize_bytes(self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _hash = reader.tgread_string()
        return cls(hash=_hash)


class InitHistoryImportRequest(TLRequest):
    CONSTRUCTOR_ID = 0x34090c3b
    SUBCLASS_OF_ID = 0xb18bb50a

    def __init__(self, peer: 'TypeInputPeer', file: 'TypeInputFile', media_count: int):
        """
        :returns messages.HistoryImport: Instance of HistoryImport.
        """
        self.peer = peer
        self.file = file
        self.media_count = media_count

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'InitHistoryImportRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'file': self.file.to_dict() if isinstance(self.file, TLObject) else self.file,
            'media_count': self.media_count
        }

    def _bytes(self):
        return b''.join((
            b';\x0c\t4',
            self.peer._bytes(),
            self.file._bytes(),
            struct.pack('<i', self.media_count),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _file = reader.tgread_object()
        _media_count = reader.read_int()
        return cls(peer=_peer, file=_file, media_count=_media_count)


class InstallStickerSetRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc78fe460
    SUBCLASS_OF_ID = 0x67cb3fe8

    def __init__(self, stickerset: 'TypeInputStickerSet', archived: bool):
        """
        :returns messages.StickerSetInstallResult: Instance of either StickerSetInstallResultSuccess, StickerSetInstallResultArchive.
        """
        self.stickerset = stickerset
        self.archived = archived

    def to_dict(self):
        return {
            '_': 'InstallStickerSetRequest',
            'stickerset': self.stickerset.to_dict() if isinstance(self.stickerset, TLObject) else self.stickerset,
            'archived': self.archived
        }

    def _bytes(self):
        return b''.join((
            b'`\xe4\x8f\xc7',
            self.stickerset._bytes(),
            b'\xb5ur\x99' if self.archived else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _stickerset = reader.tgread_object()
        _archived = reader.tgread_bool()
        return cls(stickerset=_stickerset, archived=_archived)


class MarkDialogUnreadRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc286d98f
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputDialogPeer', unread: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.unread = unread

    async def resolve(self, client, utils):
        self.peer = await client._get_input_dialog(self.peer)

    def to_dict(self):
        return {
            '_': 'MarkDialogUnreadRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'unread': self.unread
        }

    def _bytes(self):
        return b''.join((
            b'\x8f\xd9\x86\xc2',
            struct.pack('<I', (0 if self.unread is None or self.unread is False else 1)),
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _unread = bool(flags & 1)
        _peer = reader.tgread_object()
        return cls(peer=_peer, unread=_unread)


class MigrateChatRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa2875319
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, chat_id: int):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.chat_id = chat_id

    def to_dict(self):
        return {
            '_': 'MigrateChatRequest',
            'chat_id': self.chat_id
        }

    def _bytes(self):
        return b''.join((
            b'\x19S\x87\xa2',
            struct.pack('<q', self.chat_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _chat_id = reader.read_long()
        return cls(chat_id=_chat_id)


class ProlongWebViewRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb0d81a83
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', query_id: int, silent: Optional[bool]=None, reply_to: Optional['TypeInputReplyTo']=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.bot = bot
        self.query_id = query_id
        self.silent = silent
        self.reply_to = reply_to
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'ProlongWebViewRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'query_id': self.query_id,
            'silent': self.silent,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'\x83\x1a\xd8\xb0',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 32) | (0 if self.reply_to is None or self.reply_to is False else 1) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.peer._bytes(),
            self.bot._bytes(),
            struct.pack('<q', self.query_id),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 32)
        _peer = reader.tgread_object()
        _bot = reader.tgread_object()
        _query_id = reader.read_long()
        if flags & 1:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(peer=_peer, bot=_bot, query_id=_query_id, silent=_silent, reply_to=_reply_to, send_as=_send_as)


class RateTranscribedAudioRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7f1d072f
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', msg_id: int, transcription_id: int, good: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.transcription_id = transcription_id
        self.good = good

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'RateTranscribedAudioRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'transcription_id': self.transcription_id,
            'good': self.good
        }

    def _bytes(self):
        return b''.join((
            b'/\x07\x1d\x7f',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            struct.pack('<q', self.transcription_id),
            b'\xb5ur\x99' if self.good else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        _transcription_id = reader.read_long()
        _good = reader.tgread_bool()
        return cls(peer=_peer, msg_id=_msg_id, transcription_id=_transcription_id, good=_good)


class ReadDiscussionRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf731a9f4
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', msg_id: int, read_max_id: int):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.read_max_id = read_max_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ReadDiscussionRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'read_max_id': self.read_max_id
        }

    def _bytes(self):
        return b''.join((
            b'\xf4\xa91\xf7',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            struct.pack('<i', self.read_max_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        _read_max_id = reader.read_int()
        return cls(peer=_peer, msg_id=_msg_id, read_max_id=_read_max_id)


class ReadEncryptedHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7f4b690a
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputEncryptedChat', max_date: Optional[datetime]):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.max_date = max_date

    def to_dict(self):
        return {
            '_': 'ReadEncryptedHistoryRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'max_date': self.max_date
        }

    def _bytes(self):
        return b''.join((
            b'\niK\x7f',
            self.peer._bytes(),
            self.serialize_datetime(self.max_date),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _max_date = reader.tgread_date()
        return cls(peer=_peer, max_date=_max_date)


class ReadFeaturedStickersRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5b118126
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List[int]):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id

    def to_dict(self):
        return {
            '_': 'ReadFeaturedStickersRequest',
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'&\x81\x11[',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<q', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _id.append(_x)

        return cls(id=_id)


class ReadHistoryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe306d3a
    SUBCLASS_OF_ID = 0xced3c06e

    def __init__(self, peer: 'TypeInputPeer', max_id: int):
        """
        :returns messages.AffectedMessages: Instance of AffectedMessages.
        """
        self.peer = peer
        self.max_id = max_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ReadHistoryRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'max_id': self.max_id
        }

    def _bytes(self):
        return b''.join((
            b':m0\x0e',
            self.peer._bytes(),
            struct.pack('<i', self.max_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _max_id = reader.read_int()
        return cls(peer=_peer, max_id=_max_id)


class ReadMentionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x36e5bf4d
    SUBCLASS_OF_ID = 0x2c49c116

    def __init__(self, peer: 'TypeInputPeer', top_msg_id: Optional[int]=None):
        """
        :returns messages.AffectedHistory: Instance of AffectedHistory.
        """
        self.peer = peer
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ReadMentionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'M\xbf\xe56',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        return cls(peer=_peer, top_msg_id=_top_msg_id)


class ReadMessageContentsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x36a73f77
    SUBCLASS_OF_ID = 0xced3c06e

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List[int]):
        """
        :returns messages.AffectedMessages: Instance of AffectedMessages.
        """
        self.id = id

    def to_dict(self):
        return {
            '_': 'ReadMessageContentsRequest',
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'w?\xa76',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(id=_id)


class ReadReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x54aa7f8e
    SUBCLASS_OF_ID = 0x2c49c116

    def __init__(self, peer: 'TypeInputPeer', top_msg_id: Optional[int]=None):
        """
        :returns messages.AffectedHistory: Instance of AffectedHistory.
        """
        self.peer = peer
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ReadReactionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'\x8e\x7f\xaaT',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        return cls(peer=_peer, top_msg_id=_top_msg_id)


class ReceivedMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5a954c0
    SUBCLASS_OF_ID = 0x8565f897

    def __init__(self, max_id: int):
        """
        :returns Vector<ReceivedNotifyMessage>: This type has no constructors.
        """
        self.max_id = max_id

    def to_dict(self):
        return {
            '_': 'ReceivedMessagesRequest',
            'max_id': self.max_id
        }

    def _bytes(self):
        return b''.join((
            b'\xc0T\xa9\x05',
            struct.pack('<i', self.max_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _max_id = reader.read_int()
        return cls(max_id=_max_id)


class ReceivedQueueRequest(TLRequest):
    CONSTRUCTOR_ID = 0x55a5bb66
    SUBCLASS_OF_ID = 0x8918e168

    def __init__(self, max_qts: int):
        """
        :returns Vector<long>: This type has no constructors.
        """
        self.max_qts = max_qts

    def to_dict(self):
        return {
            '_': 'ReceivedQueueRequest',
            'max_qts': self.max_qts
        }

    def _bytes(self):
        return b''.join((
            b'f\xbb\xa5U',
            struct.pack('<i', self.max_qts),
        ))

    @classmethod
    def from_reader(cls, reader):
        _max_qts = reader.read_int()
        return cls(max_qts=_max_qts)

    @staticmethod
    def read_result(reader):
        reader.read_int()  # Vector ID
        return [reader.read_long() for _ in range(reader.read_int())]


class ReorderPinnedDialogsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3b1adf37
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, folder_id: int, order: List['TypeInputDialogPeer'], force: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.folder_id = folder_id
        self.order = order
        self.force = force

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.order:
            _tmp.append(await client._get_input_dialog(_x))

        self.order = _tmp

    def to_dict(self):
        return {
            '_': 'ReorderPinnedDialogsRequest',
            'folder_id': self.folder_id,
            'order': [] if self.order is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.order],
            'force': self.force
        }

    def _bytes(self):
        return b''.join((
            b'7\xdf\x1a;',
            struct.pack('<I', (0 if self.force is None or self.force is False else 1)),
            struct.pack('<i', self.folder_id),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.order)),b''.join(x._bytes() for x in self.order),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _force = bool(flags & 1)
        _folder_id = reader.read_int()
        reader.read_int()
        _order = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _order.append(_x)

        return cls(folder_id=_folder_id, order=_order, force=_force)


class ReorderStickerSetsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x78337739
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, order: List[int], masks: Optional[bool]=None, emojis: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.order = order
        self.masks = masks
        self.emojis = emojis

    def to_dict(self):
        return {
            '_': 'ReorderStickerSetsRequest',
            'order': [] if self.order is None else self.order[:],
            'masks': self.masks,
            'emojis': self.emojis
        }

    def _bytes(self):
        return b''.join((
            b'9w3x',
            struct.pack('<I', (0 if self.masks is None or self.masks is False else 1) | (0 if self.emojis is None or self.emojis is False else 2)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.order)),b''.join(struct.pack('<q', x) for x in self.order),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _masks = bool(flags & 1)
        _emojis = bool(flags & 2)
        reader.read_int()
        _order = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _order.append(_x)

        return cls(order=_order, masks=_masks, emojis=_emojis)


class ReportRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8953ab4e
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int], reason: 'TypeReportReason', message: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.id = id
        self.reason = reason
        self.message = message

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ReportRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:],
            'reason': self.reason.to_dict() if isinstance(self.reason, TLObject) else self.reason,
            'message': self.message
        }

    def _bytes(self):
        return b''.join((
            b'N\xabS\x89',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
            self.reason._bytes(),
            self.serialize_bytes(self.message),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        _reason = reader.tgread_object()
        _message = reader.tgread_string()
        return cls(peer=_peer, id=_id, reason=_reason, message=_message)


class ReportEncryptedSpamRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4b0c8c0f
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputEncryptedChat'):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer

    def to_dict(self):
        return {
            '_': 'ReportEncryptedSpamRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'\x0f\x8c\x0cK',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class ReportReactionRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3f64c076
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, reaction_peer: 'TypeInputPeer'):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.id = id
        self.reaction_peer = reaction_peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.reaction_peer = utils.get_input_peer(await client.get_input_entity(self.reaction_peer))

    def to_dict(self):
        return {
            '_': 'ReportReactionRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'reaction_peer': self.reaction_peer.to_dict() if isinstance(self.reaction_peer, TLObject) else self.reaction_peer
        }

    def _bytes(self):
        return b''.join((
            b'v\xc0d?',
            self.peer._bytes(),
            struct.pack('<i', self.id),
            self.reaction_peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _id = reader.read_int()
        _reaction_peer = reader.tgread_object()
        return cls(peer=_peer, id=_id, reaction_peer=_reaction_peer)


class ReportSpamRequest(TLRequest):
    CONSTRUCTOR_ID = 0xcf1592db
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer'):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ReportSpamRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer
        }

    def _bytes(self):
        return b''.join((
            b'\xdb\x92\x15\xcf',
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        return cls(peer=_peer)


class RequestAppWebViewRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8c5a3b3c
    SUBCLASS_OF_ID = 0x1c24a413

    def __init__(self, peer: 'TypeInputPeer', app: 'TypeInputBotApp', platform: str, write_allowed: Optional[bool]=None, start_param: Optional[str]=None, theme_params: Optional['TypeDataJSON']=None):
        """
        :returns AppWebViewResult: Instance of AppWebViewResultUrl.
        """
        self.peer = peer
        self.app = app
        self.platform = platform
        self.write_allowed = write_allowed
        self.start_param = start_param
        self.theme_params = theme_params

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'RequestAppWebViewRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'app': self.app.to_dict() if isinstance(self.app, TLObject) else self.app,
            'platform': self.platform,
            'write_allowed': self.write_allowed,
            'start_param': self.start_param,
            'theme_params': self.theme_params.to_dict() if isinstance(self.theme_params, TLObject) else self.theme_params
        }

    def _bytes(self):
        return b''.join((
            b'<;Z\x8c',
            struct.pack('<I', (0 if self.write_allowed is None or self.write_allowed is False else 1) | (0 if self.start_param is None or self.start_param is False else 2) | (0 if self.theme_params is None or self.theme_params is False else 4)),
            self.peer._bytes(),
            self.app._bytes(),
            b'' if self.start_param is None or self.start_param is False else (self.serialize_bytes(self.start_param)),
            b'' if self.theme_params is None or self.theme_params is False else (self.theme_params._bytes()),
            self.serialize_bytes(self.platform),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _write_allowed = bool(flags & 1)
        _peer = reader.tgread_object()
        _app = reader.tgread_object()
        if flags & 2:
            _start_param = reader.tgread_string()
        else:
            _start_param = None
        if flags & 4:
            _theme_params = reader.tgread_object()
        else:
            _theme_params = None
        _platform = reader.tgread_string()
        return cls(peer=_peer, app=_app, platform=_platform, write_allowed=_write_allowed, start_param=_start_param, theme_params=_theme_params)


class RequestEncryptionRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf64daf43
    SUBCLASS_OF_ID = 0x6d28a37a

    def __init__(self, user_id: 'TypeInputUser', g_a: bytes, random_id: int=None):
        """
        :returns EncryptedChat: Instance of either EncryptedChatEmpty, EncryptedChatWaiting, EncryptedChatRequested, EncryptedChat, EncryptedChatDiscarded.
        """
        self.user_id = user_id
        self.g_a = g_a
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(4), 'big', signed=True)

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'RequestEncryptionRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'g_a': self.g_a,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'C\xafM\xf6',
            self.user_id._bytes(),
            struct.pack('<i', self.random_id),
            self.serialize_bytes(self.g_a),
        ))

    @classmethod
    def from_reader(cls, reader):
        _user_id = reader.tgread_object()
        _random_id = reader.read_int()
        _g_a = reader.tgread_bytes()
        return cls(user_id=_user_id, g_a=_g_a, random_id=_random_id)


class RequestSimpleWebViewRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1a46500a
    SUBCLASS_OF_ID = 0x15eee3db

    def __init__(self, bot: 'TypeInputUser', platform: str, from_switch_webview: Optional[bool]=None, from_side_menu: Optional[bool]=None, url: Optional[str]=None, start_param: Optional[str]=None, theme_params: Optional['TypeDataJSON']=None):
        """
        :returns SimpleWebViewResult: Instance of SimpleWebViewResultUrl.
        """
        self.bot = bot
        self.platform = platform
        self.from_switch_webview = from_switch_webview
        self.from_side_menu = from_side_menu
        self.url = url
        self.start_param = start_param
        self.theme_params = theme_params

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'RequestSimpleWebViewRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'platform': self.platform,
            'from_switch_webview': self.from_switch_webview,
            'from_side_menu': self.from_side_menu,
            'url': self.url,
            'start_param': self.start_param,
            'theme_params': self.theme_params.to_dict() if isinstance(self.theme_params, TLObject) else self.theme_params
        }

    def _bytes(self):
        return b''.join((
            b'\nPF\x1a',
            struct.pack('<I', (0 if self.from_switch_webview is None or self.from_switch_webview is False else 2) | (0 if self.from_side_menu is None or self.from_side_menu is False else 4) | (0 if self.url is None or self.url is False else 8) | (0 if self.start_param is None or self.start_param is False else 16) | (0 if self.theme_params is None or self.theme_params is False else 1)),
            self.bot._bytes(),
            b'' if self.url is None or self.url is False else (self.serialize_bytes(self.url)),
            b'' if self.start_param is None or self.start_param is False else (self.serialize_bytes(self.start_param)),
            b'' if self.theme_params is None or self.theme_params is False else (self.theme_params._bytes()),
            self.serialize_bytes(self.platform),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _from_switch_webview = bool(flags & 2)
        _from_side_menu = bool(flags & 4)
        _bot = reader.tgread_object()
        if flags & 8:
            _url = reader.tgread_string()
        else:
            _url = None
        if flags & 16:
            _start_param = reader.tgread_string()
        else:
            _start_param = None
        if flags & 1:
            _theme_params = reader.tgread_object()
        else:
            _theme_params = None
        _platform = reader.tgread_string()
        return cls(bot=_bot, platform=_platform, from_switch_webview=_from_switch_webview, from_side_menu=_from_side_menu, url=_url, start_param=_start_param, theme_params=_theme_params)


class RequestUrlAuthRequest(TLRequest):
    CONSTRUCTOR_ID = 0x198fb446
    SUBCLASS_OF_ID = 0x7765cb1e

    def __init__(self, peer: Optional['TypeInputPeer']=None, msg_id: Optional[int]=None, button_id: Optional[int]=None, url: Optional[str]=None):
        """
        :returns UrlAuthResult: Instance of either UrlAuthResultRequest, UrlAuthResultAccepted, UrlAuthResultDefault.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url

    async def resolve(self, client, utils):
        if self.peer:
            self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'RequestUrlAuthRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'button_id': self.button_id,
            'url': self.url
        }

    def _bytes(self):
        assert ((self.peer or self.peer is not None) and (self.msg_id or self.msg_id is not None) and (self.button_id or self.button_id is not None)) or ((self.peer is None or self.peer is False) and (self.msg_id is None or self.msg_id is False) and (self.button_id is None or self.button_id is False)), 'peer, msg_id, button_id parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'F\xb4\x8f\x19',
            struct.pack('<I', (0 if self.peer is None or self.peer is False else 2) | (0 if self.msg_id is None or self.msg_id is False else 2) | (0 if self.button_id is None or self.button_id is False else 2) | (0 if self.url is None or self.url is False else 4)),
            b'' if self.peer is None or self.peer is False else (self.peer._bytes()),
            b'' if self.msg_id is None or self.msg_id is False else (struct.pack('<i', self.msg_id)),
            b'' if self.button_id is None or self.button_id is False else (struct.pack('<i', self.button_id)),
            b'' if self.url is None or self.url is False else (self.serialize_bytes(self.url)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 2:
            _peer = reader.tgread_object()
        else:
            _peer = None
        if flags & 2:
            _msg_id = reader.read_int()
        else:
            _msg_id = None
        if flags & 2:
            _button_id = reader.read_int()
        else:
            _button_id = None
        if flags & 4:
            _url = reader.tgread_string()
        else:
            _url = None
        return cls(peer=_peer, msg_id=_msg_id, button_id=_button_id, url=_url)


class RequestWebViewRequest(TLRequest):
    CONSTRUCTOR_ID = 0x269dc2c1
    SUBCLASS_OF_ID = 0x93cea746

    def __init__(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, from_bot_menu: Optional[bool]=None, silent: Optional[bool]=None, url: Optional[str]=None, start_param: Optional[str]=None, theme_params: Optional['TypeDataJSON']=None, reply_to: Optional['TypeInputReplyTo']=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns WebViewResult: Instance of WebViewResultUrl.
        """
        self.peer = peer
        self.bot = bot
        self.platform = platform
        self.from_bot_menu = from_bot_menu
        self.silent = silent
        self.url = url
        self.start_param = start_param
        self.theme_params = theme_params
        self.reply_to = reply_to
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'RequestWebViewRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'platform': self.platform,
            'from_bot_menu': self.from_bot_menu,
            'silent': self.silent,
            'url': self.url,
            'start_param': self.start_param,
            'theme_params': self.theme_params.to_dict() if isinstance(self.theme_params, TLObject) else self.theme_params,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'\xc1\xc2\x9d&',
            struct.pack('<I', (0 if self.from_bot_menu is None or self.from_bot_menu is False else 16) | (0 if self.silent is None or self.silent is False else 32) | (0 if self.url is None or self.url is False else 2) | (0 if self.start_param is None or self.start_param is False else 8) | (0 if self.theme_params is None or self.theme_params is False else 4) | (0 if self.reply_to is None or self.reply_to is False else 1) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.peer._bytes(),
            self.bot._bytes(),
            b'' if self.url is None or self.url is False else (self.serialize_bytes(self.url)),
            b'' if self.start_param is None or self.start_param is False else (self.serialize_bytes(self.start_param)),
            b'' if self.theme_params is None or self.theme_params is False else (self.theme_params._bytes()),
            self.serialize_bytes(self.platform),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _from_bot_menu = bool(flags & 16)
        _silent = bool(flags & 32)
        _peer = reader.tgread_object()
        _bot = reader.tgread_object()
        if flags & 2:
            _url = reader.tgread_string()
        else:
            _url = None
        if flags & 8:
            _start_param = reader.tgread_string()
        else:
            _start_param = None
        if flags & 4:
            _theme_params = reader.tgread_object()
        else:
            _theme_params = None
        _platform = reader.tgread_string()
        if flags & 1:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(peer=_peer, bot=_bot, platform=_platform, from_bot_menu=_from_bot_menu, silent=_silent, url=_url, start_param=_start_param, theme_params=_theme_params, reply_to=_reply_to, send_as=_send_as)


class SaveDefaultSendAsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xccfddf96
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', send_as: 'TypeInputPeer'):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'SaveDefaultSendAsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'\x96\xdf\xfd\xcc',
            self.peer._bytes(),
            self.send_as._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _send_as = reader.tgread_object()
        return cls(peer=_peer, send_as=_send_as)


class SaveDraftRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7ff3b806
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool]=None, invert_media: Optional[bool]=None, reply_to: Optional['TypeInputReplyTo']=None, entities: Optional[List['TypeMessageEntity']]=None, media: Optional['TypeInputMedia']=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.message = message
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.entities = entities
        self.media = media

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        if self.media:
            self.media = utils.get_input_media(self.media)

    def to_dict(self):
        return {
            '_': 'SaveDraftRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'message': self.message,
            'no_webpage': self.no_webpage,
            'invert_media': self.invert_media,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities],
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media
        }

    def _bytes(self):
        return b''.join((
            b'\x06\xb8\xf3\x7f',
            struct.pack('<I', (0 if self.no_webpage is None or self.no_webpage is False else 2) | (0 if self.invert_media is None or self.invert_media is False else 64) | (0 if self.reply_to is None or self.reply_to is False else 16) | (0 if self.entities is None or self.entities is False else 8) | (0 if self.media is None or self.media is False else 32)),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            self.peer._bytes(),
            self.serialize_bytes(self.message),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities))),
            b'' if self.media is None or self.media is False else (self.media._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _no_webpage = bool(flags & 2)
        _invert_media = bool(flags & 64)
        if flags & 16:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        _peer = reader.tgread_object()
        _message = reader.tgread_string()
        if flags & 8:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        if flags & 32:
            _media = reader.tgread_object()
        else:
            _media = None
        return cls(peer=_peer, message=_message, no_webpage=_no_webpage, invert_media=_invert_media, reply_to=_reply_to, entities=_entities, media=_media)


class SaveGifRequest(TLRequest):
    CONSTRUCTOR_ID = 0x327a30cb
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputDocument', unsave: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.unsave = unsave

    async def resolve(self, client, utils):
        self.id = utils.get_input_document(self.id)

    def to_dict(self):
        return {
            '_': 'SaveGifRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'unsave': self.unsave
        }

    def _bytes(self):
        return b''.join((
            b'\xcb0z2',
            self.id._bytes(),
            b'\xb5ur\x99' if self.unsave else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.tgread_object()
        _unsave = reader.tgread_bool()
        return cls(id=_id, unsave=_unsave)


class SaveRecentStickerRequest(TLRequest):
    CONSTRUCTOR_ID = 0x392718f8
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputDocument', unsave: bool, attached: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.unsave = unsave
        self.attached = attached

    async def resolve(self, client, utils):
        self.id = utils.get_input_document(self.id)

    def to_dict(self):
        return {
            '_': 'SaveRecentStickerRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'unsave': self.unsave,
            'attached': self.attached
        }

    def _bytes(self):
        return b''.join((
            b"\xf8\x18'9",
            struct.pack('<I', (0 if self.attached is None or self.attached is False else 1)),
            self.id._bytes(),
            b'\xb5ur\x99' if self.unsave else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _attached = bool(flags & 1)
        _id = reader.tgread_object()
        _unsave = reader.tgread_bool()
        return cls(id=_id, unsave=_unsave, attached=_attached)


class SearchRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa0fda762
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime], max_date: Optional[datetime], offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: Optional['TypeInputPeer']=None, top_msg_id: Optional[int]=None):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.peer = peer
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash
        self.from_id = from_id
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        if self.from_id:
            self.from_id = utils.get_input_peer(await client.get_input_entity(self.from_id))

    def to_dict(self):
        return {
            '_': 'SearchRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'q': self.q,
            'filter': self.filter.to_dict() if isinstance(self.filter, TLObject) else self.filter,
            'min_date': self.min_date,
            'max_date': self.max_date,
            'offset_id': self.offset_id,
            'add_offset': self.add_offset,
            'limit': self.limit,
            'max_id': self.max_id,
            'min_id': self.min_id,
            'hash': self.hash,
            'from_id': self.from_id.to_dict() if isinstance(self.from_id, TLObject) else self.from_id,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'b\xa7\xfd\xa0',
            struct.pack('<I', (0 if self.from_id is None or self.from_id is False else 1) | (0 if self.top_msg_id is None or self.top_msg_id is False else 2)),
            self.peer._bytes(),
            self.serialize_bytes(self.q),
            b'' if self.from_id is None or self.from_id is False else (self.from_id._bytes()),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
            self.filter._bytes(),
            self.serialize_datetime(self.min_date),
            self.serialize_datetime(self.max_date),
            struct.pack('<i', self.offset_id),
            struct.pack('<i', self.add_offset),
            struct.pack('<i', self.limit),
            struct.pack('<i', self.max_id),
            struct.pack('<i', self.min_id),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        _q = reader.tgread_string()
        if flags & 1:
            _from_id = reader.tgread_object()
        else:
            _from_id = None
        if flags & 2:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        _filter = reader.tgread_object()
        _min_date = reader.tgread_date()
        _max_date = reader.tgread_date()
        _offset_id = reader.read_int()
        _add_offset = reader.read_int()
        _limit = reader.read_int()
        _max_id = reader.read_int()
        _min_id = reader.read_int()
        _hash = reader.read_long()
        return cls(peer=_peer, q=_q, filter=_filter, min_date=_min_date, max_date=_max_date, offset_id=_offset_id, add_offset=_add_offset, limit=_limit, max_id=_max_id, min_id=_min_id, hash=_hash, from_id=_from_id, top_msg_id=_top_msg_id)


class SearchCustomEmojiRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2c11c0d7
    SUBCLASS_OF_ID = 0xbcef6aba

    # noinspection PyShadowingBuiltins
    def __init__(self, emoticon: str, hash: int):
        """
        :returns EmojiList: Instance of either EmojiListNotModified, EmojiList.
        """
        self.emoticon = emoticon
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'SearchCustomEmojiRequest',
            'emoticon': self.emoticon,
            'hash': self.hash
        }

    def _bytes(self):
        return b''.join((
            b'\xd7\xc0\x11,',
            self.serialize_bytes(self.emoticon),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _emoticon = reader.tgread_string()
        _hash = reader.read_long()
        return cls(emoticon=_emoticon, hash=_hash)


class SearchGlobalRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4bc6589a
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime], max_date: Optional[datetime], offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, folder_id: Optional[int]=None):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_rate = offset_rate
        self.offset_peer = offset_peer
        self.offset_id = offset_id
        self.limit = limit
        self.folder_id = folder_id

    async def resolve(self, client, utils):
        self.offset_peer = utils.get_input_peer(await client.get_input_entity(self.offset_peer))

    def to_dict(self):
        return {
            '_': 'SearchGlobalRequest',
            'q': self.q,
            'filter': self.filter.to_dict() if isinstance(self.filter, TLObject) else self.filter,
            'min_date': self.min_date,
            'max_date': self.max_date,
            'offset_rate': self.offset_rate,
            'offset_peer': self.offset_peer.to_dict() if isinstance(self.offset_peer, TLObject) else self.offset_peer,
            'offset_id': self.offset_id,
            'limit': self.limit,
            'folder_id': self.folder_id
        }

    def _bytes(self):
        return b''.join((
            b'\x9aX\xc6K',
            struct.pack('<I', (0 if self.folder_id is None or self.folder_id is False else 1)),
            b'' if self.folder_id is None or self.folder_id is False else (struct.pack('<i', self.folder_id)),
            self.serialize_bytes(self.q),
            self.filter._bytes(),
            self.serialize_datetime(self.min_date),
            self.serialize_datetime(self.max_date),
            struct.pack('<i', self.offset_rate),
            self.offset_peer._bytes(),
            struct.pack('<i', self.offset_id),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _folder_id = reader.read_int()
        else:
            _folder_id = None
        _q = reader.tgread_string()
        _filter = reader.tgread_object()
        _min_date = reader.tgread_date()
        _max_date = reader.tgread_date()
        _offset_rate = reader.read_int()
        _offset_peer = reader.tgread_object()
        _offset_id = reader.read_int()
        _limit = reader.read_int()
        return cls(q=_q, filter=_filter, min_date=_min_date, max_date=_max_date, offset_rate=_offset_rate, offset_peer=_offset_peer, offset_id=_offset_id, limit=_limit, folder_id=_folder_id)


class SearchSentMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x107e31a0
    SUBCLASS_OF_ID = 0xd4b40b5e

    # noinspection PyShadowingBuiltins
    def __init__(self, q: str, filter: 'TypeMessagesFilter', limit: int):
        """
        :returns messages.Messages: Instance of either Messages, MessagesSlice, ChannelMessages, MessagesNotModified.
        """
        self.q = q
        self.filter = filter
        self.limit = limit

    def to_dict(self):
        return {
            '_': 'SearchSentMediaRequest',
            'q': self.q,
            'filter': self.filter.to_dict() if isinstance(self.filter, TLObject) else self.filter,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\xa01~\x10',
            self.serialize_bytes(self.q),
            self.filter._bytes(),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _q = reader.tgread_string()
        _filter = reader.tgread_object()
        _limit = reader.read_int()
        return cls(q=_q, filter=_filter, limit=_limit)


class SearchStickerSetsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x35705b8a
    SUBCLASS_OF_ID = 0x40df361

    # noinspection PyShadowingBuiltins
    def __init__(self, q: str, hash: int, exclude_featured: Optional[bool]=None):
        """
        :returns messages.FoundStickerSets: Instance of either FoundStickerSetsNotModified, FoundStickerSets.
        """
        self.q = q
        self.hash = hash
        self.exclude_featured = exclude_featured

    def to_dict(self):
        return {
            '_': 'SearchStickerSetsRequest',
            'q': self.q,
            'hash': self.hash,
            'exclude_featured': self.exclude_featured
        }

    def _bytes(self):
        return b''.join((
            b'\x8a[p5',
            struct.pack('<I', (0 if self.exclude_featured is None or self.exclude_featured is False else 1)),
            self.serialize_bytes(self.q),
            struct.pack('<q', self.hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _exclude_featured = bool(flags & 1)
        _q = reader.tgread_string()
        _hash = reader.read_long()
        return cls(q=_q, hash=_hash, exclude_featured=_exclude_featured)


class SendBotRequestedPeerRequest(TLRequest):
    CONSTRUCTOR_ID = 0xfe38d01b
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', msg_id: int, button_id: int, requested_peer: 'TypeInputPeer'):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.requested_peer = requested_peer

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.requested_peer = utils.get_input_peer(await client.get_input_entity(self.requested_peer))

    def to_dict(self):
        return {
            '_': 'SendBotRequestedPeerRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'button_id': self.button_id,
            'requested_peer': self.requested_peer.to_dict() if isinstance(self.requested_peer, TLObject) else self.requested_peer
        }

    def _bytes(self):
        return b''.join((
            b'\x1b\xd08\xfe',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            struct.pack('<i', self.button_id),
            self.requested_peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        _button_id = reader.read_int()
        _requested_peer = reader.tgread_object()
        return cls(peer=_peer, msg_id=_msg_id, button_id=_button_id, requested_peer=_requested_peer)


class SendEncryptedRequest(TLRequest):
    CONSTRUCTOR_ID = 0x44fa7a15
    SUBCLASS_OF_ID = 0xc99e3e50

    def __init__(self, peer: 'TypeInputEncryptedChat', data: bytes, silent: Optional[bool]=None, random_id: int=None):
        """
        :returns messages.SentEncryptedMessage: Instance of either SentEncryptedMessage, SentEncryptedFile.
        """
        self.peer = peer
        self.data = data
        self.silent = silent
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)

    def to_dict(self):
        return {
            '_': 'SendEncryptedRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'data': self.data,
            'silent': self.silent,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'\x15z\xfaD',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 1)),
            self.peer._bytes(),
            struct.pack('<q', self.random_id),
            self.serialize_bytes(self.data),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 1)
        _peer = reader.tgread_object()
        _random_id = reader.read_long()
        _data = reader.tgread_bytes()
        return cls(peer=_peer, data=_data, silent=_silent, random_id=_random_id)


class SendEncryptedFileRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5559481d
    SUBCLASS_OF_ID = 0xc99e3e50

    def __init__(self, peer: 'TypeInputEncryptedChat', data: bytes, file: 'TypeInputEncryptedFile', silent: Optional[bool]=None, random_id: int=None):
        """
        :returns messages.SentEncryptedMessage: Instance of either SentEncryptedMessage, SentEncryptedFile.
        """
        self.peer = peer
        self.data = data
        self.file = file
        self.silent = silent
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)

    def to_dict(self):
        return {
            '_': 'SendEncryptedFileRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'data': self.data,
            'file': self.file.to_dict() if isinstance(self.file, TLObject) else self.file,
            'silent': self.silent,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'\x1dHYU',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 1)),
            self.peer._bytes(),
            struct.pack('<q', self.random_id),
            self.serialize_bytes(self.data),
            self.file._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 1)
        _peer = reader.tgread_object()
        _random_id = reader.read_long()
        _data = reader.tgread_bytes()
        _file = reader.tgread_object()
        return cls(peer=_peer, data=_data, file=_file, silent=_silent, random_id=_random_id)


class SendEncryptedServiceRequest(TLRequest):
    CONSTRUCTOR_ID = 0x32d439a4
    SUBCLASS_OF_ID = 0xc99e3e50

    def __init__(self, peer: 'TypeInputEncryptedChat', data: bytes, random_id: int=None):
        """
        :returns messages.SentEncryptedMessage: Instance of either SentEncryptedMessage, SentEncryptedFile.
        """
        self.peer = peer
        self.data = data
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)

    def to_dict(self):
        return {
            '_': 'SendEncryptedServiceRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'data': self.data,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'\xa49\xd42',
            self.peer._bytes(),
            struct.pack('<q', self.random_id),
            self.serialize_bytes(self.data),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _random_id = reader.read_long()
        _data = reader.tgread_bytes()
        return cls(peer=_peer, data=_data, random_id=_random_id)


class SendInlineBotResultRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf7bc68ba
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', query_id: int, id: str, silent: Optional[bool]=None, background: Optional[bool]=None, clear_draft: Optional[bool]=None, hide_via: Optional[bool]=None, reply_to: Optional['TypeInputReplyTo']=None, random_id: int=None, schedule_date: Optional[datetime]=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.query_id = query_id
        self.id = id
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.hide_via = hide_via
        self.reply_to = reply_to
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)
        self.schedule_date = schedule_date
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'SendInlineBotResultRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'query_id': self.query_id,
            'id': self.id,
            'silent': self.silent,
            'background': self.background,
            'clear_draft': self.clear_draft,
            'hide_via': self.hide_via,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'random_id': self.random_id,
            'schedule_date': self.schedule_date,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'\xbah\xbc\xf7',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 32) | (0 if self.background is None or self.background is False else 64) | (0 if self.clear_draft is None or self.clear_draft is False else 128) | (0 if self.hide_via is None or self.hide_via is False else 2048) | (0 if self.reply_to is None or self.reply_to is False else 1) | (0 if self.schedule_date is None or self.schedule_date is False else 1024) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.peer._bytes(),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            struct.pack('<q', self.random_id),
            struct.pack('<q', self.query_id),
            self.serialize_bytes(self.id),
            b'' if self.schedule_date is None or self.schedule_date is False else (self.serialize_datetime(self.schedule_date)),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 32)
        _background = bool(flags & 64)
        _clear_draft = bool(flags & 128)
        _hide_via = bool(flags & 2048)
        _peer = reader.tgread_object()
        if flags & 1:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        _random_id = reader.read_long()
        _query_id = reader.read_long()
        _id = reader.tgread_string()
        if flags & 1024:
            _schedule_date = reader.tgread_date()
        else:
            _schedule_date = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(peer=_peer, query_id=_query_id, id=_id, silent=_silent, background=_background, clear_draft=_clear_draft, hide_via=_hide_via, reply_to=_reply_to, random_id=_random_id, schedule_date=_schedule_date, send_as=_send_as)


class SendMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x72ccc23d
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', message: str, silent: Optional[bool]=None, background: Optional[bool]=None, clear_draft: Optional[bool]=None, noforwards: Optional[bool]=None, update_stickersets_order: Optional[bool]=None, invert_media: Optional[bool]=None, reply_to: Optional['TypeInputReplyTo']=None, random_id: int=None, reply_markup: Optional['TypeReplyMarkup']=None, entities: Optional[List['TypeMessageEntity']]=None, schedule_date: Optional[datetime]=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.media = media
        self.message = message
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.media = utils.get_input_media(self.media)
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'SendMediaRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media,
            'message': self.message,
            'silent': self.silent,
            'background': self.background,
            'clear_draft': self.clear_draft,
            'noforwards': self.noforwards,
            'update_stickersets_order': self.update_stickersets_order,
            'invert_media': self.invert_media,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'random_id': self.random_id,
            'reply_markup': self.reply_markup.to_dict() if isinstance(self.reply_markup, TLObject) else self.reply_markup,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities],
            'schedule_date': self.schedule_date,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'=\xc2\xccr',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 32) | (0 if self.background is None or self.background is False else 64) | (0 if self.clear_draft is None or self.clear_draft is False else 128) | (0 if self.noforwards is None or self.noforwards is False else 16384) | (0 if self.update_stickersets_order is None or self.update_stickersets_order is False else 32768) | (0 if self.invert_media is None or self.invert_media is False else 65536) | (0 if self.reply_to is None or self.reply_to is False else 1) | (0 if self.reply_markup is None or self.reply_markup is False else 4) | (0 if self.entities is None or self.entities is False else 8) | (0 if self.schedule_date is None or self.schedule_date is False else 1024) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.peer._bytes(),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            self.media._bytes(),
            self.serialize_bytes(self.message),
            struct.pack('<q', self.random_id),
            b'' if self.reply_markup is None or self.reply_markup is False else (self.reply_markup._bytes()),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities))),
            b'' if self.schedule_date is None or self.schedule_date is False else (self.serialize_datetime(self.schedule_date)),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 32)
        _background = bool(flags & 64)
        _clear_draft = bool(flags & 128)
        _noforwards = bool(flags & 16384)
        _update_stickersets_order = bool(flags & 32768)
        _invert_media = bool(flags & 65536)
        _peer = reader.tgread_object()
        if flags & 1:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        _media = reader.tgread_object()
        _message = reader.tgread_string()
        _random_id = reader.read_long()
        if flags & 4:
            _reply_markup = reader.tgread_object()
        else:
            _reply_markup = None
        if flags & 8:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        if flags & 1024:
            _schedule_date = reader.tgread_date()
        else:
            _schedule_date = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(peer=_peer, media=_media, message=_message, silent=_silent, background=_background, clear_draft=_clear_draft, noforwards=_noforwards, update_stickersets_order=_update_stickersets_order, invert_media=_invert_media, reply_to=_reply_to, random_id=_random_id, reply_markup=_reply_markup, entities=_entities, schedule_date=_schedule_date, send_as=_send_as)


class SendMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0x280d096f
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool]=None, silent: Optional[bool]=None, background: Optional[bool]=None, clear_draft: Optional[bool]=None, noforwards: Optional[bool]=None, update_stickersets_order: Optional[bool]=None, invert_media: Optional[bool]=None, reply_to: Optional['TypeInputReplyTo']=None, random_id: int=None, reply_markup: Optional['TypeReplyMarkup']=None, entities: Optional[List['TypeMessageEntity']]=None, schedule_date: Optional[datetime]=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.message = message
        self.no_webpage = no_webpage
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'SendMessageRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'message': self.message,
            'no_webpage': self.no_webpage,
            'silent': self.silent,
            'background': self.background,
            'clear_draft': self.clear_draft,
            'noforwards': self.noforwards,
            'update_stickersets_order': self.update_stickersets_order,
            'invert_media': self.invert_media,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'random_id': self.random_id,
            'reply_markup': self.reply_markup.to_dict() if isinstance(self.reply_markup, TLObject) else self.reply_markup,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities],
            'schedule_date': self.schedule_date,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'o\t\r(',
            struct.pack('<I', (0 if self.no_webpage is None or self.no_webpage is False else 2) | (0 if self.silent is None or self.silent is False else 32) | (0 if self.background is None or self.background is False else 64) | (0 if self.clear_draft is None or self.clear_draft is False else 128) | (0 if self.noforwards is None or self.noforwards is False else 16384) | (0 if self.update_stickersets_order is None or self.update_stickersets_order is False else 32768) | (0 if self.invert_media is None or self.invert_media is False else 65536) | (0 if self.reply_to is None or self.reply_to is False else 1) | (0 if self.reply_markup is None or self.reply_markup is False else 4) | (0 if self.entities is None or self.entities is False else 8) | (0 if self.schedule_date is None or self.schedule_date is False else 1024) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.peer._bytes(),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            self.serialize_bytes(self.message),
            struct.pack('<q', self.random_id),
            b'' if self.reply_markup is None or self.reply_markup is False else (self.reply_markup._bytes()),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(x._bytes() for x in self.entities))),
            b'' if self.schedule_date is None or self.schedule_date is False else (self.serialize_datetime(self.schedule_date)),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _no_webpage = bool(flags & 2)
        _silent = bool(flags & 32)
        _background = bool(flags & 64)
        _clear_draft = bool(flags & 128)
        _noforwards = bool(flags & 16384)
        _update_stickersets_order = bool(flags & 32768)
        _invert_media = bool(flags & 65536)
        _peer = reader.tgread_object()
        if flags & 1:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        _message = reader.tgread_string()
        _random_id = reader.read_long()
        if flags & 4:
            _reply_markup = reader.tgread_object()
        else:
            _reply_markup = None
        if flags & 8:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        if flags & 1024:
            _schedule_date = reader.tgread_date()
        else:
            _schedule_date = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(peer=_peer, message=_message, no_webpage=_no_webpage, silent=_silent, background=_background, clear_draft=_clear_draft, noforwards=_noforwards, update_stickersets_order=_update_stickersets_order, invert_media=_invert_media, reply_to=_reply_to, random_id=_random_id, reply_markup=_reply_markup, entities=_entities, schedule_date=_schedule_date, send_as=_send_as)


class SendMultiMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x456e8987
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', multi_media: List['TypeInputSingleMedia'], silent: Optional[bool]=None, background: Optional[bool]=None, clear_draft: Optional[bool]=None, noforwards: Optional[bool]=None, update_stickersets_order: Optional[bool]=None, invert_media: Optional[bool]=None, reply_to: Optional['TypeInputReplyTo']=None, schedule_date: Optional[datetime]=None, send_as: Optional['TypeInputPeer']=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.multi_media = multi_media
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.send_as = send_as

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        if self.send_as:
            self.send_as = utils.get_input_peer(await client.get_input_entity(self.send_as))

    def to_dict(self):
        return {
            '_': 'SendMultiMediaRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'multi_media': [] if self.multi_media is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.multi_media],
            'silent': self.silent,
            'background': self.background,
            'clear_draft': self.clear_draft,
            'noforwards': self.noforwards,
            'update_stickersets_order': self.update_stickersets_order,
            'invert_media': self.invert_media,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'schedule_date': self.schedule_date,
            'send_as': self.send_as.to_dict() if isinstance(self.send_as, TLObject) else self.send_as
        }

    def _bytes(self):
        return b''.join((
            b'\x87\x89nE',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 32) | (0 if self.background is None or self.background is False else 64) | (0 if self.clear_draft is None or self.clear_draft is False else 128) | (0 if self.noforwards is None or self.noforwards is False else 16384) | (0 if self.update_stickersets_order is None or self.update_stickersets_order is False else 32768) | (0 if self.invert_media is None or self.invert_media is False else 65536) | (0 if self.reply_to is None or self.reply_to is False else 1) | (0 if self.schedule_date is None or self.schedule_date is False else 1024) | (0 if self.send_as is None or self.send_as is False else 8192)),
            self.peer._bytes(),
            b'' if self.reply_to is None or self.reply_to is False else (self.reply_to._bytes()),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.multi_media)),b''.join(x._bytes() for x in self.multi_media),
            b'' if self.schedule_date is None or self.schedule_date is False else (self.serialize_datetime(self.schedule_date)),
            b'' if self.send_as is None or self.send_as is False else (self.send_as._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 32)
        _background = bool(flags & 64)
        _clear_draft = bool(flags & 128)
        _noforwards = bool(flags & 16384)
        _update_stickersets_order = bool(flags & 32768)
        _invert_media = bool(flags & 65536)
        _peer = reader.tgread_object()
        if flags & 1:
            _reply_to = reader.tgread_object()
        else:
            _reply_to = None
        reader.read_int()
        _multi_media = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _multi_media.append(_x)

        if flags & 1024:
            _schedule_date = reader.tgread_date()
        else:
            _schedule_date = None
        if flags & 8192:
            _send_as = reader.tgread_object()
        else:
            _send_as = None
        return cls(peer=_peer, multi_media=_multi_media, silent=_silent, background=_background, clear_draft=_clear_draft, noforwards=_noforwards, update_stickersets_order=_update_stickersets_order, invert_media=_invert_media, reply_to=_reply_to, schedule_date=_schedule_date, send_as=_send_as)


class SendReactionRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd30d78d4
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', msg_id: int, big: Optional[bool]=None, add_to_recent: Optional[bool]=None, reaction: Optional[List['TypeReaction']]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.big = big
        self.add_to_recent = add_to_recent
        self.reaction = reaction

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SendReactionRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'big': self.big,
            'add_to_recent': self.add_to_recent,
            'reaction': [] if self.reaction is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.reaction]
        }

    def _bytes(self):
        return b''.join((
            b'\xd4x\r\xd3',
            struct.pack('<I', (0 if self.big is None or self.big is False else 2) | (0 if self.add_to_recent is None or self.add_to_recent is False else 4) | (0 if self.reaction is None or self.reaction is False else 1)),
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            b'' if self.reaction is None or self.reaction is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.reaction)),b''.join(x._bytes() for x in self.reaction))),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _big = bool(flags & 2)
        _add_to_recent = bool(flags & 4)
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        if flags & 1:
            reader.read_int()
            _reaction = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _reaction.append(_x)

        else:
            _reaction = None
        return cls(peer=_peer, msg_id=_msg_id, big=_big, add_to_recent=_add_to_recent, reaction=_reaction)


class SendScheduledMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xbd38850a
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: List[int]):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SendScheduledMessagesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:]
        }

    def _bytes(self):
        return b''.join((
            b'\n\x858\xbd',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _id.append(_x)

        return cls(peer=_peer, id=_id)


class SendScreenshotNotificationRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa1405817
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', reply_to: 'TypeInputReplyTo', random_id: int=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.reply_to = reply_to
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SendScreenshotNotificationRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'reply_to': self.reply_to.to_dict() if isinstance(self.reply_to, TLObject) else self.reply_to,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'\x17X@\xa1',
            self.peer._bytes(),
            self.reply_to._bytes(),
            struct.pack('<q', self.random_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _reply_to = reader.tgread_object()
        _random_id = reader.read_long()
        return cls(peer=_peer, reply_to=_reply_to, random_id=_random_id)


class SendVoteRequest(TLRequest):
    CONSTRUCTOR_ID = 0x10ea6184
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', msg_id: int, options: List[bytes]):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.msg_id = msg_id
        self.options = options

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SendVoteRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id,
            'options': [] if self.options is None else self.options[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x84a\xea\x10',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.options)),b''.join(self.serialize_bytes(x) for x in self.options),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        reader.read_int()
        _options = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_bytes()
            _options.append(_x)

        return cls(peer=_peer, msg_id=_msg_id, options=_options)


class SendWebViewDataRequest(TLRequest):
    CONSTRUCTOR_ID = 0xdc0242c8
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, bot: 'TypeInputUser', button_text: str, data: str, random_id: int=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.bot = bot
        self.button_text = button_text
        self.data = data
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'SendWebViewDataRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'button_text': self.button_text,
            'data': self.data,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'\xc8B\x02\xdc',
            self.bot._bytes(),
            struct.pack('<q', self.random_id),
            self.serialize_bytes(self.button_text),
            self.serialize_bytes(self.data),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _random_id = reader.read_long()
        _button_text = reader.tgread_string()
        _data = reader.tgread_string()
        return cls(bot=_bot, button_text=_button_text, data=_data, random_id=_random_id)


class SendWebViewResultMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa4314f5
    SUBCLASS_OF_ID = 0x75e49312

    def __init__(self, bot_query_id: str, result: 'TypeInputBotInlineResult'):
        """
        :returns WebViewMessageSent: Instance of WebViewMessageSent.
        """
        self.bot_query_id = bot_query_id
        self.result = result

    def to_dict(self):
        return {
            '_': 'SendWebViewResultMessageRequest',
            'bot_query_id': self.bot_query_id,
            'result': self.result.to_dict() if isinstance(self.result, TLObject) else self.result
        }

    def _bytes(self):
        return b''.join((
            b'\xf5\x14C\n',
            self.serialize_bytes(self.bot_query_id),
            self.result._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot_query_id = reader.tgread_string()
        _result = reader.tgread_object()
        return cls(bot_query_id=_bot_query_id, result=_result)


class SetBotCallbackAnswerRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd58f130a
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, query_id: int, cache_time: int, alert: Optional[bool]=None, message: Optional[str]=None, url: Optional[str]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id
        self.cache_time = cache_time
        self.alert = alert
        self.message = message
        self.url = url

    def to_dict(self):
        return {
            '_': 'SetBotCallbackAnswerRequest',
            'query_id': self.query_id,
            'cache_time': self.cache_time,
            'alert': self.alert,
            'message': self.message,
            'url': self.url
        }

    def _bytes(self):
        return b''.join((
            b'\n\x13\x8f\xd5',
            struct.pack('<I', (0 if self.alert is None or self.alert is False else 2) | (0 if self.message is None or self.message is False else 1) | (0 if self.url is None or self.url is False else 4)),
            struct.pack('<q', self.query_id),
            b'' if self.message is None or self.message is False else (self.serialize_bytes(self.message)),
            b'' if self.url is None or self.url is False else (self.serialize_bytes(self.url)),
            struct.pack('<i', self.cache_time),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _alert = bool(flags & 2)
        _query_id = reader.read_long()
        if flags & 1:
            _message = reader.tgread_string()
        else:
            _message = None
        if flags & 4:
            _url = reader.tgread_string()
        else:
            _url = None
        _cache_time = reader.read_int()
        return cls(query_id=_query_id, cache_time=_cache_time, alert=_alert, message=_message, url=_url)


class SetBotPrecheckoutResultsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9c2dd95
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, query_id: int, success: Optional[bool]=None, error: Optional[str]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id
        self.success = success
        self.error = error

    def to_dict(self):
        return {
            '_': 'SetBotPrecheckoutResultsRequest',
            'query_id': self.query_id,
            'success': self.success,
            'error': self.error
        }

    def _bytes(self):
        return b''.join((
            b'\x95\xdd\xc2\t',
            struct.pack('<I', (0 if self.success is None or self.success is False else 2) | (0 if self.error is None or self.error is False else 1)),
            struct.pack('<q', self.query_id),
            b'' if self.error is None or self.error is False else (self.serialize_bytes(self.error)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _success = bool(flags & 2)
        _query_id = reader.read_long()
        if flags & 1:
            _error = reader.tgread_string()
        else:
            _error = None
        return cls(query_id=_query_id, success=_success, error=_error)


class SetBotShippingResultsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe5f672fa
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, query_id: int, error: Optional[str]=None, shipping_options: Optional[List['TypeShippingOption']]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id
        self.error = error
        self.shipping_options = shipping_options

    def to_dict(self):
        return {
            '_': 'SetBotShippingResultsRequest',
            'query_id': self.query_id,
            'error': self.error,
            'shipping_options': [] if self.shipping_options is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.shipping_options]
        }

    def _bytes(self):
        return b''.join((
            b'\xfar\xf6\xe5',
            struct.pack('<I', (0 if self.error is None or self.error is False else 1) | (0 if self.shipping_options is None or self.shipping_options is False else 2)),
            struct.pack('<q', self.query_id),
            b'' if self.error is None or self.error is False else (self.serialize_bytes(self.error)),
            b'' if self.shipping_options is None or self.shipping_options is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.shipping_options)),b''.join(x._bytes() for x in self.shipping_options))),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _query_id = reader.read_long()
        if flags & 1:
            _error = reader.tgread_string()
        else:
            _error = None
        if flags & 2:
            reader.read_int()
            _shipping_options = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _shipping_options.append(_x)

        else:
            _shipping_options = None
        return cls(query_id=_query_id, error=_error, shipping_options=_shipping_options)


class SetChatAvailableReactionsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xfeb16771
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', available_reactions: 'TypeChatReactions'):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.available_reactions = available_reactions

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SetChatAvailableReactionsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'available_reactions': self.available_reactions.to_dict() if isinstance(self.available_reactions, TLObject) else self.available_reactions
        }

    def _bytes(self):
        return b''.join((
            b'qg\xb1\xfe',
            self.peer._bytes(),
            self.available_reactions._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _available_reactions = reader.tgread_object()
        return cls(peer=_peer, available_reactions=_available_reactions)


class SetChatThemeRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe63be13f
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', emoticon: str):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.emoticon = emoticon

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SetChatThemeRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'emoticon': self.emoticon
        }

    def _bytes(self):
        return b''.join((
            b'?\xe1;\xe6',
            self.peer._bytes(),
            self.serialize_bytes(self.emoticon),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _emoticon = reader.tgread_string()
        return cls(peer=_peer, emoticon=_emoticon)


class SetChatWallPaperRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8ffacae1
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', wallpaper: Optional['TypeInputWallPaper']=None, settings: Optional['TypeWallPaperSettings']=None, id: Optional[int]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.wallpaper = wallpaper
        self.settings = settings
        self.id = id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SetChatWallPaperRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'wallpaper': self.wallpaper.to_dict() if isinstance(self.wallpaper, TLObject) else self.wallpaper,
            'settings': self.settings.to_dict() if isinstance(self.settings, TLObject) else self.settings,
            'id': self.id
        }

    def _bytes(self):
        return b''.join((
            b'\xe1\xca\xfa\x8f',
            struct.pack('<I', (0 if self.wallpaper is None or self.wallpaper is False else 1) | (0 if self.settings is None or self.settings is False else 4) | (0 if self.id is None or self.id is False else 2)),
            self.peer._bytes(),
            b'' if self.wallpaper is None or self.wallpaper is False else (self.wallpaper._bytes()),
            b'' if self.settings is None or self.settings is False else (self.settings._bytes()),
            b'' if self.id is None or self.id is False else (struct.pack('<i', self.id)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _wallpaper = reader.tgread_object()
        else:
            _wallpaper = None
        if flags & 4:
            _settings = reader.tgread_object()
        else:
            _settings = None
        if flags & 2:
            _id = reader.read_int()
        else:
            _id = None
        return cls(peer=_peer, wallpaper=_wallpaper, settings=_settings, id=_id)


class SetDefaultHistoryTTLRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9eb51445
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, period: int):
        """
        :returns Bool: This type has no constructors.
        """
        self.period = period

    def to_dict(self):
        return {
            '_': 'SetDefaultHistoryTTLRequest',
            'period': self.period
        }

    def _bytes(self):
        return b''.join((
            b'E\x14\xb5\x9e',
            struct.pack('<i', self.period),
        ))

    @classmethod
    def from_reader(cls, reader):
        _period = reader.read_int()
        return cls(period=_period)


class SetDefaultReactionRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4f47a016
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, reaction: 'TypeReaction'):
        """
        :returns Bool: This type has no constructors.
        """
        self.reaction = reaction

    def to_dict(self):
        return {
            '_': 'SetDefaultReactionRequest',
            'reaction': self.reaction.to_dict() if isinstance(self.reaction, TLObject) else self.reaction
        }

    def _bytes(self):
        return b''.join((
            b'\x16\xa0GO',
            self.reaction._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _reaction = reader.tgread_object()
        return cls(reaction=_reaction)


class SetEncryptedTypingRequest(TLRequest):
    CONSTRUCTOR_ID = 0x791451ed
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputEncryptedChat', typing: bool):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.typing = typing

    def to_dict(self):
        return {
            '_': 'SetEncryptedTypingRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'typing': self.typing
        }

    def _bytes(self):
        return b''.join((
            b'\xedQ\x14y',
            self.peer._bytes(),
            b'\xb5ur\x99' if self.typing else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _typing = reader.tgread_bool()
        return cls(peer=_peer, typing=_typing)


class SetGameScoreRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8ef8ecc0
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser', score: int, edit_message: Optional[bool]=None, force: Optional[bool]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id
        self.user_id = user_id
        self.score = score
        self.edit_message = edit_message
        self.force = force

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'SetGameScoreRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'score': self.score,
            'edit_message': self.edit_message,
            'force': self.force
        }

    def _bytes(self):
        return b''.join((
            b'\xc0\xec\xf8\x8e',
            struct.pack('<I', (0 if self.edit_message is None or self.edit_message is False else 1) | (0 if self.force is None or self.force is False else 2)),
            self.peer._bytes(),
            struct.pack('<i', self.id),
            self.user_id._bytes(),
            struct.pack('<i', self.score),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _edit_message = bool(flags & 1)
        _force = bool(flags & 2)
        _peer = reader.tgread_object()
        _id = reader.read_int()
        _user_id = reader.tgread_object()
        _score = reader.read_int()
        return cls(peer=_peer, id=_id, user_id=_user_id, score=_score, edit_message=_edit_message, force=_force)


class SetHistoryTTLRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb80e5fe4
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', period: int):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.period = period

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SetHistoryTTLRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'period': self.period
        }

    def _bytes(self):
        return b''.join((
            b'\xe4_\x0e\xb8',
            self.peer._bytes(),
            struct.pack('<i', self.period),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _period = reader.read_int()
        return cls(peer=_peer, period=_period)


class SetInlineBotResultsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xbb12a419
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, query_id: int, results: List['TypeInputBotInlineResult'], cache_time: int, gallery: Optional[bool]=None, private: Optional[bool]=None, next_offset: Optional[str]=None, switch_pm: Optional['TypeInlineBotSwitchPM']=None, switch_webview: Optional['TypeInlineBotWebView']=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.query_id = query_id
        self.results = results
        self.cache_time = cache_time
        self.gallery = gallery
        self.private = private
        self.next_offset = next_offset
        self.switch_pm = switch_pm
        self.switch_webview = switch_webview

    def to_dict(self):
        return {
            '_': 'SetInlineBotResultsRequest',
            'query_id': self.query_id,
            'results': [] if self.results is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.results],
            'cache_time': self.cache_time,
            'gallery': self.gallery,
            'private': self.private,
            'next_offset': self.next_offset,
            'switch_pm': self.switch_pm.to_dict() if isinstance(self.switch_pm, TLObject) else self.switch_pm,
            'switch_webview': self.switch_webview.to_dict() if isinstance(self.switch_webview, TLObject) else self.switch_webview
        }

    def _bytes(self):
        return b''.join((
            b'\x19\xa4\x12\xbb',
            struct.pack('<I', (0 if self.gallery is None or self.gallery is False else 1) | (0 if self.private is None or self.private is False else 2) | (0 if self.next_offset is None or self.next_offset is False else 4) | (0 if self.switch_pm is None or self.switch_pm is False else 8) | (0 if self.switch_webview is None or self.switch_webview is False else 16)),
            struct.pack('<q', self.query_id),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.results)),b''.join(x._bytes() for x in self.results),
            struct.pack('<i', self.cache_time),
            b'' if self.next_offset is None or self.next_offset is False else (self.serialize_bytes(self.next_offset)),
            b'' if self.switch_pm is None or self.switch_pm is False else (self.switch_pm._bytes()),
            b'' if self.switch_webview is None or self.switch_webview is False else (self.switch_webview._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _gallery = bool(flags & 1)
        _private = bool(flags & 2)
        _query_id = reader.read_long()
        reader.read_int()
        _results = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _results.append(_x)

        _cache_time = reader.read_int()
        if flags & 4:
            _next_offset = reader.tgread_string()
        else:
            _next_offset = None
        if flags & 8:
            _switch_pm = reader.tgread_object()
        else:
            _switch_pm = None
        if flags & 16:
            _switch_webview = reader.tgread_object()
        else:
            _switch_webview = None
        return cls(query_id=_query_id, results=_results, cache_time=_cache_time, gallery=_gallery, private=_private, next_offset=_next_offset, switch_pm=_switch_pm, switch_webview=_switch_webview)


class SetInlineGameScoreRequest(TLRequest):
    CONSTRUCTOR_ID = 0x15ad9f64
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser', score: int, edit_message: Optional[bool]=None, force: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.user_id = user_id
        self.score = score
        self.edit_message = edit_message
        self.force = force

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'SetInlineGameScoreRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'score': self.score,
            'edit_message': self.edit_message,
            'force': self.force
        }

    def _bytes(self):
        return b''.join((
            b'd\x9f\xad\x15',
            struct.pack('<I', (0 if self.edit_message is None or self.edit_message is False else 1) | (0 if self.force is None or self.force is False else 2)),
            self.id._bytes(),
            self.user_id._bytes(),
            struct.pack('<i', self.score),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _edit_message = bool(flags & 1)
        _force = bool(flags & 2)
        _id = reader.tgread_object()
        _user_id = reader.tgread_object()
        _score = reader.read_int()
        return cls(id=_id, user_id=_user_id, score=_score, edit_message=_edit_message, force=_force)


class SetTypingRequest(TLRequest):
    CONSTRUCTOR_ID = 0x58943ee2
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', action: 'TypeSendMessageAction', top_msg_id: Optional[int]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.action = action
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'SetTypingRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'action': self.action.to_dict() if isinstance(self.action, TLObject) else self.action,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'\xe2>\x94X',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
            self.action._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        _action = reader.tgread_object()
        return cls(peer=_peer, action=_action, top_msg_id=_top_msg_id)


class StartBotRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe6df7378
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', start_param: str, random_id: int=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.bot = bot
        self.peer = peer
        self.start_param = start_param
        self.random_id = random_id if random_id is not None else int.from_bytes(os.urandom(8), 'big', signed=True)

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'StartBotRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'start_param': self.start_param,
            'random_id': self.random_id
        }

    def _bytes(self):
        return b''.join((
            b'xs\xdf\xe6',
            self.bot._bytes(),
            self.peer._bytes(),
            struct.pack('<q', self.random_id),
            self.serialize_bytes(self.start_param),
        ))

    @classmethod
    def from_reader(cls, reader):
        _bot = reader.tgread_object()
        _peer = reader.tgread_object()
        _random_id = reader.read_long()
        _start_param = reader.tgread_string()
        return cls(bot=_bot, peer=_peer, start_param=_start_param, random_id=_random_id)


class StartHistoryImportRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb43df344
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', import_id: int):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.import_id = import_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'StartHistoryImportRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'import_id': self.import_id
        }

    def _bytes(self):
        return b''.join((
            b'D\xf3=\xb4',
            self.peer._bytes(),
            struct.pack('<q', self.import_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _import_id = reader.read_long()
        return cls(peer=_peer, import_id=_import_id)


class ToggleBotInAttachMenuRequest(TLRequest):
    CONSTRUCTOR_ID = 0x69f59d69
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, bot: 'TypeInputUser', enabled: bool, write_allowed: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.bot = bot
        self.enabled = enabled
        self.write_allowed = write_allowed

    async def resolve(self, client, utils):
        self.bot = utils.get_input_user(await client.get_input_entity(self.bot))

    def to_dict(self):
        return {
            '_': 'ToggleBotInAttachMenuRequest',
            'bot': self.bot.to_dict() if isinstance(self.bot, TLObject) else self.bot,
            'enabled': self.enabled,
            'write_allowed': self.write_allowed
        }

    def _bytes(self):
        return b''.join((
            b'i\x9d\xf5i',
            struct.pack('<I', (0 if self.write_allowed is None or self.write_allowed is False else 1)),
            self.bot._bytes(),
            b'\xb5ur\x99' if self.enabled else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _write_allowed = bool(flags & 1)
        _bot = reader.tgread_object()
        _enabled = reader.tgread_bool()
        return cls(bot=_bot, enabled=_enabled, write_allowed=_write_allowed)


class ToggleDialogPinRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa731e257
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.pinned = pinned

    async def resolve(self, client, utils):
        self.peer = await client._get_input_dialog(self.peer)

    def to_dict(self):
        return {
            '_': 'ToggleDialogPinRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'pinned': self.pinned
        }

    def _bytes(self):
        return b''.join((
            b'W\xe21\xa7',
            struct.pack('<I', (0 if self.pinned is None or self.pinned is False else 1)),
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _pinned = bool(flags & 1)
        _peer = reader.tgread_object()
        return cls(peer=_peer, pinned=_pinned)


class ToggleNoForwardsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb11eafa2
    SUBCLASS_OF_ID = 0x8af52aac

    def __init__(self, peer: 'TypeInputPeer', enabled: bool):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.enabled = enabled

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ToggleNoForwardsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'enabled': self.enabled
        }

    def _bytes(self):
        return b''.join((
            b'\xa2\xaf\x1e\xb1',
            self.peer._bytes(),
            b'\xb5ur\x99' if self.enabled else b'7\x97y\xbc',
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _enabled = reader.tgread_bool()
        return cls(peer=_peer, enabled=_enabled)


class TogglePeerTranslationsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe47cb579
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, peer: 'TypeInputPeer', disabled: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.peer = peer
        self.disabled = disabled

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'TogglePeerTranslationsRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'disabled': self.disabled
        }

    def _bytes(self):
        return b''.join((
            b'y\xb5|\xe4',
            struct.pack('<I', (0 if self.disabled is None or self.disabled is False else 1)),
            self.peer._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _disabled = bool(flags & 1)
        _peer = reader.tgread_object()
        return cls(peer=_peer, disabled=_disabled)


class ToggleStickerSetsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb5052fea
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, stickersets: List['TypeInputStickerSet'], uninstall: Optional[bool]=None, archive: Optional[bool]=None, unarchive: Optional[bool]=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.stickersets = stickersets
        self.uninstall = uninstall
        self.archive = archive
        self.unarchive = unarchive

    def to_dict(self):
        return {
            '_': 'ToggleStickerSetsRequest',
            'stickersets': [] if self.stickersets is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.stickersets],
            'uninstall': self.uninstall,
            'archive': self.archive,
            'unarchive': self.unarchive
        }

    def _bytes(self):
        return b''.join((
            b'\xea/\x05\xb5',
            struct.pack('<I', (0 if self.uninstall is None or self.uninstall is False else 1) | (0 if self.archive is None or self.archive is False else 2) | (0 if self.unarchive is None or self.unarchive is False else 4)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.stickersets)),b''.join(x._bytes() for x in self.stickersets),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _uninstall = bool(flags & 1)
        _archive = bool(flags & 2)
        _unarchive = bool(flags & 4)
        reader.read_int()
        _stickersets = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _stickersets.append(_x)

        return cls(stickersets=_stickersets, uninstall=_uninstall, archive=_archive, unarchive=_unarchive)


class TranscribeAudioRequest(TLRequest):
    CONSTRUCTOR_ID = 0x269e9a49
    SUBCLASS_OF_ID = 0x21b24936

    def __init__(self, peer: 'TypeInputPeer', msg_id: int):
        """
        :returns messages.TranscribedAudio: Instance of TranscribedAudio.
        """
        self.peer = peer
        self.msg_id = msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'TranscribeAudioRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'msg_id': self.msg_id
        }

    def _bytes(self):
        return b''.join((
            b'I\x9a\x9e&',
            self.peer._bytes(),
            struct.pack('<i', self.msg_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _msg_id = reader.read_int()
        return cls(peer=_peer, msg_id=_msg_id)


class TranslateTextRequest(TLRequest):
    CONSTRUCTOR_ID = 0x63183030
    SUBCLASS_OF_ID = 0x24243e8

    # noinspection PyShadowingBuiltins
    def __init__(self, to_lang: str, peer: Optional['TypeInputPeer']=None, id: Optional[List[int]]=None, text: Optional[List['TypeTextWithEntities']]=None):
        """
        :returns messages.TranslatedText: Instance of TranslateResult.
        """
        self.to_lang = to_lang
        self.peer = peer
        self.id = id
        self.text = text

    async def resolve(self, client, utils):
        if self.peer:
            self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'TranslateTextRequest',
            'to_lang': self.to_lang,
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': [] if self.id is None else self.id[:],
            'text': [] if self.text is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.text]
        }

    def _bytes(self):
        assert ((self.peer or self.peer is not None) and (self.id or self.id is not None)) or ((self.peer is None or self.peer is False) and (self.id is None or self.id is False)), 'peer, id parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'00\x18c',
            struct.pack('<I', (0 if self.peer is None or self.peer is False else 1) | (0 if self.id is None or self.id is False else 1) | (0 if self.text is None or self.text is False else 2)),
            b'' if self.peer is None or self.peer is False else (self.peer._bytes()),
            b'' if self.id is None or self.id is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(struct.pack('<i', x) for x in self.id))),
            b'' if self.text is None or self.text is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.text)),b''.join(x._bytes() for x in self.text))),
            self.serialize_bytes(self.to_lang),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _peer = reader.tgread_object()
        else:
            _peer = None
        if flags & 1:
            reader.read_int()
            _id = []
            for _ in range(reader.read_int()):
                _x = reader.read_int()
                _id.append(_x)

        else:
            _id = None
        if flags & 2:
            reader.read_int()
            _text = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _text.append(_x)

        else:
            _text = None
        _to_lang = reader.tgread_string()
        return cls(to_lang=_to_lang, peer=_peer, id=_id, text=_text)


class UninstallStickerSetRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf96e55de
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, stickerset: 'TypeInputStickerSet'):
        """
        :returns Bool: This type has no constructors.
        """
        self.stickerset = stickerset

    def to_dict(self):
        return {
            '_': 'UninstallStickerSetRequest',
            'stickerset': self.stickerset.to_dict() if isinstance(self.stickerset, TLObject) else self.stickerset
        }

    def _bytes(self):
        return b''.join((
            b'\xdeUn\xf9',
            self.stickerset._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _stickerset = reader.tgread_object()
        return cls(stickerset=_stickerset)


class UnpinAllMessagesRequest(TLRequest):
    CONSTRUCTOR_ID = 0xee22b9a8
    SUBCLASS_OF_ID = 0x2c49c116

    def __init__(self, peer: 'TypeInputPeer', top_msg_id: Optional[int]=None):
        """
        :returns messages.AffectedHistory: Instance of AffectedHistory.
        """
        self.peer = peer
        self.top_msg_id = top_msg_id

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'UnpinAllMessagesRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'top_msg_id': self.top_msg_id
        }

    def _bytes(self):
        return b''.join((
            b'\xa8\xb9"\xee',
            struct.pack('<I', (0 if self.top_msg_id is None or self.top_msg_id is False else 1)),
            self.peer._bytes(),
            b'' if self.top_msg_id is None or self.top_msg_id is False else (struct.pack('<i', self.top_msg_id)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _peer = reader.tgread_object()
        if flags & 1:
            _top_msg_id = reader.read_int()
        else:
            _top_msg_id = None
        return cls(peer=_peer, top_msg_id=_top_msg_id)


class UpdateDialogFilterRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1ad4a04a
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int, filter: Optional['TypeDialogFilter']=None):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.filter = filter

    def to_dict(self):
        return {
            '_': 'UpdateDialogFilterRequest',
            'id': self.id,
            'filter': self.filter.to_dict() if isinstance(self.filter, TLObject) else self.filter
        }

    def _bytes(self):
        return b''.join((
            b'J\xa0\xd4\x1a',
            struct.pack('<I', (0 if self.filter is None or self.filter is False else 1)),
            struct.pack('<i', self.id),
            b'' if self.filter is None or self.filter is False else (self.filter._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _id = reader.read_int()
        if flags & 1:
            _filter = reader.tgread_object()
        else:
            _filter = None
        return cls(id=_id, filter=_filter)


class UpdateDialogFiltersOrderRequest(TLRequest):
    CONSTRUCTOR_ID = 0xc563c1e4
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, order: List[int]):
        """
        :returns Bool: This type has no constructors.
        """
        self.order = order

    def to_dict(self):
        return {
            '_': 'UpdateDialogFiltersOrderRequest',
            'order': [] if self.order is None else self.order[:]
        }

    def _bytes(self):
        return b''.join((
            b'\xe4\xc1c\xc5',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.order)),b''.join(struct.pack('<i', x) for x in self.order),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _order = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _order.append(_x)

        return cls(order=_order)


class UpdatePinnedMessageRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd2aaf7ec
    SUBCLASS_OF_ID = 0x8af52aac

    # noinspection PyShadowingBuiltins
    def __init__(self, peer: 'TypeInputPeer', id: int, silent: Optional[bool]=None, unpin: Optional[bool]=None, pm_oneside: Optional[bool]=None):
        """
        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, Updates, UpdateShortSentMessage.
        """
        self.peer = peer
        self.id = id
        self.silent = silent
        self.unpin = unpin
        self.pm_oneside = pm_oneside

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'UpdatePinnedMessageRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'id': self.id,
            'silent': self.silent,
            'unpin': self.unpin,
            'pm_oneside': self.pm_oneside
        }

    def _bytes(self):
        return b''.join((
            b'\xec\xf7\xaa\xd2',
            struct.pack('<I', (0 if self.silent is None or self.silent is False else 1) | (0 if self.unpin is None or self.unpin is False else 2) | (0 if self.pm_oneside is None or self.pm_oneside is False else 4)),
            self.peer._bytes(),
            struct.pack('<i', self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _silent = bool(flags & 1)
        _unpin = bool(flags & 2)
        _pm_oneside = bool(flags & 4)
        _peer = reader.tgread_object()
        _id = reader.read_int()
        return cls(peer=_peer, id=_id, silent=_silent, unpin=_unpin, pm_oneside=_pm_oneside)


class UploadEncryptedFileRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5057c497
    SUBCLASS_OF_ID = 0x842a67c0

    def __init__(self, peer: 'TypeInputEncryptedChat', file: 'TypeInputEncryptedFile'):
        """
        :returns EncryptedFile: Instance of either EncryptedFileEmpty, EncryptedFile.
        """
        self.peer = peer
        self.file = file

    def to_dict(self):
        return {
            '_': 'UploadEncryptedFileRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'file': self.file.to_dict() if isinstance(self.file, TLObject) else self.file
        }

    def _bytes(self):
        return b''.join((
            b'\x97\xc4WP',
            self.peer._bytes(),
            self.file._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _file = reader.tgread_object()
        return cls(peer=_peer, file=_file)


class UploadImportedMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2a862092
    SUBCLASS_OF_ID = 0x476cbe32

    def __init__(self, peer: 'TypeInputPeer', import_id: int, file_name: str, media: 'TypeInputMedia'):
        """
        :returns MessageMedia: Instance of either MessageMediaEmpty, MessageMediaPhoto, MessageMediaGeo, MessageMediaContact, MessageMediaUnsupported, MessageMediaDocument, MessageMediaWebPage, MessageMediaVenue, MessageMediaGame, MessageMediaInvoice, MessageMediaGeoLive, MessageMediaPoll, MessageMediaDice, MessageMediaStory, MessageMediaGiveaway.
        """
        self.peer = peer
        self.import_id = import_id
        self.file_name = file_name
        self.media = media

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.media = utils.get_input_media(self.media)

    def to_dict(self):
        return {
            '_': 'UploadImportedMediaRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'import_id': self.import_id,
            'file_name': self.file_name,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media
        }

    def _bytes(self):
        return b''.join((
            b'\x92 \x86*',
            self.peer._bytes(),
            struct.pack('<q', self.import_id),
            self.serialize_bytes(self.file_name),
            self.media._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _import_id = reader.read_long()
        _file_name = reader.tgread_string()
        _media = reader.tgread_object()
        return cls(peer=_peer, import_id=_import_id, file_name=_file_name, media=_media)


class UploadMediaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x519bc2b1
    SUBCLASS_OF_ID = 0x476cbe32

    def __init__(self, peer: 'TypeInputPeer', media: 'TypeInputMedia'):
        """
        :returns MessageMedia: Instance of either MessageMediaEmpty, MessageMediaPhoto, MessageMediaGeo, MessageMediaContact, MessageMediaUnsupported, MessageMediaDocument, MessageMediaWebPage, MessageMediaVenue, MessageMediaGame, MessageMediaInvoice, MessageMediaGeoLive, MessageMediaPoll, MessageMediaDice, MessageMediaStory, MessageMediaGiveaway.
        """
        self.peer = peer
        self.media = media

    async def resolve(self, client, utils):
        self.peer = utils.get_input_peer(await client.get_input_entity(self.peer))
        self.media = utils.get_input_media(self.media)

    def to_dict(self):
        return {
            '_': 'UploadMediaRequest',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media
        }

    def _bytes(self):
        return b''.join((
            b'\xb1\xc2\x9bQ',
            self.peer._bytes(),
            self.media._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        _media = reader.tgread_object()
        return cls(peer=_peer, media=_media)

