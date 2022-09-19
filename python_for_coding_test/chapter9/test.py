import heapq


def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v in graph[now]:  # 연결된 모든 vertex 탐색
            cost = dist + v[1]  # now를 거쳐서 v[0]로 가는 경우
            if cost < distance[v[0]]:  # 이 경우가 더 빠를경우
                distance[v[0]] = cost  # v[0]로 가는 거리 줄이고
                heapq.heappush(q, (cost, v[0]))  # heapq에 넣어서 추가 개선 여지 있나 확인
    