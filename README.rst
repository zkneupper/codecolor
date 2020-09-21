=========
codecolor
=========

.. image:: https://raw.githubusercontent.com/zkneupper/codecolor/master/docs/_static/code_color_logo.png

.. image:: https://img.shields.io/pypi/v/codecolor.svg
        :target: https://pypi.python.org/pypi/codecolor

.. image:: https://img.shields.io/travis/zkneupper/codecolor.svg
        :target: https://travis-ci.com/zkneupper/codecolor

.. image:: https://readthedocs.org/projects/codecolor/badge/?version=latest
        :target: https://codecolor.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Inspect python object code with colorful syntax highlighting!


* Free software: Apache Software License 2.0
* Documentation: https://codecolor.readthedocs.io.


Codecolor adds color when inspecting source code of python objects.
It applies syntax highlighting to object source code.

The primary function of the codecolor module is the `printsource`
function. The `printsource(obj, style="default")` function prints
the syntax-highlighted source code for the python object `obj`.

Codecolor combines the code inspection functionality of
`inspect.getsource()` and syntax highlighting functionality
of the `pygments` package.


Example
--------

How does the pytorch relu function work under the hood?
You can easily inspect the source code of the pytorch relu function
by using `codecolor.printsource(relu)` to to print the source code of
the relu function with syntax highlighting.


.. code-block:: python

    from codecolor import printsource

    from torch.nn.functional import relu
    
    printsource(relu)
    # prints the source code of the relu function with syntax highlighting

.. image:: https://raw.githubusercontent.com/zkneupper/codecolor/master/docs/_static/codecolor-demo.gif



Functions:

* printsource(obj, style="default")
* getsource(obj, style="default")
* highlight_code(code, style="default")
* get_all_styles()



To-Do
--------

* Add pytest unit tests
* Flesh out readme

        * Example usage
        * Motivation
        * Installation
        * Center logo image
        
* Deploy to pypi




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage