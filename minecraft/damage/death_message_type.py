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

class DeathMessageType(StrEnum):
    """
    Which kind of death message a damage type produces.

    Members are the names data packs use for ``death_message_type`` in a damage type, so a
    platform can write them as they are.
    """

    DEFAULT = "default"
    """
    The regular message built from the damage type and whoever caused it, such as "Steve was
    slain by Zombie".
    """

    FALL_VARIANTS = "fall_variants"
    """
    A message about the fall itself, naming what the player fell from or who knocked them off,
    such as ``death.fell.assist.item``. Fall damage uses it.
    """

    INTENTIONAL_GAME_DESIGN = "intentional_game_design"
    """
    The message with the "[Intentional Game Design]" link, used when a bed or respawn anchor
    explodes in a dimension where it cannot set the spawn point.
    """

__all__ = ["DeathMessageType"]