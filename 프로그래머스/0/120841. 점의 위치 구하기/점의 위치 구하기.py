def solution(dot):
    answer = 0
    a, b = dot
    
    if a > 0 and b > 0:
        answer = 1
    elif a < 0 and b > 0:
        answer = 2
    elif a < 0 and b < 0:
        answer = 3
    else:
        answer = 4
    return answer