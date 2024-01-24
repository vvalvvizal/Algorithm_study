n = int(input())
count = 0
length = 64
stick = []
total = 0

while total != n: 
    if n == length:
        stick.append(length)
        break
    else:
        length = length//2
        stick.append(length)
        total = sum(stick)
        if total>n:
            stick.remove(length)

print(len(stick))
