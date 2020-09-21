#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""codecolor
~~~~~~~~

Codecolor adds color when inspecting source code of python objects.
It applies syntax highlighting to object source code.

The primary function of the codecolor module is the `printsource`
function. The `printsource(obj, style="default")` function prints
the syntax-highlighted source code for the python object `obj`.

Codecolor combines the code inspection functionality of
`inspect.getsource()` and syntax highlighting functionality
of the `pygments` package.


Example:
    How does the pytorch relu function work under the hood?
    You can easily inspect the source code of the pytorch relu function
    by using `codecolor.printsource(relu)` to to print the source code of
    the relu function with syntax highlighting.

    >>> from codecolor import printsource
    >>> from torch.nn.functional import relu
    >>> printsource(relu)
    # prints the source code of the relu function with syntax highlighting

Functions:

    printsource(obj, style="default")

    getsource(obj, style="default")

    highlight_code(code, style="default")

    get_all_styles()

"""


__author__ = "Zachary Jonathan Kneupper"
__email__ = "zachary.kneupper@gmail.com"
__version__ = "0.0.2"


from .codecolor import (
    get_all_styles,
    highlight_code,
    getsource,
    printsource,
)
