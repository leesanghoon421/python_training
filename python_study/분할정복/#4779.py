import sys
for i in sys.stdin:
#패턴 초기화
    signal="-"
    for j in range(int(i)):
#패턴 분석을 통해 (signal + signal만큼의 공백 + signal)이
#그 다음 signal이 됨을 파악
        signal = signal+" "*len(signal)+signal
    print(signal)