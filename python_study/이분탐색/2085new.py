N, M = map(int, input().split())
trees = list(map(int, input().split()))
#이분탐색을 위한 기준 start, end 설정
start, end = 1, max(trees) 

while start <= end:         #이분탐색 알고리즘 이용
    mid = (start+end) // 2  #중간점 mid 설정
    
    sum = 0   
    for i in trees:
        if i >= mid:
            sum += i - mid
    

    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)