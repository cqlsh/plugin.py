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

from enum import StrEnum

class HeightMap(StrEnum):
    """
    Which blocks count when looking for the highest block of a column.

    Members are vanilla's names, the keys of the ``Heightmaps`` in chunk files, so a platform
    hands a member to the server as it is. The ``_WG`` maps only exist while a chunk generates.
    """

    MOTION_BLOCKING = "MOTION_BLOCKING"
    """
    The highest block that blocks movement or holds a fluid, leaves included. Rain and snow
    fall down to it.
    """

    MOTION_BLOCKING_NO_LEAVES = "MOTION_BLOCKING_NO_LEAVES"
    """
    Like :attr:`MOTION_BLOCKING`, but looking through leaves. Mobs spawning on the surface pick
    their height from it, so they do not land on tree tops.
    """

    OCEAN_FLOOR = "OCEAN_FLOOR"
    """
    The highest block that blocks movement, looking through water and lava, so the ground at
    the bottom of a sea.
    """

    OCEAN_FLOOR_WG = "OCEAN_FLOOR_WG"
    """
    :attr:`OCEAN_FLOOR` while the chunk is still generating.
    """

    WORLD_SURFACE = "WORLD_SURFACE"
    """
    The highest block that is not air, water included.
    """

    WORLD_SURFACE_WG = "WORLD_SURFACE_WG"
    """
    :attr:`WORLD_SURFACE` while the chunk is still generating.
    """

__all__ = ["HeightMap"]