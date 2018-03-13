import util

def depthFirstSearch(problem):
    fringe = util.Stack()
    current_state = [problem.getStartState(), []]
    successors = None
    explored = set()
    item = None

    while(not problem.isGoalState(current_state[0])):
        (current_pos, directions) = current_state 
        successors = problem.getSuccessors(current_state[0])
        for nextGameState, action, cost in successors:
            fringe.push((nextGameState, directions + [action]))
        while (True):
            if (fringe.isEmpty()):
                return None
            item = fringe.pop() 
            if (str(item[0]) not in explored):
                break    
        current_state = item
        explored.add(str(item[0]))
    
    
    solution= current_state
    return solution
    
def breadthFirstSearch(problem):
    fringe = util.Queue()
    current_state = [problem.getStartState(), []]
    fringe.push(current_state)
    visited = []
    while not fringe.isEmpty():
        current_state= fringe.pop()
        node, actions = current_state
        for nextGameState, action, cost in problem.getSuccessors(node):
            if not str(nextGameState) in visited:
                if problem.isGoalState(nextGameState):
                    return (nextGameState ,actions + [action])
                fringe.push((nextGameState, actions + [action]))
                visited.append(str(nextGameState))


# Abbreviations
dfs = depthFirstSearch
bfs = breadthFirstSearch
