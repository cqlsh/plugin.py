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

from typing import Self
from enum import IntEnum

from ..chat_color import ChatColor

class AdvancementDisplayType(IntEnum):
    """
    The frame of an advancement, which sets its icon, its color and how players hear about it.

    Members are the frame ids of the Java protocol and, being plain integers, go into a packet
    as they are. The lowercase member name is the ``frame`` of an advancement file in a data
    pack, like ``"challenge"``.
    """

    _value_: int
    _color: ChatColor

    TASK = 0, ChatColor.GREEN
    """
    A plain advancement with a square frame. The chat says a player "has made the advancement".
    """

    CHALLENGE = 1, ChatColor.DARK_PURPLE
    """
    A challenge with a spiked frame. Completing one plays a fanfare, and the chat says a player
    "has completed the challenge".
    """

    GOAL = 2, ChatColor.GREEN
    """
    A goal with a rounded frame. The chat says a player "has reached the goal".
    """

    def __new__(cls, frame: int, color: ChatColor) -> Self:
        """
        Keeps the frame id as the member's integer and its chat color beside it.
        """
        member = int.__new__(cls, frame)
        member._value_ = frame
        member._color = color

        return member

    @property
    def color(self) -> ChatColor:
        """
        :class:`ChatColor`: The color Minecraft gives the name of such an advancement in chat,
        like in the message announcing that a player earned it.
        """
        return self._color

__all__ = ["AdvancementDisplayType"]