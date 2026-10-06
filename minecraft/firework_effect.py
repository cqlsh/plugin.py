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

from collections.abc import Iterable, Mapping
from typing import Final, Self, cast
from enum import IntEnum

from .configuration.serialization.configuration_serializable import ConfigurationSerializable
from .color import Color

class FireworkEffect(ConfigurationSerializable):
    """
    One explosion of a firework rocket or firework star: its shape, colors and extras.

    Effects are immutable. Build one with :meth:`builder` like in Bukkit, or directly by calling
    the class with keywords.

    Parameters
    ----------
    type: :class:`FireworkEffect.Type`
        The shape of the explosion.
    colors: Iterable[:class:`Color`]
        The colors of the explosion, at least one.
    fade_colors: Iterable[:class:`Color`]
        The colors the particles fade to, none by default.
    flicker: :class:`bool`
        Whether the particles twinkle.
    trail: :class:`bool`
        Whether the particles leave a trail.

    Raises
    ------
    ValueError
        ``colors`` is empty.
    """

    __slots__ = ("colors", "fade_colors", "flicker", "trail", "type")

    type: Final[FireworkEffect.Type]
    """
    :class:`FireworkEffect.Type`: The shape of the explosion.
    """

    colors: Final[tuple[Color, ...]]
    """
    Tuple[:class:`Color`, ...]: The colors of the explosion, never empty.
    """

    fade_colors: Final[tuple[Color, ...]]
    """
    Tuple[:class:`Color`, ...]: The colors the particles fade to, empty if they keep their
    color.
    """

    flicker: Final[bool]
    """
    :class:`bool`: Whether the particles twinkle, which glowstone dust adds when crafting.
    """

    trail: Final[bool]
    """
    :class:`bool`: Whether the particles leave a trail, which a diamond adds when crafting.
    """

    def __init__(
        self,
        type: FireworkEffect.Type,
        colors: Iterable[Color],
        fade_colors: Iterable[Color] = (),
        flicker: bool = False,
        trail: bool = False
    ) -> None:
        self.colors = tuple(colors)

        if not self.colors:
            raise ValueError("Cannot make FireworkEffect without any color")

        self.type = type
        self.fade_colors = tuple(fade_colors)
        self.flicker = flicker
        self.trail = trail

    @classmethod
    def builder(cls) -> FireworkEffect.Builder:
        """
        A new builder for an effect, starting as a :attr:`Type.BALL` without colors.
        """
        return FireworkEffect.Builder()

    def serialize(self) -> Mapping[str, object]:
        return {
            "flicker": self.flicker,
            "trail": self.trail,
            "colors": list(self.colors),
            "fade-colors": list(self.fade_colors),
            "type": self.type.name
        }

    @classmethod
    def deserialize(cls, data: Mapping[str, object]) -> Self:
        name = data.get("type")
        flicker = data.get("flicker")
        trail = data.get("trail")

        if not isinstance(name, str) or name not in FireworkEffect.Type.__members__:
            raise ValueError(f"{name} is not a firework effect type")

        if not isinstance(flicker, bool) or not isinstance(trail, bool):
            raise ValueError("flicker and trail have to be booleans")

        return cls(
            type=FireworkEffect.Type[name],
            colors=cls._colors(data=data, key="colors"),
            fade_colors=cls._colors(data=data, key="fade-colors"),
            flicker=flicker,
            trail=trail
        )

    @classmethod
    def _colors(cls, data: Mapping[str, object], key: str) -> list[Color]:
        """
        Reads a list of colors from a config entry with the error Bukkit gives for anything else.
        """
        values = data.get(key)

        if not isinstance(values, Iterable):
            raise ValueError(f"{key} is not a list of colors")

        colors: list[Color] = []

        for value in cast(Iterable[object], values):
            if not isinstance(value, Color):
                raise ValueError(f"{value} is not a Color in {values}")

            colors.append(value)

        return colors

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True

        if not isinstance(other, FireworkEffect):
            return False

        return (
            self.type is other.type
            and self.flicker == other.flicker
            and self.trail == other.trail
            and self.colors == other.colors
            and self.fade_colors == other.fade_colors
        )

    def __hash__(self) -> int:
        return hash((self.type, self.flicker, self.trail, self.colors, self.fade_colors))

    def __repr__(self) -> str:
        return (
            f"<FireworkEffect type={self.type.name} colors={self.colors} fade_colors={self.fade_colors} "
            f"flicker={self.flicker} trail={self.trail}>"
        )

    class Type(IntEnum):
        """
        The shape of a firework explosion.

        Members are the shape ids that Java and Bedrock both use, so a platform sends them as
        they are.
        """

        BALL = 0
        """
        A small ball, the shape of a star crafted without a shape ingredient.
        """

        BALL_LARGE = 1
        """
        A large ball, crafted with a fire charge.
        """

        STAR = 2
        """
        A star, crafted with a gold nugget.
        """

        BURST = 4
        """
        A burst of particles, crafted with a feather.
        """

        CREEPER = 3
        """
        A creeper face, crafted with any mob head.
        """

    class Builder:
        """
        Collects the parts of a :class:`FireworkEffect`. Every method returns the builder, so
        calls chain until :meth:`build`.
        """

        __slots__ = ("_colors", "_fade_colors", "_flicker", "_trail", "_type")

        def __init__(self) -> None:
            self._type = FireworkEffect.Type.BALL
            self._colors: list[Color] = []
            self._fade_colors: list[Color] = []
            self._flicker = False
            self._trail = False

        def with_type(self, type: FireworkEffect.Type) -> Self:
            """
            Sets the shape, Bukkit's ``with(Type)``, a name Python reserves.
            """
            self._type = type

            return self

        def with_flicker(self) -> Self:
            """
            Makes the particles twinkle.
            """
            self._flicker = True

            return self

        def flicker(self, flicker: bool) -> Self:
            """
            Sets whether the particles twinkle.
            """
            self._flicker = flicker

            return self

        def with_trail(self) -> Self:
            """
            Makes the particles leave a trail.
            """
            self._trail = True

            return self

        def trail(self, trail: bool) -> Self:
            """
            Sets whether the particles leave a trail.
            """
            self._trail = trail

            return self

        def with_color(self, *colors: Color) -> Self:
            """
            Adds one or more colors of the explosion.
            """
            self._colors.extend(colors)

            return self

        def with_fade(self, *colors: Color) -> Self:
            """
            Adds one or more colors the particles fade to.
            """
            self._fade_colors.extend(colors)

            return self

        def build(self) -> FireworkEffect:
            """
            The finished effect.

            Raises
            ------
            ValueError
                No color was added.
            """
            return FireworkEffect(
                type=self._type,
                colors=self._colors,
                fade_colors=self._fade_colors,
                flicker=self._flicker,
                trail=self._trail
            )

__all__ = ["FireworkEffect"]