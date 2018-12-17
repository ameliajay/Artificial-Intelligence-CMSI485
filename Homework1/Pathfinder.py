'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to all
of the goals with optimal cost.

This task is done in the solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
import heapq

def heuristic_cost(state, goals):
    options = []
    for i in range(len(goals)):
        options.append(abs(state[0] - goals[i][0]) + abs(state[1] - goals[i][1]))
    return min(options)

def make_soln(node):
    solution = []
    while node.parent is not None:
        solution.append(node.action)
        node = node.parent
    solution.reverse()
    return solution

def solve (problem, initial, goals):
    goals2 = []
    for (col, row) in goals:
        goals2.append((col, row))

    visited = set()

    frontier = []
    heapq.heappush(frontier, SearchTreeNode(initial, None, None, 0, heuristic_cost(initial, goals2)))

    while len(frontier) > 0:
        current_node = heapq.heappop(frontier)

        if current_node.state in goals and current_node.state not in goals2:
            continue

        if current_node.state in goals2:
            goals2.remove(current_node.state)
            if len(goals2) is 0:
                return make_soln(current_node)
            for i in range(len(frontier)):
                heapq.heappop(frontier)
            heapq.heappush(frontier, current_node)

        visited.add((current_node.state, current_node.action))

        for child in problem.transitions(current_node.state):
            if (child[2], child[0]) in visited:
                continue
            heapq.heappush(frontier, SearchTreeNode(child[2], child[0], current_node, child[1] + current_node.totalCost, heuristic_cost(child[2], goals2)))

    return None


class PathfinderTests(unittest.TestCase):

    def test_maze1(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals   = [(5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 8)

    def test_maze2(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.M.X",
                "X.X.X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (1, 3)
        goals   = [(3, 3), (5, 3)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze3(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.MMX",
                "X...M.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals   = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 12)

    def test_maze4(self):
        maze = ["XXXXXXX",
                "X.....X",
                "X.M.XXX",
                "X...X.X",
                "XXXXXXX"]
        problem = MazeProblem(maze)
        initial = (5, 1)
        goals   = [(5, 3), (1, 3), (1, 1)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)

    def test_maze5(self):
                #0123456789
        maze = ["XXXXXXXXXX", #0
                "X........X", #1
                "X..MMMMXXX", #2
                "X..M..M..X", #3
                "XXXM..M..X", #4
                "X..M..M..X", #5
                "XXXXXXXXXX"] #6
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals   = [(8, 1), (1, 3), (8, 3), (8, 5), (1, 5)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 34)

    def test_maze6(self):
                #0123456789
        maze = ["XXXXXXXXXX", #0
                "X........X", #1
                "X..MMMMXXX", #2
                "X..M..M..X", #3
                "XXXM..M..X", #4
                "X..X..M..X", #5
                "XXXXXXXXXX"] #6
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals   = [(8, 1), (1, 3), (8, 3), (8, 5), (1, 5)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)

    def test_maze7(self):
                #          11111111112
                #012345678901234567890
        maze = ["XXXXXXXXXXXXXXXXXXXXX", #0
                "X..X....M....X..M.X.X", #1
                "X...X..M.M..M..MM..MX", #2
                "XMM..XMMMMM..X....X.X", #3
                "X..M..X.........M...X", #4
                "XX.......XX.XXMXXMM.X", #5
                "X.XXX.MM....X...X...X", #6
                "X...X.MM....M.XX..XXX", #7
                "XXM.X..MMMMMX..M..X.X", #8
                "X.X.........X..M....X", #9
                "XXXXXXXXXXXXXXXXXXXXX"] #10
        problem = MazeProblem(maze)
        initial = (10, 4)
        goals   = [(1, 1), (19, 1), (19, 8), (1, 9)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)

    def test_maze8(self):
                #          11111111112
                #012345678901234567890
        maze = ["XXXXXXXXXXXXXXXXXXXXX", #0
                "X..X....M....X..M.X.X", #1
                "X...X..M.M..M..MM..MX", #2
                "XMM..XMMMMM..X....X.X", #3
                "X..M..X.........M...X", #4
                "XX.......XX.XXMXXMM.X", #5
                "X.XXX.MM....X...X...X", #6
                "X...X.MM....M.XX..XXX", #7
                "XXM.X..MMMMMX..M..X.X", #8
                "X.X.........X..M....X", #9
                "XXXXXXXXXXXXXXXXXXXXX"] #10
        problem = MazeProblem(maze)
        initial = (10, 4)
        goals   = [(1, 1), (19, 1), (19, 8), (1, 6)]
        soln = solve(problem, initial, goals)
        print(soln)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 79)

    def test_maze9(self):
                #          11111111112
                #012345678901234567890
        maze = ["XXXXXXXXXXXXXXXXXXXXX", #0
                "X..X....M....X..M.X.X", #1
                "X...X..M.M..M..MM..MX", #2
                "XMM..XMMMMM..X....X.X", #3
                "X..M..X.........M...X", #4
                "XX.......XX.XXMXXMM.X", #5
                "X.XXX.MM....X...X...X", #6
                "X...X.MM....M.XX..XXX", #7
                "XXM.X..MMMMMX..M..X.X", #8
                "X.X.........X..M....X", #9
                "XXXXXXXXXXXXXXXXXXXXX"] #10
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals   = [(8, 2), (1, 4), (4, 1), (12, 2), (18, 2), (1, 6), (6, 8), (8, 7), (13, 6), (1, 9)]
        soln = solve(problem, initial, goals)
        self.assertTrue(soln is None)

    def test_maze10(self):
                #          11111111112
                #012345678901234567890
        maze = ["XXXXXXXXXXXXXXXXXXXXX", #0
                "X..X....M....X..M.X.X", #1
                "X...X..M.M..M..MM..MX", #2
                "XMM..XMMMMM..X....X.X", #3
                "X..M..X.........M...X", #4
                "XX.......XX.XXMXXMM.X", #5
                "X.XXX.MM....X...X...X", #6
                "X...X.MM....M.XX..XXX", #7
                "XXM.X..MMMMMX..M..X.X", #8
                "X.X.........X..M....X", #9
                "XXXXXXXXXXXXXXXXXXXXX"] #10
        problem = MazeProblem(maze)
        initial = (1, 1)
        goals   = [(8, 2), (1, 4), (4, 1), (12, 2), (18, 2), (1, 6), (6, 8), (8, 7), (13, 6), (19, 8)]
        soln = solve(problem, initial, goals)
        (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
        self.assertTrue(is_soln)
        self.assertEqual(soln_cost, 93)
#     def test_maze1(self):
#         maze = ["XXXXXXX",
#                 "X.....X",
#                 "X.M.M.X",
#                 "X.X.X.X",
#                 "XXXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (1, 3)
#         goals   = [(5, 3)]
#         soln = solve(problem, initial, goals)
#         (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
#         self.assertTrue(is_soln)
#         self.assertEqual(soln_cost, 8)
# # #
#     def test_maze2(self):
#         maze = ["XXXXXXX",
#                 "X.....X",
#                 "X.M.M.X",
#                 "X.X.X.X",
#                 "XXXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (1, 3)
#         goals   = [(3, 3), (5,3)]
#         soln = solve(problem, initial, goals)
#         (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
#         self.assertTrue(is_soln)
#         self.assertEqual(soln_cost, 12)
# # #
#     def test_maze3(self):
#         maze = ["XXXXXXX",
#                 "X.....X",
#                 "X.M.MMX",
#                 "X...M.X",
#                 "XXXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (5, 1)
#         goals   = [(5, 3), (1, 3), (1, 1)]
#         soln = solve(problem, initial, goals)
#         (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
#         self.assertTrue(is_soln)
#         self.assertEqual(soln_cost, 12)
# # #
#     def test_maze4(self):
#         maze = ["XXXXXXX",
#                 "X.....X",
#                 "X.M.XXX",
#                 "X...X.X",
#                 "XXXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (5, 1)
#         goals   = [(5, 3), (1, 3), (1, 1)]
#         soln = solve(problem, initial, goals)
#         self.assertTrue(soln == None)
# # #
#     def test_maze5(self):
#         maze = ["XXXXXXXXXXXX",
#                 "XX....X..M.X",
#                 "X...MMM.M..X",
#                 "X..........X",
#                 "X.MMMMMMMM.X",
#                 "XXX..M....XX",
#                 "XXXXXXXXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (3, 5)
#         goals = [(9, 5), (6, 3), (3, 1)]
#         soln = solve(problem, initial, goals)
#         (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
#         self.assertTrue(is_soln)
#         self.assertEqual(soln_cost, 18)
# #
#     def test_maze6(self):
#         maze = ["XXXXXX",
#                 "X....X",
#                 "XXXXXX",
#                 "X....X",
#                 "XXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (3, 3)
#         goals = [(2, 1), (4, 1)]
#         soln = solve(problem, initial, goals)
#         self.assertTrue(soln == None)
# #
#     def test_maze7(self):
#         maze = ["XXXXX",
#                 "X...X",
#                 "XXX.X",
#                 "X.XXX",
#                 "XXXXX"]
#         problem = MazeProblem(maze)
#         initial = (1, 3)
#         goals = [(1, 1)]
#         soln = solve(problem, initial, goals)
#         self.assertTrue(soln == None)
# #
#     def test_maze8(self):
#         maze = ["XXXXXX",
#                 "X....X",
#                 "X.MM.X",
#                 "X....X",
#                 "XXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (1, 2)
#         goals = [(4, 2)]
#         soln = solve(problem, initial, goals)
#         (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
#         self.assertTrue(is_soln)
#         self.assertEqual(soln_cost, 5)
# #
#     def test_maze9(self):
#         maze = ["XXXXXXX",
#                 "X.....X",
#                 "XX.XXXX",
#                 "X.....X",
#                 "XXXXXXX"]
#         problem = MazeProblem(maze)
#         initial = (5, 3)
#         goals = [(1, 1), (2, 1), (3, 1), (5, 1)]
#         soln = solve(problem, initial, goals)
#         self.assertTrue(soln == None)
# #
#     def test_maze10(self):
#         maze = ["XXXXX",
#                 "X...X",
#                 "X...X",
#                 "X...X",
#                 "XXXXX"]
#         problem = MazeProblem(maze)
#         initial = (2, 3)
#         goals = [(1, 1), (2, 1), (3, 1)]
#         soln = solve(problem, initial, goals)
#         (soln_cost, is_soln) = problem.soln_test(soln, initial, goals)
#         self.assertTrue(is_soln)
#         self.assertEqual(soln_cost, 7)



#
if __name__ == '__main__':
    unittest.main()
