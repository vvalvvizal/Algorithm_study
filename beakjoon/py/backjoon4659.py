while True:
    one = False
    two = True
    three = True

    check = {'a': 0, 'u': 0, 'i': 0, 'o': 0, 'e': 0}
    string = input()
    if string == 'end':
        break
    else:
        # 모음의 등장 횟수를 체크
        for s in string:
            if s in check:
                check[s] += 1
    

    if sum(check.values()) >= 1:
        one = True

    for i in range(len(string) - 2):
        if string[i] in check:
            if string[i+1] in check and string[i+2] in check:
                two = False
                break
        else:
            if string[i+1] not in check and string[i+2] not in check:
                two = False
                break

    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            if string[i] != 'e' and string[i] != 'o':
                three = False
                
    if one and two and three:
        print(f'<{string}> is acceptable.')
    else:
        print(f'<{string}> is not acceptable.')
