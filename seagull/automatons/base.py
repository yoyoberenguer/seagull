# -*- coding: utf-8 -*-

"""Base class for all Automaton implementations"""


# Import standard library
import abc
from typing import Dict, Tuple, Union

# Import modules
import numpy as np
from matplotlib.axes._subplots import AxesSubplot


class Automaton(abc.ABC):
    """Base class for all Automaton implementation"""

    @abc.abstractproperty
    def layout(self) -> np.ndarray:
        """numpy.ndarray: Automaton layout or structure"""
        pass

    @property
    def size(self) -> Tuple[int, int]:
        """tuple: Size of the automaton"""
        return self.layout.shape

    def view(self) -> AxesSubplot:
        """View the automaton

        Returns
        -------
        matplotlib.axes._subplots.AxesSubplot
            Graphical view of the automaton
        """
        pass
