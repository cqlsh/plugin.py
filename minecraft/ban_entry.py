"""
The MIT License (MIT)

Copyright (c) 2026-present cqlsh

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from warnings import deprecated
from abc import abstractmethod
from datetime import datetime

from .util.interface import Interface

class BanEntry[T](Interface):
    """
    One entry of a ban list, for a player profile or an IP address as ``T``.

    Changes stay on this object until :meth:`save` writes them to the server's ban list, the
    file ``banned-players.json`` or ``banned-ips.json``. Saving an entry that was removed in
    the meantime bans the target again, and changes made to the list elsewhere may not show up
    here.
    """

    __slots__ = ()

    @property
    @deprecated("Use ban_target", category=None)
    @abstractmethod
    def target(self) -> str:
        """
        :class:`str`: The banned player's name or the banned IP address as text.
        """

    @property
    @abstractmethod
    def ban_target(self) -> T:
        """
        The banned player profile or IP address.
        """

    @property
    @abstractmethod
    def created(self) -> datetime:
        """
        :class:`datetime.datetime`: When the ban was created.
        """

    @created.setter
    @abstractmethod
    def created(self, created: datetime) -> None:
        ...

    @property
    @abstractmethod
    def source(self) -> str:
        """
        :class:`str`: Who issued the ban, usually a player name, ``"Server"`` for the console or
        a plugin's name. Any text is allowed.
        """

    @source.setter
    @abstractmethod
    def source(self, source: str) -> None:
        ...

    @property
    @abstractmethod
    def expiration(self) -> datetime | None:
        """
        :class:`datetime.datetime` | ``None``: When the ban ends, ``None`` for a ban that never
        ends.
        """

    @expiration.setter
    @abstractmethod
    def expiration(self, expiration: datetime | None) -> None:
        ...

    @property
    @abstractmethod
    def reason(self) -> str | None:
        """
        :class:`str` | ``None``: Why the target was banned, shown to it when it tries to join.
        Setting ``None`` uses the server's default reason.
        """

    @reason.setter
    @abstractmethod
    def reason(self, reason: str | None) -> None:
        ...

    @abstractmethod
    def save(self) -> None:
        """
        Writes the entry to the ban list, replacing an older entry for the same target.
        """

    @abstractmethod
    def remove(self) -> None:
        """
        Removes the entry from the ban list, which lifts the ban.
        """

__all__ = ["BanEntry"]