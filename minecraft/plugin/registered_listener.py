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

from collections.abc import Callable
from inspect import isawaitable
from types import MethodType
from typing import Final

from ..event.event_exception import EventException
from ..event.event_priority import EventPriority
from ..event.cancellable import Cancellable
from .event_executor import EventExecutor
from ..event.listener import Listener
from ..event.event import Event
from .plugin import Plugin

class RegisteredListener:
    """
    One handler registered for an event, together with the listener and plugin it belongs to.

    The plugin manager creates one per handler and keeps it in the event's handler list, sorted
    by :attr:`priority`. The executor is bound to the listener once here, so running the
    handler for an event is a single call.

    Parameters
    ----------
    listener: :class:`Listener`
        The listener the handler belongs to.
    executor: :class:`EventExecutor`
        Runs the handler, usually the plain method of the listener's class.
    priority: :class:`EventPriority`
        When the handler runs compared to the others for the same event.
    plugin: :class:`Plugin`
        The plugin that registered the handler.
    ignore_cancelled: :class:`bool`
        Whether to skip the handler while the event is cancelled.
    """

    __slots__ = ("callback", "ignore_cancelled", "listener", "plugin", "priority")

    listener: Final[Listener]
    """
    :class:`Listener`: The listener the handler belongs to.
    """

    plugin: Final[Plugin]
    """
    :class:`Plugin`: The plugin that registered the handler. Disabling it removes this
    registration from every handler list.
    """

    priority: Final[EventPriority]
    """
    :class:`EventPriority`: When the handler runs compared to the others for the same event.
    """

    ignore_cancelled: Final[bool]
    """
    :class:`bool`: Whether the handler is skipped while the event is cancelled.
    """

    callback: Final[Callable[[Event], object]]
    """
    :class:`collections.abc.Callable`: The executor bound to the listener. Calling it with an
    event runs the handler without the cancel check or error wrapping of :meth:`call_event`.
    """

    def __init__[L: Listener, E: Event](
        self,
        listener: L,
        executor: EventExecutor[L, E],
        priority: EventPriority,
        plugin: Plugin,
        ignore_cancelled: bool
    ) -> None:
        self.listener = listener
        self.plugin = plugin
        self.priority = priority
        self.ignore_cancelled = ignore_cancelled
        self.callback = MethodType(executor, listener)

    def call_event(self, event: Event, /) -> None:
        """
        Runs the handler for ``event``, unless it ignores cancelled events and ``event`` is
        cancelled.

        Raises
        ------
        EventException
            The handler raised, its exception is chained as ``__cause__``.
        """
        if self.ignore_cancelled and isinstance(event, Cancellable) and event.cancelled:
            return

        try:
            self.callback(event)
        except Exception as error:
            raise self._failure(event=event) from error

    async def call_event_async(self, event: Event, /) -> None:
        """
        |coro|

        Runs the handler like :meth:`call_event` and awaits what it returns if that is
        awaitable. Asynchronous events go through here, since their handlers may be coroutines.

        Raises
        ------
        EventException
            The handler raised, its exception is chained as ``__cause__``.
        """
        if self.ignore_cancelled and isinstance(event, Cancellable) and event.cancelled:
            return

        try:
            result = self.callback(event)

            if result is not None and isawaitable(result):
                await result
        except Exception as error:
            raise self._failure(event=event) from error

    def _failure(self, event: Event) -> EventException:
        """
        Builds the exception for a failed handler, so both call paths report it the same way.
        """
        return EventException(f"Could not pass event {event.event_name} to {self.plugin.name}")

__all__ = ["RegisteredListener"]