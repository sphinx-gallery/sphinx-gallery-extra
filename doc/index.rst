======================
Sphinx-Gallery Extras!
======================

`Sphinx-Gallery <https://github.com/sphinx-gallery/sphinx-gallery>`_ is a `Sphinx <http://sphinx-doc.org/>`_
extension that lets you build galleries out of
your Python scripts. While sphinx-gallery has a lot of great functionality, there are always
new features that could be added! As the sphinx-gallery team needs to ensure that its package
remains stable for a diverse group of users, this can make it more difficult to try new ideas
in the core sphinx-gallery package.

This repository is for more experimental, still-evolving, or useful but out-of-scope features.
Its contents are **not** "officially" supported features of sphinx gallery, meaning that they
may not work in some Python versions, some documentation build systems, etc. However, we think
that having a place for this code will make it easier for the community to contribute in a
more fluid manner.

**See the sections below for a list of the features currently in this repository**

An image scraper for image files that are saved to disk
=======================================================


The gallery linked below contains examples that demonstrate the different sub-projects in
this repository.

.. toctree::

   auto_examples/index


Use Sphinx-Gallery with Jupyter Notebooks
=========================================

 If you'd like to store your examples in Jupyter Notebook format, Sphinx-Gallery
provides a helper function to convert ``.ipynb`` format into Python files formatted
for Sphinx-Gallery. Here's how to use it:
 1. Put your Jupyter Notebooks in a folder in your documentation
2. In your ``conf.py`` file, use the ``convert_ipynb_to_gallery`` function to
   generate Sphinx-Gallery python. For example, this code snippet uses ``glob`` to
   convert Jupyter Notebooks in the same folder:
    .. code-block:: python
      from glob import glob
      from sphinx_gallery.notebooks import convert_ipynb_to_gallery
       # Collect a list of all ipynb files
      ipynb_files = glob('path/to/my/notebooks/*.ipynb')
       # Loop through each file and convert to Sphinx-Gallery Python
      for nb_file in ipynb_files:
          convert_ipynb_to_gallery(nb_file)
 Now, Sphinx-Gallery will process these Python files for your gallery. We recommend
adding these files to your ``.gitignore`` file in order to avoid duplicating
content across your files.
