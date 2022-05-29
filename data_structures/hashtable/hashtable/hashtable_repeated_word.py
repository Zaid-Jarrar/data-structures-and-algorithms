from hashtable.hashtable_ import HashTable
# def hashmap_repeated_word(text):

    # words = ''
    # hashmap = HashTable()
    # 
    # for word in text:
    #     # converting the letter to lowercase
    #     lower_word = word.lower()
    #     # if the letter is a space or a punctuation mark, ignore it
    #     if ord(lower_word) in range(ord('a'), ord('z') + 1):
    #     # if the letter is a letter, add it to the words string
    #         words += lower_word
    #     # if the words length is greater than 1, check if the word is in the hashmap
    #     elif len(words):
    #         # if the word is in the hashmap, return the word
    #         if hashmap.contains(words):
    #             return words
    #         else:

    #             # if the word is not in the hashmap, add it to the hashmap
    #             hashmap.set(words, None)
    #             # reset the words string
    #             words= ''

    # return None
        
def repeated_word(text):
    try:
        words = ''
        hashmap = HashTable()
        for word in text:
            lower_word = word.lower()
            if ord(lower_word) in range(ord('a'), ord('z') + 1):
                words += lower_word
            elif len(words):
                if hashmap.contains(words):
                    return words
                else:
                    hashmap.set(words, None)
                    words = ''
        if len(words) and hashmap.contains(words):
            return words
        return None
    except Exception:
        raise Exception("Invalid input")

          

if __name__ == '__main__':
    text = "it it"
    print(repeated_word(text))
    # print(repeated_word(12))
