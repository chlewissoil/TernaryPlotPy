# -*- mode: python -*-
"""A triangle-plot general class, meant to support the soil texture triangle. 
   Written by C. P. H. Lewis while at the University of California, Berkeley, 2008-2009. """
#TODO: use the transforms technique in matplotlib; see http://matplotlib.sourceforge.net/examples/api/custom_projection_example.html?highlight=subclass
import pylab as p
import matplotlib.cm as cm
from math import sqrt
from matplotlib.mlab import csv2rec
from matplotlib.mlab import load
from matplotlib.cbook import to_filehandle

class SoilTrianglePlot:
    """For plotting things like soil texture data, which we describe in three coordinates but really have two (silt+sand+clay == 100 percent).
    
    Formatting of colors, linestyles, etc. is mostly inherited from the matplotlib plot, which mostly uses MATLAB(tm) arguments. """

    def _toCart(self, threecoords):
        'Given an array of triples of coords in 0-100, returns arrays of Cartesian x- and y- coords'
        global type
        global sqrt
        assert (type(threecoords) == type([])), 'Expected a list of 3-coordinate tuple points'
        cartxs = []
        cartys = []
        for triple in threecoords:
            (b, l, r) = triple
            assert (b + l + r == 100), "3-coordinate values must sum to 100; %d, %d, %d don't" % (b, l, r)
            cartxs.append(100 - b - l / 2.0)
            cartys.append(sqrt(3) * l / 2.0)
        return (cartxs, cartys)

    def satisfies_bounds(self, point, limits):
        'point is 3 coordinates; limits is 3 pairs. Returns True or False (for closed set).'
        global True
        global False
        for i in [0, 1, 2]:
            if not (limits[i][0] <= point[i] <= limits[i][1]):
                return False
        return True

    def scatter(self, threecoords, **kwargs):
        'Scatterplots data given in triples, with the matplotlib keyword arguments'
        global p
        (xs, ys) = self._toCart(threecoords)
        p.scatter(xs, ys, **kwargs)

    def plot(self, threecoords, descriptor, **kwargs):
        'Plots data given in triples, with most of the matplotlib keyword arguments'
        global p
        (xs, ys) = self._toCart(threecoords)
        p.plot(xs, ys, descriptor, **kwargs)

    def colorbar(self, label):
        'Draws the colorbar and labels it'
        global p
        cb = p.colorbar()
        cb = cb.set_label(label)

    def line(self, begin, end, simplestyle = 'k-', **kwargs):
        global p
        (xs, ys) = self._toCart([begin, end])
        p.plot(xs, ys, simplestyle, **kwargs)

    def outline(self):
        self.line((0, 100, 0), (100, 0, 0), 'k-')
        self.line((0, 100, 0), (0, 0, 100), 'k-')
        self.line((0, 0, 100), (100, 0, 0), 'k-', label='_nolegend_')

    def grid(self, triple = ([25, 50, 100], [25, 50, 100], [25, 50, 100]), labels = ()):
        'Grid lines will be drawn for ([bottom],[left],[right]) values.'
        global p
        global str
        global len
        global sqrt
        (bs, ls, rs) = triple
        lstyle = {'color': '0.6',
         'dashes': (1, 1),
         'linewidth': 0.5}
        for b in bs:
            assert 0 <= b <= 100, 'Bottom value not in 0-100 range'
            self.line((b, 0, 100 - b), (b, 100 - b, 0), **lstyle)
            p.text(100 - b, -5, b, rotation=300, fontsize=9)
        for l in ls:
            assert 0 <= l <= 100, 'Left value not in 0-100 range'
            self.line((0, l, 100 - l), (100 - l, l, 0), **lstyle)
            p.text(l / 2.0 - 2 * len(str(l)), sqrt(3) * l / 2 - 1, l, fontsize=9)
        for r in rs:
            assert 0 <= r <= 100, 'Right value not in 0-100 range'
            self.line((0, 100 - r, r), (100 - r, 0, r), **lstyle)
            p.text(50 + r / 2.0, sqrt(3) * (50 - r / 2.0), r, rotation=60, fontsize=9)
        if (len(labels) > 0):
            p.text(50 - len(labels[0]) / 2, -12, labels[0], fontsize=8)
            p.text(15 - len(labels[1]) / 2, sqrt(3) * (25 - len(labels[1]) / 2), labels[1], rotation=60, fontsize=8)
            p.text(82 - len(labels[2]) / 2, 48 - len(labels[2]) / 2, labels[2], rotation=300, fontsize=8)

    def soil_categories(self, sclabel = '_nolegend_', country = 'USA'):
        """ Draws dashed lines between the soil-type categories. These are regional; options  are:
        'USA' (boundaries estimated from Brady & Weil, 12th ed, fig 4.7.)
        'Britain' (boundaries estimated from White, _Principles and Practices of Soil Science, 2006, fig. 2.3.a
        'Australia' (boundaries estimated from White, ibid., fig. 2.3.b)."""

        global p
        global range
        global sqrt
        global len
        self.grid((range(10, 100, 10), range(10, 100, 10), range(10, 100, 10)))
        lstyle = {'color': 'black',
         'dashes': (4, 1, 2, 1),
         'linewidth': 0.80000000000000004}
        if country=='USA':
            self.line((85, 0, 15), (90, 10, 0), **lstyle)
            self.line((70, 0, 30), (85, 15, 0), **lstyle)
            self.line((50, 0, 50), (23, 27, 50), **lstyle)
            self.line((20, 0, 80), (10, 10, 80), **lstyle)
            self.line((10, 10, 80), (0, 10, 90), **lstyle)
            self.line((80, 20, 0), (52, 20, 28), **lstyle)
            self.line((52, 20, 28), (45, 27, 28), **lstyle)
            self.line((45, 27, 28), (0, 27, 73), **lstyle)
            self.line((52, 20, 28), (52, 6, 42), **lstyle)
            self.line((52, 6, 42), (44, 6, 50), **lstyle)
            self.line((45, 27, 28), (45, 55, 0), **lstyle)
            self.line((65, 35, 0), (45, 35, 20), **lstyle)
            self.line((45, 40, 15), (0, 40, 60), **lstyle)
            self.line((20, 27, 53), (20, 40, 40), **lstyle)
            self.line((20, 40, 40), (0, 60, 40), label=sclabel, **lstyle)
        if country== 'Britain':
            self.line((85, 0, 15), (90, 10, 0), **lstyle)
            self.line((70, 0, 30), (85, 15, 0), **lstyle)
            self.line((82,18,0),(0,18,82), **lstyle)
            self.line((70,30,0),(50,30,20),**lstyle)
            self.line((50,30,20),(50,0,50), **lstyle)
            self.line((20,35,45),(20,0,80), **lstyle)
            self.line((0,55,45),(20,35,45), **lstyle)
            self.line((45,35,20),(0,35,65), **lstyle)
            self.line((45,35,20),(50,30,20),**lstyle)
            self.line((45,35,20),(45,55,0), **lstyle)
        if country == 'Australia':
            self.line((0,75,25),(75,0,25), **lstyle)
            self.line((35,40,25),(0,40,60), **lstyle)
            self.line((50,25,25),(0,25,75), **lstyle)
            self.line((50,25,25),(82,18,0), **lstyle)
            self.line((35,40,25),(72,28,0), **lstyle)
            self.line((92,0,8),(87,9,4), **lstyle)
            self.line((91.5,8.5,0),(63,12,25),**lstyle)
            self.line((76.25, 10.5, 13.25),(50,50,0),**lstyle)
        labels = ('Sand (%)', 'Clay (%)', 'Silt (%)')
        p.text(40 - len(labels[0]) / 2, -10, labels[0])
        p.text(13 - len(labels[1]) / 2, sqrt(3) * (25 - len(labels[1]) / 2), labels[1], rotation=60)
        p.text(80 - len(labels[2]) / 2, 50 - len(labels[2]) / 2, labels[2], rotation=300)

    def patch(self,limits, **kwargs): 
        '''Fill the area bounded by limits.
              Limits format: [[bmin,bmax],[lmin,lmax],[rmin,rmax]]
              Other arguments as for pylab.fill()'''
        coords = []
        bounds = [[1,-1,1],[1,0,-1],[-1,0,0],[1,-1,0],[1,1,-1],[-1,1,0],[0,-1,0],
                  [0,1,-1],[-1,1,1],[0,-1,1],[0,0,-1],[-1,0,1]]
        for pt in bounds:     #plug in values for these limits
            for i in [0,1,2]:
                if pt[i] == 1: 
                    pt[i] = limits[i][1]
                else:
                    if pt[i] == 0:pt[i] = limits[i][0]
            for i in [0,1,2]:
                if pt[i] == -1: pt[i] = 99 - sum(pt) 
            if self.satisfies_bounds(pt, limits): coords.append(pt) 
        coords.append(coords[0]) #close the loop
        xs, ys = self._toCart(coords)
        p.fill(xs, ys, **kwargs) 

    def scatter_from_csv(self, filename, sand = 'sand', silt = 'silt', clay = 'clay', diameter = '', hue = '', tags = '', **kwargs):
        """Loads data from filename (expects csv format). Needs one header row with at least the columns {sand, silt, clay}. Can also plot two more variables for each point; specify the header value for columns to be plotted as diameter, hue. Can also add a text tag offset from each point; specify the header value for those tags.
        Note! text values (header entries, tag values ) need to be quoted to be recognized as text. """
        fh = file(filename, 'rU')
        soilrec = csv2rec(fh)
        count = 0
        if (sand in soilrec.dtype.names):
            count = count + 1
        if (silt in soilrec.dtype.names):
            count = count + 1
        if (clay in soilrec.dtype.names):
            count = count + 1
        if (count < 3):
            print "ERROR: need columns for sand, silt and clay identified in ', filename"
        locargs = {'s': None, 'c': None}
        for (col, key) in ((diameter, 's'), (hue, 'c')):
            col = col.lower()
            if (col != '') and (col in soilrec.dtype.names):
                locargs[key] = soilrec.field(col)
            else:
                print 'ERROR: did not find ', col, 'in ', filename
        for k in kwargs:
            locargs[k] = kwargs[k]
        values = zip(*[soilrec.field(sand), soilrec.field(clay), soilrec.field(silt)])
        print values
        (xs, ys) = self._toCart(values)
        p.scatter(xs, ys, label='_', **locargs)
        if (tags != ''):
            tags = tags.lower()
            for (x, y, tag) in zip(*[xs, ys, soilrec.field(tags)]):
                print x,
                print y,
                print tag
                p.text(x + 1, y + 1, tag, fontsize=12)
        fh.close()

    def __init__(self, stitle = ''):
        global p
        global True
        p.clf()
        p.axis('off')
        p.axis('equal')
        p.hold(True)
        p.title(stitle)
        self.outline()

    def text(self, loctriple, word, **kwargs):
        global p
        (x, y) = self._toCart([loctriple])
        p.text(x[0], y[0], word, **kwargs)

    def show(self, filename = 'trianglegraph_test'):
        global p
        p.legend(loc=1)
        p.axis([-10, 110, -10, 110])
        p.ylim(-10, 100)
        p.savefig(filename)
        p.show()

    def close(self):
        global p
        p.close()

if (__name__ == '__main__'):
    print 'producing demo graph trianglegraph_test.png'
    st = SoilTrianglePlot('Soil Texture')
    st.text((65, 28, 7), 'Sandy clay loam', fontsize=9)
#    st.grid(([10, 20, 30, 40, 50, 60, 70, 80, 90], [25, 50, 75], [8, 52, 16]))
    st.soil_categories()
    st.line((30, 20, 50), (2, 98, 0), 'b:', label='line')
    st.patch([[10, 90], [50, 70], [10, 90]], facecolor='#249090', edgecolor='#451212', label='translucent', alpha='0.5')
    st.scatter([(50, 20, 30), (10, 90, 0), (0, 50, 50), (22,60,18)], s=50, c='g', label='data')
    st.patch([[0, 100], [83, 92], [5, 33]], facecolor='burlywood', label='patch')
    st.show()
