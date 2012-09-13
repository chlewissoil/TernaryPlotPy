'''Draws three triangle-axis plots; two are soil plots, one not. CPHLewis, UCBerkeley, 2008-2012.'''
from matplotlib import use
use('Agg') # This is a graphics backend; you might prefer another one
from trianglegraph import SoilTrianglePlot
import matplotlib.cm as cm

#One to load data from a .csv file
fstp = SoilTrianglePlot('Data read from triangleplot_demo.csv;\n size of marker increases with porosity')
fstp.soil_categories()
fstp.scatter_from_csv('triangleplot_demo.csv', diameter='porosity', hue='om', tags='site', cmap=cm.copper_r, alpha=0.5)
fstp.colorbar('Organic matter (%)')
fstp.show('triangleplot_subtle')

from random import sample, randint, random #to make up a pile of data, in function randomtriples
def randomtriples(count):
    xs = sample(range(0,100), count)
    ys = map(lambda x: randint(0, 100-x), xs)
    zs = map(lambda x: 100 - x, map(lambda x,y:x+y, xs, ys))
    ws = sample(range(0,300),count)
    cs = map(lambda x: random(), ws)
    return zip(xs, ys, zs), ws, cs

data, weights, colors = randomtriples(25) #Points are (bottom, left,right) , ie (sand, clay,silt)

stp = SoilTrianglePlot('The soil texture classes') # Argument is the plot title
stp.soil_categories() #Draws the boundaries of sandy loam, etc.
stp.scatter(data, s=weights, c=colors, label='_', cmap = cm.autumn, alpha=0.60, marker='d') #scatter doesn't work well with legend, so label="_" (hides it); cmap chooses the color scheme; alpha allows some transparency to see overlapping data
stp.colorbar('porosity')
stp.line((75,25,0),(0, 67, 33), 'g', label='model 1', linewidth=3) 
stp.line((12,80,8), (0,12,88), 'b', label='model 2', linewidth=3)
stp.show('triangleplot_gaudy') # is also saved to file of <argument> name

btp = SoilTrianglePlot('Soil categories of England and Wales')
btp.soil_categories(country='Britain')
btp.show('triangleplot_british')

atp = SoilTrianglePlot('Soil categories of Australia')
atp.soil_categories(country='Australia')
atp.show('triangleplot_australian')

tp = SoilTrianglePlot('Poetry as sociology') # No soil-specific stuff
tp.grid(([25,50,75],[33.3, 66.6],[20,40,60,80]), labels=('Sugar','Spice','Everything nice'))
tp.patch([[10,90],[50,70],[10,90]], facecolor='#eeaa88', label='observed')
tp.patch([[5,12],[22, 57],[60,100]], facecolor='#aa88ee', label='predicted')
tp.text((75, 15, 10), 'WHY?', fontsize=48)
tp.show('triangleplot_general')

 
