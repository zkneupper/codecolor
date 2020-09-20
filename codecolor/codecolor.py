#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Codecolor Module

This module defines the following codecolor functions:
    * get_all_styles
    * highlight_code
    * getsource
    * printsource

Todo:
    * Run codespell on module (optional?)
    * Add type hints to all functions (optional?)
    * Add docstring style convention note in documentation for contributors.
        # Use this docstring style convention:
        # https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""


# Python standard library imports
import inspect
import sys
from typing import NoReturn


# External library imports
import pygments
from pygments import styles


# WHY DOES PYTEST RAISE AttributeError: module 'pygments' has no attribute 'styles'?
#
# Importing `from pygments import styles` because pytest raised an AttributeError
# when it tried to execute `pygments.styles.get_all_styles()`:
#
# >>> AttributeError: module 'pygments' has no attribute 'styles'
# >>> ../codecolor/codecolor.py:37: AttributeError
#
# Replaced:     return list(pygments.styles.get_all_styles())
# With:         return list(styles.get_all_styles())


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


def highlight_code(code, style="default") -> str:
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


def printsource(
    obj, style="default", end="\n", file=sys.stdout, flush=False
) -> NoReturn:
    """Print the syntax-highlighted source code for the python object `obj`.

    Print the syntax-highlighted source code for the python object `obj` to
    sys.stdout (by default) or to a stream.

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

        end (:obj:`str`, optional): String appended after the source code
            string.

            Defaults to the newline string "\n".

        file (optional): A file-like object (stream).

            Defaults to the current sys.stdout.

        flush (:obj:`bool`, optional): Whether to forcibly flush the stream.

            Defaults to False.

    Example:
        How does the pytorch relu function work under the hood?
        You can easily inspect the source code of the pytorch relu function
        by using `codecolor.printsource(relu)` to to print the source code of
        the relu function with syntax highlighting.

        >>> from codecolor import printsource
        >>> from torch.nn.functional import relu
        >>> printsource(relu)
        # prints the source code of the relu function with syntax highlighting

    """

    highlighted_code = getsource(obj, style=style)

    print(
        highlighted_code, end=end, file=file, flush=flush,
    )
