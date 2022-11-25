# import os
# import sys

# project = "NNDT"
# copyright = ""
# author = "Konstantin Ushenin"  # 'NNDT-team'

# master_doc = "index"  #

# extensions = [
#     "nbsphinx",  # provides a source parser for .ipynb files
#     "sphinx.ext.autodoc",  # include docs from docstrings
#     "sphinx.ext.mathjax",  # render math via JavaScript
#     "sphinx.ext.autosummary",  # generate autodoc summaries
#     "sphinx.ext.napoleon",  # support for NumPy and Google style docstrings
#     "sphinx.ext.viewcode",  # add links to highlighted source code
#     "sphinx_copybutton",  # add a "copy" button to code blocks.
#     "sphinx_tabs.tabs",  # create tabbed content in Sphinx documentation
# ]

# templates_path = ["_templates"]

# # todo_include_todos = True  # as GPJax

# nb_execution_mode = "auto"  # Execution mode for notebooks. 'off', 'force', 'cache', 'inline' are available
# nbsphinx_allow_errors = (
#     False  # stop build process if an exception is raised (in .ipynb)
# )
# # nbsphinx_execute_arguments = ["--InlineBackend.figure_formats={'svg', 'pdf'}"]
# nbsphinx_responsive_width = "700px"

# # LaTex config example:
# # https://github.com/JaxGaussianProcesses/GPJax/blob/master/docs/conf.py#LL122

# # Variables to decorate cite
# # html_static_path = ["_static"]
# # html_css_files = ["css/nndt_theme.css"]

# autosummary_generate = True
# autodoc_typehints = "none"  # As GPJax. "signature", "description", "none", "both"

# napoleon_use_rtype = False

# html_theme = "sphinx_book_theme"  # https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
# # Sometimes in the future...
# # html_logo = "_static/nndt_logo.svg"
# # html_favicon = "_static/nndt_logo.svg"
# Copyright 2018 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# Currently type aliases are expanded. We tried a workaround along the lines of:
# https://github.com/sphinx-doc/sphinx/issues/6518#issuecomment-589613836
# Unfortunately, this workaround makes Sphinx drop module-level documentation.
# See https://github.com/google/jax/issues/3452.

# -- Project information -----------------------------------------------------

project = "JAX"
copyright = "2020, The JAX Authors. NumPy and SciPy documentation are copyright the respective authors."
author = "The JAX authors"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "2.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath("sphinxext"))
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_autodoc_typehints",
    "myst_nb",
    "sphinx_remove_toctrees",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.8.1/", None),
}

suppress_warnings = [
    "ref.citation",  # Many duplicated citations in numpy/scipy docstrings.
    "ref.footnote",  # Many unreferenced footnotes in numpy/scipy docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# Note: important to list ipynb before md here: we have both md and ipynb
# copies of each notebook, and myst will choose which to convert based on
# the order in the source_suffix list. Notebooks which are not executed have
# outputs stored in ipynb but not in md, so we must convert the ipynb.
source_suffix = [".rst", ".ipynb", ".md"]

# The main toctree document.
main_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    # Sometimes sphinx reads its own outputs as inputs!
    "build/html",
    "build/jupyter_execute",
    "notebooks/README.md",
    "README.md",
    # Ignore markdown source for notebooks; myst-nb builds from the ipynb
    # These are kept in sync using the jupytext pre-commit hook.
    "notebooks/*.md",
    "jep/9407-type-promotion.md",
    # TODO: revert to jax-101/*.md once 08-pjit has a notebook
    "jax-101/01-jax-basics.md",
    "jax-101/02-jitting.md",
    "jax-101/03-vectorization.md",
    "jax-101/04-advanced-autodiff.md",
    "jax-101/05-random-numbers.md",
    "jax-101/05.1-pytrees.md",
    "jax-101/06-parallelism.md",
    "jax-101/07-state.md",
    "autodidax.md",
    # Attempt to fix RTD build failure
    "transformations.md",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


autosummary_generate = True
napolean_use_rtype = False

# mathjax_config = {
#     'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}},
# }

# Additional files needed for generating LaTeX/PDF output:
# latex_additional_files = ['references.bib']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo_only": True,
    "show_toc_level": 2,
    "repository_url": "https://github.com/google/jax",
    "use_repository_button": True,  # add a "link to repository" button
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/jax_logo_250px.png"

html_favicon = "_static/favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for myst ----------------------------------------------
myst_heading_anchors = 3  # auto-generate 3 levels of heading anchors
myst_enable_extensions = ["dollarmath"]
nb_execution_mode = "force"
nb_execution_allow_errors = False
nb_merge_streams = True

# Notebook cell execution timeout; defaults to 30.
nb_execution_timeout = 100

# List of patterns, relative to source directory, that match notebook
# files that will not be executed.
nb_execution_excludepatterns = [
    # Slow notebook: long time to load tf.ds
    "notebooks/neural_network_with_tfds_data.*",
    # Slow notebook
    "notebooks/Neural_Network_and_Data_Loading.*",
    # Strange error apparently due to asynchronous cell execution
    "notebooks/thinking_in_jax.*",
    # Has extra requirements: networkx, pandas, pytorch, tensorflow, etc.
    "jep/9407-type-promotion.*",
    # TODO(jakevdp): enable execution on the following if possible:
    "jax-101/*",
    "notebooks/xmap_tutorial.*",
    "notebooks/jax_Array.*",
]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "JAXdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (main_doc, "JAX.tex", "JAX Documentation", "The JAX authors", "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(main_doc, "jax", "JAX Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        main_doc,
        "JAX",
        "JAX Documentation",
        author,
        "JAX",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

# Tell sphinx-autodoc-typehints to generate stub parameter annotations including
# types, even if the parameters aren't explicitly documented.
always_document_param_types = True


# Remove auto-generated API docs from sidebars. They take too long to build.
remove_from_toctrees = ["_autosummary/*"]
