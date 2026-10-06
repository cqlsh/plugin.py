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

from ..util.interface import Interface

class DataPackFormat(Interface):
    """
    The format version of a data pack, which decides the game versions that can load it.

    Since Minecraft 1.21.9 a format has a minor version beside the major one. Formats compare
    by major version first and by minor version second, so ``older < newer`` holds and a list
    of formats sorts from oldest to newest.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def major(self) -> int:
        """
        :class:`int`: The major version, the number that packs made before 1.21.9 declare as
        their ``pack_format``.
        """

    @property
    @abstractmethod
    def minor(self) -> int:
        """
        :class:`int`: The minor version, 0 for packs that only declare a major version.
        """

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DataPackFormat):
            return False

        return self.major == other.major and self.minor == other.minor

    def __hash__(self) -> int:
        return hash((self.major, self.minor))

    def __lt__(self, other: DataPackFormat, /) -> bool:
        major = self.major
        other_major = other.major

        if major != other_major:
            return major < other_major

        return self.minor < other.minor

    def __le__(self, other: DataPackFormat, /) -> bool:
        major = self.major
        other_major = other.major

        if major != other_major:
            return major < other_major

        return self.minor <= other.minor

    def __gt__(self, other: DataPackFormat, /) -> bool:
        major = self.major
        other_major = other.major

        if major != other_major:
            return major > other_major

        return self.minor > other.minor

    def __ge__(self, other: DataPackFormat, /) -> bool:
        major = self.major
        other_major = other.major

        if major != other_major:
            return major > other_major

        return self.minor >= other.minor

__all__ = ["DataPackFormat"]