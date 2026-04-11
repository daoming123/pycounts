# read version from installed package
from importlib.metadata import version

__version__ = version("pycounts")
# populate package namespace

from .pycounts import count_words  # noqa: F401
from .plotting import plot_words   # noqa: F401

