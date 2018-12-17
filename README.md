# Artificial-Intelligence-CMSI485
*Loyola Marymount University Intro to Artificial Intelligence (CMSI-485) class projects from Fall 2018*

## Classwork 1
The aim of this project was to implement a breadth-first search tree on a maze pathfinding problem. Given a maze structure with an initial state and a list of goal states, the Pathfinder.solve method should return a path (a list of directions like ["U", "L", "L", "D"]) to the optimal goal state in the maze. 

### MazeProblem.py
Class MazeProblem

Methods:
- MazeProblem constructor parameterized by a list of strings representing a maze with initial state and goal states (a state is a tuple in the form (column, row))
- goalTest parameterized by state: returns whether or not that state is a goal state
- trasitions parameterized by state: returns all the legal transitions from that state in a list of tuples containing the action taken and the state resulting in that action
- solnTest parameterized by a path: returns whether or not this path is a solution to the MazeProblem (this method was given by the professor)

### SearchTreeNode.py
Class SearchTreeNode

Methods:
- SearchTreeNode constructor parameterized by the state of the node being created, the action taken to get there, and its parent node

### Pathfinder.py
Class Pathfinder

Methods:
- solve parameterized by a MazeProblem: returns a path (list of directions) that is a solution to the given MazeProblem
