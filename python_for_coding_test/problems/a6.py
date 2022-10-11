import heapq
def solution(food_times, k):

    if sum(food_times)<=k:
        return -1

    used_time = 0
    prev_time = 0
    length = len(food_times)

    q = []
    for i, food_time in enumerate(food_times):
        heapq.heappush(q, (food_time, i+1))

    while used_time + ((q[0][0]-prev_time) * length) <= k:
        now = heapq.heappop(q)[0]
        used_time += (now-prev_time)*length
        length -= 1
        prev_time = now

    result = sorted(q, key=lambda x: (x[1], x[0]))
    return result[(k-used_time)%length][1]

