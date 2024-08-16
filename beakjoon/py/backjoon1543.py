import sys
document = []
list_ = input()


for i in list_:
    document.append(i)

find = []
list_ = input()

for i in list_:
        find.append(i)

count = 0
result = 0
i = 0

while i < len(document):
    if document[i:i+len(find)] == find:
        result += 1
        i += len(find)
    else:
        i += 1



print(result)