<!-- Copyright 2024 pyclinsci authors. See license.md file for details. -->

# *pyclinsci*

*pyclinsci* is a Python package gathering tools for clinical science
activities. Beyond gathering different tools, the objective of this module is
to provide different method or classes to simplify development of new tools and
accelerate development of these tools.

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Installation](#installation)
  - [Install released version](#install-released-version)
  - [Install development version](#install-development-version)
- [Documentation](#documentation)
- [Contributing](#contributing)

<!-- /code_chunk_output -->

## Installation

### Install released version

*pyclinsci* is currently not available through
[pip](https://pip.pypa.io/en/stable) or
[conda](https://docs.conda.io/en/latest).

### Install development version

The different branches of *pyclinsci* are under active development. All
branches might not be properly documented. While `prod` branch is usually
stable, it may have undocumented changes or bugs.

If you want to keep up-to-date with the latest code, make sure you have
[Git](https://git-scm.com) installed, and then clone the `prod` branch (this
will create a *pyclinsci* directory in your current directory):

```bash
git clone --depth=1 https://github.com/brobertpc120/pyclinsci.git
```

When you want to update your copy of the source code, run `git pull` from
within the *pyclinsci* directory and Git will download and apply any changes.

This package has been developed using [Poetry](https://python-poetry.org/).
Poetry is a tool for dependency management and packaging in Python. It allows
you to declare the libraries your project depends on and it will manage
(install/update) them for you. Poetry offers a lockfile to ensure repeatable
installs, and can build your project for distribution.

In order to use Poetry, you need to install the Python package:

```bash
pip install pip poetry wheel setuptools -U
```

A `makefile` offers different possibilities to work with the package:

- `install` installs packages and prepare environment
- `clean` removes all temporary files and API docs
- `format` runs [ruff](https://docs.astral.sh/ruff/) linter on source code
- `test` runs all the tests using [pytest](https://docs.pytest.org/en/8.2.x/)
- `sphinx-html` builds API HTML doc using Sphinx
- `sphinx-pdf` builds API PDF doc using Sphinx
- `sphinx-xml` builds API XML doc using Sphinx
- `sphinx-clean`removes all API docs

## Documentation

## Contributing

All contributors of *pyclinsci* do not have dedicated time to develop and
support this package. As our resources are limited, we very much value your
contributions, be it bug fixes, new core features, or documentation
improvements. For more information, please read our
[contribution guide](contributing.md).
