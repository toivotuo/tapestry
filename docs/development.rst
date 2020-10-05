Development
===========

In this section, we describe the development conventions and tools
used for Tapestry. Keeping good documentation "hygiene" is always
paramount for maintainable code!

The Python packages used to implement the development conventions
below can be installed with a requirements file a the top level of the
'tapestry' repository::

    pip install -r requirements-dev.txt

Code style guide
----------------

As a Python code style the `Google Python Style Guide`_ is
adopted. The Google style guide is followed both in how the code is
formatted as well as with documenting the Python code with docstrings.

.. _`Google Python Style Guide`: https://google.github.io/styleguide/pyguide.html

Code conformance to the Google style guide can be checked with
'flake8'::

    flake8 --docstring-convention=google FILENAME

Likewise, 'pylint' can be used, but by default pylint does not follow
the Google style guide. Custom .pylintrc would be required.

Automatic formatting of code to conform with the Google style guide
can be achieved with \'yapf_\' (add -i to rewrite the file in-place)::

     yapf --style=google FILENAME

.. _yapf: https://pypi.org/project/yapf/

Documentation conventions
-------------------------

The Google style guide should be followed for documentation of the
code in docstrings.

For documentation that is not written in docstrings, Sphinx is
used. The 'autodoc' facility of Sphinx is also used to pull the
documentation from docstrings and produce browsable code
documentation.

Starting from the 'tapestry' repository root, documentation as HTML
can be produced with::

    cd docs
    ./run-apidoc.sh
    make html

Built documentation will be available in '_build/html' in the
repository root.

Development process issues
--------------------------

Coverage ratio of tests for the code can be run with::

    coverage run --source='.' manage.py test
    coverage report

However, as the code currently has limited to no documentation, code
coverage is somewhat beside the point. Unit testing setup with Django
native facilities and 'pytest' have also not yet been setup.

Documentation improvements
--------------------------

A number of documentation process improvements are planned:

  * Generate and publish documents as GitHub Pages with the Sphinx
    'sphinx.ext.githubpages' extension.

  * Use the Sphinx 'sphinx.ext.todo' extension to publish a clear list
    of the FIXME and TODO notes from the code as a list of
    improvements to be done.

  * Documentation coverage checks with Sphinx.
