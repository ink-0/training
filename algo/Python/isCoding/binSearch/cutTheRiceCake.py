def solution():
    n,m = map(int,input().split())
    high= list(map(int,input().split()))
    def bin_search(target,data,start,end):
        while start<=end:
            mid = (start+end)//2
            pri = data[mid]
            sumRice = sum([d-pri for d in data if d-pri>0])
            
            if sumRice>= target:
                return mid
            else:
                start = mid+1

    high.sort()
    result = bin_search(m,high,0,n-1)
    print(high[result])
solution()