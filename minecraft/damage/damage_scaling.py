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

class DamageScaling(StrEnum):
    """
    Whether a damage type hurts players more or less depending on the difficulty.

    Scaled damage to a player is dropped on Peaceful, halved plus one on Easy but never above
    the original, left as it is on Normal and multiplied by 1.5 on Hard. Members are the names
    data packs use for ``scaling`` in a damage type, so a platform can write them as they are.
    """

    NEVER = "never"
    """
    The damage is the same on every difficulty.
    """

    WHEN_CAUSED_BY_LIVING_NON_PLAYER = "when_caused_by_living_non_player"
    """
    Scaled only when a living entity that is not a player causes the damage, so mobs hit harder
    on Hard while players hit every difficulty alike. Most vanilla damage types use this.
    """

    ALWAYS = "always"
    """
    Scaled no matter what causes the damage, like explosions.
    """

__all__ = ["DamageScaling"]