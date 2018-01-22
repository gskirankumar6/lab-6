def character_word_count(word):
    ls = []
for i in word:

    word_count = word.count(i)
    ls.append((i,word_count))
    return ls

print (character_word_count("i am good"))