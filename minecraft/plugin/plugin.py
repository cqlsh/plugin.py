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

from abc import ABC, abstractmethod
from logging import Logger
from pathlib import Path

class Plugin(ABC):
    """
    A plugin loaded by the server.

    The server only talks to plugins through this interface: it calls :meth:`on_load` for every
    plugin first, then :meth:`on_enable` in load order, and :meth:`on_disable` on shutdown or
    reload. Plugins are compared by identity, so two loaded copies of the same plugin are two
    different plugins.
    """

    __slots__ = ()

    @property
    @abstractmethod
    def name(self) -> str:
        """
        :class:`str`: The name from the plugin's description. It also names the data folder and
        prefixes every log line of the plugin.
        """

    @property
    @abstractmethod
    def enabled(self) -> bool:
        """
        :class:`bool`: Whether the plugin is enabled. Handlers and tasks of a disabled plugin do
        not run, and registering new ones raises :exc:`IllegalPluginAccessException`.
        """

    @property
    @abstractmethod
    def logger(self) -> Logger:
        """
        :class:`logging.Logger`: The plugin's logger, whose records carry the plugin's name.
        """

    @property
    @abstractmethod
    def data_folder(self) -> Path:
        """
        :class:`pathlib.Path`: The folder for the plugin's own files, ``plugins/<name>``. It is
        not created up front, only once the plugin saves something into it.
        """

    @abstractmethod
    def on_load(self) -> None:
        """
        Called once the plugin is loaded. Every plugin gets this call before any plugin is
        enabled, so other plugins and the worlds may not be usable yet.
        """

    @abstractmethod
    def on_enable(self) -> None:
        """
        Called when the plugin is enabled, the place to register listeners and commands.
        """

    @abstractmethod
    def on_disable(self) -> None:
        """
        Called when the plugin is disabled on shutdown or reload. Its listeners and scheduled
        tasks are removed right after this returns.
        """

__all__ = ["Plugin"]