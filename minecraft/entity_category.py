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

class EntityCategory(Enum):
    """
    A group of mobs that enchantments, potions and other mobs treat differently.

    From Minecraft 1.20.5 on the game groups entities through entity type tags such as
    ``#minecraft:undead`` instead, so reading a living entity's category is deprecated there.
    The enum stays for plugins written against older servers.
    """

    NONE = 0
    """
    Not in any group, nothing special applies.
    """

    UNDEAD = 1
    """
    Zombies, skeletons and the like: healed by Harming and hurt by Healing, immune to poison and
    drowning, hurt extra by Smite and ignored by the Wither. Most of them burn in daylight and
    sink in water, except drowned, phantoms and the Wither itself.
    """

    ARTHROPOD = 2
    """
    Spiders, silverfish, endermites and bees: Bane of Arthropods hurts them extra and slows
    them. Spiders are immune to poison.
    """

    ILLAGER = 3
    """
    Raid mobs like pillagers, vindicators and evokers: immune to evoker fangs, hostile to
    villagers, wandering traders, iron golems and players, and spared by a vindicator named
    Johnny.
    """

    WATER = 4
    """
    Mobs that live underwater, except drowned: hurt extra by Impaling, swimming instead of
    floating or sinking. All but dolphins are immune to drowning, and all but guardians and
    turtles suffocate after long on land.
    """

__all__ = ["EntityCategory"]