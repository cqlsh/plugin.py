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

class InvalidDescriptionException(Exception):
    """
    Raised when a ``plugin.yml`` misses a required entry or has one of the wrong type.

    The message names the entry, such as ``"version is not defined"`` or ``"load is not a valid
    choice"``. The plugin manager logs it with the file name and skips that plugin, the others
    still load.

    Parameters
    ----------
    message: :class:`str`
        What is wrong with the file. Defaults to ``"Invalid plugin.yml"``, like in Bukkit.
    """

    def __init__(self, message: str = "Invalid plugin.yml") -> None:
        Exception.__init__(self, message)

__all__ = ["InvalidDescriptionException"]