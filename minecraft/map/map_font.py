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

from collections.abc import Iterable
from typing import Final

from ..chat_color import ChatColor

class MapFont:
    """
    A bitmap font that a map canvas draws text with.

    Text for maps knows two special characters. A line break starts a new line, and a color
    string, the section sign followed by a map palette index and a semicolon like ``"§48;"``,
    switches the color of the following characters. These are not :class:`ChatColor` codes.
    """

    __slots__ = ("_byte_widths", "_chars", "_height", "_malleable", "_valid", "_widths")

    def __init__(self) -> None:
        self._chars: dict[str, MapFont.CharacterSprite] = {}
        self._widths: dict[str, int] = {}
        self._byte_widths = bytearray(b"\xff" * 256)
        self._valid = {ChatColor.COLOR_CHAR, "\n"}
        self._height = 0
        self._malleable = True

    def set_char(self, ch: str, sprite: MapFont.CharacterSprite) -> None:
        """
        Sets the sprite for the character ``ch``, replacing an older one. The font grows to the
        height of its tallest sprite.

        Raises
        ------
        ValueError
            ``ch`` is not exactly one character.
        RuntimeError
            The font is fixed, like the built-in Minecraft font.
        """
        if not self._malleable:
            raise RuntimeError("this font is not malleable")

        if len(ch) != 1:
            raise ValueError(f"{ch!r} is not a single character")

        self._chars[ch] = sprite
        self._widths[ch] = sprite.width
        self._valid.add(ch)

        if ord(ch) < 256:
            self._byte_widths[ord(ch)] = sprite.width if 0 <= sprite.width < 255 else 255

        if sprite.height > self._height:
            self._height = sprite.height

    def get_char(self, ch: str) -> MapFont.CharacterSprite | None:
        """
        The sprite for the character ``ch``, or ``None`` if the font has none.
        """
        return self._chars.get(ch)

    def get_width(self, text: str) -> int:
        """
        The width of ``text`` in pixels when drawn with this font, with one pixel of space
        between the characters.

        Like in Bukkit, color strings add no width of their own but their characters still count
        toward the spacing, so colored text measures a little wider than it is drawn.

        Raises
        ------
        ValueError
            ``text`` has a character the font has no sprite for, or a color string without its
            semicolon.
        """
        if not text:
            return 0

        visible = text

        if ChatColor.COLOR_CHAR in text:
            visible = self._visible(text=text)

        if visible.isascii():
            widths = visible.encode().translate(self._byte_widths)
        else:
            encoded = visible.encode("latin-1", "ignore")

            if len(encoded) != len(visible):
                return self._exact_width(text=visible) + len(text) - 1

            widths = encoded.translate(self._byte_widths)

        if 255 in widths:
            return self._exact_width(text=visible) + len(text) - 1

        return sum(widths) + len(text) - 1

    def _visible(self, text: str) -> str:
        """
        ``text`` without its color strings, for :meth:`get_width`. A color string ends at the
        next semicolon, even if another section sign comes first, like in Bukkit.
        """
        if not self._valid.issuperset(text):
            raise ValueError("text contains invalid characters")

        visible: list[str] = []
        start = 0
        color = text.find(ChatColor.COLOR_CHAR)

        while color != -1:
            visible.append(text[start:color])
            start = text.find(";", color) + 1

            if not start:
                raise ValueError("Text contains unterminated color string")

            color = text.find(ChatColor.COLOR_CHAR, start)

        visible.append(text[start:])

        return "".join(visible)

    def _exact_width(self, text: str) -> int:
        """
        The summed width of the sprites for ``text``, one character at a time. :meth:`get_width`
        only comes here for what its byte table cannot hold: text beyond Latin-1, characters
        without a sprite and sprites wider than 254 pixels.
        """
        try:
            return sum(map(self._widths.__getitem__, text))
        except KeyError:
            if self._valid.issuperset(text):
                raise ValueError("text contains a line break, measure each line on its own") from None

            raise ValueError("text contains invalid characters") from None

    @property
    def height(self) -> int:
        """
        :class:`int`: The height of the font in pixels, the height of its tallest sprite.
        """
        return self._height

    def is_valid(self, text: str) -> bool:
        """
        Whether the font has a sprite for every character of ``text``, apart from line breaks
        and section signs.
        """
        return self._valid.issuperset(text)

    class CharacterSprite:
        """
        The pixels of one character of a :class:`MapFont`.

        Parameters
        ----------
        width: :class:`int`
            The width of the character in pixels.
        height: :class:`int`
            The height of the character in pixels.
        data: Iterable[:class:`bool`]
            Whether each pixel is solid, row by row from the top left.

        Raises
        ------
        ValueError
            ``data`` does not have ``width * height`` pixels.
        """

        __slots__ = ("_data", "height", "width")

        width: Final[int]
        """
        :class:`int`: The width of the character in pixels.
        """

        height: Final[int]
        """
        :class:`int`: The height of the character in pixels.
        """

        def __init__(self, width: int, height: int, data: Iterable[bool]) -> None:
            self._data: Final = tuple(data)

            if len(self._data) != width * height:
                raise ValueError("size of data does not match dimensions")

            self.width = width
            self.height = height

        def get(self, row: int, column: int) -> bool:
            """
            Whether the pixel in ``row`` and ``column`` is solid. Pixels outside the sprite are
            transparent.
            """
            if 0 <= row < self.height and 0 <= column < self.width:
                return self._data[row * self.width + column]

            return False

__all__ = ["MapFont"]