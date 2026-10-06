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

from typing import Never, Self, overload
from collections.abc import Callable

from .event_priority import EventPriority

class EventHandler:
    """
    Marks a method of a :class:`Listener` as the handler for the event its second parameter is
    annotated with.

    Works bare as ``@EventHandler`` and with options as ``@EventHandler(priority=...)``. The
    method is returned unchanged, so calling it directly costs nothing extra and IDEs keep its
    signature. Handlers of asynchronous events may be ``async def``, handlers of synchronous
    events may not, which the plugin manager checks when the listener is registered.

    Parameters
    ----------
    priority: :class:`EventPriority`
        When the handler runs compared to the others for the same event.
    ignore_cancelled: :class:`bool`
        Whether to skip the handler while the event is cancelled.
    """

    __slots__ = ("ignore_cancelled", "priority")

    priority: EventPriority
    """
    :class:`EventPriority`: When the handler runs compared to the others for the same event.
    Defaults to :attr:`EventPriority.NORMAL`.
    """

    ignore_cancelled: bool
    """
    :class:`bool`: Whether the handler is skipped while the event is cancelled, so it only sees
    events that will actually happen. Has no effect on events that are not
    :class:`Cancellable`. Defaults to ``False``.
    """

    @overload
    def __new__[F: Callable[[Never, Never], object]](cls, function: F, /) -> F:
        ...

    @overload
    def __new__(cls, /, *, priority: EventPriority = EventPriority.NORMAL, ignore_cancelled: bool = False) -> Self:
        ...

    def __new__(
        cls,
        function: Callable[[Never, Never], object] | None = None,
        /,
        *,
        priority: EventPriority = EventPriority.NORMAL,
        ignore_cancelled: bool = False
    ) -> Self | Callable[[Never, Never], object]:
        handler = super().__new__(cls)
        handler.priority = priority
        handler.ignore_cancelled = ignore_cancelled

        if function is None:
            return handler

        return handler(function)

    def __call__[F: Callable[[Never, Never], object]](self, function: F, /) -> F:
        """
        Tags ``function`` with this marker and hands it back untouched.
        """
        setattr(function, "__event_handler__", self)

        return function

    @classmethod
    def of(cls, function: object) -> Self | None:
        """
        The marker ``function`` was decorated with, or ``None``. The plugin manager uses it to
        find handlers on a listener instead of guessing from method names.
        """
        marker = getattr(function, "__event_handler__", None)

        if isinstance(marker, cls):
            return marker

        return None

__all__ = ["EventHandler"]