d, num = input().split() # d: 총 단계 수, num: 이동 경로를 나타내는 문자열
d = int(d) # d를 정수형으로 변환
x, y = map(int, input().split()) # x: 가로 이동거리, y: 세로 이동거리
size = (2**d)

def find(num, idx, curX, curY, size):
    # 단계가 0이 되면 현재 좌표를 기억하고 리턴
    if size == 0:
        # 전역 변수선언 
        global tarX, tarY
        tarX, tarY = curX, curY # 타겟 좌표 설정
        return

    # 자리수별로 번호에 따른 다음 이동을 찾아 재귀 호출
    if num[idx] == '1':
        find(num, idx+1, curX+size, curY+size, size//2)
    elif num[idx] == '2':
        find(num, idx+1, curX, curY+size, size//2)
    elif num[idx] == '3':
        find(num, idx+1, curX, curY, size//2)
    elif num[idx] == '4':
        find(num, idx+1, curX+size, curY, size//2)

# 좌표로 정답 숫자열을 찾는 translate함수
def translate(tarX, tarY, size, ans):
    # 단계가 0이 되면 정답 출력하고 리턴
    if size == 0:
        print(ans)
        return

    # 좌표를 바탕으로 size를 기준으로 단위 사각형을 찾아나감
    if size <= tarX < 2*size and size <= tarY < 2*size:
        translate(tarX-size, tarY-size, size//2, ans+'1')
    elif 0 <= tarX < size and size <= tarY < 2*size:
        translate(tarX, tarY-size, size//2, ans+'2')
    elif 0 <= tarX < size and 0 <= tarY < size:
        translate(tarX, tarY, size//2, ans+'3')
    elif size <= tarX < 2*size and 0 <= tarY < size:
        translate(tarX-size, tarY, size//2, ans+'4')

# 초기좌표 잡기
tarX = tarY = 0
find(num, 0, tarX, tarY, size//2)

# 이동거리만큼 좌표 이동
tarX += x
tarY += y

# 좌표가 범위내인지 체크
if 0 <= tarX < size and 0 <= tarY < size:
    translate(tarX, tarY, size//2, '')
else:
    print(-1)
