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

from warnings import deprecated
from typing import Final, Self
from enum import StrEnum

from .equipment_slot import EquipmentSlot

class EquipmentSlotGroup(StrEnum):
    """
    A set of equipment slots an attribute modifier applies in, such as all armor slots.

    Members are the names the game writes for an attribute modifier's ``slot``, so a modifier
    for :attr:`ARMOR` counts while the item is worn on feet, legs, chest or head. Bukkit marks
    this type experimental, so it may still change between versions.
    """

    _value_: str
    _slots: frozenset[EquipmentSlot]
    _example: EquipmentSlot

    ANY = "any", EquipmentSlot.HAND, *EquipmentSlot
    """
    Every slot.
    """

    MAINHAND = "mainhand", EquipmentSlot.HAND
    """
    The main hand.
    """

    OFFHAND = "offhand", EquipmentSlot.OFF_HAND
    """
    The off hand.
    """

    HAND = "hand", EquipmentSlot.HAND, EquipmentSlot.OFF_HAND
    """
    Either hand.
    """

    FEET = "feet", EquipmentSlot.FEET
    """
    The boots slot.
    """

    LEGS = "legs", EquipmentSlot.LEGS
    """
    The leggings slot.
    """

    CHEST = "chest", EquipmentSlot.CHEST
    """
    The chestplate slot.
    """

    HEAD = "head", EquipmentSlot.HEAD
    """
    The helmet slot.
    """

    ARMOR = "armor", EquipmentSlot.CHEST, EquipmentSlot.FEET, EquipmentSlot.LEGS, EquipmentSlot.HEAD
    """
    Any of the four armor slots of a player or mob, but not an animal's body armor.
    """

    SADDLE = "saddle", EquipmentSlot.SADDLE
    """
    The saddle slot.
    """

    def __new__(cls, key: str, example: EquipmentSlot, *slots: EquipmentSlot) -> Self:
        """
        Keeps the group's slots as a set, so checking a slot is one hash lookup, and the first
        slot as the example Bukkit hands out.
        """
        member = str.__new__(cls, key)
        member._value_ = key
        member._slots = frozenset([example, *slots])
        member._example = example

        return member

    def test(self, slot: EquipmentSlot) -> bool:
        """
        Whether ``slot`` belongs to this group, the same as ``slot in group``.
        """
        return slot in self._slots

    def __contains__(self, slot: object) -> bool:
        return slot in self._slots

    @property
    @deprecated("For internal compatibility use only", category=None)
    def example(self) -> EquipmentSlot:
        """
        :class:`EquipmentSlot`: One slot of the group, like :attr:`EquipmentSlot.CHEST` for
        :attr:`ARMOR`.
        """
        return self._example

    @classmethod
    def of(cls, slot: EquipmentSlot) -> EquipmentSlotGroup:
        """
        The group that stands for ``slot`` alone. Body armor has no group of its own and falls
        under :attr:`ARMOR`. In Bukkit this is ``EquipmentSlot.getGroup()``, moved here so the
        two types do not depend on each other.
        """
        return GROUP_BY_SLOT[slot]

    @classmethod
    def get_by_name(cls, name: str) -> Self | None:
        """
        The group called ``name``, in any case, or ``None``.
        """
        member = cls._value2member_map_.get(name.lower())

        if isinstance(member, cls):
            return member

        return None

GROUP_BY_SLOT: Final = (
    EquipmentSlotGroup.MAINHAND,
    EquipmentSlotGroup.OFFHAND,
    EquipmentSlotGroup.FEET,
    EquipmentSlotGroup.LEGS,
    EquipmentSlotGroup.CHEST,
    EquipmentSlotGroup.HEAD,
    EquipmentSlotGroup.ARMOR,
    EquipmentSlotGroup.SADDLE
)

__all__ = ["EquipmentSlotGroup"]