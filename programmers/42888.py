def solution(record):
    answer = []

    dic = {}

    for rec in record:
        rec = rec.split()
        if len(rec) == 3:
            dic[rec[1]] = rec[2]

    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            answer.append(dic[rec[1]]+"님이 들어왔습니다.")
        elif rec[0] == "Leave":
            answer.append(dic[rec[1]]+"님이 나갔습니다.")

    return answer
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record))

