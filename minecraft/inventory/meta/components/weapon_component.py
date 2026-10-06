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

from abc import abstractmethod

from ....configuration.serialization.configuration_serializable import ConfigurationSerializable

class WeaponComponent(ConfigurationSerializable):
    """
    The ``minecraft:weapon`` item component, which makes any item wear down when it hits and
    lets it knock a shield out of use.

    The component exists from Minecraft 1.21.5 on. Bukkit marks it experimental, so it may still
    change between versions.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def item_damage_per_attack(self) -> int:
        """
        :class:`int`: How much durability the item loses per hit. Swords lose 1, axes 2, and 0
        keeps a weapon from wearing down by attacking. Setting a negative value raises
        :exc:`ValueError`.
        """

    @item_damage_per_attack.setter
    @abstractmethod
    def item_damage_per_attack(self, damage: int) -> None:
        ...

    @property
    @abstractmethod
    def disable_blocking_for_seconds(self) -> float:
        """
        :class:`float`: How long a hit keeps the target from blocking with a shield, in seconds.
        Axes use 5, 0 never disables the shield.
        """

    @disable_blocking_for_seconds.setter
    @abstractmethod
    def disable_blocking_for_seconds(self, time: float) -> None:
        ...

__all__ = ["WeaponComponent"]