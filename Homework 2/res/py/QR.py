import numpy as np

def QR(A):
    R = np.zeros_like(A, shape=(n,n))
    V = np.array(A)
    m,n = V.shape
    for i in range(n):
        R[i,i]      = np.linalg.norm(V[:,i], axis=0)
        Qi          = np.divide(V[:,i], R[i,i])
        R[i,i+1:n]  = Qi @ V[:,i+1:n]
        V[:,i+1:n] -= np.einsum('i,j->ij', Qi, R[i,i+1:n])
    return V, R

def dummy_modified_gs(A):
    n = len(A)
    R = np.zeros_like(A)
    Q = np.zeros((n,n))
    V = np.array(A)

    for i in range(n):
        ei = np.linalg.norm(V[:,i],axis=0)
        R[i,i] = ei
        Q[:,i] = V[:,i]/ ei
        for j in range(i+1, n):
            R[i,j] = Q[:,i] @ V[:,j]
            V[:,j] -= R[i,j]*Q[:,i]

    return (Q, R)

def dummy_gs(A):
    m,n = A.shape
    R = np.zeros((n,n))
    Q = np.zeros_like(A)
    V = np.array(A)

    for i in range(n):
        for j in range(i):
            R[i,j] = Q[:,i] @ V[:,j]
            V[:,j] -= R[i,j]*Q[:,i]
        R[i,i] = np.linalg.norm(V[:,i])
        Q[:,i] = np.divide(V[:,i], R[i,i])
    return (Q, R)
