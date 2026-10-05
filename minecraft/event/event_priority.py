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

class EventPriority(IntEnum):
    """
    When a listener runs compared to the other listeners of the same event.

    Handlers run from :attr:`LOWEST` up to :attr:`MONITOR`, so a higher priority sees the event
    later and has more say over the outcome. Members are plain integers, which lets a handler
    list use them directly as sort keys and list indices.
    """

    LOWEST = 0
    """
    Runs first. Handy for setting a default that other plugins are expected to override.
    """

    LOW = 1
    """
    Runs before the bulk of plugins at :attr:`NORMAL` and can still be overruled by them.
    """

    NORMAL = 2
    """
    The priority a handler gets when none is given.
    """

    HIGH = 3
    """
    Runs after :attr:`NORMAL`, so it can undo or replace what most plugins decided.
    """

    HIGHEST = 4
    """
    The last priority allowed to change the event, so a cancellation or value set here has the
    final say.
    """

    MONITOR = 5
    """
    Runs last and only observes, for logging or statistics. Changing the event here breaks the
    promise that the outcome seen at :attr:`HIGHEST` is the one that happens.
    """

__all__ = ["EventPriority"]