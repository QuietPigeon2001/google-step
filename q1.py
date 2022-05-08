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
    for i in range(len(words)):
        words[i] = sorted(words[i])

        # Converts characters into string
        words[i] = "".join(words[i])    

    # Newly sorted list
    sorted_list = sorted(words)     

    def binary_search(arr, x):
        """
        Function to search for the targeted string with binary search 
        """
        l = 0
        r = len(arr)
        while (l <= r):
            mid = l + ((r - l) // 2)
            res = (x == arr[mid])
            if (x == arr[mid]):
                return True 
     
            if (x > arr[mid]):
                l = mid + 1
     
            else:
                r = mid - 1
        return False

    res = binary_search(sorted_list, sorted_word)
    
    file.close()

    return res

    
print(main())
