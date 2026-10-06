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

class RenderType(IntEnum):
    """
    How the client shows the scores of an objective.

    Members are the render type ids of the Java protocol and, being plain integers, go into a
    packet as they are. The lowercase member name is the render type in the ``/scoreboard``
    command.
    """

    INTEGER = 0
    """
    Scores as numbers, ``integer`` in the ``/scoreboard`` command.
    """

    HEARTS = 1
    """
    Scores as hearts, ``hearts`` in the ``/scoreboard`` command. Only the player list draws
    hearts, the sidebar and the line below a name still show the number.
    """

__all__ = ["RenderType"]