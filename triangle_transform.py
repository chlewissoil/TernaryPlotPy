# -*- mode: python -*-
"""A plotting class to plot three-part composition from tabular data. 
   Written by C. P. H. Lewis while at the University of California, Berkeley, 2008-2009. """

from matplotlib.axes import Axes
from matplotlib.mlab import csv2rec
from math import sqrt
from matplotlib.mlab import load
import matplotlib.cm as cm
from matplotlib.transforms import Affine2D


# This was written to display soil texture data: 
#   percent-silt + percent-clay + percent-sand == 100 
# Other fields may call it a three-phase diagram or even a simplex. 

class TriangleAxes(Axes):
    """Draws a triangle and uses it to plot data that we describe in three coordinates, but which really has two (e.g. silt+sand+clay == 100 percent). Can draw the boundaries of the US soil texture categories."""

#WORKING NOTES: following  http://matplotlib.sourceforge.net/examples/api/custom_projection_example.html?highlight=subclass , which is more complicated... Also, haven't figured out how Aff2D uses its 3rd D.x

    def __init__(self, *args, **kwargs):
        Axes.__init__(self, *args, **kwargs)
        self.triangle_transform = Affine2D([[0.5, sqrt(3)/2],[1,0]])
        self.cla()

     
