def solution(my_string):
    answer = ''
    vowels = "aeiouAEIOU"
    answer = ''.join([char for char in my_string if char not in vowels])
    return answer