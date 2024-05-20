import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    n,m = list(map(int, input().split( )))
    value = list(map(int, input().split( )))
    index = list(range(len(value)))
    index[m] = "target"

    # 순서 설정을 위한 변수 초기화
    order = 0
    
    while True:
        # value의 첫번째 값이 최댓값인 경우
        if value[0]==max(value):
            order += 1
                        
            # index의 첫번쨰 값이 target인 경우
            if index[0]=="target":
                print(order)    # 출력
                break
            # index의 첫번째 값이 target이 아닌 경우
            else:
                value.pop(0)    # value의 첫번째 값 pop
                index.pop(0)    # index의 첫번째 값 pop
        # 전부 해당이 안되는 경우 value와 index의 첫번째 값을 맨뒤로 보냄
        else: 
            value.append(value.pop(0))
            index.append(index.pop(0))