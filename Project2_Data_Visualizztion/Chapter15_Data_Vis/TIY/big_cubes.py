# 15-2 Cubes:
    # Plot the first five cubic numbers
    # Then plot the first 5000 cubic numbers

import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c='red', s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

plt.show()