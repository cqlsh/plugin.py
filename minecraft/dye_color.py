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
from typing import Final, Self
from enum import IntEnum

from .color import Color

class DyeColor(IntEnum):
    """
    One of the 16 dye colors of wool, carpets, beds, banners, shulker boxes, sheep and more.

    Members are the color ids of the Java protocol, from white at 0 to black at 15, and go into
    a packet as they are.
    """

    _value_: int
    _dye_data: int
    _color: Color
    _firework_color: Color

    WHITE = 0x0, 0xF, 0xF9FFFE, 0xF0F0F0
    """
    White dye, ``#F9FFFE``, in fireworks ``#F0F0F0``.
    """

    ORANGE = 0x1, 0xE, 0xF9801D, 0xEB8844
    """
    Orange dye, ``#F9801D``, in fireworks ``#EB8844``.
    """

    MAGENTA = 0x2, 0xD, 0xC74EBD, 0xC354CD
    """
    Magenta dye, ``#C74EBD``, in fireworks ``#C354CD``.
    """

    LIGHT_BLUE = 0x3, 0xC, 0x3AB3DA, 0x6689D3
    """
    Light blue dye, ``#3AB3DA``, in fireworks ``#6689D3``.
    """

    YELLOW = 0x4, 0xB, 0xFED83D, 0xDECF2A
    """
    Yellow dye, ``#FED83D``, in fireworks ``#DECF2A``.
    """

    LIME = 0x5, 0xA, 0x80C71F, 0x41CD34
    """
    Lime dye, ``#80C71F``, in fireworks ``#41CD34``.
    """

    PINK = 0x6, 0x9, 0xF38BAA, 0xD88198
    """
    Pink dye, ``#F38BAA``, in fireworks ``#D88198``.
    """

    GRAY = 0x7, 0x8, 0x474F52, 0x434343
    """
    Gray dye, ``#474F52``, in fireworks ``#434343``.
    """

    LIGHT_GRAY = 0x8, 0x7, 0x9D9D97, 0xABABAB
    """
    Light gray dye, ``#9D9D97``, in fireworks ``#ABABAB``. Called ``SILVER`` before 1.13.
    """

    CYAN = 0x9, 0x6, 0x169C9C, 0x287697
    """
    Cyan dye, ``#169C9C``, in fireworks ``#287697``.
    """

    PURPLE = 0xA, 0x5, 0x8932B8, 0x7B2FBE
    """
    Purple dye, ``#8932B8``, in fireworks ``#7B2FBE``.
    """

    BLUE = 0xB, 0x4, 0x3C44AA, 0x253192
    """
    Blue dye, ``#3C44AA``, in fireworks ``#253192``.
    """

    BROWN = 0xC, 0x3, 0x835432, 0x51301A
    """
    Brown dye, ``#835432``, in fireworks ``#51301A``.
    """

    GREEN = 0xD, 0x2, 0x5E7C16, 0x3B511A
    """
    Green dye, ``#5E7C16``, in fireworks ``#3B511A``.
    """

    RED = 0xE, 0x1, 0xB02E26, 0xB3312C
    """
    Red dye, ``#B02E26``, in fireworks ``#B3312C``.
    """

    BLACK = 0xF, 0x0, 0x1D1D21, 0x1E1B1B
    """
    Black dye, ``#1D1D21``, in fireworks ``#1E1B1B``.
    """

    def __new__(cls, wool_data: int, dye_data: int, color: int, firework_color: int) -> Self:
        """
        Builds both colors once with the member, so reading them later is a plain lookup.
        """
        member = int.__new__(cls, wool_data)
        member._value_ = wool_data
        member._dye_data = dye_data
        member._color = Color.from_rgb(color)
        member._firework_color = Color.from_rgb(firework_color)

        return member

    @property
    def color(self) -> Color:
        """
        :class:`Color`: The color the dye gives leather armor, sheep, banners and beacon beams.
        """
        return self._color

    @property
    def firework_color(self) -> Color:
        """
        :class:`Color`: The color of a firework star made with this dye.
        """
        return self._firework_color

    @property
    @deprecated("Magic value", category=None)
    def wool_data(self) -> int:
        """
        :class:`int`: The block data of wool in this color before 1.13, the same as the
        member's value.
        """
        return self._value_

    @property
    @deprecated("Magic value", category=None)
    def dye_data(self) -> int:
        """
        :class:`int`: The item data of this dye before 1.13, ``15 - wool_data``.
        """
        return self._dye_data

    @classmethod
    def get_by_color(cls, color: Color) -> DyeColor | None:
        """
        The dye whose :attr:`color` is exactly ``color``, or ``None``. Only the 16 dye colors
        themselves match, a mixed color gives ``None``.
        """
        return BY_COLOR.get(color)

    @classmethod
    def get_by_firework_color(cls, color: Color) -> DyeColor | None:
        """
        The dye whose :attr:`firework_color` is exactly ``color``, or ``None``.
        """
        return BY_FIREWORK_COLOR.get(color)

    @classmethod
    @deprecated("Magic value", category=None)
    def get_by_wool_data(cls, data: int) -> DyeColor | None:
        """
        The dye for wool block data from before 1.13, or ``None``. Only the lowest 8 bits of
        ``data`` count, like Java's byte.
        """
        index = data & 0xFF

        if index >= len(DYES):
            return None

        return DYES[index]

    @classmethod
    @deprecated("Magic value", category=None)
    def get_by_dye_data(cls, data: int) -> DyeColor | None:
        """
        The dye for dye item data from before 1.13, or ``None``. Only the lowest 8 bits of
        ``data`` count, like Java's byte.
        """
        index = data & 0xFF

        if index >= len(DYES):
            return None

        return DYES[len(DYES) - 1 - index]

    @classmethod
    @deprecated("Legacy use only", category=None)
    def legacy_value_of(cls, name: str) -> DyeColor:
        """
        The dye called ``name``, accepting ``SILVER``, the name of :attr:`LIGHT_GRAY` before 1.13.

        Raises
        ------
        ValueError
            No dye has that name.
        """
        if name == "SILVER":
            return DyeColor.LIGHT_GRAY

        try:
            return cls[name]
        except KeyError:
            raise ValueError(f"No enum constant DyeColor.{name}") from None

DYES: Final = tuple(DyeColor)

BY_COLOR: Final = {dye.color: dye for dye in DyeColor}

BY_FIREWORK_COLOR: Final = {dye.firework_color: dye for dye in DyeColor}

__all__ = ["DyeColor"]