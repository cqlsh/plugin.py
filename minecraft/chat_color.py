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

from typing import Final, Self, overload
from enum import StrEnum, nonmember

COLOR_CHAR: Final = "\u00a7"

STRIP_COLOR_PATTERN: Final = re.compile(f"(?i){COLOR_CHAR}[0-9A-FK-ORX]")

TRANSLATABLE_CODES: Final = "0123456789AaBbCcDdEeFfKkLlMmNnOoRrXx"

TRANSLATED_CODES: Final = {code: COLOR_CHAR + code.lower() for code in TRANSLATABLE_CODES}

HEX_DIGITS: Final = frozenset("0123456789ABCDEFabcdef")

class ChatColor(StrEnum):
    """
    A legacy formatting code for chat, names, scoreboards and item lore.

    Members are the two-character codes themselves, the section sign followed by the code, so
    ``ChatColor.RED + "Hello"`` and ``f"{ChatColor.RED}Hello"`` build formatted text just like
    Java's string concatenation. Bedrock clients know a few extra colors and show ``§m`` and
    ``§n`` as colors instead of strikethrough and underline.
    """

    _value_: str
    _char: str
    _is_format: bool

    COLOR_CHAR = nonmember(COLOR_CHAR)
    """
    :class:`str`: The section sign that starts every code.
    """

    BLACK = "0"
    """
    Black, ``#000000``.
    """

    DARK_BLUE = "1"
    """
    Dark blue, ``#0000AA``.
    """

    DARK_GREEN = "2"
    """
    Dark green, ``#00AA00``.
    """

    DARK_AQUA = "3"
    """
    Dark aqua, ``#00AAAA``.
    """

    DARK_RED = "4"
    """
    Dark red, ``#AA0000``.
    """

    DARK_PURPLE = "5"
    """
    Dark purple, ``#AA00AA``.
    """

    GOLD = "6"
    """
    Gold, ``#FFAA00``.
    """

    GRAY = "7"
    """
    Gray, ``#AAAAAA``.
    """

    DARK_GRAY = "8"
    """
    Dark gray, ``#555555``.
    """

    BLUE = "9"
    """
    Blue, ``#5555FF``.
    """

    GREEN = "a"
    """
    Green, ``#55FF55``.
    """

    AQUA = "b"
    """
    Aqua, ``#55FFFF``.
    """

    RED = "c"
    """
    Red, ``#FF5555``.
    """

    LIGHT_PURPLE = "d"
    """
    Light purple, ``#FF55FF``.
    """

    YELLOW = "e"
    """
    Yellow, ``#FFFF55``.
    """

    WHITE = "f"
    """
    White, ``#FFFFFF``.
    """

    MAGIC = "k", True
    """
    Obfuscated text that keeps changing into random characters.
    """

    BOLD = "l", True
    """
    Bold text.
    """

    STRIKETHROUGH = "m", True
    """
    Struck through text. Bedrock shows a color instead.
    """

    UNDERLINE = "n", True
    """
    Underlined text. Bedrock shows a color instead.
    """

    ITALIC = "o", True
    """
    Italic text.
    """

    RESET = "r"
    """
    Back to the default color without formatting. A color code also ends every format before it,
    so ``§l§cA`` is red but not bold.
    """

    def __new__(cls, char: str, is_format: bool = False) -> Self:
        """
        Makes the member the full code, so it works as a string, and keeps its letter apart.
        """
        member = str.__new__(cls, COLOR_CHAR + char)
        member._value_ = COLOR_CHAR + char
        member._char = char
        member._is_format = is_format

        return member

    @property
    def char(self) -> str:
        """
        :class:`str`: The letter or digit after the section sign, such as ``"c"`` for
        :attr:`RED`.
        """
        return self._char

    @property
    def is_format(self) -> bool:
        """
        :class:`bool`: Whether the code formats text instead of coloring it, like :attr:`BOLD`.
        """
        return self._is_format

    @property
    def is_color(self) -> bool:
        """
        :class:`bool`: Whether the code is a color, so neither a format nor :attr:`RESET`.
        """
        return not self._is_format and self is not ChatColor.RESET

    @classmethod
    def get_by_char(cls, code: str) -> ChatColor | None:
        """
        The code for the letter or digit at the start of ``code``, or ``None``. Only lowercase
        letters match, like in Bukkit.

        Raises
        ------
        ValueError
            ``code`` is empty.
        """
        if not code:
            raise ValueError("Code must have at least one char")

        return BY_CHAR.get(code[0])

    @overload
    @classmethod
    def strip_color(cls, input: str) -> str:
        ...

    @overload
    @classmethod
    def strip_color(cls, input: None) -> None:
        ...

    @classmethod
    def strip_color(cls, input: str | None) -> str | None:
        """
        ``input`` without any formatting codes, in either case, or ``None`` for ``None``. Useful
        to compare or log text that players can color.
        """
        if input is None:
            return None

        if COLOR_CHAR not in input:
            return input

        return STRIP_COLOR_PATTERN.sub("", input)

    @classmethod
    def translate_alternate_color_codes(cls, alt_color_char: str, text: str) -> str:
        """
        ``text`` with every ``alt_color_char`` that stands before a valid code replaced by the
        section sign, so ``"&cHello"`` becomes ``"§cHello"``. The code letter is lowercased, an
        ``alt_color_char`` before anything else stays as it is.
        """
        if alt_color_char not in text:
            return text

        if alt_color_char in TRANSLATABLE_CODES:
            return cls._translate_one_by_one(alt_color_char=alt_color_char, text=text)

        parts = text.split(alt_color_char)
        translated = [parts[0]]

        for part in parts[1:]:
            code = TRANSLATED_CODES.get(part[:1])

            if code is None:
                translated.append(alt_color_char + part)
                continue

            translated.append(code + part[1:])

        return "".join(translated)

    @classmethod
    def _translate_one_by_one(cls, alt_color_char: str, text: str) -> str:
        """
        Bukkit's character by character translation, needed when ``alt_color_char`` is itself a
        code letter and one replacement can create the next. The split in
        :meth:`translate_alternate_color_codes` is faster for every other character.
        """
        chars = list(text)

        for index in range(len(chars) - 1):
            if chars[index] == alt_color_char and chars[index + 1] in TRANSLATABLE_CODES:
                chars[index] = COLOR_CHAR
                chars[index + 1] = chars[index + 1].lower()

        return "".join(chars)

    @classmethod
    def get_last_colors(cls, input: str) -> str:
        """
        The codes in effect at the end of ``input``: the last color, hex or named, with any
        formats that follow it. Prepending them to the next line of a wrapped text keeps its
        look.
        """
        result = ""
        index = input.rfind(COLOR_CHAR, 0, len(input) - 1)

        while index != -1:
            hex_color = cls._hex_color(input=input, index=index)

            if hex_color is not None:
                return hex_color + result

            color = BY_CHAR.get(input[index + 1])

            if color is not None:
                result = color + result

                if color.is_color or color is ChatColor.RESET:
                    return result

            index = input.rfind(COLOR_CHAR, 0, index)

        return result

    @classmethod
    def _hex_color(cls, input: str, index: int) -> str | None:
        """
        The hex color ``§x§R§R§G§G§B§B`` that ends with the section sign at ``index``, or
        ``None``. Spigot writes hex colors this way in legacy text.
        """
        if index < 12 or input[index - 12] != COLOR_CHAR or input[index - 11] != "x":
            return None

        for position in range(index - 10, index + 1, 2):
            if input[position] != COLOR_CHAR or input[position + 1] not in HEX_DIGITS:
                return None

        return input[index - 12:index + 2]

BY_CHAR: Final = {color.char: color for color in ChatColor}

__all__ = ["ChatColor"]