import re


def solution(words, queries):
    answer = [0]*len(queries)
    m = re.compile("prodo??")

    words_copy = words[:]
    for i in range(len(queries)):
        for w in words_copy:
            q = queries[i]
            m = re.compile(q)
            answer[i] += len(m.findall(w))

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))
