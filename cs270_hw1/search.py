
"""
In search.py, you will implement search algorithms and search problem
definitions
"""

import weakref
import heapq
import itertools


class SearchProblem:
    """
    This class outlines the structure of a search problem.

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        raise NotImplementedError()

    def is_goal_state(self, state):
        """
        Returns True if and only if the state is a valid goal state
        """
        raise NotImplementedError()

    def get_successors(self, state):
        raise NotImplementedError()

    def eval_heuristic(self,state):
        """Evaluates the heuristic function at a given state.  Default
        implementation returns 0 (trivial heuristic)."""
        return 0

class SearchNode:
    """Attributes:
    - state: a state object (problem dependent)
    - parent: a reference to the parent SearchNode or None.  If not None,
      this is a weak reference so that search trees are deleted upon last
      reference to the root.
    - paction: the action taken to arrive here from the parent (problem
      dependent)
    - children: a list of children
    """
    def __init__(self, state, parent=None, paction=None, arccost=1):
        """Initializes a SearchNode with a given state.
        """
        self.state = state
        self.parent = None
        if parent is not None:
            self.parent = weakref.proxy(parent)
            parent.children.append(self)
        self.paction = paction
        self.cost_from_start = 0
        if parent is not None:
            self.cost_from_start = parent.cost_from_start + arccost
        self.children = []

    def is_leaf(self):
        """Returns true if this is a leaf node"""
        return len(self.children) == 0

    def get_depth(self):
        """Returns the depth of this node (root depth = 0)"""
        if self.parent is None:
            return 0
        return self.parent.get_depth() + 1

    def path_from_root(self):
        """Returns the path from the root to this node"""
        if self.parent is None:
            return [self]
        p = self.parent.path_from_root()
        p.append(self)
        return p
        
def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    visitedList = []
    
    #*** YOUR CODE HERE ***
    #This takes a really long time due to revisited states.  How can
    #you detect them?
    root = SearchNode(problem.get_start_state())
    q = [root]
    while len(q) > 0:
        n = q.pop(0)
        if(n.state not in visitedList):
            visitedList.append(n.state)
            print "state",n.state,"depth",n.get_depth()
            succ, act = problem.get_successors(n.state)
            for (s,a) in zip(succ,act):
                c = SearchNode(s,n,a)
                if problem.is_goal_state(s):
                    return [n.paction for n in c.path_from_root() if n.parent != None]
                q.append(c)
    print "No path found!"
    return []

def greedy_search(problem):
    
    
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    def add_task(task):
        'Add a new task or update the priority of an existing task'
        priority = problem.eval_heuristic(task.state)
        if task in entry_finder:
            remove_task(task)
        count = next(counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heapq.heappush(pq, entry)

    def remove_task(task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task():
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while pq:
            priority, count, task = heapq.heappop(pq)
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
                
    visitedList = []
    
    #*** YOUR CODE HERE ***
    #This takes a really long time due to revisited states.  How can
    #you detect them?
    
    root = SearchNode(problem.get_start_state())
    add_task(root)
    while len(pq) > 0:
        n = pop_task()
        if(n.state not in visitedList):
            visitedList.append(n.state)
            print "state",n.state,"depth",n.get_depth()
            succ, act = problem.get_successors(n.state)
            for (s,a) in zip(succ,act):
                c = SearchNode(s,n,a)
                if problem.is_goal_state(s):
                    return [n.paction for n in c.path_from_root() if n.parent != None]
                add_task(c)
    print "No path found!"
    return []




def get_goal(grid):
    for i in range (len(grid)):
        for j in range (len(grid[0])):
            if(grid[i][j]=="R"):
                return (i,j)
    return -1

class MazeProblem(SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """
    def __init__(self, grid):
        """
        Stores the maze grid.
        """
        self.grid = grid
        self.goal = get_goal(grid)
        #*** YOUR CODE HERE (optional) ***
        

    def get_start_state(self):
        "Returns the start state"
        #*** YOUR CODE HERE ***
        for i,row in enumerate(self.grid):
            for j,val in enumerate(row):
                if val=='E':
                    return (i,j)
        raise ValueError("No player start state?")

    def is_goal_state(self, state):
        "Returns whether this search state is a goal state of the problem"
        #*** YOUR CODE HERE ***
        return self.grid[state[0]][state[1]] == 'R'

    def get_successors(self, state):
        """
        Returns successor states and actions.

        Return value: (succ,act) where
        - succ: a list of successor states
        - act: a list of actions, one for each successor state
        """
        successors = []
        actions = []
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        acts = ['n','s','e','w']
        for d,a in zip(dirs,acts):
            nstate = (state[0]+d[0],state[1]+d[1])
            if (nstate[0]>=0 and nstate[0]<len(self.grid) and nstate[1]>=0 and nstate[1]<len(self.grid[nstate[0]]) and self.grid[nstate[0]][nstate[1]]!="a"):
            #*** YOUR CODE HERE ***
            #This code is incorrect!  Not all of these states are successors
                successors.append(nstate)
                actions.append(a)
        return successors, actions

    def eval_heuristic(self,state):
        '''This is the heuristic that will be used for greedy search'''
        return abs(self.goal[0] - state[0]) + abs(self.goal[1] - state[1])


def pretty_print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print grid[i][j],
        print ""
