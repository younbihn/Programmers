# from collections import Counter

# def solution(participant, completion):
#     keys_view = (Counter(participant) - Counter(completion)).keys()
#     keys_list = list(keys_view)
#     answer = keys_list[0]
#     return answer

from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]