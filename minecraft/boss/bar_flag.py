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

from enum import IntEnum

class BarFlag(IntEnum):
    """
    An extra effect a boss bar has on the players who see it.

    Members are the bits of the flag byte in the Java protocol, so a platform joins them with
    ``|`` into the byte it sends.
    """

    DARKEN_SKY = 0x01
    """
    Darkens the sky, like during a fight against the wither.
    """

    PLAY_BOSS_MUSIC = 0x02
    """
    Plays the music of the Ender Dragon fight. Clients only play it in the End.
    """

    CREATE_FOG = 0x04
    """
    Pulls the fog in close around the player, like during the Ender Dragon fight.
    """

__all__ = ["BarFlag"]