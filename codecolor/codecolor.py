#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Add Module Docstring
"""


# Python standard library imports
import inspect


# External library imports
import pygments

from pygments import styles

# Importing `from pygments import styles` because 
# pytest raised an AttributeError when it tried to execute
# `pygments.styles.get_all_styles()`:
# 
# >>> AttributeError: module 'pygments' has no attribute 'styles'
# >>> 
# >>> ../codecolor/codecolor.py:37: AttributeError
# 
# Replaced
#     return list(pygments.styles.get_all_styles())
# with
#     return list(styles.get_all_styles())
#
# WHY DOES PYTEST RAISE AttributeError: module 'pygments' has no attribute 'styles'?


__all__ = [
    "get_all_styles",
    "highlight_code",
    "getsource",
    "printsource",
]


def get_all_styles() -> list:
    """Returns a list of available styles by name (as strings).

    Return a list of names of available syntax highlighting styles
    from the `pygments` package. This list includes both builtin and
    plugin styles.

    Returns:
        list: The list of names of available syntax highlighting styles
        from the pygments package. This is a list of strings.
    """

    # return list(pygments.styles.get_all_styles())
    return list(styles.get_all_styles())


def highlight_code(code, style="default"):
    """Add docstring"""

    assert style in get_all_styles()

    highlighted_code = pygments.highlight(
        code,
        pygments.lexers.PythonLexer(),
        pygments.formatters.Terminal256Formatter(style=style),
    )

    return highlighted_code


def getsource(obj, style="default") -> str:
    """Add docstring

    If you set style=None, function will return the code 
    with no syntax highlighting.

    """

    code_string = inspect.getsource(obj)

    if style is not None:
        code_string = highlight_code(code_string, style=style)

    return code_string


def printsource(obj, style="default"):
    """Add docstring"""
    highlighted_code = getsource(obj, style=style)
    print(highlighted_code)
