# exersice 4
chose = input("Do you want to code or decode (C/D): ").lower()
message = input("Enter your message: ").split()

result = []

for word in message:
    if chose == 'c':   # Coding
        if len(word) >= 3:
            new_word = word[1:] + word[0]   
            new_word = "abc" + new_word + "ghi"  
        else:
            new_word = word[::-1]          
    elif chose == 'd': # Decoding
        if len(word) < 3:
            new_word = word[::-1]
        else:
            core = word[3:-3]              
            new_word = core[-1] + core[:-1] 
    else:
        new_word = word
    result.append(new_word)

print(" ".join(result))