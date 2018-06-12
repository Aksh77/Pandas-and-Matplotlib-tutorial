import matplotlib.pyplot as plt
import numpy as np

# Create a Figure
fig = plt.figure(figsize=(12, 4))

#set up axes
#abc = number of rows (a), the number of columns (b) and the plot number (c)
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot the data

#vertical bars
ax1.bar([1,2,3],[3,4,5], width=0.25, color="darkgreen")
#vertical line
ax1.axvline(0.65, linewidth=4, color="lightgreen")

#horizontal bars
ax2.barh([0.5,1,2.5],[0,1,2], height=0.50, color="blue")
#horizontal line
ax2.axhline(0.45, linewidth=3, color="lightblue")

#scatter plot
x = np.random.randn(10)     #x-axis
y = np.random.randn(10)     #y-axis
ax3.scatter(x, y, marker='^')

# Show the plot
plt.show()
