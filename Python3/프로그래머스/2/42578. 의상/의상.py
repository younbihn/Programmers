from collections import Counter

def solution(clothes):
    kind_counter = Counter(kind for _, kind in clothes)
    answer = 1
    for cnt in kind_counter.values():
        answer *= (cnt + 1)
    return answer - 1