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

from ..util.interface import Interface

class Sittable(Interface):
    """
    An animal that can sit still: cats, wolves and parrots, which sit when their owner tells
    them to, as well as camels, foxes and pandas.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def sitting(self) -> bool:
        """
        :class:`bool`: Whether the animal sits. Making it sit drops the path it was following,
        so it stops where it is.
        """

    @sitting.setter
    @abstractmethod
    def sitting(self, sitting: bool) -> None:
        ...

__all__ = ["Sittable"]