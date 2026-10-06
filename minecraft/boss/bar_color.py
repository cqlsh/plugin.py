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

class BarColor(IntEnum):
    """
    The color of a boss bar.

    Members are the color ids of the Java protocol and, being plain integers, go into a packet
    as they are, without reading :attr:`value`.
    """

    PINK = 0
    """
    Pink, ``pink`` in the ``/bossbar`` command and the color of the Ender Dragon's bar.
    """

    BLUE = 1
    """
    Blue, ``blue`` in the ``/bossbar`` command.
    """

    RED = 2
    """
    Red, ``red`` in the ``/bossbar`` command and the color of a raid's bar.
    """

    GREEN = 3
    """
    Green, ``green`` in the ``/bossbar`` command.
    """

    YELLOW = 4
    """
    Yellow, ``yellow`` in the ``/bossbar`` command.
    """

    PURPLE = 5
    """
    Purple, ``purple`` in the ``/bossbar`` command and the color of the wither's bar.
    """

    WHITE = 6
    """
    White, ``white`` in the ``/bossbar`` command and the color a bar made with it starts with.
    """

__all__ = ["BarColor"]