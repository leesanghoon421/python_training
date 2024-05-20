#n by n pixel의 video를 압축하는 문제
#pixel수를 결정할 n을 입력받는다.
n=int(input())
#2차원 list를 입력받는다.
video=[list(map(int, input())) for k in range(n)]

#압축기 compressor 함수를 정의한다.
def compressor(x, y, n):    #parameter는 x,y좌표, n이다.
    pixel = video[x][y]     #특정좌표의 값을 pixel값으로 설정
#pixel의 오른쪽과 아래쪽으로 퍼져나가며 조사를 진행한다.
    for i in range(x, x+n):
        for j in range(y, y+n):
#조사한 부분중 pixel과 일치하지 않는 값이 존재하면 pixel을 -1로 설정
            if pixel != video[i][j]:
                pixel = -1
                break

#pixel값이 -1로 나오면 n을 절반으로 줄여서 조사를 다시 진행           
    if pixel == -1:
#이떄 새로운 괄호를 만들어준다.
        print("(", end='')
        n = n // 2
        compressor(x, y, n)
        compressor(x, y + n, n)
        compressor(x + n, y, n)
        compressor(x + n, y + n, n)
        print(")", end='')
#조사 내역이 전부 pixel과 일치하면 pixel값과 같게 압축한다.
    elif pixel == 1:
        print(1, end='')
        
    else:
        print(0, end='')
        
        
compressor(0, 0, n)