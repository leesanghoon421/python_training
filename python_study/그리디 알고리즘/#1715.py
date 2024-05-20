import heapq
import sys
input = sys.stdin.readline

n=int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)    # cards 리스트를 힙으로 바꿔주는 함수
ans = 0        # 결과의 초기값을 0으로 설정

while len(cards) > 1:   # cards 리스트의 길이가 1보다 클때 연산을 진행
    tmp = heapq.heappop(cards) + heapq.heappop(cards)   # 최소값 두개의 합을 tmp에 저장하고
    heapq.heappush(cards, tmp)      # 해당 tmp값을 heap에 넣음
    ans += tmp      # 정답에 tmp값을 더해나감
    
print(ans)