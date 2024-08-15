while True:
    sstr = input()
    if sstr == '.':
        break
    stack = []
    for s in sstr:
        if s in '([':
            stack.append(s)
        elif s in ')]':
            if not stack or (s == ')' and '(' not in stack) or (s == ']' and '[' not in stack):
                stack.append(s)
                break
            else:
                if (s == ')' and stack[-1] == '(') or (s == ']' and stack[-1] == '['): #짝이 맞으면 
                    stack.pop() 
                else:
                    stack.append(s) 
                    break
    else:
        if not stack: #비어있으면 
            print('yes')
            continue
    print('no') #짝 안 맞는게 들어있으면 
