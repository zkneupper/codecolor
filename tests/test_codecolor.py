#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Tests for `codecolor` package.

Write tests for the following functions:
    * get_all_styles
    * highlight_code
    * getsource

No tests for:
    * printsource

"""


# External library imports
import codecolor
import pytest

# from codecolor import codecolor


########################################
##### Tests for `get_all_styles()` #####
########################################


def test_get_all_styles_return_type():
    """Write test."""

    output = codecolor.get_all_styles()

    # Assert that the output returned is a list
    assert isinstance(output, list)

    # Assert that every element of the returned list is a string
    assert all([isinstance(x, str) for x in output])


def test_get_all_styles_default():
    """Unit test: "default" exists.

    Assert that the "default" style is included in the list of 
    styles returned by `codecolor.get_all_styles()`.
    """

    output = codecolor.get_all_styles()

    assert "default" in output


########################################
##### Tests for `highlight_code()` #####
########################################


def test_highlight_code_return_type():
    """Write test."""

    code = "import this"
    highlighted_code = codecolor.highlight_code(code, style="default")

    # Assert that the output returned is a string.
    assert isinstance(highlighted_code, str)


def test_highlight_code_return_len():
    """Write test."""

    code = "import this"
    highlighted_code = codecolor.highlight_code(code, style="default")

    # Assert returned value is at least as long as the input code string.
    assert len(highlighted_code) >= len(code)


########################################
##### Tests for `test_getsource()` #####
########################################


def test_getsource_return_type_0():
    """Write test."""

    import pathlib

    obj = pathlib.Path.iterdir
    code_string = codecolor.getsource(obj)

    # Assert that the output returned is a string.
    assert isinstance(code_string, str)


def test_getsource_return_type_1():
    """Write test."""

    import pathlib

    obj = pathlib.Path.iterdir
    code_string = codecolor.getsource(obj, style="default")

    # Assert that the output returned is a string.
    assert isinstance(code_string, str)


def test_getsource_return_type_2():
    """Write test."""

    import pathlib

    obj = pathlib.Path.iterdir
    code_string = codecolor.getsource(obj, style=None)

    # Assert that the output returned is a string.
    assert isinstance(code_string, str)


########################################
##### Tests for `test_printsource()` ###
########################################
#
#
# def test_printsource():
#     """Write test."""
#
#     # codecolor.printsource()
#
#     assert True
#
#
########################################
########################################
########################################
