# -*- coding: utf-8 -*-

"""
CUT(1)                                                     User Commands                                                     CUT(1)

NAME
       cut - remove sections from each line of files

SYNOPSIS
       cut OPTION... [FILE]...

DESCRIPTION
       Print selected parts of lines from each FILE to standard output.

       With no FILE, or when FILE is -, read standard input.

       Mandatory arguments to long options are mandatory for short options too.

       -b, --bytes=LIST
              select only these bytes

       -c, --characters=LIST
              select only these characters

       -d, --delimiter=DELIM
              use DELIM instead of TAB for field delimiter

       -f, --fields=LIST
              select  only  these fields;  also print any line that contains no delimiter character, unless the -s option is speci‐
              fied

       -n     (ignored)

       --complement
              complement the set of selected bytes, characters or fields

       -s, --only-delimited
              do not print lines not containing delimiters

       --output-delimiter=STRING
              use STRING as the output delimiter the default is to use the input delimiter

       -z, --zero-terminated
              line delimiter is NUL, not newline

       --help display this help and exit

       --version
              output version information and exit

       Use one, and only one of -b, -c or -f.  Each LIST is made up of one range, or many ranges  separated  by  commas.   Selected
       input is written in the same order that it is read, and is written exactly once.  Each range is one of:

       N      N'th byte, character or field, counted from 1

       N-     from N'th byte, character or field, to end of line

       N-M    from N'th to M'th (included) byte, character or field

       -M     from first to M'th (included) byte, character or field

AUTHOR
       Written by David M. Ihnat, David MacKenzie, and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
       Report cut translation bugs to <http://translationproject.org/team/>

COPYRIGHT
       Copyright    ©    2017    Free    Software    Foundation,   Inc.    License   GPLv3+:   GNU   GPL   version   3   or   later
       <http://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       Full documentation at: <http://www.gnu.org/software/coreutils/cut>
       or available locally via: info '(coreutils) cut invocation'

GNU coreutils 8.28                                          October 2017                                                     CUT(1)
"""

from __future__ import print_function

import sys

import click


def range2tuple(rng):
    bounds = rng.split('-')
    if len(bounds) == 1:
        n = int(bounds[0])
        return n - 1, n
    if bounds[0] == '':
        return None, int(bounds[1])
    if bounds[1] == '':
        return int(bounds[0]) - 1, None
    return int(bounds[0]) - 1, int(bounds[1])


def list2slice(lst):
    return [slice(*range2tuple(rng)) for rng in lst.split(',')]


@click.command()
@click.option('-c', '--characters', help='select only these characters')
@click.option('-f', '--fields',
              help='select  only  these fields;  also print any line that contains no delimiter character, unless the -s option is specified')
@click.option('-d', '--delimiter', default='\t',
              help='use DELIM instead of TAB for field delimiter')
def cut(characters, fields, delimiter):
    """UNIX cut command."""
    for line in sys.stdin:
        line = line.rstrip('\n')
        if characters:
            print(''.join(line[s] for s in list2slice(characters)))
        if fields:
            f = line.split(delimiter)
            print(delimiter.join(delimiter.join(f[s]) for s in list2slice(fields)))


if __name__ == '__main__':
    cut()
