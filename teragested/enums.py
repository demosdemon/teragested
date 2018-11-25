# -*- coding: utf-8 -*-
""".. module:: teragested.enums

Contains various Enum constants used in teragested.
"""

from enum import Enum, IntEnum, IntFlag, auto


class RedirectionInstruction(IntEnum):
    """Instructions describing what kind of thing to do for a redirection."""

    OutputDirection = auto()
    InputDirection = auto()
    InputADirection = auto()
    AppendingTo = auto()
    ReadingUntil = auto()
    ReadingString = auto()
    DuplicatingInput = auto()
    DuplicatingOutput = auto()
    DeblankReadingUntil = auto()
    CloseThis = auto()
    ErrAndOut = auto()
    InputOutput = auto()
    OutputForce = auto()
    DuplicatingInputWord = auto()
    DuplicatingOutputWord = auto()
    MoveInput = auto()
    MoveOutput = auto()
    MoveInputWord = auto()
    MoveOutputWord = auto()
    AppendErrAndOut = auto()

    @property
    def clobering(self):
        return self in (
            RedirectionInstruction.OutputDirection,
            RedirectionInstruction.ErrAndOut,
        )

    @property
    def output_redirect(self):
        return self in (
            RedirectionInstruction.OutputDirection,
            RedirectionInstruction.InputOutput,
            RedirectionInstruction.ErrAndOut,
            RedirectionInstruction.AppendErrAndOut,
        )

    @property
    def input_redirect(self):
        return self in (
            RedirectionInstruction.InputDirection,
            RedirectionInstruction.InputADirection,
            RedirectionInstruction.InputOutput,
        )

    @property
    def write_redirect(self):
        return self in (
            RedirectionInstruction.OutputDirection,
            RedirectionInstruction.InputOutput,
            RedirectionInstruction.ErrAndOut,
            RedirectionInstruction.AppendingTo,
            RedirectionInstruction.AppendErrAndOut,
            RedirectionInstruction.OutputForce,
        )

    @property
    def translate_redirect(self):
        return self in (
            RedirectionInstruction.DuplicatingInputWord,
            RedirectionInstruction.DuplicatingOutputWord,
            RedirectionInstruction.MoveInputWord,
            RedirectionInstruction.MoveOutputWord,
        )


class RedirectionError(IntEnum):
    AmbiguousRedirect = auto()
    NoClobberRedirect = auto()
    RestrictedRedirect = auto()
    HereDocRedirect = auto()
    BadVarRedirect = auto()


class RedirectionFlags(IntFlag):
    Active = 0x01
    Undoable = 0x02
    ClExec = 0x04
    Internal = 0x08
    User = 0x10
    SavClExec = 0x20
    SaveFd = 0x40
    VarAssign = 0x80


class CommandType(IntEnum):
    For = auto()
    Case = auto()
    While = auto()
    If = auto()
    Simple = auto()
    Select = auto()
    Connection = auto()
    FunctionDef = auto()
    Until = auto()
    Group = auto()
    Arith = auto()
    Cond = auto()
    ArithFor = auto()
    Subshell = auto()
    Coproc = auto()


class WordFlags(IntFlag):
    HasDollar = 0x000001  #: dollar sign present
    Quoted = 0x000002  #: some form of quote character is present
    Assignment = 0x000004  #: this word is a variable assignment
    SplitSpace = 0x000008  #: split this word on " " regardless of ``$IFS```
    NoSplit = 0x000010  #: do not perform word splitting because ``$IFS`` is empty
    NoGlob = 0x000020  #: do not perform globbing on this word
    NoSplit2 = 0x000040  #: do not split word except for $@ expansion because of context
    TildeExp = 0x000080  #: tilde expand this assignment word
    DollarAt = 0x000100  #: $@ and its special handling
    DollarStar = 0x000200  #: $* and its special handling
    NoComSub = 0x000400  #: do not perform command substitution on this word
    AssignRhs = 0x000800  #: word is rhs of an assignment statement
    NoTilde = 0x001000  #: do not perform tilde expansion on this word
    ITilde = 0x002000  #: internal flag for word expansion
    NoExpand = 0x004000  #: don't expand at all -- quote removal
    CompAssign = 0x008000  #: compund assignment
    AssnBltn = 0x010000  #: word is a builtin command that takes assignments
    AssignArg = 0x020000  #: word is assignment argument to command
    HasQuotedNull = 0x040000  #: word contains a quoted nul character
    DQuote = 0x080000  #: word should be treated as if double quoted
    NoProcSub = 0x100000  #: don't perform process substitution
    HasCTLSEC = 0x200000  #: word contains literal CTLSEC characters
    AssignAssoc = 0x400000  #: word looks like an assoc array assignment
    AssignArray = 0x800000  #: word looks like an indexed array assignment
    ArrayInd = 0x1000000  #: word is an array index being expanded
    AssgnGlobal = 0x2000000  #: word is a global assignment to declare
    NoBrace = 0x4000000  #: do not perform brace expansion
    Complete = 0x8000000  #: word is being expanded for completion


class ParamFlags(IntFlag):
    NoComSub = 0x01  #: Do not perform command substitution
    IgnUnbound = 0x02  #: Ignore unbound vars even if ``-u`` is set
    NoSplit2 = 0x04  #: same as :member:`WordFlags.NoSplit2`
    AssignRhs = 0x08  #: same as :member:`WordFlags.AssignRhs`
    Complete = 0x10  #: same as :member:`WordFlags.Complete`


class SubshellFlags(IntFlag):
    Async = 0x01  #: subshell caused by ``command &``
    Paren = 0x02  #: subshell caused by ``( ... )``
    ComSub = 0x04  #: subshell caused by ```command``` or ``$(command)``
    Fork = 0x08  #: subshell cause by executing a disk command
    Pipe = 0x10  #: subshell from a pipeline element
    ProcSub = 0x20  #: subshell cause by ``<(command)`` or ``>(command)``
    Coproc = 0x40  #: subshell from coproc pipeline
    ResetTrap = 0x80  #: subshell needs to reset trap strings on first call to trap


class CommandFlags(IntFlag):
    WantSubshell = 0x01  #: user wants a subshell; ``( command )``
    ForceSubshell = 0x02  #: shell needs to force a subshell
    InvertReturn = 0x04  #: invert the exit value
    IgnoreReturn = 0x08  #: ignore the exit value (for ``set -e``)
    NoFunctions = 0x10  #: Ignore functions during lookup
    InhibitExpansion = 0x20  #: do not expand the command words
    NoFork = 0x40  #: Don't fork; just call execve
    TimePipeline = 0x80  #: time a pipeline
    TimePosix = 0x100  #: ``time -p``; use POSIX.2 time output spec
    Ampersand = 0x200  #: ``command &``
    StdinRedir = 0x400  #: async command needs implicit ``</dev/null``
    CommandBuilding = 0x0800  #: command executed by the ``command`` builtin
    CoprocSubshell = 0x1000
    LastPipe = 0x2000
    Stdpath = 0x4000  #: use standard path for command lookup


class Conditional(IntFlag):
    And = auto()
    Or = auto()
    Unary = auto()
    Binary = auto()
    Term = auto()
    Expr = auto()


class CasePatternFlag(IntFlag):
    FallThrough = 0x01
    TestNext = 0x02


class ReservedWord(Enum):
    """These are only recognized as the first word of a command."""

    IF = "if"
    THEN = "then"
    ELSE = "else"
    ELIF = "elif"
    FI = "fi"
    CASE = "case"
    ESAC = "esac"
    FOR = "for"
    SELECT = "select"
    WHILE = "while"
    UNTIL = "until"
    DO = "do"
    DONE = "done"
    IN = "in"
    FUNCTION = "function"
    TIME = "time"
    LCURLY = "{"
    RCURLY = "}"
    BANG = "!"
    COND_START = "[["
    COND_END = "]]"
    COPROC = "coproc"


class Token(Enum):
    """These are other shell token literals."""

    TIMEIGN = "--"
    TIMEOPT = "-p"
    AND_AND = "&&"
    OR_OR = "||"
    GREATER_GREATER = ">>"
    LESS_LESS = "<<"
    LESS_AND = "<&"
    GREATER_AND = ">&"
    SEMI_SEMI = ";;"
    SEMI_AND = ";&"
    SEMI_SEMI_AND = ";;&"
    LESS_LESS_MINUS = "<<-"
    LESS_LESS_LESS = "<<<"
    AND_GREATER = "&>"
    AND_GREATER_GREATER = "&>>"
    LESS_GREATER = "<>"
    GREATER_BAR = ">|"
    BAR_AND = "|&"
    EOF = r"\Z"
    RANGLE = ">"
    LANGLE = "<"
    MINUS = "-"
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    VBAR = "|"
    AMPERSAND = "&"
    NEWLINE = "\n"
    EQUAL = "="
