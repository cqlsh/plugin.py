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

import re

from typing import Final, Self
from enum import Enum

NOT_NAME_CHARACTER: Final = re.compile(r"[^a-z!]")

class PermissionDefault(Enum):
    """
    Who has a permission that nobody set explicitly.

    It is written as ``default`` of a permission in ``plugin.yml``. Every value accepts a few
    spellings there, and :meth:`get_by_name` resolves all of them.
    """

    _value_: str
    _for_ops: bool
    _for_others: bool

    TRUE = True, True, "true"
    """
    Everyone has the permission.
    """

    FALSE = False, False, "false"
    """
    Nobody has the permission unless it is granted.
    """

    OP = True, False, "op", "isop", "operator", "isoperator", "admin", "isadmin"
    """
    Server operators have the permission, everyone else does not. Bukkit's default when a
    permission names none.
    """

    NOT_OP = False, True, "!op", "notop", "!operator", "notoperator", "!admin", "notadmin"
    """
    Everyone except server operators has the permission.
    """

    def __new__(cls, for_ops: bool, for_others: bool, name: str, *aliases: str) -> Self:
        """
        Keeps both answers on the member and registers every other spelling as an alias, so
        ``PermissionDefault("isadmin")`` finds :attr:`OP` as well.
        """
        member = object.__new__(cls)
        member._value_ = name
        member._for_ops = for_ops
        member._for_others = for_others

        for alias in aliases:
            member._add_value_alias_(alias)

        return member

    def __str__(self) -> str:
        return self._value_

    def get_value(self, op: bool) -> bool:
        """
        Whether someone has a permission with this default, given whether they are an operator.
        Runs for every check of a permission that nobody set explicitly.
        """
        if op:
            return self._for_ops

        return self._for_others

    @classmethod
    def get_by_name(cls, name: str) -> Self | None:
        """
        The default spelled ``name``, or ``None`` if no value is spelled that way. Case and
        every character besides letters and ``!`` are ignored, so ``"Is OP"`` finds :attr:`OP`.
        """
        lowered = name.lower()
        member = cls._value2member_map_.get(lowered)

        if member is None:
            member = cls._value2member_map_.get(NOT_NAME_CHARACTER.sub("", lowered))

        if isinstance(member, cls):
            return member

        return None

__all__ = ["PermissionDefault"]