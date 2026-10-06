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

from collections.abc import Mapping
from abc import abstractmethod
from typing import Self

from ...util.interface import Interface

class ConfigurationSerializable(Interface):
    """
    An object that can be stored in a config file and read back.

    A config writes what :meth:`serialize` returns together with a ``==`` key naming the class,
    and calls :meth:`deserialize` of that class when it loads such an entry. Bukkit accepts three
    ways to read an object back, Python has one: the :meth:`deserialize` class method, which
    type checkers can hold every implementation to.
    """

    __slots__ = ()

    @abstractmethod
    def serialize(self) -> Mapping[str, object]:
        """
        The object's state as plain values: strings, numbers, booleans, ``None``, lists,
        mappings and other serializable objects. Anything else cannot be written to the file.
        """

    @classmethod
    @abstractmethod
    def deserialize(cls, data: Mapping[str, object]) -> Self:
        """
        Rebuilds an object from what :meth:`serialize` returned. Config files outlive plugin
        updates, so ``data`` may come from an older version of the class.
        """

__all__ = ["ConfigurationSerializable"]