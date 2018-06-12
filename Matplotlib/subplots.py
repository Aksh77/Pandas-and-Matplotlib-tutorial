%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# Create a Figure
fig = plt.figure(figsize=(10,5))

#set up axes
#abc = number of rows (a), the number of columns (b) and the plot number (c)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

# Show the plot
plt.show()
