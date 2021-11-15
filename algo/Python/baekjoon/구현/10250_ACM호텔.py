for _ in range (int(input())):
    H,W,N = map(int, input().split())
    a = N%H
    b = N//H+1

    if ( a== 0 ) :
        a = H
        b -= 1

    print(a*100+b)