def solution(money, costs):
    pay = [1, 5, 10, 50, 100, 500]
    answer = 0
    money_left = money
    for i in range(6):
        m = money_left // pay[5 - i]
        m_cost = min([costs[j]*pay[5-i]/pay[j] for j in range(6-i)])
        answer += m*m_cost
        money_left -= m* pay[5-i]
        if money_left == 0:
            return answer