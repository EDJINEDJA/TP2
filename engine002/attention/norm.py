import numpy as np

def norm(d_k : int, similarity_matrix : np.array):
    """Normalize the cosine similarity matrix
        Args : 
            d_q : int (first dimension of the 1D matrix K_i)
            similarity_matrix : np.array (the matrix of the cosine similarity between vectors)
        Return :
            scale_dotProduct : np.array (1/sqrt(d_k)*dotProduct)
    """
    return NotImplementedError
