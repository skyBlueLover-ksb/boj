def solution(lines):
    answer = 1
    q = []
    first_start = None
    case = []
    for line in lines:
        end = int(line[11:13]) * 3600 + int(line[14:16]) * 60 + float(line[17:23])
        end = int(end * 1000)
        start = end - int(1000 * float(line[24:-1])) + 1
        q.append((start, end))
        case.append(end)
        if first_start:
            first_start = min(first_start, start)
        else:
            first_start = start
    case = [first_start] + case

    for c in case:
        number = 0
        for v in q:
            if v[0] >= c and v[0] < c + 1000:
                number += 1
            elif v[1] >= c and v[1] < c + 1000:
                number += 1
            elif v[0] <= c and c + 1000 <= v[1]:
                number += 1
        answer = max(number, answer)

    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
lines = 	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))