import sys
SIZE = 26   

def main():
    input_file= sys.argv[1]

    print("Enter output file name: (no need to include format)")
    name = input()
    output_file = open(name + ".txt", 'w+')

    # Reads words.txt and stores the words into a list
    with open("words.txt") as file:
        words = file.readlines()
        words = [line.rstrip() for line in words]

    # Reads words.txt and stores the words into a list
    with open(input_file) as test_file:
        test_words = test_file.readlines()
        test_words = [line.rstrip() for line in test_words]  

    scores = [1,3,2,2,1,3,3,1,1,4,4,2,2,1,1,3,4,1,1,1,2,3,3,4,3,4]
    
    # List to store anagrams with the highest scores
    list = []

    # Iterates thru each string from file input
    for test in test_words:
        freq1 = [0] * SIZE
        ls = len(test)

        # Dictionary to assign scores to each anagram
        test_dict = {}
        
        # Records frequencies of each char in test
        for i in range(ls):
            freq1[ord(test[i]) - ord('a')] += 1
            max_score = 0

        # Iteratates thru the entire search list
        for i in range(len(words)):

            # Declares a new list of frequencies of each word
            freq2 = [0] * SIZE
            flag = 0
            score = 0

            # Records frequencies of each char in word:
            for j in range(len(words[i])):
                freq2[ord(words[i][j]) - ord('a')] += 1


            # Compares both lists of frequencies
            for k in range(SIZE):
                if freq2[k] > freq1[k] and freq2[k] >= 1:
                    flag = 1
                    break
            
            # Calculates score for each anagram found
            if flag == 0:
                for k in range(SIZE):
                    score += freq2[k] * scores[k]
            test_dict[words[i]] = score
       
        # Finds the anagram with the highest score
        anagram = max(test_dict, key = test_dict.get)

        # Appends anagram to list
        list.append(anagram)    

    # Transfer elements from list to file output
    for w in list:
        output_file.write(w + "\n")

    # Closes files
    test_file.close()
    file.close()
    output_file.close()
    
    return "File created."

print(main())
