%matplotlib inline

# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

#customize color and linewidth
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)

#scatter plot
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')

plt.show()
