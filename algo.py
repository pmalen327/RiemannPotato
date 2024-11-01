import numpy as np


def potato(X: np.array) -> int:
    denom = X.shape[1] - 1
    # covariance matrix
    C = (X @ X.T) / denom

    return 0


# Computes a Riemannian metric between a matrix A and B
def ds(A: np.array, B: np.array) -> float:
    # compute similar matrix
    matC = (A)**(-1/2) @ B @ (A)**(-1/2)
    # compute eigenvalues
    eigen = np.linalg.eigvals(matC)
    metric = np.sqrt(sum([np.log(val)**2 for val in eigen]))
    return metric