import argparse

from algorithms.search import *
from solver.solver import Solver
from viewer.viewer import SolutionViewer

parser = argparse.ArgumentParser(description='Solves Unblockme puzzles.')

parser.add_argument('puzzlename', metavar='filename',
					help='the puzzle filename to solve.')

parser.add_argument('--BFS', dest='search_method', action='store_const',
                    const=bfs,
                    help='Uses BFS search to solve the puzzle')

parser.add_argument('--DFS', dest='search_method', action='store_const',
                    const=dfs,
                    help='Uses DFS search to solve the puzzle')

parser.add_argument('--auto-play', dest='run_mode', action='store_const',
                    const=True,
                    help='It plays the solution automatically.')

parser.add_argument('--step-by-step', dest='run_mode', action='store_const',
                    const=False,
                    help='It allows to show the solution step-by-step')

args = parser.parse_args()

solver= Solver(args.puzzlename, args.search_method)
solution= solver.solve()

SolutionViewer(solver.problem.startState, solution, args.run_mode)