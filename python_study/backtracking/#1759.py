import sys
input = sys.stdin.readline

l, c = map(int, input().split())
letters = list(map(str, input().split()))
# 사전순으로 정렬
letters.sort()
# 모음 리스트 생성
vowel = ['a', 'e', 'i', 'o', 'u']
# 정답 코드 담아둘 리스트
ans_code = []
# back_tracking 함수 생성
def back_tracking(cnt, idx):
    # 조건 체크
    if cnt == l:
        # 모음, 자음 개수 확인
        vowel_num, const_num = 0, 0
        for i in range(l):
            if ans_code[i] in vowel:
                vowel_num += 1
            else:
                const_num += 1

        # 모음 1개 이상, 자음 2개 이상
        if vowel_num >= 1 and const_num >= 2:
            ans = ''.join(ans_code)
            print(ans)
        return

    # 반복문을 통해 암호 생성
    for i in range(idx, c):
        ans_code.append(letters[i])
        back_tracking(cnt + 1, i + 1) # 재귀를 통한 백트래킹
        ans_code.pop()

back_tracking(0, 0)