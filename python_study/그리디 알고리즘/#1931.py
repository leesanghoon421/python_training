N = int(input())
time_list = []

for i in range(N):
  start, end = map(int, input().split())
  time_list.append([start, end])

time_list.sort(key=lambda a: a[0])  # 시작 시간을 기준으로 오름차순 정렬
time_list.sort(key=lambda a: a[1])  # 끝나는 시간을 기준으로 다시 오름차순 정렬

fin_time = 0    # 회의의 마지막 시간
count = 0       # 회의의 수

for i, j in time_list:
  if i >= fin_time:     # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    count += 1          # counting 진행
    fin_time = j        # 마지막 시간 재설정

print(count)
