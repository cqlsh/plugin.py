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

from typing import Final
from enum import StrEnum

class WorldType(StrEnum):
    """
    The terrain a world generates with.

    Members are Bukkit's names for the types, the ``level-type`` values of older
    ``server.properties`` files, so a member is its own name: ``WorldType.NORMAL == "DEFAULT"``.
    """

    NORMAL = "DEFAULT"
    """
    The usual terrain, ``minecraft:normal`` in newer ``server.properties`` files.
    """

    FLAT = "FLAT"
    """
    A superflat world built from the layers in its generator settings, ``minecraft:flat``.
    """

    LARGE_BIOMES = "LARGEBIOMES"
    """
    The usual terrain with much larger biomes, ``minecraft:large_biomes``.
    """

    AMPLIFIED = "AMPLIFIED"
    """
    The usual terrain stretched to extreme heights, ``minecraft:amplified``. It takes far more
    work to generate and to render than a normal world.
    """

    @classmethod
    def get_by_name(cls, name: str) -> WorldType | None:
        """
        The type with the given name in any case, like ``"largeBiomes"``, or ``None``.
        """
        world_type = BY_NAME.get(name)

        if world_type is None:
            return BY_NAME.get(name.upper())

        return world_type

BY_NAME: Final = {
    name: world_type
    for world_type in WorldType
    for name in (str(world_type), world_type.lower())
}

__all__ = ["WorldType"]