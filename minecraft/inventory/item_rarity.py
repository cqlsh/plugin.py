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

class ItemRarity(IntEnum):
    """
    How rare an item is, which decides the default color of its name.

    Members are ordered from least to most rare and are the rarity ids of the Java protocol, so
    ``rarity >= ItemRarity.RARE`` compares rarity directly. An enchanted item shows its name one
    step rarer, but at least as :attr:`RARE`.
    """

    COMMON = 0
    """
    White name, the rarity of most items.
    """

    UNCOMMON = 1
    """
    Yellow name, like a bottle o' enchanting or a mob head.
    """

    RARE = 2
    """
    Aqua name, like a beacon or a conduit.
    """

    EPIC = 3
    """
    Light purple name, like an enchanted golden apple or a dragon egg.
    """

__all__ = ["ItemRarity"]