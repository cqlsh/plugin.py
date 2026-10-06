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

from typing import Final
from enum import Enum

class PluginAwareness:
    """
    Something a plugin declares it is aware of, listed under ``awareness`` in ``plugin.yml``.

    Entries are YAML tags starting with ``!@``. Known tags become members of :class:`Flags`,
    any other tag becomes an instance of this class holding the raw tag, so a plugin written
    for a newer server still loads instead of failing on an awareness this one does not know.

    Parameters
    ----------
    tag: :class:`str`
        The raw tag, such as ``"!@SomethingNew"``.
    """

    __slots__ = ["tag"]

    tag: Final[str]
    """
    :class:`str`: The raw tag from ``plugin.yml``, kept so the entry can still be logged.
    """

    def __init__(self, tag: str) -> None:
        self.tag = tag

    def __repr__(self) -> str:
        return f"<PluginAwareness tag={self.tag!r}>"

    class Flags(Enum):
        """
        The awarenesses this server knows, valued by their tag in ``plugin.yml``.
        """

        UTF8 = "!@UTF8"
        """
        The plugin's text resources are encoded in UTF-8. Deprecated since 1.9, every plugin is
        treated as UTF-8 aware, so declaring it changes nothing.
        """

__all__ = ["PluginAwareness"]