N = int(input())
yaksu_list=list(map(int,input().split()))
yaksu_list.sort()
print(yaksu_list[-1]*yaksu_list[0])