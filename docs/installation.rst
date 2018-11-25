============
Installation
============

At this time, teragested is not available on PyPI.

At the command line::

  $ virtualenv breakdance
  New python executable in /Users/brandon/breakdance/bin/python2.7
  Also creating executable in /Users/brandon/breakdance/bin/python
  Installing setuptools, pip, wheel...
  done.
  $ source breakdance/bin/activate
  [venv:~/breakdance]$ pip install "git+https://github.com/demosdemon/teragested.git#egg=teragested"
  Collecting teragested from git+https://github.com/demosdemon/teragested.git#egg=teragested
    Cloning https://github.com/demosdemon/teragested.git to /private/var/folders/5t/s1_46rmd03xcnrcf1yq88v_40000gn/T/pip-install-WLaDGj/teragested
  Collecting attrs (from teragested)
    Using cached https://files.pythonhosted.org/packages/3a/e1/5f9023cc983f1a628a8c2fd051ad19e76ff7b142a0faf329336f9a62a514/attrs-18.2.0-py2.py3-none-any.whl
  Collecting click (from teragested)
    Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
  Collecting parsy (from teragested)
    Downloading https://files.pythonhosted.org/packages/3e/9f/e36bd40f753586ddd0b5b7cb6ce8224102ae315e0bd8536157df8fe81c9d/parsy-1.2.0.tar.gz
  Building wheels for collected packages: teragested, parsy
    Running setup.py bdist_wheel for teragested ... done
    Stored in directory: /private/var/folders/5t/s1_46rmd03xcnrcf1yq88v_40000gn/T/pip-ephem-wheel-cache-lOCwhj/wheels/10/09/68/5b1eaf31dd1032fe71b5b359ec0ba277634422261f65fd9ac6
    Running setup.py bdist_wheel for parsy ... done
    Stored in directory: /Users/brandon/Library/Caches/pip/wheels/a4/79/1a/ad60ea55eaec19321741431ac2875ee485918f57d8ef8716e7
  Successfully built teragested parsy
  Installing collected packages: attrs, click, parsy, teragested
  Successfully installed attrs-18.2.0 click-7.0 parsy-1.2.0 teragested-0.0.1.dev17
  [venv:~/breakdance]$ teragested --help
  Usage: teragested [OPTIONS]

    Interact with the teragested parser and a shell script.

  Options:
    --help  Show this message and exit.
