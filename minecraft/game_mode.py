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
from typing import Final
from enum import IntEnum

class GameMode(IntEnum):
    """
    The rules a player plays by.

    Members are the game mode ids of the Java protocol and, being plain integers, go into a
    packet as they are. The lowercase member name is the mode in the ``/gamemode`` command and
    in ``server.properties``. Bedrock uses the same ids except for spectator, which the Bedrock
    platform translates.
    """

    CREATIVE = 1
    """
    Flying, breaking blocks at once, no damage and every item from the creative inventory.
    """

    SURVIVAL = 0
    """
    The normal game with health, hunger and everything gathered by hand.
    """

    ADVENTURE = 2
    """
    Survival for maps: a player only breaks or places blocks where the ``can_break`` or
    ``can_place_on`` component of the held item allows it.
    """

    SPECTATOR = 3
    """
    Flying through blocks without touching the world, invisible to players in other modes and
    able to look through the eyes of other entities.
    """

    @classmethod
    @deprecated("Magic value", category=None)
    def get_by_value(cls, value: int) -> GameMode | None:
        """
        The mode with the given id, or ``None``. ``GameMode(value)`` does the same but raises
        :exc:`ValueError` for unknown ids.
        """
        return BY_VALUE.get(value)

BY_VALUE: Final = {int(mode): mode for mode in GameMode}

__all__ = ["GameMode"]