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

class BarStyle(IntEnum):
    """
    How a boss bar draws its progress, as one bar or split into notches.

    Members are the overlay ids of the Java protocol and, being plain integers, go into a packet
    as they are, without reading :attr:`value`.
    """

    SOLID = 0
    """
    One continuous bar, ``progress`` in the ``/bossbar`` command.
    """

    SEGMENTED_6 = 1
    """
    Split into 6 notches, ``notched_6`` in the ``/bossbar`` command.
    """

    SEGMENTED_10 = 2
    """
    Split into 10 notches, ``notched_10`` in the ``/bossbar`` command.
    """

    SEGMENTED_12 = 3
    """
    Split into 12 notches, ``notched_12`` in the ``/bossbar`` command.
    """

    SEGMENTED_20 = 4
    """
    Split into 20 notches, ``notched_20`` in the ``/bossbar`` command.
    """

__all__ = ["BarStyle"]