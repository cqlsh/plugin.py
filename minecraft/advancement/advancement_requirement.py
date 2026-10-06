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

from collections.abc import Sequence
from abc import abstractmethod

from ..util.interface import Interface

class AdvancementRequirement(Interface):
    """
    One requirement of an advancement: a group of criteria of which a player has to complete at
    least one.

    An advancement is done once every one of its requirements is met, so the requirements
    combine with "and" while the criteria inside one combine with "or".
    """

    __slots__ = ()

    @property
    @abstractmethod
    def required_criteria(self) -> Sequence[str]:
        """
        Sequence[:class:`str`]: The names of the criteria in this group, as the advancement
        file names them.
        """

    @property
    def strict(self) -> bool:
        """
        :class:`bool`: Whether the group holds a single criterion, which a player then has to
        complete itself.
        """
        return len(self.required_criteria) == 1

__all__ = ["AdvancementRequirement"]