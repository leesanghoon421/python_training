import sys
import itertools
input = sys.stdin.readline

n = int(input())
sol_list = list(map(int,input().split()))   # 산도를 입력받음
combi_list = itertools.combinations(sol_list, 2)    # 모든 조합 생성후 리스트에 담음
mixed_list = [sum(t) for t in combi_list]       # 튜플로 구성된 리스트에서 튜플값들을 더하여 리스트에 다시 입력
acid_list = [abs(num) for num in mixed_list]    # 해당 값들의 절대값을 리스트에 담음
min_mix = min(acid_list)    # 그중 최소값을 찾음
for i in range(n):
    for j in range(i+1, n):
        # 최소값과 일치하는 값을 갖고 있는 두 조합을 선택하여 출력
        if abs(sol_list[i] + sol_list[j]) == min_mix:
            print(sol_list[i], sol_list[j])
            break
# 이중 for문을 탈출하는 방법
    else:   
        continue
    break