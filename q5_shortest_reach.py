# Question 5 Shortest Reach Function
# Author: Joachim Wambua

# Function to find shortest reach
def shortestReach(n, edges, s):
    # Initialise array to hold edge weights with initial value = -1
    edge_weights = [-1 for index in range(n)]
    # Initialise array variable to hold final result of cummulative edge weights
    result = []

    for x in range(n):
        edges[x][x] = 0
        edge_weights[x] = edges[s][x]

    visited_nodes = set()
    # Loop to check & evaluate least edge weights
    for y in range(n):
        pos = -1
        least_distance = -1
        for z in range(n):
            # Is current vertex either a source vertex or an already visited?
            if (z == s) or (z in visited_nodes):
                # If yes, skip
                continue
            # If an edge exists between two nodes/vertices
            if edge_weights[z] != -1:
                # if the least distance is -1 or greater than current edge weight,
                if (least_distance == -1) or (least_distance > edge_weights[z]):
                    # Set new least distance as the weight of current edge
                    least_distance = edge_weights[z]
                    pos = z
        if pos == -1:
            continue
        # Add current node to visited nodes once edge weight has been set
        visited_nodes.add(pos)

        for m in range(n):
            if edges[pos][m] == -1:
                continue
            # Check edge weights and add them accordingly
            if edge_weights[m] == -1 or edge_weights[m] > edge_weights[pos] + edges[pos][m]:
                # Cumulatively sum up the edge weights
                edge_weights[m] = edge_weights[pos] + edges[pos][m]
    for w in range(n):
        if w == s:
            continue
        # Append weight to final result array
        result.append(edge_weights[w])
    #  Return Final Result
    return result


if __name__ == '__main__':
    # User input for test
    test_cases = int(input('Enter No of Test Cases'))

    # Loop to collect user input for test cases
    for index in range(0, test_cases):
        # user input for no. of vertices
        n_ = int(input('Enter No of nodes: '))
        # user input for no. of edges
        edges_ = int(input('Enter No of edges: '))
        edge_arr = [[-1 for i in range(n_)] for i in range(n_)]

        # Loop through edges collecting their corresponding vertices and edge weights
        for j in range(0, edges_):
            first_node, second_node, weight = input().split()
            first_node = int(first_node) - 1
            second_node = int(second_node) - 1
            weight = int(weight)

            if (edge_arr[first_node][second_node] == -1) or (weight < edge_arr[first_node][second_node]):
                edge_arr[first_node][second_node] = weight
                edge_arr[second_node][first_node] = weight
        # Collect starting node/vertex from user input
        s = int(input('Enter starting node: '))
        s -= 1

        print(shortestReach(n_, edge_arr, s))

