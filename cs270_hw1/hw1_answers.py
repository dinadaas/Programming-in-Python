
def hw1_answers(problem_number):
    if problem_number == "4.1.1":
        return "Must be either north, south, east, or west of the given state, of block type “d” “E” “R” and must be within the proper (x,y) confines of the given grid."
    if problem_number == "4.1.2":
        return "The worst case branching factor is 4, since there are four possible moves (every n,s,e,w block is visited). The size of the state space is the size of the given grid."
        
    if problem_number == "4.2.1":
        return "BFS without VSD would have to visit O(n) nodes, since it will have to cycle through each state each time. BFS+VSD would have to visit O(1) nodes, since only new states will be visited."
    if problem_number == "4.1.2":
        return "A grid of Boolean values indicating whether a state has been visited or not is the preferred method of VSD as opposed to a list of visited states, since with a grid of Boolean values, you do not need to iterate through the entire list to check to see if a state has been visited, as you would with method 1. Furthermore, the time and space complexity of the Boolean method is O(1) and O(n*m), respectively, as opposed to the time and space complexity of the list method, which is O(n) and O(n). "
        
    if problem_number == "4.3.1":
        return "Greedy search is indeed guaranteed to always find a path to the goal if one exists. This is because the only difference between gs and bfs is that it changes the order of chosing the next successor. This path is not guaranteed to be optimal, however, because the path taken by other methods could be shorter"
    if problem_number == "4.3.2":
        return "For my heuristic, I chose the function abs(self.goal[0] - state[0]) + abs(self.goal[1] - state[1]). This heuristic is admissable because it is optimistic, meaning it never overestimates the distance from the goal state. This result is guaranteed to be optimistic because the heuristic returns the sum of the total distance between the current and goal state. Furthermore, it is consistent because for each node N and each child N’ of N, the value returned is always less than or equal to the actual distance between the current and goal state."

    return "Invalid problem number"
