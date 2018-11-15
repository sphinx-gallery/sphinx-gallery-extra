import sys
import copy
import os
import codecs
from .py_source_parser import split_code_and_text_blocks
from .utils import replace_py_ipynb

###############################################################################
# Notebook-to-SG Python utility
 def convert_ipynb_to_gallery(path_ipynb, folder_out=None):
    """Convert a Jupyter Notebook to a Sphinx-Gallery Python script.
     This is a (somewhat hacky) helper function to enable an
    .ipynb -> .py -> rst conversion within the Sphinx-Gallery workflow. It
    uses Pandoc to convert Jupyter Notebook markdown into a collection of
    Python and rST comment blocks.
     Parameters
    ----------
    path_ipynb : str
        Path to a Jupyter Notebook
    folder_out : str
        Path to an output folder where generated Python files will be placed.
     Outputs
    -------
    path_out : str
        Path to the output Python file.
    """
    try:
        import pypandoc as pdoc
    except ImportError:
        raise ImportError("ipynb to py conversion requires pandoc and pypandoc. "
                          "Please install them and re-run the function.")
    if folder_out is None:
        folder_out = os.path.dirname(path_ipynb)
     # Load the Jupyter Notebook and iterate through a list of its cells
    nb_dict = json.load(codecs.open(path_ipynb, encoding='utf-8'))
    cells = nb_dict['cells']
    python_file = ""
    for ii, cell in enumerate(cells):
        if ii == 0:
            if cell['cell_type'] != 'markdown':
                raise ValueError("The first cell of the Jupyter Notebook must be of"
                                "type 'markdown'. Found type %s" % cell['cell_type'])
            # Generate the rST and embed it in a comment.
            rst_source = _md_to_sg_py(''.join(cell['source']), comment=False)
            rst_source = '"""\n' + rst_source + '\n"""'
            python_file += rst_source
        else:
            if cell['cell_type'] == 'markdown':
                # Convert markdown into rst and add it to our source file
                # First line of comments to designate block
                rst_source = '\n\n\n'
                rst_source += '#' * 70 + '\n'
                rst_source += _md_to_sg_py(''.join(cell['source']))
                python_file += rst_source
            elif cell['cell_type'] == 'code':
                # If code, simply pass through the Python
                for ii, line in enumerate(cell['source']):
                    # Ensure "magics" are commented out
                    if line.startswith('%'):
                        cell['source'][ii] = line.replace('%', '# %', 1)
                    # If `plt.ion` is used, disable it so SG captures plots
                    if 'plt.ion' in line:
                        cell['source'][ii] = '# ' + line
                python_file += '\n\n'
                python_file += ''.join(cell['source'])
     # Write a new file name
    name_ipynb = os.path.basename(path_ipynb)
    path_out = os.path.join(folder_out, name_ipynb.replace('.ipynb', '.py'))
    with codecs.open(path_out, 'w', encoding='utf-8') as ff:
        ff.write(python_file)
    return path_out
 def _md_to_sg_py(md, comment=True):
    """Use pandoc to convert markdown to rst."""
    import pypandoc as pdoc
    rst = []
     # Create the rST and add comments to the start of each line
    rst_body = pdoc.convert_text(md, 'rst', 'md')
    for ln in rst_body.split('\n'):
        # Ensure that escape characters are double-escaped for Sphinx
        ln = ln.replace('\\', '\\\\')
        if comment is True:
            ln = '# ' + ln
        rst.append(ln)
    
    rst = '\n'.join(rst)
    return rst
 if __name__ == '__main__':
    import sys
    convert_ipynb_to_gallery(sys.argv[-1]) 