# Convert ipynb file to Python so it will be processed
from sphinx_gallery import notebook as snb
snb.convert_ipynb_to_gallery('../examples/sin_func/plot_notebook.ipynb')