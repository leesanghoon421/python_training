import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
letters = list(map(str, input().split()))  
# 사전순으로 정렬
letters.sort()
# 가능한 조합 전부 생성
pos_code = combinations(letters, l)
# 모음 리스트 생성
vowel = ['a', 'e', 'i', 'o', 'u']
# 모음 1개 이상, 자음 2개 이상인 코드만 출력
for code in pos_code:
    vowel_num = 0
    const_num = 0
    for i in range(l):
        if code[i] in vowel:
            vowel_num += 1
        else:
            const_num += 1
    if vowel_num >=1 and const_num >=2:
        ans_code = ''.join(code)
        print(ans_code)