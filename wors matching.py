def match_words(words):
    count = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)

    print("Lists of words with first & last cahacter same\n", lst)
    return count
    
li = ["abc", "cfc", "xyz", "aba", "1221", "sajidsss", "safwansss", "nahiansss", "afnansss"]
word = match_words(li)
print("Number of words having first & last character same:", word)