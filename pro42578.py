import collections
def solution(clothes):
    answer = 1
    dict = collections.defaultdict(list)

    for clothe in clothes:
        dict[clothe[1]].append(clothe[0])

    for d in dict:
        answer = answer * (len(dict[d])+1)

    return answer-1