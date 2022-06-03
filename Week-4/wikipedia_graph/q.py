from collections import deque

def main():
    start = input("Enter starting point: ")
    end = input("Enter endpoint: ")
    pages = {}
    links = {}

    with open('data/pages_small.txt', encoding="utf8") as f:
        for data in f.read().splitlines():
            page = data.split('\t')
            # page[0]: id, page[1]: title
            pages[page[0]] = page[1]

    with open('data/links_small.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
            # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}

    def find_key(value, d):
        """
        Finds the key to the value
        :type value: str
        :type d: Dict{str: str}
        :rtype: str
        """
        for k, v in d.items():
            if v == value:
                return k
    
    # Get the IDs of our start and end points so that we don't have to run the code many times
    start_id = find_key(start, pages)
    end_id = find_key(end, pages)

    # Check if the inputs are valid
    if not find_key(start, pages) in pages or not find_key(end, pages) in pages:
        print("Location does not exist.")
        return 0

    def dfs_search(node, visited, links, target):
            """
            :type node: str
            :type links: Dict{str: str}
            :type target: str
            :rtype: List[str]
            """
        path = []
        def dfs(node, visited, links, target):
            # Check if the node has been visited, if yes then returns
            if node in visited:
                return

            # Mark node as visited
            visited.add(node)

            # Add the value to the node to path
            path.append(pages[node])

            # If node matches target
            if node == target:
                print("dfs", path)
                return path

            # If node exists in links
            if node in links:
                # Traverse the links with recursion
                nodes = links[node]
                for linked_node in nodes:
                    dfs(linked_node, visited, links, target)

        dfs(node, visited, links, target)


    def bfs(node, links, target):
        """
        :type node: str
        :type links: Dict{str: str}
        :type target: str
        :rtype: List[str]
        """
        path = []
        to_visit = [node]
        visited = set()

        # Traverse all vertices at the present depth
        while to_visit:
            next_nodes = []
            for to_visit_node in to_visit:
                # If node matches target
                if to_visit_node == target:
                    path.append(pages[to_visit_node])
                    print("bfs", path)
                    return path

                # If the node has been visited, then skip this iteration
                if to_visit_node in visited:
                    continue

                # Marks node as visited
                visited.add(to_visit_node)

                # Check if node is present in links
                if to_visit_node in links:
                    # Add the nodes of the following depth to the list
                    next_nodes += links[to_visit_node]

                    # Adds node to path
                    path.append(pages[to_visit_node])

            # Moves on to the lower depth
            to_visit = next_nodes

    dfs_search(start_id, set(), links, end_id)
    bfs(start_id, links, end_id)

if __name__ == '__main__':
    main()
