# import heapq #최소힙 

# def devide_conquer(n): #분할정복 
#     q1 = []
#     q2 = []
#     q3 =[]
#     q4 = []
#     result = []

#     if n==2: 
#         heapq.heappush(result,holl[0][0])
#         heapq.heappush(result,holl[0][1])
#         heapq.heappush(result,holl[1][1])
#         heapq.heappush(result,holl[1][0])

#     else:
#         for i in range(n//2):
#             for j in range(n//2):
#                 heapq.heappush(q1,holl[i][j])

#         for i in range(n//2,n):
#             for j in range(n//2, n):
#                 heapq.heappush(q4,holl[i][j])
#         for i in range(n//2):
#             for j in range(n//2,n):
#                 heapq.heappush(q2,holl[i][j])
#         for i in range(n//2, n):
#             for j in range(n//2):
#                 heapq.heappush(q3,holl[i][j])


#         qq1 =heapq.heappop(q1)
#         qq2 = heapq.heappop(q2)
#         qq3 = heapq.heappop(q3)
#         qq4 = heapq.heappop(q4)
#         #첫번째로 작은것들 빼내기 


#         heapq.heappush(result,qq1)
#         heapq.heappush(result,qq2)
#         heapq.heappush(result,qq3)
#         heapq.heappush(result,qq4)

#     heapq.heappop(result)

#     if n>=2:
#         return devide_conquer(n//2) #분할정복
#     else:
#         return heapq.heappop(result)

    
# n = int (input())
# holl = [[]*n for _ in range(n)]
# for i in range(n):
#     holl[i] = list(map(int,input().split()))

# min = devide_conquer(n)
# print(min) 

def find_special_seat(arr):
    if len(arr) == 1:
        return min(arr[0])

    n = len(arr)
    half = n // 2
    quarters = [
        [row[:half] for row in arr[:half]],
        [row[half:] for row in arr[:half]],
        [row[:half] for row in arr[half:]],
        [row[half:] for row in arr[half:]]
    ]

    candidates = []
    for quarter in quarters:
        candidates.append(find_special_seat(quarter))

    second_min = min(candidate for candidate in candidates if candidate != min(candidates))
    #이 윗줄 진짜 천재적이다
    return second_min


N = int(input())
chairs = [list(map(int, input().split())) for _ in range(N)]
result = find_special_seat(chairs)
print(result)