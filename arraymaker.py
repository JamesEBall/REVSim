import numpy as np


class Grid:

    def __init__(self, x, y, params) 
        #x = grid x
        #y = grid y
        #params number of facies

        self.x = x
        self.y = y
        self.params = 
        self.array = []



    def genrandomgrid(self, dimensions):
        if dimensions == 2:
            return(np.random.randint(self.params, size=(self.x, self.y)))
        else:
            return("Datashapes other than 2D have not been added yet")

    def show2dgrid(zvals, self.x, self.y, colours):
        #colours e.g. ['yellow','black','orange']
        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(colours)
        bounds =[ ]
        for i in range (0,self.params):
            bounds.append(i)
            
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        # tell imshow about color map so that only set colors are used
        img = plt.imshow(zvals,interpolation='nearest',
                            cmap = cmap,norm=norm)
        # make a color bar

        #define ticks
        cblegend = []
        for i in range(0,numvals):
            cblegend.append(i)
        
        cb = plt.colorbar(img,boundaries=bounds,ticks=cblegend)
        labels = np.arange(0, int(cblegend[-1]) + 1, 1)
        loc = labels + .5
        cb.set_ticklabels(labels)
        cb.set_ticks(loc)
        cb.ax.tick_params(width=0)
        cb.set_label('Facies Value', rotation=90)

