# REVSim
 Revsim is a simple program which allows the user to test and create Representative Elementary Volume curves, or REV's.

Below is an example of a randomly generated array, an array of values (in the example below 0,1 or 2) rendered in a 100x100 grid.

![arrayimage](https://github.com/JBallGeo/REVSim/blob/main/images/randgrid.png)

We can sample this grid, to produce a plot of the samples, in this example we produce a simple moving average of a single sample, averaging the values as we increase the number of iterations. There is a cleare trend in the data towards the system mean which we have measured from the grid above.

![revsma](https://github.com/JBallGeo/REVSim/blob/main/images/revsma.png)


We can continue to model this many times, in this case 50 times over 50 sample iterations, as we can see the model will trend towards the mean however the upper and lower bounds becomes smaller. We can measure the slope of this function, which we call the conditioning gradient. It tells us how a model responds to input data, and how much input data we need to extract or put into a model to get a precise understanding of system averages.

![sphagimage](https://github.com/JBallGeo/REVSim/blob/main/images/sphagexample.png)


![minmaximage](https://github.com/JBallGeo/REVSim/blob/main/images/minmaxexample.png)

