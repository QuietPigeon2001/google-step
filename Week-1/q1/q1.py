def main():
    # Reads words.txt and stores the words into a list
    with open("words.txt") as file:
        words = file.readlines()
        words = [line.rstrip() for line in words]
    
    # Converts all characters to lower case
    word = input().lower()  

    # Rejects if input is empty or contains non-alphabetics
    if not word or not word.isalpha(): 
        return False

    # Sorts characters in the word in alphabetical order
    sorted_word = "".join(sorted(word))
    
    # Converts characters into string and sorts all the characters in all words in file in alphabetical order
    sorted_list = []
    for i in range(len(words)):
            w = "".join(sorted(words[i]))
            sorted_list.append(w)

    # Maps words to their own sorted characteres
    sorted_words_map = {}
    for i in range(len(words)):
        original_word = words[i]
        if not sorted_list[i] in sorted_words_map:
            sorted_words_map[sorted_list[i]] = [original_word]
        else:
            sorted_words_map[sorted_list[i]].append(original_word)

    return sorted_words_map[sorted_word]

if __name__== "__main__":
    print(main())
