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

## Homework 2a
The aim of this project was to implement a basic propositional logic inference engine for use in a maze pitfall problem. (Example of a maze pitfall problem: an agent is in a maze with an initial state and a goal state and must make their way to the goal state without falling into any pits on the way. The states surrounding the pits would be "warning states" which would give us more information for our inference engine about the location of the pits.) The logic inference engine had these restrictions: the maze knowledge base must be in Conjuctive Normal Form (a conjuction of clauses made up of a disjunction of propositions), all queries for the knowledge base must be made in the form of clauses, and inference must be implemented using resolution.

#### maze_clause.py
Class MazeClause

Methods:
- MazeClause constructor parameterized by a list of maze propositions (a proposition is in the form of a tuple in the form ((symbol, location), True or False value)): it checks if the clause is valid (valid means that the clause is logically equivalent to true) and adds a dictionary of propositions and their truth values
- get_prop parameterized by a proposition: returns the truth value of that proposition
- is_valid: returns whether or not a MazeClause is valid
- is_empty: returns whether or not a MazeClause has any propositions in it
- eq (equals) parameterized by another MazeClause: returns true if the two clauses have the same propositions (order does not matter) and are both valid
- hash: hases an immutable set of the stored propositions for ease of lookup in a set
- resolve (static method) parameterized by two clauses: returns a set containing the resulting clause after implementing resolution on the two clauses given; uses the not_resolved method parameterized by a proposition and the combined list of propositions from both clauses which returns the set of propositions that still need to be resolved

#### maze_knowledge_base.py
Class MazeKnowledgeBase

Methods:
- MazeKnowledgeBase constructor giving the knowledge base (KB) a set of clauses
- tell parameterized by a MazeClause: adds that clause to the KB
- ask parameterized by a query in the form of a MazeClause: returns true if the KB entails the query, false otherwise (used the definition of entailment to write this method)

## Homework 3
The aim of this project was to create a decision-network-based Ad Agent that maximizes the sales of a certain product (in this case a "Defendotron", a made-up security system that comes in two different models) based on any user's collected demographic data. For this project, the Ad Agent had to choose one of two music choices for the ad and one of two visual choices for the ad. Given 100,000 data points of demographic data (in hw3_data.csv) I created a Bayesian Network structure and then passed in that structure as a parameter to the pomegranate library's BayesianNetwork.from_structure method to create my Bayesian Network model. Using this model, I used enumeration inference to decide which ads to show the user in order to maximize the sales of the product.

#### ad_engine.py
Class AdEngine

Methods:
- AdEngine constructor parameterized by a data file (in this case hw3_data.csv), the structure for the BN, the decision varibles (Ad1 and Ad2), and a utility map (maps the amount of money gained from the sale of each model of the "Defendotron"): state_names are the names of the different metrics that data was collected on, and the constructor creates the model of the BN based on the structure and the state_names
- decide parameterized by evidence (given in the form of a dictionary like {"T": 1}): returns the best combo of musical and visual ads to show to maximize sales in the form of a dictionary (like {"Ad1": 0, "Ad2": 1})
