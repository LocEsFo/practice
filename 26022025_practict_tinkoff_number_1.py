def word_anton(word):
    count = 0
    word = word.lower()
    for char in word:
        if char == 'r':
            count += 1
        elif char == 'm':
            count -= 1
        if count == 1:
            return True
    
    return False
            
            
string = input('Введите набор: ')

print(word_anton(string))