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

from typing import Protocol

from ..event.listener import Listener
from ..event.event import Event

class EventExecutor[L: Listener = Listener, E: Event = Event](Protocol):
    """
    Runs a handler for an event, given the listener the handler belongs to.

    A plain method of a :class:`Listener` already fits, since its ``self`` is the listener, so a
    decorated method is registered as it is and costs a single call per event. A lambda fits as
    well, for registering a handler without decorating anything.
    """

    def __call__(self, listener: L, event: E, /) -> object:
        """
        Handles ``event`` for ``listener``. An awaitable it returns is awaited when the event is
        asynchronous, anything else is ignored.
        """

__all__ = ["EventExecutor"]