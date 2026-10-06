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

from typing import ClassVar
from enum import Enum

class Event:
    """
    Something that happened on the server which plugins can react to.

    The plugin manager hands a fired event to its handlers in priority order. This class keeps
    no storage of its own, so events with ``__slots__`` list every field they set, including
    :attr:`asynchronous` when they can fire off the main thread.
    """

    __slots__ = ()

    asynchronous: bool = False
    """
    :class:`bool`: Whether the event is fired on the plugin event loop instead of the main
    server thread. Its handlers may be coroutines and are awaited in priority order, several
    such events can be in flight at once, and a handler that blocks instead of awaiting holds
    up all of them. Firing it from inside a synchronous event raises :exc:`RuntimeError`.
    """

    event_name: ClassVar[str] = "Event"
    """
    :class:`str`: The name of the event's class, such as ``"PlayerJoinEvent"``. A class can set
    its own in the class body, its subclasses still report their own class name.
    """

    def __init_subclass__(cls) -> None:
        """
        Stamps :attr:`event_name` onto every event class, so reading it is a plain class
        attribute instead of a property call.
        """
        super().__init_subclass__()

        if "event_name" not in cls.__dict__:
            cls.event_name = cls.__name__

    class Result(Enum):
        """
        What happens with an action that a handler can deny or force.

        Events like :class:`PlayerInteractEvent` use it where a plain cancel is not enough, for
        example to block the clicked block but still let the item in hand be used.
        """

        DENY = 0
        """
        The action does not happen, or gets undone if it already did. Some actions cannot be
        denied.
        """

        DEFAULT = 1
        """
        The server decides as it would without any plugin.
        """

        ALLOW = 2
        """
        The action happens even where the server would normally refuse it. Some actions cannot
        be forced.
        """

__all__ = ["Event"]