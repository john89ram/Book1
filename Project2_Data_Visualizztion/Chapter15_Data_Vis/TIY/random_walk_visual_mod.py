# 15-4 Modified Random Walks 
    # Modify the the choices in distance or take a direction out form the list and see how the patterns look when creating the graph.

import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Keep making new walks, as long as the program is active
while True:
    # Create an instance of RandomWalk
    rw = RandomWalk(50000)
    rw.fill_walk_modded()

    # Plot the point in the walk 
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=128)
    
    #ax.scatter(rw.x_values, rw.y_values, s=15)
    
    # Stylizing the walk to see important patterns
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
               edgecolors='none', s=15)
    # Emphasize the first and last points
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)
    
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break