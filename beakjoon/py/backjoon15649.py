def backtrack():#DFS 
        if len(sequence)==m:#종료조건 
            print(" ".join(map(str,sequence)))
            return
        for i in range(1,n+1):
            if i not in sequence:
                 sequence.append(i)
                 backtrack()
                 sequence.pop()


n, m = map(int, input().split())
#길이가  m인 수열 
#길이가 m이 되면 가지쳐서 올라오기
sequence = [] 
visited = [False] * (n+1)
backtrack()
#n까지의 수 중에 길이가 m인 수열 
