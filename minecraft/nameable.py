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

from .util.interface import Interface

class Nameable(Interface):
    """
    An entity or block that can carry a custom name, like one given with a name tag or an anvil.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def custom_name(self) -> str | None:
        """
        :class:`str` | ``None``: The custom name, ``None`` if there is none. It appears in death
        messages, as the nameplate of a mob and as the title of a container's inventory. Setting
        ``None`` or an empty string removes it. Players always keep their real name, so setting
        it on them changes nothing.
        """

    @custom_name.setter
    @abstractmethod
    def custom_name(self, name: str | None) -> None:
        ...

__all__ = ["Nameable"]