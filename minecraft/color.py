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

from typing import TYPE_CHECKING, ClassVar, Final, Self, overload
from collections.abc import Mapping
from struct import Struct

from .configuration.serialization.configuration_serializable import ConfigurationSerializable

if TYPE_CHECKING:
    from .dye_color import DyeColor

FLOAT: Final = Struct("<f")

class Color(ConfigurationSerializable):
    """
    An immutable color with alpha, red, green and blue channels from 0 to 255.

    Colors are made through the ``from_*`` class methods, never by calling the class. Red,
    green and blue are kept together as one ``0xRRGGBB`` integer next to alpha, which keeps every
    number small enough for CPython's fast integer path, so :meth:`as_rgb` for a packet and
    comparing two colors are single integer operations.
    """

    __slots__ = ("_alpha", "_rgb")

    _alpha: int
    _rgb: int

    WHITE: ClassVar[Color]
    """
    :class:`Color`: ``#FFFFFF``.
    """

    SILVER: ClassVar[Color]
    """
    :class:`Color`: ``#C0C0C0``.
    """

    GRAY: ClassVar[Color]
    """
    :class:`Color`: ``#808080``.
    """

    BLACK: ClassVar[Color]
    """
    :class:`Color`: ``#000000``.
    """

    RED: ClassVar[Color]
    """
    :class:`Color`: ``#FF0000``.
    """

    MAROON: ClassVar[Color]
    """
    :class:`Color`: ``#800000``.
    """

    YELLOW: ClassVar[Color]
    """
    :class:`Color`: ``#FFFF00``.
    """

    OLIVE: ClassVar[Color]
    """
    :class:`Color`: ``#808000``.
    """

    LIME: ClassVar[Color]
    """
    :class:`Color`: ``#00FF00``.
    """

    GREEN: ClassVar[Color]
    """
    :class:`Color`: ``#008000``.
    """

    AQUA: ClassVar[Color]
    """
    :class:`Color`: ``#00FFFF``.
    """

    TEAL: ClassVar[Color]
    """
    :class:`Color`: ``#008080``.
    """

    BLUE: ClassVar[Color]
    """
    :class:`Color`: ``#0000FF``.
    """

    NAVY: ClassVar[Color]
    """
    :class:`Color`: ``#000080``.
    """

    FUCHSIA: ClassVar[Color]
    """
    :class:`Color`: ``#FF00FF``.
    """

    PURPLE: ClassVar[Color]
    """
    :class:`Color`: ``#800080``.
    """

    ORANGE: ClassVar[Color]
    """
    :class:`Color`: ``#FFA500``.
    """

    @classmethod
    def _create(cls, rgb: int, alpha: int, /) -> Self:
        """
        Wraps already checked channels into a color, for every factory except :meth:`from_rgb`.
        """
        color = object.__new__(cls)
        color._rgb = rgb
        color._alpha = alpha

        return color

    @classmethod
    def _check(cls, alpha: int, red: int, green: int, blue: int) -> None:
        """
        Raises the error for the first channel outside 0 to 255. Only called once the quick
        combined check of all channels failed, so valid colors never get here.
        """
        for name, value in [("Alpha", alpha), ("Red", red), ("Green", green), ("Blue", blue)]:
            if not 0 <= value <= 255:
                raise ValueError(f"{name}[{value}] is not between 0-255")

    @overload
    @classmethod
    def from_argb(cls, argb: int, /) -> Self:
        ...

    @overload
    @classmethod
    def from_argb(cls, alpha: int, red: int, green: int, blue: int, /) -> Self:
        ...

    @classmethod
    def from_argb(
        cls,
        argb_or_alpha: int,
        red: int | None = None,
        green: int | None = None,
        blue: int | None = None,
        /
    ) -> Self:
        """
        A color from one ``0xAARRGGBB`` integer, of which only the lowest 32 bits count, or from
        its four channels.

        Raises
        ------
        ValueError
            A channel lies outside 0 to 255.
        """
        if red is None or green is None or blue is None:
            return cls._create(argb_or_alpha & 0xFFFFFF, argb_or_alpha >> 24 & 0xFF)

        if (argb_or_alpha | red | green | blue) & ~0xFF:
            cls._check(alpha=argb_or_alpha, red=red, green=green, blue=blue)

        return cls._create(red << 16 | green << 8 | blue, argb_or_alpha)

    @overload
    @classmethod
    def from_rgb(cls, rgb: int, /) -> Self:
        ...

    @overload
    @classmethod
    def from_rgb(cls, red: int, green: int, blue: int, /) -> Self:
        ...

    @classmethod
    def from_rgb(cls, rgb_or_red: int, green: int | None = None, blue: int | None = None, /) -> Self:
        """
        An opaque color from one ``0xRRGGBB`` integer or from its three channels. The factory
        plugins call most, so it builds the color itself instead of going through another call.

        Raises
        ------
        ValueError
            The integer uses bits above ``0xFFFFFF`` or a channel lies outside 0 to 255.
        """
        color = object.__new__(cls)
        color._alpha = 255

        if green is None or blue is None:
            if rgb_or_red >> 24:
                raise ValueError(f"Extraneous data in: {rgb_or_red}")

            color._rgb = rgb_or_red

            return color

        if (rgb_or_red | green | blue) & ~0xFF:
            cls._check(alpha=255, red=rgb_or_red, green=green, blue=blue)

        color._rgb = rgb_or_red << 16 | green << 8 | blue

        return color

    @overload
    @classmethod
    def from_bgr(cls, bgr: int, /) -> Self:
        ...

    @overload
    @classmethod
    def from_bgr(cls, blue: int, green: int, red: int, /) -> Self:
        ...

    @classmethod
    def from_bgr(cls, bgr_or_blue: int, green: int | None = None, red: int | None = None, /) -> Self:
        """
        An opaque color from one ``0xBBGGRR`` integer or from its three channels in that order.

        Raises
        ------
        ValueError
            The integer uses bits above ``0xFFFFFF`` or a channel lies outside 0 to 255.
        """
        if green is None or red is None:
            if bgr_or_blue >> 24:
                raise ValueError(f"Extraneous data in: {bgr_or_blue}")

            return cls._create((bgr_or_blue & 0xFF) << 16 | bgr_or_blue & 0xFF00 | bgr_or_blue >> 16, 255)

        if (bgr_or_blue | green | red) & ~0xFF:
            cls._check(alpha=255, red=red, green=green, blue=bgr_or_blue)

        return cls._create(red << 16 | green << 8 | bgr_or_blue, 255)

    @property
    def alpha(self) -> int:
        """
        :class:`int`: How opaque the color is, 255 for fully opaque. Most of the game ignores
        alpha, map colors and text shadows are among the few places that use it.
        """
        return self._alpha

    @property
    def red(self) -> int:
        """
        :class:`int`: The red channel.
        """
        return self._rgb >> 16

    @property
    def green(self) -> int:
        """
        :class:`int`: The green channel.
        """
        return self._rgb >> 8 & 0xFF

    @property
    def blue(self) -> int:
        """
        :class:`int`: The blue channel.
        """
        return self._rgb & 0xFF

    def with_alpha(self, alpha: int) -> Color:
        """
        A copy with ``alpha`` replaced, Bukkit's ``setAlpha``. Colors never change in place.

        Raises
        ------
        ValueError
            ``alpha`` lies outside 0 to 255.
        """
        if alpha & ~0xFF:
            raise ValueError(f"Alpha[{alpha}] is not between 0-255")

        return Color._create(self._rgb, alpha)

    def with_red(self, red: int) -> Color:
        """
        A copy with ``red`` replaced, Bukkit's ``setRed``.

        Raises
        ------
        ValueError
            ``red`` lies outside 0 to 255.
        """
        if red & ~0xFF:
            raise ValueError(f"Red[{red}] is not between 0-255")

        return Color._create(self._rgb & 0x00FFFF | red << 16, self._alpha)

    def with_green(self, green: int) -> Color:
        """
        A copy with ``green`` replaced, Bukkit's ``setGreen``.

        Raises
        ------
        ValueError
            ``green`` lies outside 0 to 255.
        """
        if green & ~0xFF:
            raise ValueError(f"Green[{green}] is not between 0-255")

        return Color._create(self._rgb & 0xFF00FF | green << 8, self._alpha)

    def with_blue(self, blue: int) -> Color:
        """
        A copy with ``blue`` replaced, Bukkit's ``setBlue``.

        Raises
        ------
        ValueError
            ``blue`` lies outside 0 to 255.
        """
        if blue & ~0xFF:
            raise ValueError(f"Blue[{blue}] is not between 0-255")

        return Color._create(self._rgb & 0xFFFF00 | blue, self._alpha)

    def as_rgb(self) -> int:
        """
        The color as ``0xRRGGBB``, the form leather armor, potions and dust particles are sent
        in.
        """
        return self._rgb

    def as_argb(self) -> int:
        """
        The color as ``0xAARRGGBB``.
        """
        return self._alpha << 24 | self._rgb

    def as_bgr(self) -> int:
        """
        The color as ``0xBBGGRR``.
        """
        rgb = self._rgb

        return (rgb & 0xFF) << 16 | rgb & 0xFF00 | rgb >> 16

    def mix_colors(self, *colors: Color) -> Color:
        """
        Mixes this color with ``colors`` the way the game mixes dyes on leather armor: the
        channels are averaged, then scaled back up so the brightest channel keeps the average
        brightness of the inputs. Mixing only black gives black. The scaling runs in 32-bit
        floats like Bukkit's, since 64-bit floats round about one mix in eight differently.
        """
        rgb = self._rgb
        total_red = rgb >> 16
        total_green = rgb >> 8 & 0xFF
        total_blue = rgb & 0xFF
        total_max = max(total_red, total_green, total_blue)

        for color in colors:
            rgb = color._rgb
            red = rgb >> 16
            green = rgb >> 8 & 0xFF
            blue = rgb & 0xFF

            total_red += red
            total_green += green
            total_blue += blue
            total_max += max(red, green, blue)

        count = len(colors) + 1
        average_red = total_red // count
        average_green = total_green // count
        average_blue = total_blue // count
        maximum_of_averages = max(average_red, average_green, average_blue)

        if maximum_of_averages == 0:
            return Color._create(0, 255)

        gain = Color._float32(value=(total_max // count) / maximum_of_averages)
        red = int(Color._float32(value=average_red * gain))
        green = int(Color._float32(value=average_green * gain))
        blue = int(Color._float32(value=average_blue * gain))

        return Color._create(red << 16 | green << 8 | blue, 255)

    def mix_dyes(self, *dyes: DyeColor) -> Color:
        """
        Mixes this color with the colors of ``dyes``, like dyeing leather armor of this color
        with those dyes in a crafting grid.
        """
        return self.mix_colors(*[dye.color for dye in dyes])

    @classmethod
    def _float32(cls, value: float) -> float:
        """
        Rounds ``value`` to the nearest 32-bit float, the precision Bukkit mixes colors in.
        """
        return FLOAT.unpack(FLOAT.pack(value))[0]

    def serialize(self) -> Mapping[str, object]:
        return {"ALPHA": self._alpha, "RED": self.red, "BLUE": self.blue, "GREEN": self.green}

    @classmethod
    def deserialize(cls, data: Mapping[str, object]) -> Self:
        return cls.from_argb(
            cls._channel(data=data, key="ALPHA", default=255),
            cls._channel(data=data, key="RED"),
            cls._channel(data=data, key="GREEN"),
            cls._channel(data=data, key="BLUE")
        )

    @classmethod
    def _channel(cls, data: Mapping[str, object], key: str, default: int | None = None) -> int:
        """
        Reads one channel from a config entry with the same errors Bukkit gives.
        """
        value = data.get(key, default)

        if value is None:
            raise ValueError(f"{key} not in map {dict(data)}")

        if isinstance(value, bool) or not isinstance(value, int | float):
            raise ValueError(f"{key}({value}) is not a number")

        return int(value)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Color) and self._rgb == other._rgb and self._alpha == other._alpha

    def __hash__(self) -> int:
        return self._rgb

    def __repr__(self) -> str:
        return f"<Color argb=0x{self._alpha:02X}{self._rgb:06X}>"

Color.WHITE = Color.from_rgb(0xFFFFFF)
Color.SILVER = Color.from_rgb(0xC0C0C0)
Color.GRAY = Color.from_rgb(0x808080)
Color.BLACK = Color.from_rgb(0x000000)
Color.RED = Color.from_rgb(0xFF0000)
Color.MAROON = Color.from_rgb(0x800000)
Color.YELLOW = Color.from_rgb(0xFFFF00)
Color.OLIVE = Color.from_rgb(0x808000)
Color.LIME = Color.from_rgb(0x00FF00)
Color.GREEN = Color.from_rgb(0x008000)
Color.AQUA = Color.from_rgb(0x00FFFF)
Color.TEAL = Color.from_rgb(0x008080)
Color.BLUE = Color.from_rgb(0x0000FF)
Color.NAVY = Color.from_rgb(0x000080)
Color.FUCHSIA = Color.from_rgb(0xFF00FF)
Color.PURPLE = Color.from_rgb(0x800080)
Color.ORANGE = Color.from_rgb(0xFFA500)

__all__ = ["Color"]