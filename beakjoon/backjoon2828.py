n, m = map(int, input().split())
j = int(input())
count =0
s_pos = 1
e_pos = m
for _ in range(j):
    x = int(input())

    if x < s_pos:
        count += (s_pos-x)
        s_pos = x
        e_pos = x+m-1 
    elif x>e_pos:
        count += (x-e_pos)
        e_pos = x 
        s_pos = e_pos - m +1

print(count)