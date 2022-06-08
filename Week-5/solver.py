import csv

def util(infile, outfile):
    """
    Main function for TSP
    :type: str
    :rtype: List[int]
    """

    # Reads input and create a list of coordinates
    with open(infile, 'r') as file:
        rows = csv.reader(file)
        next(rows)
        coords = list(rows)

    def cost(start, end):
        """
        Returns the distance between two nodes
        :type: List[float]
        :rtype: float
        """
        res = (start[0] - end[0])**2 + (start[1] - end[1])**2
        return res**0.5

    def maps(index, coords):
        """
        Calculates all the distances between the selected node and other nodes
        :type index: int
        :type coords: List[float]
        :rtype: Dict{int: float}
        """
        costs = {}
        coord = coords[index]
        for linked_node in coords:
            # Calculates distance between other points
            if linked_node != coord:
                costs[coords.index(linked_node)] = cost(linked_node, coord)
        return costs

    def get_key(val, d):
        """
        Returns the key of a given value
        :type val: float
        :type d: Dict{int: float}
        :rtype: int
        """
        for k, v in d.items():
            if val == v:
                return k

    # Converts list items from string to float
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            coords[i][j] = float(coords[i][j])

    route = []

    # Selects the first node as starting point
    curr = 0
    route.append(curr)
    links = {}

    # While the path has not contained all of the nodes
    while len(route) < len(coords):
        # Gets all the costs of travelling to other nodes
        nodes = maps(curr, coords)

        # Gets the next node with the minimum cost
        min_path = min(nodes.values())
        nx = get_key(min_path, nodes)

        while True:
            # Check if the next node is already in the route
            if nx in route:
                # Removes the node from selection
                nodes.pop(nx)

                # Get another node with the minimum cost 
                nx = get_key(min(nodes.values()), nodes)
            else:
                # Adds the next node to route
                route.append(nx)
                links[curr] = nx
                curr = nx
                break

    print(links)

    def swap(route, node_1, node_2):
        new_route = []
        new_route.append(route[0])
        new_route.append(route[node_1])
        new_route.append(route[node_2])
        new_route.append(route[node_1 + 1])
        for i in range(node_2, len(route)):
            new_route.append(route[i])
        return new_route

    def pathLength(route):
        path_length = 0
        for i in range(len(route) - 1):
            path_length += cost(coords[route[i]], coords[route[i+1]])
        return path_length

    shortened = True
    while shortened:
        shorted = False
        curr_route = route
        curr_len = pathLength(route)
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                new_route = swap(route, i, j)
                new_length = pathLength(new_route)
                if new_length < curr_len:
                    curr_route = new_route
                    curr_len = new_length
                    shortened = True
                print(i, j)
                print(shortened)
    print(curr_route)

    print(pathLength(route))

    
    # Converts list items in route from int to str
    for i in range(len(route)):
        route[i] = str(route[i])

    # Overwrites the output file with the header "index"
    header = ["index"]
    with open(outfile, 'w', newline='') as output:
        writer = csv.writer(output, delimiter=",")
        writer.writerow(header)
        for row in route:
            col = [num.strip() for num in row.strip(', ').split(',')]
            writer.writerow(col)

    return route

def main():
    # Iterates thru all 7 inputs
    for i in range(1):
        infile = "google-step-tsp/input_" + str(i) + ".csv"
        outfile = "google-step-tsp/output_" + str(i) + ".csv"
        util(infile, outfile)
        print(i)
        if i == 6:
            print("Done!")

if __name__ == "__main__":
    main()