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

from abc import abstractmethod
from uuid import UUID

from ..util.interface import Interface

class AnimalTamer(Interface):
    """
    Something that can own a tamed animal, an online or an offline player.

    A tamed wolf, cat or parrot keeps only its owner's :attr:`unique_id`, so the owner stays the
    same while offline and across name changes.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def name(self) -> str | None:
        """
        :class:`str` | ``None``: The owner's name, ``None`` if the server does not know it, like
        for an offline player who never joined this server.
        """

    @property
    @abstractmethod
    def unique_id(self) -> UUID:
        """
        :class:`uuid.UUID`: The owner's UUID, the value tamed animals store.
        """

__all__ = ["AnimalTamer"]