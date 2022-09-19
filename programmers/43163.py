from collections import deque


def solution(begin, target, words):
    answer = 0
    n = len(words) + 1
    graph = [[] for _ in range(n)]
    possible = False

    def is_differ_1(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return True

    def word(idx):
        if idx == 0:
            return begin
        else:
            return words[idx - 1]

    for i in range(n):
        for j in range(i + 1, n):
            if is_differ_1(word(i), word(j)):
                graph[i].append(j)
                graph[j].append(i)
        if not possible:
            if word(i) == target:
                possible = True

    if not possible:
        return 0

    def bfs(start):
        q = deque()
        q.append((start, 0))

        while q:
            u, step = q.popleft()
            if word(u) == target:
                return step
            for v in graph[u]:
                q.append((v, step + 1))
            print(u)

    return bfs(0)


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
