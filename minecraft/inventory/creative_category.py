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

from enum import Enum

class CreativeCategory(Enum):
    """
    A tab of the creative inventory as it was before Minecraft 1.19.3.

    Since then the client builds its creative tabs by itself and the server no longer knows
    which tab an item belongs to, so asking an item type for its category is deprecated on
    newer servers.
    """

    BUILDING_BLOCKS = 0
    """
    Building blocks like dirt, bricks, planks, ores and slabs.
    """

    DECORATIONS = 1
    """
    Decoration like candles, saplings, flowers, fences, walls and carpets.
    """

    REDSTONE = 2
    """
    Redstone parts like buttons, levers, pressure plates, repeaters and pistons.
    """

    TRANSPORTATION = 3
    """
    Transport like minecarts, rails, boats and elytra.
    """

    MISC = 4
    """
    Everything that fits nowhere else, like gems, dyes, spawn eggs, music discs and banner
    patterns.
    """

    FOOD = 5
    """
    Food like meat, berries and edible mob drops.
    """

    TOOLS = 6
    """
    Tools like pickaxes, axes, hoes and flint and steel, with their enchanted books.
    """

    COMBAT = 7
    """
    Weapons and armor like swords, bows and tipped arrows, with their enchanted books.
    """

    BREWING = 8
    """
    Potions of every kind and the ingredients to brew them.
    """

__all__ = ["CreativeCategory"]