ifeq ($(VIRTUAL_ENV), )
VIRTUAL_ENV := $(shell pipenv --venv 2>/dev/null)
endif

ifeq ($(VIRTUAL_ENV), )
VIRTUAL_ENV := $(CURDIR)/.venv
endif

ifeq ($(PLATFORM_APP_DIR), )
PYTHON ?= $(VIRTUAL_ENV)/bin/python
else
PYTHON ?= $(shell command -v python)
endif

SPHINXBUILD ?= $(VIRTUAL_ENV)/bin/sphinx-build
export SPHINXBUILD

python_code := bashlex tests docs

help:
	@echo 'Usage: make <target>'
	@echo '  Where <target> is one of:'
	@echo '    all         Execute all build operations.'
	@echo '    clean       Delete the generated output.'
	@echo '    docs        Build the sphinx documentation.'
	@echo '    debug-make  Print all of the `make` variables for debugging.'
	@echo '    format      Execute black and isort formatters on python code.'
	@echo '    help        Show this message and exit.'
	@echo '    lock        Regenerate the lockfile.'
	@echo '    sync        Synchronize the virtual environment with the lockfile.'
	@echo '    test        Executes py.test unit tests.'

debug-make:
	@echo "CURDIR      := $(CURDIR)"
	@echo "VIRTUAL_ENV := $(VIRTUAL_ENV)"
	@echo "PYTHON      := $(PYTHON)"
	@echo "python_code := $(python_code)"

Pipfile.lock: Pipfile
	pipenv lock --pre

all: lock sync format test

clean:
	git clean -xdf -e .env -e .venv

docs: $(PYTHON)
	$(VIRTUAL_ENV)/bin/sphinx-apidoc -f -o docs -P -M bashlex tests
	$(MAKE) -C docs html

format: $(PYTHON)
	$(PYTHON) -m isort --recursive $(python_code)
	$(PYTHON) -m black $(python_code)

lock: Pipfile.lock

sync $(PYTHON): Pipfile.lock
	pipenv sync --dev
	pipenv clean
	@touch $(PYTHON)

test: $(PYTHON)
	$(PYTHON) -m pytest $(python_code)

.PHONY: all clean docs debug-make format help lock sync test
