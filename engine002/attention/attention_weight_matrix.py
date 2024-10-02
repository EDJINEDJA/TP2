import numpy as np

def A(a_x1 : np.array, a_x2 : np.array, a_x3 : np.array, a_x4 : np.array):
    """ Attention weight matrix
        Args :
           a_x1 : np.array 1D matrix (attention of x_1) 
           ...
           a_x4 : np.array 1D matrix (attention of x_4) 
        Return:
         A : np.array (attention weight matrix)

    """
    return NotImplementedError