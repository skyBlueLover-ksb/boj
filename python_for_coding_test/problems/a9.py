def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        start = 0

        ans = 0
        while start + i <= len(s):
            part = s[start:start + i]
            start += i
            count = 0
            while start + i <= len(s) and part == s[start:start+i]:
                count += 1
                start += i
            if count > 0:
                ans += len(str(count + 1))+i
            else:
                ans += i
        ans += len(s) - start

        answer = min(answer, ans)

    return answer

s_l = ["aabbaccc", "ababcdcdababcdcd",
"abcabcdede",
"abcabcabcabcdededededede",
"xababcdcdababcdcd"]

for s in s_l:
    print(solution(s))