import numpy as np
import math
from sklearn.decomposition import NMF
import warnings
warnings.filterwarnings("error")
def matrix_factorization(R,P,Q,K, steps, alpha, beta):
    for step in range(steps):
        #print("step: " + str(step))
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    pq = 0
                    pq2 = 0
                    for k in range(K):
                        try:
                            #pq += np.dot(P[i,:],Q[:,j])
                            pq += P[i][k]*Q[k][j]
                            #print("pq " + str(pq))
                            pq2 += P[i][k] * P[i][k] + Q[k][j]*Q[k][j]
                            #print("pq2 " + str(pq2))
                        except RuntimeWarning:
                            print(pq)
                            print(pq2)
                            #break
                            return P, Q 
                    try:
                        e = (R[i][j] - pq)
                        #e = math.sqrt(pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2) + (beta/2)*pq2)
                        #print("(R[i][j] - pq): " + str(R[i][j] - pq))
                        #print("(R[i][j] - pq)*(R[i][j] - pq): " + str((R[i][j] - pq)*(R[i][j] - pq)))
                        #e = R[i][j] - pq
                        #print("e " + str(e))
                    except RuntimeWarning:
                        print(e)
                        #break
                        return P, Q 
                    for k in range(K):
                        try:
                            P[i][k] = P[i][k] + alpha * (2*e*Q[k][j]- beta*P[i][k])
                            #print("Pik " + str(P[i][k]))
                            Q[k][j] = Q[k][j] + alpha * (2*e*P[i][k]- beta*Q[k][j])
                            #print("Qkj " + str(Q[k][j]))
                        except RuntimeWarning:
                            print(P[i][k])
                            print(Q[k][j])
                            #break
                            return P, Q 
    return P, Q 

print("Part 1")
R = np.array([[5,3,0,1], [4,0,0,1], [1,1,0,5],[1,0,0,4],[0,1,5,4]])
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
print("Using matrix_factorization function")
print(R)
print(nR)
print("Using sklearn NMR method")
model = NMF(n_components = K, init="random", random_state = 0, max_iter=5000)
W = model.fit_transform(R)
H = model.components_
nR2 = np.dot(W,H)
print(R)
print(nR2)
print("Part 2")
R = np.array([[4,3,0,1, 2], [5,0,0,1,0], [1,2,1,5,4],[1,0,0,4,0],[0,1,5,4,0],[5,5,0,0,1]])
nRow = np.shape(R)[0]
nCol = np.shape(R)[1]
K = 3
P = np.random.random((nRow, K))
Q = np.random.random((K, nCol))
steps = 10000
alpha = 0.0002
beta = 0.02
nP = matrix_factorization(R,P,Q,K, steps, alpha, beta)[0]
nQ = matrix_factorization(R,P,Q,K, steps, alpha, beta)[1]
nR = np.matmul(nP,nQ)
print("Using matrix_factorization function")
print(R)
print(nR)
print("Using sklearn NMR method")
model = NMF(n_components = K, init="random", random_state = 0, max_iter=10000)
W = model.fit_transform(R)
H = model.components_
nR2 = np.dot(W,H)
print(R)
print(nR2)

