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

from abc import abstractmethod
from enum import StrEnum

from ..util.interface import Interface

class PlayerTextures(Interface):
    """
    The skin and cape stored in a player profile.

    Texture URLs have to point to Mojang's texture server ``textures.minecraft.net``, clients
    load nothing from elsewhere. Only Mojang can sign textures, so changing any of them drops
    :attr:`timestamp` and the signature.
    """

    __slots__ = ()

    class SkinModel(StrEnum):
        """
        The arm width of a skin, valued by the variant names of Mojang's skin API.
        """

        CLASSIC = "classic"
        """
        Arms four pixels wide, like Steve's.
        """

        SLIM = "slim"
        """
        Arms three pixels wide, like Alex's.
        """

    @property
    @abstractmethod
    def empty(self) -> bool:
        """
        :class:`bool`: Whether the profile stores neither a skin nor a cape.
        """

    @abstractmethod
    def clear(self) -> None:
        """
        Removes skin and cape, so the player shows a default skin.
        """

    @property
    @abstractmethod
    def skin(self) -> str | None:
        """
        :class:`str` | ``None``: The URL of the skin, such as
        ``http://textures.minecraft.net/texture/b3fbd454...``, or ``None`` if none is set.
        """

    @abstractmethod
    def set_skin(self, skin_url: str | None, skin_model: PlayerTextures.SkinModel | None = None) -> None:
        """
        Sets the skin and its model. ``None`` as ``skin_url`` removes the skin, ``None`` as
        ``skin_model`` means :attr:`SkinModel.CLASSIC`.
        """

    @property
    @abstractmethod
    def skin_model(self) -> PlayerTextures.SkinModel:
        """
        :class:`PlayerTextures.SkinModel`: The model of the skin, :attr:`SkinModel.CLASSIC` if no
        skin is set.
        """

    @property
    @abstractmethod
    def cape(self) -> str | None:
        """
        :class:`str` | ``None``: The URL of the cape, or ``None`` if none is set. Setting
        ``None`` removes it.
        """

    @cape.setter
    @abstractmethod
    def cape(self, cape_url: str | None) -> None:
        ...

    @property
    @abstractmethod
    def timestamp(self) -> int:
        """
        :class:`int`: When Mojang last updated the textures, in milliseconds since 1970, or 0 if
        unknown or changed since.
        """

    @property
    @abstractmethod
    def signed(self) -> bool:
        """
        :class:`bool`: Whether the textures carry a valid signature from Mojang, which is only
        the case while nobody changed them.
        """

__all__ = ["PlayerTextures"]