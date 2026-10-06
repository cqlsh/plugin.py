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
from typing import Any

from .interface import Interface

class OldEnum[T: OldEnum[Any]](Interface):
    """
    A type that was a Java enum until Minecraft turned it into a registry, like ``Sound`` or
    ``Biome``.

    It keeps the enum's name, position and ordering so older plugin code still runs. ``T`` is the
    type itself, like Java's ``OldEnum<Sound>``, so an entry only compares to entries of its own
    type. Data packs can add entries to these registries that have neither a fixed name nor a
    fixed position, so new code should identify entries by their key instead.
    """

    __slots__ = ()

    @property
    @deprecated("Only for backwards compatibility, use the key", category=None)
    @abstractmethod
    def name(self) -> str:
        """
        :class:`str`: The name the entry had as an enum constant, such as ``"PLAINS"``.
        """

    @property
    @deprecated("Only for backwards compatibility, use the key", category=None)
    @abstractmethod
    def ordinal(self) -> int:
        """
        :class:`int`: The position the entry had as an enum constant. It can change between
        server versions.
        """

    @deprecated("Only for backwards compatibility, old enums can not be compared", category=None)
    @abstractmethod
    def __lt__(self, other: T, /) -> bool:
        """
        Whether this entry comes before ``other`` by :attr:`ordinal`, so lists of entries still
        sort the way they did as enum constants.
        """

__all__ = ["OldEnum"]