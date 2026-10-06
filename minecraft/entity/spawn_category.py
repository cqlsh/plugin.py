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

class SpawnCategory(StrEnum):
    """
    A group of mobs that share a mob cap and the rules for natural spawning.

    Members are the vanilla category names that data packs use for a biome's ``spawners``, which
    differ from Bukkit's for animals and water animals. The caps given below are the vanilla
    defaults per player, which servers can change per category.
    """

    MONSTER = "monster"
    """
    Hostile mobs like zombies, creepers and witches. Cap 70.
    """

    ANIMAL = "creature"
    """
    Passive land animals like cows, striders and turtles. Cap 10, and they do not despawn when
    players move away.
    """

    WATER_ANIMAL = "water_creature"
    """
    Squids and dolphins. Cap 5.
    """

    WATER_AMBIENT = "water_ambient"
    """
    Fish like cod, salmon, pufferfish and tropical fish. Cap 20.
    """

    WATER_UNDERGROUND_CREATURE = "underground_water_creature"
    """
    Glow squids in underground water. Cap 5.
    """

    AMBIENT = "ambient"
    """
    Bats. Cap 15.
    """

    AXOLOTL = "axolotls"
    """
    Axolotls, which have a category and cap of their own. Cap 5.
    """

    MISC = "misc"
    """
    Everything that does not spawn naturally as a mob, like players, armor stands and boats. No
    cap.
    """

__all__ = ["SpawnCategory"]