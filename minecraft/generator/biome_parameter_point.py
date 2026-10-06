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
from abc import abstractmethod

from ..util.interface import Interface

class BiomeParameterPoint(Interface):
    """
    The climate noise at one spot of a world, which the vanilla generator uses to pick the
    biome there. A biome provider gets it to pick a biome of its own the same way.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def temperature(self) -> float:
        """
        :class:`float`: How warm the spot is, from snowy biomes at low values to deserts and
        badlands at high ones.
        """

    @property
    @abstractmethod
    def humidity(self) -> float:
        """
        :class:`float`: How wet the spot is, from dry plains and savannas at low values to
        jungles at high ones.
        """

    @property
    @abstractmethod
    def continentalness(self) -> float:
        """
        :class:`float`: How far inland the spot lies, from deep ocean at low values to the
        heart of a continent at high ones.
        """

    @property
    @abstractmethod
    def erosion(self) -> float:
        """
        :class:`float`: How worn down the terrain is, from mountains at low values to flat land
        and swamps at high ones.
        """

    @property
    @abstractmethod
    def depth(self) -> float:
        """
        :class:`float`: How far below the surface the spot lies, about 0 at the surface and
        growing underground, where cave biomes like the deep dark take over.
        """

    @property
    @abstractmethod
    def weirdness(self) -> float:
        """
        :class:`float`: Which variant of a biome appears, like a rarer form of it, and where
        valleys and peaks run.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def max_temperature(self) -> float:
        """
        :class:`float`: The highest possible temperature.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def min_temperature(self) -> float:
        """
        :class:`float`: The lowest possible temperature.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def max_humidity(self) -> float:
        """
        :class:`float`: The highest possible humidity.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def min_humidity(self) -> float:
        """
        :class:`float`: The lowest possible humidity.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def max_continentalness(self) -> float:
        """
        :class:`float`: The highest possible continentalness.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def min_continentalness(self) -> float:
        """
        :class:`float`: The lowest possible continentalness.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def max_erosion(self) -> float:
        """
        :class:`float`: The highest possible erosion.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def min_erosion(self) -> float:
        """
        :class:`float`: The lowest possible erosion.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def max_depth(self) -> float:
        """
        :class:`float`: The highest possible depth.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def min_depth(self) -> float:
        """
        :class:`float`: The lowest possible depth.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def max_weirdness(self) -> float:
        """
        :class:`float`: The highest possible weirdness.
        """

    @property
    @deprecated("No longer supported", category=None)
    @abstractmethod
    def min_weirdness(self) -> float:
        """
        :class:`float`: The lowest possible weirdness.
        """

__all__ = ["BiomeParameterPoint"]