
import numpy

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    '''
    R: rating matrix
    P: |U| * K (User features matrix)
    Q: |D| * K (Item features matrix)
    K: latent features
    steps: iterations
    alpha: learning rate
    beta: regularization parameter'''
    Q = Q

    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    # calculate error
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])

                    for k in range(K):
                        # calculate gradient with a and beta parameter
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])

        eR = numpy.dot(P,Q)

        e = 0

        for i in range(len(R)):

            for j in range(len(R[i])):

                if R[i][j] > 0:

                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)

                    for k in range(K):

                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        # 0.001: local minimum
        if e < 0.001:

            break

    return P, Q

R = numpy.array([[5,3,0,1], [4,0,0,1], [1,1,0,5],[0,1,5,4]])
nRow = numpy.shape(R)[0]
nCol = numpy.shape(R)[1]
K = 2
P = numpy.random.random((nRow, K))
Q = numpy.random.random((K, nCol))
steps = 5000
alpha = 0.0002
beta = 0.02
nP = matrix_factorization(R,P,Q,K, steps, alpha, beta)[0]
nQ = matrix_factorization(R,P,Q,K, steps, alpha, beta)[1]
nR = numpy.matmul(nP,nQ)
print(R)
print(nR)
