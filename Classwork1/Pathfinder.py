'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
import queue

class Pathfinder:
    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def solve(problem):
        solution = []
        frontier = queue.Queue()
        # SearchTreeNode parameterized by a state, action, and parent node
        frontier.put(SearchTreeNode(problem.initial, None, None))
        while not frontier.empty():
            current_node = frontier.get()
            if problem.goalTest(current_node.state):
                while current_node.parent is not None:
                    solution.append(current_node.action)
                    current_node = current_node.parent
                solution.reverse()
                return solution
            # each potential child given in the form of a transition with action
            # taken to get there and state you end up in when that action taken
            for child in problem.transitions(current_node.state):
                frontier.put(SearchTreeNode(child[1], child[0], current_node))

        return []


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)
    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)
    def test_maze3(self):
        maze = ["XXXXXXX",\
                "XXX...X",\
                "XXX...X",\
                "X..*..X",\
                "XXX...X",\
                "X....GX",\
                "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)
    def test_maze4(self):
        maze = ["XXXX", "X*.X", "X.GX", "XXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 2)
    def test_maze5(self):
        maze = ["XXXXXX",\
                "X....X",\
                "XG.X.X",\
                "XXXX.X",\
                "X.*..X",\
                "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 9)

if __name__ == '__main__':
    unittest.main()
