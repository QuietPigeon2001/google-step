import sys

# Usage: $python q2.py input_file output_file

SIZE = 26   
SCORES = [1,3,2,2,1,3,3,1,1,4,4,2,2,1,1,3,4,1,1,1,2,3,3,4,3,4]

def read(file):
    """
    Returns a list of strings read from each line in given file
    :type file: .txt
    :rtype: List[string]
    """
    words = file.readlines()
    words = [line.rstrip() for line in words]
    return words

def main():
    input_file = "medium.txt"    
    output_name = "a"

    output_file = open(output_name,'w+')

    # Reads words.txt and stores the words into a list
    with open("words.txt") as file:
        words = read(file)
    # Reads words.txt and stores the words into a list
    with open(input_file) as test_file:
        test_words = read(test_file)

    # List to store anagrams with the highest scores
    list = []

    # Iterates thru each string from file input
    for test in test_words:
        test_letter_frequency = [0] * SIZE

        # Dictionary to assign scores to each anagram
        word_scores = {}
        
        # Records frequencies of each char in test
        for i in range(len(test)):
            test_letter_frequency[ord(test[i]) - ord('a')] += 1

        # Iteratates thru the entire search list
        for i in range(len(words)):

            # Declares a new list of frequencies of each word
            dictionary_word_frequency = [0] * SIZE
            flag = False 
            score = 0

            # Records frequencies of each char in word:
            for letter in words[i]:
                dictionary_word_frequency[ord(letter) - ord('a')] += 1

            # Compares both lists of frequencies
            for k in range(SIZE):
                if dictionary_word_frequency[k] > test_letter_frequency[k]:
                    flag = True 
                    break
            
            # Calculates score for each anagram found
            if flag == False:
                for k in range(SIZE):
                    score += dictionary_word_frequency[k] * SCORES[k]
            word_scores[words[i]] = score
       
        # Finds the anagram with the highest score
        anagram = max(word_scores, key = word_scores.get)

        # Appends anagram to list
        list.append(anagram)    

    # Transfer elements from list to file output
    for w in list:
        output_file.write(w + "\n")
    
    return "File created."

    # Closes file
    output_file.close()

if __name__ == "__main__":
    print(main())
