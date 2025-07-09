def occurence():
    s = input("Enter the string")
    max_count = 0
    for ch in s:
        if ch.isalpha():
            count = s.count(ch)
            if count > max_count:
                max_count = count
                max_char = ch
    a = [max_char,max_count]
    return a 

print(occurence())
    
