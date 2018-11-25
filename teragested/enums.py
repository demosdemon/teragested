# -*- coding: utf-8 -*-
"""Contains various Enum constants used in teragested."""

from enum import Enum, IntEnum, IntFlag, auto


class CharacterFlag(IntFlag):
    """Values for character flags in syntax tables."""

    #: nothing special, an ordinary character
    Word = 0x0000
    #: shell meta character
    ShellMeta = 0x0001
    #: shell break character
    ShellBreak = 0x0002
    #: back quote
    BackQuote = 0x0004
    #: shell quote character
    Quote = 0x0008
    #: special character that needs quoting
    Special = 0x0010
    #: shell expansion character
    Expansion = 0x0020
    #: characters escaped by backslash in double quotes
    BSDQuote = 0x0040
    #: characters escaped by backslash in here docs
    BshDoc = 0x0080
    #: globbing characters
    Glob = 0x0100
    #: extended globbing characters
    XGlob = 0x0200
    #: Quote + backslash
    XQuote = 0x0400
    #: single-character shell variable name
    SpecialVar = 0x0800
    #: values of OP for ``${wordOPstuff}``
    SubStop = 0x1000
    #: whitespace (blank) character
    Blank = 0x2000


class RedirectionInstruction(IntEnum):
    """Instructions describing what kind of thing to do for a redirection."""

    #: replace stdout, truncate dest, ``> foo``
    OutputDirection = auto()
    #: replace stdin, read src, ``< foo``
    InputDirection = auto()
    #: implicit ``< /dev/null`` from ``command &``
    InputADirection = auto()
    #: replace stdout, append dest, ``>> foo``
    AppendingTo = auto()
    #: heredoc, ``<< FOOBAR``
    ReadingUntil = auto()
    #: here-string, ``<<< foobar``
    ReadingString = auto()
    #: copy ``word`` and set to ``n`` (default 0), ``[n]<&word``
    DuplicatingInput = auto()
    #: copy ``word`` and set to ``n`` (default 1), ``[n]<&word``
    DuplicatingOutput = auto()
    #: dedent leading '\t' from ``<<-FOOBAR`` docs
    DeblankReadingUntil = auto()
    #: close the file descriptor, ``<&-``
    CloseThis = auto()
    #: replace stdout & stderr, truncate dest, ``&> foo``
    ErrAndOut = auto()
    #: replace stdout & stdin, truncate dest, ``<> foo``
    InputOutput = auto()
    #: replace stdout, clobber dest, ``>| foo``
    OutputForce = auto()
    #: open or copy the fd for ``word`` into a new fd and set the variable ``foo``, ``{foo}<&word``
    DuplicatingInputWord = auto()
    #: open or copy the fd for ``word`` into a new fd and set the variable ``foo``, ``{foo}>&word``
    DuplicatingOutputWord = auto()
    #: move fd ``y`` to ``x`` (default 0) closing ``y``, ``[x]<&y-``
    MoveInput = auto()
    #: move fd ``y`` to ``x`` (default 1) closing ``y``, ``[x]>&y-``
    MoveOutput = auto()
    #: copy the fd ``x`` to a new fd and set the variable ``foo``, ``{foo}<&x-``
    MoveInputWord = auto()
    #: copy the fd ``x`` to a new fd and set the variable ``foo``, ``{foo}>&x-``
    MoveOutputWord = auto()
    #: replace stdout and stderr, append dest, ``&>> foo``
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
    #: dollar sign present
    HasDollar = 0x000001
    #: some form of quote character is present
    Quoted = 0x000002
    #: this word is a variable assignment
    Assignment = 0x000004
    #: split this word on " " regardless of ``$IFS```
    SplitSpace = 0x000008
    #: do not perform word splitting because ``$IFS`` is empty
    NoSplit = 0x000010
    #: do not perform globbing on this word
    NoGlob = 0x000020
    #: do not split word except for $@ expansion because of context
    NoSplit2 = 0x000040
    #: tilde expand this assignment word
    TildeExp = 0x000080
    #: $@ and its special handling
    DollarAt = 0x000100
    #: $* and its special handling
    DollarStar = 0x000200
    #: do not perform command substitution on this word
    NoComSub = 0x000400
    #: word is rhs of an assignment statement
    AssignRhs = 0x000800
    #: do not perform tilde expansion on this word
    NoTilde = 0x001000
    #: internal flag for word expansion
    ITilde = 0x002000
    #: don't expand at all -- quote removal
    NoExpand = 0x004000
    #: compund assignment
    CompAssign = 0x008000
    #: word is a builtin command that takes assignments
    AssnBltn = 0x010000
    #: word is assignment argument to command
    AssignArg = 0x020000
    #: word contains a quoted nul character
    HasQuotedNull = 0x040000
    #: word should be treated as if double quoted
    DQuote = 0x080000
    #: don't perform process substitution
    NoProcSub = 0x100000
    #: word contains literal CTLSEC characters
    HasCTLSEC = 0x200000
    #: word looks like an assoc array assignment
    AssignAssoc = 0x400000
    #: word looks like an indexed array assignment
    AssignArray = 0x800000
    #: word is an array index being expanded
    ArrayInd = 0x1000000
    #: word is a global assignment to declare
    AssgnGlobal = 0x2000000
    #: do not perform brace expansion
    NoBrace = 0x4000000
    #: word is being expanded for completion
    Complete = 0x8000000


class ParamFlags(IntFlag):
    #: Do not perform command substitution
    NoComSub = 0x01
    #: Ignore unbound vars even if ``-u`` is set
    IgnUnbound = 0x02
    #: same as :attr:`WordFlags.NoSplit2`
    NoSplit2 = 0x04
    #: same as :attr:`WordFlags.AssignRhs`
    AssignRhs = 0x08
    #: same as :attr:`WordFlags.Complete`
    Complete = 0x10


class SubshellFlags(IntFlag):
    #: subshell caused by ``command &``
    Async = 0x01
    #: subshell caused by ``( ... )``
    Paren = 0x02
    #: subshell caused by ```command``` or ``$(command)``
    ComSub = 0x04
    #: subshell cause by executing a disk command
    Fork = 0x08
    #: subshell from a pipeline element
    Pipe = 0x10
    #: subshell cause by ``<(command)`` or ``>(command)``
    ProcSub = 0x20
    #: subshell from coproc pipeline
    Coproc = 0x40
    #: subshell needs to reset trap strings on first call to trap
    ResetTrap = 0x80


class CommandFlags(IntFlag):
    #: user wants a subshell, ``( command )``
    WantSubshell = 0x01
    #: shell needs to force a subshell
    ForceSubshell = 0x02
    #: invert the exit value
    InvertReturn = 0x04
    #: ignore the exit value (for ``set -e``)
    IgnoreReturn = 0x08
    #: Ignore functions during lookup
    NoFunctions = 0x10
    #: do not expand the command words
    InhibitExpansion = 0x20
    #: Don't fork, just call execve
    NoFork = 0x40
    #: time a pipeline
    TimePipeline = 0x80
    #: ``time -p``, use POSIX.2 time output spec
    TimePosix = 0x100
    #: ``command &``
    Ampersand = 0x200
    #: async command needs implicit ``</dev/null``
    StdinRedir = 0x400
    #: command executed by the ``command`` builtin
    CommandBuilding = 0x0800
    CoprocSubshell = 0x1000
    LastPipe = 0x2000
    #: use standard path for command lookup
    Stdpath = 0x4000


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
