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

from typing import ClassVar, Final, Self, overload
from enum import IntEnum, nonmember
from dataclasses import dataclass
from warnings import deprecated

SEMITONES: Final = 12

@dataclass(frozen=True, slots=True, init=False, eq=False, repr=False)
class Note:
    """
    One of the 25 notes a note block can play, from F#0 up to F#2.

    Octaves start at F#, so F#1 is twelve semitones above F#0. Each of the 25 notes exists only
    once and is handed out again on every construction, so creating a note is a lookup and two
    notes are equal exactly when they are the same object. Notes are frozen, since every plugin
    shares them.

    Parameters
    ----------
    note: :class:`int`
        The note block's ``note`` value, 0 to 24.
    octave: :class:`int`
        The octave, 0 to 2. Octave 2 only holds F#.
    tone: :class:`Note.Tone`
        The tone within the octave.
    sharped: :class:`bool`
        Whether the tone is raised by a semitone. B# and E# become C and F.

    Raises
    ------
    ValueError
        The note lies outside F#0 to F#2.
    """

    _cache: ClassVar[dict[int, Note]] = {}

    _id: int

    octave: int
    """
    :class:`int`: The octave, 0 to 2.
    """

    tone: Note.Tone
    """
    :class:`Note.Tone`: The tone within the octave, without its sharp.
    """

    is_sharped: bool
    """
    :class:`bool`: Whether the note is the sharp of :attr:`tone`, like F#.
    """

    pitch: float
    """
    :class:`float`: The pitch to play the note with, the value ``/playsound`` and sound methods
    expect. It doubles every octave, from 0.5 at F#0 over 1.0 at F#1 to 2.0 at F#2.
    """

    @overload
    def __new__(cls, note: int, /) -> Note:
        ...

    @overload
    def __new__(cls, octave: int, tone: Note.Tone, sharped: bool, /) -> Note:
        ...

    def __new__(cls, note_or_octave: int, tone: Note.Tone | None = None, sharped: bool = False, /) -> Note:
        note = note_or_octave

        if tone is not None:
            note = note_or_octave * SEMITONES + (tone + (1 if sharped else 0)) % SEMITONES

            if not 0 <= note <= 24:
                raise ValueError("Tone and octave have to be between F#0 and F#2")

        try:
            return cls._cache[note]
        except KeyError:
            if not 0 <= note <= 24:
                raise ValueError("The note value has to be between 0 and 24.") from None

            return cls._cache.setdefault(note, cls._create(note=note))

    @classmethod
    def _create(cls, note: int) -> Note:
        """
        Builds a note the first time it is asked for. The cache keeps it from then on, and
        ``setdefault`` makes sure two threads racing here still end up with the same object.
        """
        position = note % SEMITONES
        tone = Note.Tone(position)
        instance = object.__new__(cls)

        object.__setattr__(instance, "_id", note)
        object.__setattr__(instance, "octave", note // SEMITONES)
        object.__setattr__(instance, "tone", tone)
        object.__setattr__(instance, "is_sharped", position != int(tone))
        object.__setattr__(instance, "pitch", 2 ** ((note - SEMITONES) / SEMITONES))

        return instance

    @classmethod
    def flat(cls, octave: int, tone: Note.Tone) -> Note:
        """
        The flat of ``tone`` in ``octave``, such as A flat, which is the same note as G#.

        Raises
        ------
        ValueError
            ``octave`` is 2, which holds no flats.
        """
        if octave == 2:
            raise ValueError("Octave cannot be 2 for flats")

        return cls(cls.natural(octave=octave, tone=tone)._id - 1)

    @classmethod
    def sharp(cls, octave: int, tone: Note.Tone) -> Note:
        """
        The sharp of ``tone`` in ``octave``, such as A#.

        Raises
        ------
        ValueError
            The note lies outside F#0 to F#2.
        """
        return cls(octave, tone, True)

    @classmethod
    def natural(cls, octave: int, tone: Note.Tone) -> Note:
        """
        ``tone`` in ``octave`` without sharp or flat, such as A.

        Raises
        ------
        ValueError
            ``octave`` is 2, which holds only F#.
        """
        if octave == 2:
            raise ValueError("Octave cannot be 2 for naturals")

        return cls(octave, tone, False)

    def sharped(self) -> Note:
        """
        The note a semitone higher.

        Raises
        ------
        ValueError
            This is F#2, the highest note.
        """
        if self._id == 24:
            raise ValueError("This note cannot be sharped because it is the highest known note!")

        return Note(self._id + 1)

    def flattened(self) -> Note:
        """
        The note a semitone lower.

        Raises
        ------
        ValueError
            This is F#0, the lowest note.
        """
        if self._id == 0:
            raise ValueError("This note cannot be flattened because it is the lowest known note!")

        return Note(self._id - 1)

    @property
    @deprecated("Magic value, use octave, tone and is_sharped", category=None)
    def id(self) -> int:
        """
        :class:`int`: The note block's ``note`` value, 0 to 24.
        """
        return self._id

    def __repr__(self) -> str:
        sharp = "#" if self.is_sharped else ""

        return f"<Note {self.tone.name}{sharp}{self.octave}>"

    class Tone(IntEnum):
        """
        A tone within an octave, without its sharp.

        Members are the semitone positions inside a note block octave, which starts at F# with 0,
        as plain integers, and every sharp position resolves to its tone as well, so
        ``Note.Tone(2)`` is :attr:`G`.
        """

        _value_: int
        _sharpable: bool

        TONES_COUNT = nonmember(SEMITONES)
        """
        :class:`int`: The number of semitones in an octave, sharps included.
        """

        G = 1, True
        A = 3, True
        B = 5, False
        C = 6, True
        D = 8, True
        E = 10, False
        F = 11, True

        def __new__(cls, position: int, sharpable: bool) -> Self:
            """
            Keeps whether the tone has a sharp and registers the sharp's position as an alias,
            the way Bukkit's lookup by id also finds the sharped tones.
            """
            member = int.__new__(cls, position)
            member._value_ = position
            member._sharpable = sharpable

            if sharpable:
                member._add_value_alias_((position + 1) % SEMITONES)

            return member

        @property
        def sharpable(self) -> bool:
            """
            :class:`bool`: Whether the tone has a sharp. B and E have none, B# is C and E# is F.
            """
            return self._sharpable

        @deprecated("Magic value", category=None)
        def get_id(self, sharped: bool = False) -> int:
            """
            The tone's position in the octave, one higher if ``sharped`` and the tone has a sharp.
            """
            if sharped and self._sharpable:
                return (self._value_ + 1) % SEMITONES

            return self._value_

        @deprecated("Magic value", category=None)
        def is_sharped(self, id: int) -> bool:
            """
            Whether ``id`` is the position of this tone's sharp rather than of the tone itself.

            Raises
            ------
            ValueError
                ``id`` belongs to neither the tone nor its sharp.
            """
            if id == self._value_:
                return False

            if self._sharpable and id == (self._value_ + 1) % SEMITONES:
                return True

            raise ValueError("The id isn't matching to the tone.")

        @classmethod
        @deprecated("Magic value", category=None)
        def get_by_id(cls, id: int) -> Self | None:
            """
            The tone at position ``id`` of an octave, sharps included, or ``None``.
            """
            member = cls._value2member_map_.get(id)

            if isinstance(member, cls):
                return member

            return None

__all__ = ["Note"]