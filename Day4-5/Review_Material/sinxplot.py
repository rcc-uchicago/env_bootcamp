import matplotlib.pyplot as plt
import numpy as np

# We set up a numpy array covering the range we want to plot.
xvals = np.linspace(-5, 5, 500)

# Now we use these x-values to generate a series of coordinates to plot with
# whatever function we like. In this case we're using the numpy sin function.
# The plot() function is for plotting lines and points in 2D.
plt.plot(xvals, np.sin(xvals))

# We can add axes labels and a plot title.
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Test Plot')

# And finally we display our plot.
plt.show()
