import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Union, List

def f(x : np.array, t : np.array):
    """Define the f fonction
    Args :
        x : np.array
        t : np.array
    Return :
        return the function f
    """
    return NotImplementedError

def animator(x : List, t : List, path : str, f : f) -> None:
    """
    
    """
    # Define x_min and x_max from x 
    ...

    # Define t_min and t_max from t
    ...

    # Generate 100 values between x_min and x_max
    ...

    # Generate 100 values between t_min and t_max
    ...

    fig, axis = plt.subplots()

    axis.set_xlim([x_min, x_max])
    axis.set_ylim([-1, 1])

    # Add title
    ...

    # Add y_label
    ...

    # Add x_label
    ...

    animated_plot, = axis.plot([], [])

    def update_data(frame):
        """Define the update data function
           Args : 
            frame : int
        """

        t = t_values[frame]

        # For each t, calculate the Y with respect to X
        ...

        animated_plot.set_data(X, Y)
        return animated_plot,

    animation = FuncAnimation(fig=fig, func=update_data, frames=len(t_values), interval=25, repeat=True)

    # Save  the render using  the path
    ...

    plt.show()