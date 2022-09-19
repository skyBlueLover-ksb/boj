def solution(answers):
    answer = []
    n = len(answers)
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = 0, 0, 0

    for i in range(n):
        if a1[i % 5] == answers[i]:
            s1 += 1
        if a2[i % 8] == answers[i]:
            s2 += 1
        if a3[i % 10] == answers[i]:
            s3 += 1
    max_s = max(s1, s2, s3)
    s_l = [s1, s2, s3]
    for i in range(1, 4):
        if s_l[i - 1] == max_s:
            answer.append(i)

    return answer