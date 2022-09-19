from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    tickets.sort(key=lambda x: (x[0], x[1]))

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for v in graph.keys():
        graph[v].sort(reverse=True)

    stack = ["ICN"]

    while stack:
        u = stack[-1]
        if not graph[u]:
            answer.append(stack.pop())
        else:
            stack.append(graph[u].pop())
    answer.reverse()

    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))