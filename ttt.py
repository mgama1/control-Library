from pyctrl import pyctrl as pyc
import numpy as np

A=np.array([[3, 10],[5,2]])
B=np.array([1,1])
C=np.array([1,0])
D=np.array([0])

print (pyc().ss2tf(A,B,C,D) )
