# -*- coding: utf-8 -*-
"""Various data models used within teragested."""
from abc import ABC, abstractmethod
from typing import List, Optional, Union

import attr

from .enums import (
    CasePatternFlag,
    CommandFlags,
    CommandType,
    RedirectionFlags,
    RedirectionInstruction,
    Token,
    WordFlags,
)


@attr.s
class Word:
    word: str = attr.ib()
    flags: WordFlags = attr.ib(default=0)


WordList = List[Word]
Redirectee = Union[int, Word]


@attr.s
class Redirect:
    """Structure describing a redirection.

    If a `redirector` is negative, the parser or translator encountered an out-
    of-range file descriptor.
    """

    #: descriptor or varname to be redirected
    redirector: Redirectee = attr.ib()
    rflags: RedirectionFlags = attr.ib()
    #: what to do with the information
    instruction: RedirectionInstruction = attr.ib()
    #: file descriptor or filename
    redirectee: Redirectee = attr.ib()
    #: The word that appeared in <<foo
    here_doc_eof: Optional[str] = attr.ib(default=None)


@attr.s
class Element:
    word: Optional[Word] = attr.ib(default=None)
    redirect: List[Redirect] = attr.ib(factory=list)


@attr.s
class Command(ABC):
    @property
    @abstractmethod
    def type(self) -> CommandType:
        raise NotImplementedError

    flags: CommandFlags = attr.ib(default=0)
    line: int = attr.ib(default=-1)
    redirects: List[Redirect] = attr.ib(factory=list)


@attr.s
class Connection(Command):
    type = CommandType.Connection
    first: Command = attr.ib(default=None)
    second: Command = attr.ib(default=None)
    connector: Token = attr.ib(default=None)


@attr.s
class Pattern:
    patterns: WordList = attr.ib()
    action: Command = attr.ib()
    flags: CasePatternFlag = attr.ib(default=0)


@attr.s
class Case(Command):
    type = CommandType.Case
    word: Word = attr.ib(default=None)
    clauses: List[Pattern] = attr.ib(factory=list)
