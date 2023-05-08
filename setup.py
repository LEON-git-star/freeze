#pip install py2exe
###pypy.py is filename
from distutils.core import setup
import py2exe

py2exe.freeze(
    windows=['pypy.py'],
    zipfile=None,
    options = {
    'compressed': 1,
    'optimize': 2,
    'bundle_files': 1,
    },
    version_info = {
        'version' : '1.0.0',
        'description' : 'a',
        'product_name' : 'a',
        'product_version' : '1.0.0',
        'copyright' : 'bbb',
    }
)
