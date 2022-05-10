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

    # Sorted all the characters in all words in file in alphabetical order
    sorted_list = []
    for i in range(len(words)):
        # Converts characters into string
            w = "".join(sorted(words[i]))
            sorted_list.append(w)

    # Maps words to their own sorted characteres
    sorted_words_map = {}
    for i in range(len(words)):
        sorted_words_map[words[i]] = sorted_list[i]
   
    # Sorted items in list in alphabetical order
    sorted_list = sorted(sorted_list)

    def binary_search(sorted_array, search_string):
        """
        Function to search for the targeted string with binary search 
        """
        l = 0
        r = len(sorted_array)
        while (l <= r):
            mid = l + ((r - l) // 2)
            if (search_string == sorted_array[mid]):
                return sorted_array[mid]
            if (search_string > sorted_array[mid]):
                l = mid + 1
            else:
                r = mid - 1
        return False

    # Searches for key with values matching the anagram
    res = []
    for key in sorted_words_map:
        if sorted_words_map[key] == binary_search(sorted_list, sorted_word):
            res.append(key)

    return res

if __name__== "__main__":
    print(main())
