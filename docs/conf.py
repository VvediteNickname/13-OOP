# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
# Добавляем папку с исходным кодом в sys.path, чтобы Sphinx её нашёл.
# Если seq.py и fasta_reader.py лежат в родительской папке относительно docs/,
# то путь — "..". Если в той же папке — ".".
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "Classes for FASTA"
copyright = "2026, Тася"
author = "Тася"
release = "0.1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",       # авто-документация из docstrings
    "sphinx.ext.napoleon",      # поддержка Google/NumPy-style docstrings
    "sphinx.ext.viewcode",      # ссылки «[source]» рядом с классами
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "ru"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]