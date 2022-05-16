# Usage: Enter the url, then enter the webpage. Code exits when input is empty.

def cache_queue(cache, n):
    """
    Checks if the pair already exists in the cache. If yes, it will put the pair to the last of the table, else, the oldest pair will beremoved and the newest pair will be added.
    :type cache: Dictionary
    :type n: int 
    """ 
    # A list to store the order of url's (oldest -> newest)
    ordered_list = []

    while True:
        # Prompts for user input
        print("Url:")
        url = input()
        print("Webpage: ")
        webpage = input()
            
        # Adds url to list to record order (in reverse order)
        ordered_list.append(url)

        # Exits program when no input is registered
        if not url or not webpage:
            exit()
        
        # Checks if the url is already in cache
        if not url in cache:
            # Adds pair to cache
            cache[url] = webpage
        else:
            # Refreshes order of url when repeated
            ordered_list.remove(url)

        # Checks if the number of url's exceeds length    
        if len(ordered_list) > n:
            # Removes the oldest cache and its order
            del cache[ordered_list[-1]]
            ordered_list.pop(0)
        
        # Prints url in reverse order (newest -> oldest)
        print(ordered_list[::-1])

def main():
    # Initializes hash table 
    cache = {}
    # n = maximum number of url's stored
    print("Enter the max. no. of cache to be stored: ")
    n = int(input())
    cache_queue(cache, n)

if __name__ == "__main__":
    main() 
