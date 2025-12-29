# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Data Load Script with DLT'
copyright = '2025, Aarish Gilani'
author = 'Aarish Gilani'
release = 'v0.0.1-alpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.mermaid']

# Mock imports for external dependencies
autodoc_mock_imports = [
    'dlt',
    'dlt.common',
    'dlt.sources',
    'dlt.sources.filesystem',
    'dlt.destinations',
    'pendulum',
    'pandas',
]

html_css_files = [
    'style.css',
]

html_theme_options = {
    'github_button': True,
    'github_user': 'aarishgilani',
    'github_repo': 'dlt-filesystem-sql',
    'github_type': 'No Text Variant',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
import site

# Add project root to path
sys.path.insert(0, os.path.abspath('../..'))

# Add system site-packages to access globally installed packages
sys.path.extend(site.getsitepackages())
