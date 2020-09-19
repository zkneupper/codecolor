#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Add Module Docstring
"""


# Python standard library imports
import inspect


# External library imports
import pygments


__all__ = [
    "get_all_styles",
    "highlight_code",
    "getsource",
    "printsource",
]


def get_all_styles():
    """Add docstring"""

    return list(pygments.styles.get_all_styles())


def highlight_code(code, style="default"):
    """Add docstring"""

    assert style in get_all_styles()

    highlighted_code = pygments.highlight(
        code,
        pygments.lexers.PythonLexer(),
        pygments.formatters.Terminal256Formatter(style=style),
    )

    return highlighted_code


def getsource(obj, style="default"):
    """Add docstring"""
    highlighted_code = highlight_code(inspect.getsource(obj), style=style)
    return highlighted_code


def printsource(obj, style="default"):
    """Add docstring"""
    highlighted_code = getsource(obj, style=style)
    print(highlighted_code)
