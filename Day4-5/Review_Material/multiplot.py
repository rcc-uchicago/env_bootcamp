import matplotlib.pyplot as plt
import numpy as np

# This time will make a figure with two subplots arranged vertically.
# First we initialize our figure
plt.figure()

# Again We set up numpy arrays covering the range we want to plot.
xvals1 = np.linspace(-5, 5, 500)
xvals2 = np.linspace(-5, 5, 20)

# This creates a subplot on a notional grid with 2 rows and 1 column and
# selects the 1st plot (top row).
plt.subplot(211)

# Plot both sin(x) with a blue solid line and cos(x) with red dashed line. We
# can do this with a single plot() command.
plt.plot(xvals1, np.sin(xvals1), 'b-', xvals1, np.cos(xvals1), 'r--')

# And add a legend
plt.legend(["sin", "cos"])

# Select the lower plot
plt.subplot(212)

# Plot sinh(x) and cosh(x) with yellow triangles and green circles connected
# by lines. We do this as four plots - using the denser x value list for the
# lines, and sparser for the points.
# We can use several plot commands to do this.
plt.plot(xvals1, np.sinh(xvals1), 'y-')
plt.plot(xvals2, np.sinh(xvals2), 'y^', label="sinh")
plt.plot(xvals1, np.cosh(xvals1), 'g-')
plt.plot(xvals2, np.cosh(xvals2), 'go', label="cosh")
# Let also fill the area between the curves, but make it semi-transparent
# using the fill_between() function.
plt.fill_between(xvals1, np.cosh(xvals1), np.sinh(xvals1), facecolor='green',
        alpha=0.2)

# Tune a few other settings
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
# Since we've set some labels in the plot commands above we can call
# legend() without any arguments.
plt.legend()

# And finally we display our plot.
plt.show()

