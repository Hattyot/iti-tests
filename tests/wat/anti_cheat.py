"""All of this is highly experminetal garbage."""
import gc
import sys


def no_exception_traceback():
    """__traceback__ gives access to frames"""
    gc.get_referents(BaseException.__dict__)[0]['__traceback__'] = None


def ban_some_imports():
    """
    Ban some imports that cant be banned by default in ptester.py
    this needs to be run before no_closure
    """
    banned_imports = ['pytest', '_pytest', 'importlib']
    sys.meta_path[0].find_spec.__closure__[0].cell_contents['banned_imports'] += banned_imports


def take_down_network():
    sys.meta_path[0].find_spec.__closure__[1].cell_contents.take_down_network()


def no_closure():
    """__closure__ gives access to cells which we dont want."""
    gc.get_referents(no_exception_traceback.__class__.__dict__)[0]['__closure__'] = None
