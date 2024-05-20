import sys

input = sys.stdin.readline  #시간초과 방지

N, M = map(int,input().split())     #나무 수 N, 원하는 나무 길이 M 입력
trees = [int(n) for n in input().split()]   #나무들의 길이 입력


def tree_cut():     #기준 길이를 정하는 함수 define
    standard_len = 0    #기준 길이 0으로 초기화
    while True:         # 기준 길이를 1씩 늘려주며 반복
        standard_len += 1
        sum = 0
        for i, tree in enumerate(trees):    #trees 리스트의 원소를 integer type으로 그대로 입력받기 위해 이용
            if tree > standard_len:         #tree의 길이가 기준 길이 보다 길면 그 차를 sum에 더해줌
                sum += tree - standard_len
            else:
                continue                    #tree의 길이가 기준 길이 보다 짧으면 그냥 넘어감
        if sum == M:                        #sum의 결과가 원하는 길이와 일치하면 해당 기준 길이를 출력
            return (standard_len)
        elif sum < M:                       #sum의 결과가 원하는 길이보다 작으면 이전 기준 길이를 이용해야 충분한 나무를 획득
            return (standard_len-1)

print(tree_cut())           #함수 결과를 출력