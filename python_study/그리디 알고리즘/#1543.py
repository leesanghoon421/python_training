word = str(input())
search = str(input())
#문자열과 찾고자하는 타겟 문자열을 입력받는다.
count = 0
i = 0
#카운터 역할을 할 count와 i를 0으로 초기화해놓음
while i <= len(word) - len(search):
    #문자열에서 위치를 잡고 타겟 문자열 길이만큼 조사를 하여
    if word[i:i + len(search)]==search:
        #일치할 경우 카운터 count를 증가시킴
        count += 1
        #i위치도 search의 길이만큼 옮겨서 다음조사를 준비
        i += len(search)
    else:
        #일치하는 문자열을 찾지 못한경우 한칸 옮겨서 다음 조사 진행
        i += 1
        
print(count)