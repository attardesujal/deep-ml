import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    if not vectors:
        return []
    
    # Check if there are observations to avoid division by zero errors
    if len(vectors[0]) <= 1:
        raise ValueError("Covariance requires at least 2 observations per feature.")
    
    # np.cov uses ddof=1 (sample covariance) by default
    cov_matrix = np.cov(vectors)
    
    # Handle edge case where input is a single feature
    if cov_matrix.ndim == 0:
        return [[float(cov_matrix)]]
        
    return cov_matrix.tolist()
