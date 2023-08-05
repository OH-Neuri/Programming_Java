def solution(arr):
    from math import gcd
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = answer * arr[i] // gcd(answer,arr[i])
    return answer