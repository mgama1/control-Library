import pytest
import sympy as sym
import numpy as np
from pyctrl import *
pyc=pyctrl()

def test_ss2tf_1():
    A = np.array([[3, 10], [5, 2]])
    B = np.array([1, 1])
    C = np.array([1, 0])
    D = np.array([0])
    assert (pyc.ss2tf(A,B,C,D) == sym.Matrix([[(s + 8)/(s**2 - 5*s - 44)]]))

