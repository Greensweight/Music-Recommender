import numpy as np
import math

def matrix_factorization(R,P,Q,K, steps, alpha, beta):
    for step in range(100):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    pq = 0
                    pq2 = 0
                    for k in range(K):
                        pq += P[i][k]*Q[k][j]
                        pq2 += P[i][k] * P[i][k] + Q[k][j]*Q[k][j]
                    e = math.sqrt((R[i][j] - pq)*(R[i][j] - pq) + (beta/2)*pq2)
                    print(e)
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2*e*Q[k][j]- beta*P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2*e*P[i][k]- beta*Q[k][j])
    return P, Q 


R = np.array([[5,3,0,1], [4,0,0,1], [1,1,0,5],[0,1,5,4]])
nRow = np.shape(R)[0]
nCol = np.shape(R)[1]
K = 2
P = np.random.random((nRow, K))
Q = np.random.random((K, nCol))
steps = 5000
alpha = 0.0002
beta = 0.02
nP = matrix_factorization(R,P,Q,K, steps, alpha, beta)[0]
nQ = matrix_factorization(R,P,Q,K, steps, alpha, beta)[1]
nR = np.matmul(nP,nQ)
print(R)
print(nR)
