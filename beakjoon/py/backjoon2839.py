# n = int(input())
# count= 0
# if n >= 5:
#     tmp =  n // 5
#     count += tmp
#     n = n - tmp*5
#     if n>=3:
#         tmp = n//3
#         count += tmp
#         n = n - tmp * 3
#         if n>0:
#             count = -1
# if n>=3:
#    tmp = n//3
#    count += tmp
#    n = n - tmp * 3
#    if n>0:
#       count = -1
# else :
#     count = -1 

# print(count)

num = int(input())
count = 0

while num >= 0:
  if num % 5 == 0:
    count += int(num // 5)
    print(count)
    break
  
  num -= 3
  count += 1
  
else:
  print(-1)