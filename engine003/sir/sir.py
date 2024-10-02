import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union

def sir(S : Union[int,float] , I : Union[int,float] , R : Union[int,float] , time : Union[int,float] , sir_values : List[Tuple[int, float]]):
    """Define SIR model
        Args : 
            S : float proportion susceptible
            I : float proportion infected
            R : float proportion recovered
            time : int simulation duration
            results
       
    """
    return NotImplemented


def visualize(time : np.array, sir_values: np.array):
    """Visualize sir curves
        Args : 
            time :  np.array simulation duration
            sir_values : np.array values of sir at each time during the simulation duration
       
    """
    return NotImplementedError