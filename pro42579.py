import collections, heapq
def solution(genres, plays):
    answer = []
    dict1 = collections.defaultdict(list)
    dict2 = collections.defaultdict(int)
    for i, (genre, play) in enumerate(zip(genres,plays)):
        dict1[genre].append((i, play))
        dict2[genre] += play

    for k, v  in sorted(dict2.items(), key = lambda x:x[1], reverse=True):
        for i,p in sorted(dict1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
genres =["classic", "pop", "classic", "classic", "pop"]
plays =[500, 600, 150, 800, 2500]
print(solution(genres, plays))
