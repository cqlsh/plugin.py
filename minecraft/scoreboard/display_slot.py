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

class DisplaySlot(IntEnum):
    """
    Where an objective shows up on the screen.

    Members are the slot ids of the Java protocol and, being plain integers, go into a packet as
    they are. A player in a team with a color sees the sidebar for that color instead of the
    plain :attr:`SIDEBAR`, if one is set. Bedrock only knows :attr:`PLAYER_LIST`,
    :attr:`SIDEBAR` and :attr:`BELOW_NAME`.
    """

    BELOW_NAME = 2
    """
    Below the name tag of each player, ``below_name`` in the ``/scoreboard`` command.
    """

    PLAYER_LIST = 0
    """
    Next to the names in the player list, ``list`` in the ``/scoreboard`` command.
    """

    SIDEBAR = 1
    """
    The sidebar on the right of the screen, ``sidebar`` in the ``/scoreboard`` command.
    """

    SIDEBAR_BLACK = 3
    """
    The sidebar for players in a black team, ``sidebar.team.black``.
    """

    SIDEBAR_DARK_BLUE = 4
    """
    The sidebar for players in a dark blue team, ``sidebar.team.dark_blue``.
    """

    SIDEBAR_DARK_GREEN = 5
    """
    The sidebar for players in a dark green team, ``sidebar.team.dark_green``.
    """

    SIDEBAR_DARK_AQUA = 6
    """
    The sidebar for players in a dark aqua team, ``sidebar.team.dark_aqua``.
    """

    SIDEBAR_DARK_RED = 7
    """
    The sidebar for players in a dark red team, ``sidebar.team.dark_red``.
    """

    SIDEBAR_DARK_PURPLE = 8
    """
    The sidebar for players in a dark purple team, ``sidebar.team.dark_purple``.
    """

    SIDEBAR_GOLD = 9
    """
    The sidebar for players in a gold team, ``sidebar.team.gold``.
    """

    SIDEBAR_GRAY = 10
    """
    The sidebar for players in a gray team, ``sidebar.team.gray``.
    """

    SIDEBAR_DARK_GRAY = 11
    """
    The sidebar for players in a dark gray team, ``sidebar.team.dark_gray``.
    """

    SIDEBAR_BLUE = 12
    """
    The sidebar for players in a blue team, ``sidebar.team.blue``.
    """

    SIDEBAR_GREEN = 13
    """
    The sidebar for players in a green team, ``sidebar.team.green``.
    """

    SIDEBAR_AQUA = 14
    """
    The sidebar for players in an aqua team, ``sidebar.team.aqua``.
    """

    SIDEBAR_RED = 15
    """
    The sidebar for players in a red team, ``sidebar.team.red``.
    """

    SIDEBAR_LIGHT_PURPLE = 16
    """
    The sidebar for players in a light purple team, ``sidebar.team.light_purple``.
    """

    SIDEBAR_YELLOW = 17
    """
    The sidebar for players in a yellow team, ``sidebar.team.yellow``.
    """

    SIDEBAR_WHITE = 18
    """
    The sidebar for players in a white team, ``sidebar.team.white``.
    """

__all__ = ["DisplaySlot"]