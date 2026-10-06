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

class EquipmentSlot(IntEnum):
    """
    A slot an entity holds or wears an item in.

    Members are the slot ids of the Java protocol's equipment packet and, being plain integers,
    go into it as they are.
    """

    HAND = 0
    """
    The main hand.
    """

    OFF_HAND = 1
    """
    The off hand, which a player swaps with the main hand by pressing F.
    """

    FEET = 2
    """
    Boots.
    """

    LEGS = 3
    """
    Leggings.
    """

    CHEST = 4
    """
    A chestplate or an elytra.
    """

    HEAD = 5
    """
    A helmet, a carved pumpkin or a mob head, or any item put there by a command.
    """

    BODY = 6
    """
    Armor that covers a whole animal, like horse armor, wolf armor or a llama's carpet. Only
    entities that can wear such armor have this slot.
    """

    SADDLE = 7
    """
    The saddle of horses, pigs, striders, camels and the like. A slot of its own from
    Minecraft 1.21.5 on.
    """

__all__ = ["EquipmentSlot"]