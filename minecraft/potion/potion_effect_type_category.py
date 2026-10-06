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

class PotionEffectTypeCategory(Enum):
    """
    Whether a potion effect helps or harms the entity that has it.

    The game colors an effect's line in item tooltips by its category.
    """

    BENEFICIAL = 0
    """
    Helps the entity, like Regeneration, Absorption or Fire Resistance. Shown in blue.
    """

    HARMFUL = 1
    """
    Hurts or hinders the entity, like Blindness, Wither or Levitation. Shown in red.
    """

    NEUTRAL = 2
    """
    Neither helps nor hurts, like Glowing or Bad Omen. Shown in blue.
    """

__all__ = ["PotionEffectTypeCategory"]