word = input()

word1 = ''
word2 = ''
word3 = ''
min_word = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        word1 = word[:i]
        word2 = word[i:j]
        word3 = word[j:]    
        new_word = (f'{word1[::-1]}{word2[::-1]}{word3[::-1]}')
        
        if new_word<=min_word: #사전순으로 작은가?
            min_word = new_word 

        
print(min_word)