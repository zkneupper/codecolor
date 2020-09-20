#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Add Module Docstring
"""


# Python standard library imports
import inspect
import sys

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


# Use this docstring style convention:
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


# To Do:
#     * Add function doc strings
#     * Add module doc string
#     * Run codespell on module
#     * Add type hints to all functions (optional?)


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
    """Apply syntax highlighting to the string of python `code`.

    Args:
        code (str): The string of python code to be styled.
        style (:obj:`str`, optional): The style to apply.
            The name of the syntax highlighting style to apply to the `code`.

            Defaults to "default". The "default" style is the same syntax 
            highlighting style used by default in ipython and jupyter notebooks.

            Any style must be listed among the available syntax highlighting
            styles from the `pygments` package. See `get_all_styles()`.

    Returns:
        str: A string of python code that has been syntax highlighted.

    """

    assert style in get_all_styles()

    highlighted_code = pygments.highlight(
        code,
        pygments.lexers.PythonLexer(),
        pygments.formatters.Terminal256Formatter(style=style),
    )

    return highlighted_code


def getsource(obj, style="default") -> str:
    """Return the syntax-highlighted source code for the python object `obj`.

    Args:
        obj : A python module, class, method, function, traceback, frame, or
            code object.
        style (:obj:`str` or `NoneType`, optional): The style to apply.
            The name of the syntax highlighting style to apply to the `code`.

            Defaults to "default". The "default" style is the same syntax 
            highlighting style used by default in ipython and jupyter notebooks.

            If style=None, no syntax highlighting style will be applied, and 
            the `code` string will be returned unchanged.

            If `style` is not None, `style` must be a style listed among the 
            available syntax highlighting styles from the `pygments` package.
            See `get_all_styles()`.

    Returns:
        str: The text of the syntax-highlighted source code for the object 
            `obj`.

            The source code is returned as a single string.

    Raises:
        OSError: If the source code cannot be retrieved.

    """

    code_string = inspect.getsource(obj)

    if style is not None:
        code_string = highlight_code(code_string, style=style)

    return code_string


# def printsource(obj, style="default"):
def printsource(obj, style="default", end="\n", file=sys.stdout, flush=False):
    """Add docstring

    """

    highlighted_code = getsource(obj, style=style)

    print(
        highlighted_code, end=end, file=file, flush=flush,
    )
