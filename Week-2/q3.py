# Usage: Enter the url, then enter the webpage. Code exits when input is empty.

def cache_queue(cache, n):
    """
    Checks if the pair already exists in the cache. If yes, it will put the pair to the last of the table, else, the oldest pair will beremoved and the newest pair will be added.
    :type cache: Dictionary
    """  
    # Converts hash table to list
    ordered_list = []

    while True:
        print("Url:")
        url = input()
        print("Webpage: ")
        webpage = input()
         
        pair = {url: webpage}
        ordered_list.append(list(pair.items()))    
        if not url or not webpage:
            exit()
        
        if not url in cache:
            # Adds pair to hash table
            cache[url] = webpage
        else:
            ordered_list.remove(list(pair.items()))
        if len(ordered_list) > n:
            del cache[ordered_list[-1][0][0]]
            ordered_list.pop(0)

        print(ordered_list[::-1])

def main():
    cache = {}
    cache_queue(cache, 4)

if __name__ == "__main__":
    main() 
