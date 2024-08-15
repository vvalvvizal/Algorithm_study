n = int(input())

rank = [1] * n
people = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(n):
    for j in range(n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank[i] += 1

print(" ".join(map(str, rank)))

# n = int(input())

# rank= n
# list_ = [[] for _ in range(n+1)]
# result = [[] for _ in range(n+1)]
# for _ in range(1,n+1):
#     x, y = map(int, input().split())
#     list_.append((x,y))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#        if list_[j][0]>list_[i][0] and list_[j][1]>list_[i][1]:
#            result[i] = rank+1
