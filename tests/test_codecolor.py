#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Tests for `codecolor` package.

Write tests for the following functions:
    * get_all_styles
    * highlight_code
    * getsource
    * printsource
"""


# External library imports
import codecolor
import pytest


# from codecolor import codecolor
# from click.testing import CliRunner
# from codecolor import cli


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


def test_highlight_code():
    """Write test."""

    # codecolor.highlight_code()

    assert True


########################################
########################################
########################################


def test_getsource():
    """Write test."""

    # codecolor.getsource()

    assert True


def test_printsource():
    """Write test."""

    # codecolor.printsource()

    assert True


#############################################################
#############################################################

# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'codecolor.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
