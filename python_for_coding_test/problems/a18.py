def solution(p):
    answer = []

    def is_ok(mystr):
        stack = []
        for i in range(len(mystr)):
            if mystr[i]=="(":
                stack.append("(")
            else:
                try:
                    stack.pop()
                except:
                    return False
        return True

    if len(p)==0:
        return ""
    def separate(p):
        if len(p)==0:
            return ""
        stack = []
        stack.append(p[0])
        idx = 1
        while stack:
            if p[idx] != stack[-1]:
                stack.pop()
            else:
                stack.append(p[idx])
            idx+=1
        u, v = p[:idx], p[idx:]
        return u, v

    u,v = separate(p)
    if is_ok(u):
        answer.append(u)
        answer.append(solution(v))
    else:
        a = []
        for i in range(1, len(u)-1):
            if u[i]=="(":
                a.append(")")
            else:
                a.append("(")
        answer.append("(" + solution(v) + ")" + "".join(a))



    return "".join(answer)

p = "()))((()"
print(solution(p))