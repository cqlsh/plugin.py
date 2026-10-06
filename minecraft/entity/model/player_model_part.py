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

class PlayerModelPart(IntEnum):
    """
    A layer of a player's skin that the player can switch off in the skin settings.

    Members are the bits of the skin parts byte, which clients send with their settings and
    player entities carry in their data, so ``parts & PlayerModelPart.HAT`` tests one layer.
    Bukkit marks this type experimental, so it may still change between versions.
    """

    CAPE = 0x01
    """
    The cape, shown only if the player owns one.
    """

    JACKET = 0x02
    """
    The outer layer over the torso.
    """

    LEFT_SLEEVE = 0x04
    """
    The outer layer over the left arm.
    """

    RIGHT_SLEEVE = 0x08
    """
    The outer layer over the right arm.
    """

    LEFT_PANTS_LEG = 0x10
    """
    The outer layer over the left leg.
    """

    RIGHT_PANTS_LEG = 0x20
    """
    The outer layer over the right leg.
    """

    HAT = 0x40
    """
    The outer layer over the head.
    """

__all__ = ["PlayerModelPart"]