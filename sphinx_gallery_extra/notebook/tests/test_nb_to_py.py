from __future__ import division, absolute_import, print_function
import json
import tempfile
import os
import pytest
import codecs

import sphinx_gallery.gen_rst as sg
from sphinx_gallery.notebook import (rst2md, jupyter_notebook, save_notebook,
                                     python_to_jupyter_cli, convert_ipynb_to_gallery)
from sphinx_gallery.tests.test_gen_rst import gallery_conf


###############################################################################
# Notebook to Python converter
 def test_notebook_to_sg_py():
    """Test that notebook to Python conversion works as expected."""
    path_base = os.path.dirname(__file__)
    path_notebook = os.path.join(path_base, 'tinybuild', 'notebooks', 'plot_notebook.ipynb')
    path_examples = os.path.join(path_base, 'tinybuild', 'examples')
    convert_ipynb_to_gallery(path_notebook, path_examples)
    with codecs.open(os.path.join(path_examples, 'plot_notebook.py'), encoding='utf-8') as ff:
        lines = ff.read()
    assert '.. math::\n\n\n   e=mc^2' in lines
    assert ':math:`e=mc^2' in lines
    assert '\n# plt.ion()' in lines
    assert '\n# %matplotlib inline' in lines