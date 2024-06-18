# Copyright 2024 pyclinsci authors. See license.md file for details.

# Internal variables
NAME           = pyclinsci
INSTALL_STAMP  = .install.stamp
POETRY         = $(shell command -v poetry 2> /dev/null)
TESTOPTS       = -v
SPHINXBUILD    = sphinx-build
PAPER          = a4
SOURCEDIR      = docs/src
BUILDDIR       = docs
ALLSPHINXOPTS  = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) $(SOURCEDIR)
I18NSPHINXOPTS = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) ../..

# Default construction
.DEFAULT_GOAL := help

# Generate make help
.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install         installs packages and prepare environment"
	@echo "  clean           removes all temporary files and API docs"
	@echo "  format          runs ruff linter on source code"
	@echo "  test            runs all the tests using pytest"
	@echo "  sphinx-html     builds API HTML doc using Sphinx"
	@echo "  sphinx-pdf      builds API PDF doc using Sphinx"
	@echo "  sphinx-xml      builds API XML doc using Sphinx"
	@echo "  sphinx-clean    removes all API docs"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

# Install package
install: $(INSTALL_STAMP)
$(INSTALL_STAMP): pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install
	touch $(INSTALL_STAMP)

# Clean up all temporary files
.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP)
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	make sphinx-clean

# Test python package with pytest
.PHONY: test
test: $(INSTALL_STAMP)
	$(POETRY) run pytest $(TESTOPTS)

# Reformat source code
.PHONY: format
format: $(INSTALL_STAMP)
	$(POETRY) run ruff check --fix ./tests/ src/$(NAME)

# Clean up all temporary files
.PHONY: sphinx-clean
sphinx-clean:
	rm -rf $(BUILDDIR)/html
	rm -rf $(BUILDDIR)/xml
	rm -rf $(BUILDDIR)/*.pdf
	rm -rf $(BUILDDIR)/.buildinfo

# Generate HTML API user manual
.PHONY: sphinx-html
sphinx-html:
	$(POETRY) run $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	touch $(BUILDDIR)/.nojekyll
	rm -rf $(BUILDDIR)/doctrees/
	rm -rf $(BUILDDIR)/.nojekyll

# Generate PDF API user manual
.PHONY: sphinx-pdf
sphinx-pdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	mv $(BUILDDIR)/latex/*.pdf $(BUILDDIR)
	rm -rf $(BUILDDIR)/latex/
	rm -rf $(BUILDDIR)/doctrees/
	rm -rf $(BUILDDIR)/.nojekyll

# Generate XML API user manual
.PHONY: sphinx-xml
sphinx-xml:
	rm -rf $(BUILDDIR)/xml/
	$(SPHINXBUILD) -b xml $(ALLSPHINXOPTS) $(BUILDDIR)/xml
	rm -rf $(BUILDDIR)/doctrees/
	rm -rf $(BUILDDIR)/.nojekyll
