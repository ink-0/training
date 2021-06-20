def solution(X, Y, D):
    Y-=X

    if Y%D ==0:
        return Y//D
    else:
        return Y//D+1
# https://app.codility.com/demo/results/trainingG568SX-GFT/
#