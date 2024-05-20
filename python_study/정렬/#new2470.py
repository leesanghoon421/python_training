import sys

input = sys.stdin.readline

n = int(input())  # 입력받을 숫자의 개수를 정수형으로 입력받음
sol_list = list(map(int, input().split()))  # 숫자들을 입력받아 정수형 리스트로 저장
sol_list.sort()  # 리스트를 정렬

# 투포인터 알고리즘 이용
left, right = 0, n-1  # 리스트의 가장 왼쪽과 오른쪽 포인터를 0, n-1로 초기화
min_mix = float('inf')  # 가장 작은 합의 절대값을 초기화
result = None  # 최종 결과값을 초기화

while left < right:  # 왼쪽 포인터와 오른쪽 포인터가 서로 만날 때까지 반복
    mix = sol_list[left] + sol_list[right]  # 현재 두 값을 더함
    if abs(mix) < min_mix:  # 더한 값의 절대값이 현재까지의 최소값보다 작으면
        min_mix = abs(mix)  # 최소값을 업데이트
        result = (sol_list[left], sol_list[right])  # 현재 조합을 결과값으로 저장
    if mix == 0:  # 두 값의 합이 0이라면
        break  # 반복문 탈출
    elif mix < 0:  # 두 값의 합이 0보다 작다면
        left += 1  # 왼쪽 포인터를 오른쪽으로 한 칸 옮김
    else:  # 두 값의 합이 0보다 크다면
        right -= 1  # 오른쪽 포인터를 왼쪽으로 한 칸 옮김

print(*result)  # 결과값 출력
