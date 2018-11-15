import os

import pytest
import numpy as np
from PIL import Image

from sphinx_gallery.gen_gallery import _complete_gallery_conf
from sphinx_gallery.scrapers import (figure_rst, mayavi_scraper, SINGLE_IMAGE,
                                     matplotlib_scraper, ImageFileScraper,
                                     ImagePathIterator, save_figures)
from sphinx_gallery.utils import _TempDir


@pytest.fixture
def gallery_conf(tmpdir):
    """Sets up a test sphinx-gallery configuration"""
    gallery_conf = _complete_gallery_conf({}, str(tmpdir), True, False)
    gallery_conf.update(examples_dir=_TempDir(), gallery_dir=str(tmpdir))
    return gallery_conf


def test_save_figures_to_disk(gallery_conf):	
    """Test embedding figures that were written to disk."""	
    path_file = os.path.dirname(__file__)	
    _touch(os.path.join(path_file, 'preexistingimage.png'))	
    gallery_conf.update(	
        image_scrapers=(matplotlib_scraper, ImageFileScraper()))	
    time.sleep(.2)  # To make sure file touches work as expected	
    fname_template = os.path.join(gallery_conf['gallery_dir'], 'image{0}.png')	
    image_path_iterator = ImagePathIterator(fname_template)	
    block = ('',) * 3	
    block_vars = dict(image_path_iterator=image_path_iterator,	
                      src_file=__file__)	
     # PNG	
    _touch(os.path.join(path_file, 'tmpimage.png'))	
    image_rst = save_figures(block, block_vars, gallery_conf)	
     assert len(image_path_iterator) == 1	
    assert '/image1.png' in image_rst	
    assert '/image2.png' not in image_rst	
     # JPG / 2 images in one block	
    _touch(os.path.join(path_file, 'tmpimage.jpeg'))	
    _touch(os.path.join(path_file, 'tmpimage.jpg'))	
     image_rst = save_figures(block, block_vars, gallery_conf)	
    assert len(image_path_iterator) == 3	
    assert '/image2.png' in image_rst	
    assert '/image3.png' in image_rst	
     # Cleanup	
    for ext in ['png', 'jpeg', 'jpg']:	
        os.remove(os.path.join(path_file, 'tmpimage.%s') % ext)	
    os.remove(os.path.join(path_file, 'preexistingimage.png'))


def _touch(path):	
    if os.path.exists(path):	
        os.utime(path, None)	
    else:	
        with open(path, 'w') as ff:	
            pass	