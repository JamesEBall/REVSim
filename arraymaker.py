import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pylab
import time 
import pandas as pd
import statistics
import math
from scipy.interpolate import UnivariateSpline
from random import randrange

import seaborn as sns
sns.set()

class grid:

    def __init__(self, x, y, params):
        #x = grid x
        #y = grid y
        #params number of facies

        self.x = x
        self.y = y
        self.params = params
        self.array = []
        self.cmap = []
        self.norm = []
        img = []
        


    def input(self, inputdata, params):
        self.array = inputdata
        self.x = inputdata[1]
        self.y = inputdata[0]
        self.params = params

    def update(self):
        return plt.imshow(self.array,interpolation='nearest',
                                cmap = self.cmap,norm=self.norm
                                )


    def genrandomgrid(self):
            self.array = np.random.randint(self.params, size=(self.x, self.y))

    def show2dgrid(self):
        global img
        bounds=[]

        for i in range (0,self.params+2):
            bounds.append(i)


        self.cmap = plt.cm.tab10  # define the colormap replace if needed
        # extract all colors from the .jet map
        cmaplist = [self.cmap(i) for i in range(self.cmap.N)]

        # create the new map
        self.cmap = mpl.colors.LinearSegmentedColormap.from_list(
            'Custom cmap', cmaplist, self.cmap.N)

        self.norm = mpl.colors.BoundaryNorm(bounds, self.cmap.N)


        # tell imshow about color map so that only set colors are used
        img = self.update()

        cmapbounds = bounds
        del cmapbounds[-1]
        #define ticks
        cblegend = cmapbounds

        #define colour bar remove blink colour
        cb = plt.colorbar(img,boundaries=cmapbounds,ticks=cblegend)
        labels = np.arange(0, int(cblegend[-1]), 1)
        loc = labels + .5
        cb.set_ticklabels(labels)
        cb.set_ticks(loc)
        cb.ax.tick_params(width=0)
        cb.set_label('Facies Value', rotation=90)
        self.update()
        return plt.show(block=False)

    def gridblink(self, x, y):
        global img
        reset = self.array[x, y]
        self.array[x, y] = self.params+1 #blinks with next colour
        self.update()
        time.sleep(1)
        self.array[x, y] = reset #blinks with next colour
        self.update()

    def randomreturn(self, n, iterations, valuemode):
        #arraystructure = [[x1,y1,v1],[x2,y2,v2]]

        cords = self.array
        shape = list(cords.shape)
        self.randarry = []
        self.graphdata = []
        data = []

        for i in range(0,iterations):
            randomseq = []
            for i in range(n):
                x = randrange(shape[1])
                y = randrange(shape[0])
                if valuemode == True:
                    randomseq.append([self.array[x,y]]) 
                    #only returns grid values and not x,y
                else:
                    randomseq.append(x,y,self.array[x,y]) 
                    #returns coords and value in array
            data.append(randomseq)
        self.graphdata = data
        return self.graphdata

    def mean(self): #returns mean value of array
        self.mean = np.mean(self.array)
        return self.mean

    def plot(self, type):
        #variables
        iterations = len(self.graphdata[0])
        numruns = len(self.graphdata)

        #creates moving adverages of data
        def movavg():
            def mov_avg(x, w):
                for m in range(len(x)-(w-1)):
                    yield sum(np.ones(w) * x[m:m+w]) / w 

            rawdata = self.graphdata

            data = {'y':[]}#dataframe
            df = pd.DataFrame(data)
            #df = df.transpose()

            x = []
            for n in range(0,iterations):
                x.append(n+1)

            self.iterations = x #x value for graph

            for run in range(0,numruns):
                y = [val for sublist in self.graphdata[run] for val in sublist]
                df['y'] = y
                df['SMA' + str(run)] = df.y.rolling(iterations, min_periods=1).mean()
            del df['y']
            return df

        df = movavg()

        #sphaghetti plot
        def sphagetti():

            #plot moving avergdge data from dataframe
            for run in range(0,numruns):
                plt.plot(self.iterations,df['SMA' + str(run)])

            plt.xlim([1,iterations])
            plt.ylim([0,self.params-1])
            plt.xlabel('Iterations')
            plt.ylabel('Measured property')


            print('Input parameters:')
            print('Iterations:', iterations)
            print('Number of sample runs:', numruns)
            print('Mean value:', self.mean())

            return plt.show(block=False)

        #minmax plot
        def minmax():

            #checks to see if minmax values have been generated, if not creates them.
            is_local = "minmaxdf" in locals()
            if is_local == True:
                return
            else:
                #creates new dataframe with max and min variables in.
                minmaxdf = pd.DataFrame()
                minmaxdf['iteration'] = self.iterations
                del self.iterations
                minmaxdf['Max'] = df.max(axis=1)
                minmaxdf['Min'] = df.min(axis=1)
                self.iterations = minmaxdf['iteration']

            max1 = minmaxdf['Max']
            min1 = minmaxdf['Min']
            x = minmaxdf['iteration']

            ymax = max1.values.tolist()
            ymin = min1.values.tolist()

            #curve is y = 1/x
            smax = UnivariateSpline(x, ymax, k=5, s=iterations)
            xsmax = np.linspace(0, iterations , 100)
            ysmax = smax(xsmax)

            smin = UnivariateSpline(x, ymin, k=5, s=iterations)
            xsmin = np.linspace(0, iterations , 100)
            ysmin = smin(xsmin)

            #plt.plot(xsmax, ysmax,color='red')
            #plt.plot(xsmin, ysmin,color='blue')
            
            plt.plot(x, max1, 'r+', alpha=0.3)
            plt.plot(x, min1, 'b+', alpha=0.3)


            mean = self.mean #call mean
            plt.axhline(mean, color='r', linestyle=':')#mean line
            plt.figtext(1, 0, mean, wrap=True, horizontalalignment='right', fontsize=12)#mean text
            plt.xlim([1,iterations])
            plt.ylim([0,self.params-1])
            plt.xlabel('Iterations')
            plt.ylabel('Measured property')
            
            return plt.show(block=False)


        #max min difference
        def minmax_curve():
            #checks to see if minmax values have been generated, if not creates them.
            is_local = "minmaxdf" in locals()
            if is_local == True:
                return
            else:
                #creates new dataframe with max and min variables in.
                minmaxdf = pd.DataFrame()
                minmaxdf['iteration'] = self.iterations
                minmaxdf['Max'] = df.max(axis=1)
                minmaxdf['Min'] = df.min(axis=1)
            
            #set x axis 
            x = minmaxdf['iteration']

            plt.plot(x, minmaxdf['Max'] - minmaxdf['Min'])
            plt.xlim([1,iterations])
            plt.ylim([0,self.params-1])
            plt.xlabel('Iterations')
            plt.ylabel('Max/min iter. difference')
            return plt.show(block=False)


        #standard deviation of each iteration
        def stdev():
            #checks to see if minmax values have been generated, if not creates them.
            is_local = "minmaxdf" in locals()
            if is_local == True:
                return
            else:
                #creates new dataframe with max and min variables in.
                minmaxdf = pd.DataFrame()
                minmaxdf['iteration'] = self.iterations
                minmaxdf['Max'] = df.max(axis=1)
                minmaxdf['Min'] = df.min(axis=1)
            
            e = []
            y = []
            epos = []
            eneg = []

            for row in range(0,len(self.iterations)):
                values = df.loc[row]
                values = list(values)
                dev = statistics.stdev(values,self.mean)
                e.append(dev/2)
                y.append(statistics.mean(list(values))) #mean
                epos.append(statistics.mean(list(values))+(dev/2)) #for graph
                eneg.append(statistics.mean(list(values))-(dev/2))

            x = self.iterations

            plt.plot(x, y)
            #plt.plot(x, epos)
            #plt.plot(x, eneg)
            plt.fill_between(x, epos, eneg,color='gray', alpha=0.2)
            plt.xlim(1, len(x))
            plt.xlabel('Iterations')
            plt.ylabel('Standard Deviation')





        if type == 'sphagetti':
            return sphagetti()
        elif type == 'minmax': #sphagetti must be plotted before minmax
            return minmax()
        elif type == 'minmax_curve': 
            return minmax_curve()
        elif type == 'stdev': #sphagetti must be plotted before stdev
            return stdev()
        else:
            return ('Error: no valid type selected')


