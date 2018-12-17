# Artificial-Intelligence-CMSI485
*Loyola Marymount University Intro to Artificial Intelligence (CMSI-485) class projects from Fall 2018*

## Classwork 1
The aim of this project was to implement a breadth-first search tree on a maze pathfinding problem. Given a maze structure with an initial state and a list of goal states, the Pathfinder.solve method should return a path (a list of directions like ["U", "L", "L", "D"]) to the optimal goal state in the maze. 

#### MazeProblem.py
Class MazeProblem

Methods:
- MazeProblem constructor parameterized by a list of strings representing a maze with initial state and goal states (a state is a tuple in the form (column, row))
- goalTest parameterized by state: returns whether or not that state is a goal state
- trasitions parameterized by state: returns all the legal transitions from that state in a list of tuples containing the action taken and the state resulting in that action
- solnTest parameterized by a path: returns whether or not this path is a solution to the MazeProblem (this method was given by the professor)

#### SearchTreeNode.py
Class SearchTreeNode

Methods:
- SearchTreeNode constructor parameterized by the state of the node being created, the action taken to get there, and its parent node

#### Pathfinder.py
Class Pathfinder

Methods:
- solve parameterized by a MazeProblem: returns a path (list of directions) that is a solution to the given MazeProblem

## Homework 1
The aim of this project was to find a solution to a maze pathfinding problem (similar to the one from Classwork 1) that takes the agent from the initial state to all of the accessible goal states with optimal cost. My code performed well all of my own test cases and on all but two of the test cases it was graded on. It could be improved by using dynamic programming.

#### MazeProblem.py
Class MazeProblem (with a costMap that details the cost of being in a state with the given maze componenets; cost is 1 for components not listed in the costMap)

Methods:
- MazeProblem constructor parameterized by a list of strings representing a maze
- transitions parameterized by state: returns all legal transitions from that state in a list of tuples
- cost parameterized by state: returns cost of a state given the costMap
- solnTest parameterized by a path: returns whether or not a path is the optimal cost solution to the MazeProblem

#### SearchTreeNode.py
Class SearchTreeNode

Methods:
- SearchTreeNode constructor parameterized by the state of the node being created, action taken to get to that state, parent node, total cost of the path of actions that led to the state, heuristic estimate of the cost from this node to the nearest goal state that still needs to be visited
- lt (less than) method parameterized by another node: returns whether or not the node is "less than" the other node in terms of total cost plus heuristic cost

#### Pathfinder.py
Class Pathfinder

Methods:
- heuristicCost parameterized by state and list of goals still needing to be visited: returns the heuristic cost (measured by Mahattan Distance) from state to the nearest goal
- make_soln parameterized by a SearchTreeNode: returns the path that was used to get to that node
- solve parameterized by a MazeProblem, an initial state, and a list of goal states: uses a min heap to decide which nodes to visit next in order to find the optimal cost path solution and returns that solution in a list of directions
