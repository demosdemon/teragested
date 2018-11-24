# -*- coding: utf-8 -*-
""".. module:: bashlex.enums

Contains various Enum constants used in bashlex.
"""

from enum import Enum, IntEnum, IntFlag, auto


class RedirectionInstruction(IntEnum):
    """Instructions describing what kind of thing to do for a redirection."""

    OUTPUT_DIRECTION = auto()
    INPUT_DIRECTION = auto()
    INPUT_A_DIRECTION = auto()
    APPENDING_TO = auto()
    READING_UNTIL = auto()
    READING_STRING = auto()
    DUPLICATING_INPUT = auto()
    DUPLICATING_OUTPUT = auto()
    DEBLANK_READING_UNTIL = auto()
    CLOSE_THIS = auto()
    ERR_AND_OUT = auto()
    INPUT_OUTPUT = auto()
    OUTPUT_FORCE = auto()
    DUPLICATING_INPUT_WORD = auto()
    DUPLICATING_OUTPUT_WORD = auto()
    MOVE_INPUT = auto()
    MOVE_OUTPUT = auto()
    MOVE_INPUT_WORD = auto()
    MOVE_OUTPUT_WORD = auto()
    APPEND_ERR_AND_OUT = auto()

    @property
    def clobering(self):
        return self in (
            RedirectionInstruction.OUTPUT_DIRECTION,
            RedirectionInstruction.ERR_AND_OUT,
        )

    @property
    def output_redirect(self):
        return self in (
            RedirectionInstruction.OUTPUT_DIRECTION,
            RedirectionInstruction.INPUT_OUTPUT,
            RedirectionInstruction.ERR_AND_OUT,
            RedirectionInstruction.APPEND_ERR_AND_OUT,
        )

    @property
    def input_redirect(self):
        return self in (
            RedirectionInstruction.INPUT_DIRECTION,
            RedirectionInstruction.INPUT_A_DIRECTION,
            RedirectionInstruction.INPUT_OUTPUT,
        )

    @property
    def write_redirect(self):
        return self in (
            RedirectionInstruction.OUTPUT_DIRECTION,
            RedirectionInstruction.INPUT_OUTPUT,
            RedirectionInstruction.ERR_AND_OUT,
            RedirectionInstruction.APPENDING_TO,
            RedirectionInstruction.APPEND_ERR_AND_OUT,
            RedirectionInstruction.OUTPUT_FORCE,
        )

    @property
    def translate_redirect(self):
        return self in (
            RedirectionInstruction.DUPLICATING_INPUT_WORD,
            RedirectionInstruction.DUPLICATING_OUTPUT_WORD,
            RedirectionInstruction.MOVE_INPUT_WORD,
            RedirectionInstruction.MOVE_OUTPUT_WORD,
        )


class RedirectionError(IntEnum):
    AmbiguousRedirect = auto()


class RedirectionFlags(IntFlag):
    ACTIVE = 0x01
    UNDOABLE = 0x02
    CLOSE_ON_EXEC_ON = 0x04
    INTERNAL = 0x08
    USER = 0x10
    CLOSE_ON_EXEC_OFF = 0x20
    SAVEFD = 0x40
    VARASSIGN = 0x80


class CommandType(IntEnum):
    FOR = auto()
    CASE = auto()
    WHILE = auto()
    IF = auto()
    SIMPLE = auto()
    SELECT = auto()
    CONNECTION = auto()
    FUNCTION_DEF = auto()
    UNTIL = auto()
    GROUP = auto()
    ARITH = auto()
    COND = auto()
    ARITH_FOR = auto()
    SUBSHELL = auto()
    COPROC = auto()


class WordFlags(IntFlag):
    #: dollar sign present
    HASDOLLAR = 0x000001
    #: some form of quote character is present
    QUOTED = 0x000002
    #: this word is a variable assignment
    ASSIGNMENT = 0x000004
    #: split this word on " " regardless of IFS
    SPLITSPACE = 0x000008
    #: do not perform word splitting because IFS is an empty string
    NOSPLIT = 0x000010
    #: do not perform globbing on this word
    NOGLOB = 0x000020
    #: do not split work except for $@ expansion because contex does not allow it
    NOSPLIT2 = 0x000040
    #: tilde expand this assignment word
    TILDEEXP = 0x000080
    #: $@ and its special handling
    DOLLARAT = 0x000100
    #: $* and its special handling
    DOLLARSTAR = 0x000200
    #: do not perform command substitution on this word
    NOCOMSUB = 0x000400
    #: word is rhs of an assignment statement
    ASSIGNRHS = 0x000800
    #: do not perform tilde expansion on this word
    NOTILDE = 0x001000
    #: internal flag for word expansion
    ITILDE = 0x002000
    #: don't expand at all -- quote removal
    NOEXPAND = 0x004000
    #: compund assignment
    COMPASSIGN = 0x008000
    #: word is a builtin command that takes assignments
    ASSNBLTIN = 0x010000
    #: word is assignment argument to command
    ASSIGNARG = 0x020000
    #: word contains a quoted nul character
    HASQUOTEDNULL = 0x040000
    #: word should be treated as if double quoted
    DQUOTE = 0x080000
    #: don't perform process substitution
    NOPROCSUB = 0x100000
    #: word contains literal CTLSEC characters
    HASCTLESC = 0x200000
    #: word looks like an assoc array assignment
    ASSIGNASSOC = 0x400000
    #: word looks like an indexed array assignment
    ASSICNARRAY = 0x800000
    #: word is an array index being expanded
    ARRAYIND = 0x1000000
    #: word is a global assignment to declare
    ASSNGLOBAL = 0x2000000
    #: do not perform brace expansion
    NOBRACE = 0x4000000
    #: word is being expanded for completion
    COMPLETE = 0x8000000


class ParamFlags(IntFlag):
    #: Do not perform command substitution
    NOCOMSUB = 0x01
    #: Ignore unbound vars even if -u is set
    IGNUNBOUND = 0x02
    #: same as WordFlags
    NOSPLIT2 = 0x04
    #: same as WordFlags
    ASSIGNRHS = 0x08
    #: same as WordFlags
    COMPLETE = 0x10


class SubshellFlags(IntFlag):
    #: subshell caused by `command &`
    ASYNC = 0x01
    #: subshell caused by ( ... )
    PAREN = 0x02
    #: subshell caused by `command` or $(command)
    COMSUB = 0x04
    #: subshell cause by executing a disk command
    FORK = 0x08
    #: subshell from a pipeline element
    PIPE = 0x10
    #: subshell cause by <(command) or >(command)
    PROCSUB = 0x20
    #: subshell from coproc pipeline
    COPROC = 0x40
    #: subshell needs to reset trap strings on first call to trap
    RESETTRAP = 0x80


class CommandFlags(IntFlag):
    #: user wants a subshell: ( command )
    WANT_SUBSHELL = 0x01
    #: shell needs to force a subshell
    FORCE_SUBSHELL = 0x02
    #: invert the exit value
    INVERT_RETURN = 0x04
    #: ignore the exit value (for set -e)
    IGNORE_RETURN = 0x08
    #: Ignore functions during lookup
    NO_FUNCTIONS = 0x10
    #: do not expand the command words
    INHIBIT_EXPANSION = 0x20
    #: Don't fork; just call execve
    NO_FORK = 0x40
    #: time a pipeline
    TIME_PIPELINE = 0x80
    #: time -p; use POSIX.2 time output spec
    TIME_POSIX = 0x100
    #: command &
    AMPERSAND = 0x200
    #: async command needs implicit </dev/null
    STDIN_REDIR = 0x400
    #: command executed by the `command` builtin
    COMMAND_BUILTIN = 0x0800
    COPROC_SUBSHELL = 0x1000
    LASTPIPE = 0x2000
    #: use standard path for command lookup
    STDPATH = 0x4000


class Conditional(IntFlag):
    AND = auto()
    OR = auto()
    UNARY = auto()
    BINARY = auto()
    TERM = auto()
    EXPR = auto()


class CasePatternFlag(IntFlag):
    FALL_THROUGH = 0x01
    TEST_NEXT = 0x02


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
