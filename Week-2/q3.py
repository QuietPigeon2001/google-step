# Usage: Enter the url, then enter the webpage. Code exits when input is empty.

def cache_queue(cache):
    """
    Checks if the pair already exists in the cache. If yes, it will put the pair to the last of the table, else, the oldest pair will be removed and the newest pair will be added.
    :type cache: Dictionary
    """
    print("Url:")
    url = input()
    print("Webpage: ")
    webpage = input()

    if not url or not webpage:
        exit()
    
    # Converts hash table to list
    cache_list = list(cache.items())

    if not url in cache:
        # Adds pair to hash table
        cache[url] = webpage

        # Deletes the first item in the list from hash table
        del cache[cache_list[0][0]]
    else:
        # Removes pair from hash table
        del cache[url]

        # Adds pair back to the end of the hash table
        cache[url] = webpage

    print(cache)

def main():  
    cache = {"d.com": "D", "c.com": "C", "e.com": "E", "a.com": "A"}
    print(cache)
    while True:
        cache_queue(cache)

if __name__ == "__main__":
    main()
