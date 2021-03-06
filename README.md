# REVSim
 Revsim is an interactive tool which allows a user to generate, input, test and create Representative Elementary Volume curves, or REV's.

Below is an example of a randomly generated array, an array of values (in the example below 0,1 or 2) rendered in a 100x100 grid.

<img src="https://github.com/JamesEBall/REVSim/blob/main/images/randgrid.png" width=400>

We can sample this grid, to produce a plot of the samples, in this example we produce a simple moving average of a single sample, averaging the values as we increase the number of iterations. There is a clear trend in the data towards the system mean which we have measured from the grid above.

<img src="https://github.com/JamesEBall/REVSim/blob/main/images/revsma.png" width=500>


We can continue to model this many times, in this case 30 times over 500 sample iterations, as we can see the model will trend towards the mean however the upper and lower bounds becomes smaller. We can measure the slope of this function, which we call the conditioning gradient. It tells us how a model responds to input data, and how much input data we need to extract or put into a model to get a precise understanding of system averages.

<img src="https://github.com/JamesEBall/REVSim/blob/main/images/plots1.png" width=500>


