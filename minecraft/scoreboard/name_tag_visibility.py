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

class NameTagVisibility(IntEnum):
    """
    Who sees the name tags of a team's players.

    Deprecated since Bukkit 1.9, use :class:`Team.OptionStatus` with the name tag option
    instead. It only remains for the deprecated name tag visibility of a :class:`Team`.

    Members are the visibility ids of the Java protocol and, being plain integers, go into a
    packet as they are.
    """

    ALWAYS = 0
    """
    Everyone sees the name tag, ``always`` in the ``/team`` command.
    """

    NEVER = 1
    """
    Nobody sees the name tag, ``never`` in the ``/team`` command.
    """

    HIDE_FOR_OTHER_TEAMS = 2
    """
    Hidden from players of other teams, so only teammates see it, ``hideForOtherTeams`` in the
    ``/team`` command.
    """

    HIDE_FOR_OWN_TEAM = 3
    """
    Hidden from teammates, ``hideForOwnTeam`` in the ``/team`` command.
    """

__all__ = ["NameTagVisibility"]