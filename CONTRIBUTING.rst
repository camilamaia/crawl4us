========
CONTRIBUTING
========

Install `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_

Create a virtualenv to crawl4us:

.. code:: bash

  $ mkvirtualenv crawl
  
Clone and install crawl4us lib:

.. code:: bash

  $ workon crawl
  $ git clone git@github.com:camilamaia/crawl4us.git
  $ cd crawl4us
  $ pip install -r requirements-dev.txt
  $ pip install -r requirements.txt
  
Deploy
------------

Install requirements:

.. code:: bash

  $ workon crawl
  $ pip install twine
  $ pip install wheel

Update the version on setup.py, commit and push it. 

Deploy the new version:

.. code:: bash

  $ workon crawl
  $ pip install twine
  $ cd crawl4us
  $ python setup.py sdist
  $ pip install wheel
  $ python setup.py bdist_wheel
  $ twine upload dist/* --skip-existing

For more information: https://packaging.python.org/tutorials/distributing-packages/
