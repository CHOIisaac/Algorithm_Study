def solution(num_list):
    answer = 0
    odd = 0
    even = 0 
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        elif i % 2 == 1:
            odd += num_list[i]
    answer = even if even > odd else odd
    return answer