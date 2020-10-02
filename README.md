TAPESTRY
========

Experiments in implementing a payment processing engine where "every
bank is considered as a CSM". Part of the TLBOP work to finally be
done with the Computer Science MSc at the University of Helsinki.

What's in the name? Star Trek: TNG (S6E15)


Development conventions
-----------------------

    coverage run --source='.' manage.py test
	coverage report

	yapf --style=google FILENAME
	https://github.com/google/yapf/

	flake8 --docstring-convention=google FILENAME

	https://google.github.io/styleguide/pyguide.html

	pytest [FIXME]

	sphinx-apidoc -o docs tapestry
	make html

Development documentation improvements in the pipeline:

  * Generate and publish documents as GitHub Pages with the Sphinx
    'sphinx.ext.githubpages' extension.

  * Use the Sphinx 'sphinx.ext.todo' extension to publish a clear list
    of the FIXME and TODO notes from the code as a list of
    improvements to be done.

  * Documentation coverage checks with Sphinx.
