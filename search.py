"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from util import Stack, Queue
import util
import sys
from time import sleep

from game import Directions

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def depthFirstSearch(problem):
    # TODO 05
    qu = Stack()
    qu.push(((problem.getStartState()), []))

    # store the visited state
    traveled = []

    while qu.isEmpty() is False:
        (stat, path) = qu.pop()
        if(problem.isGoalState(stat)):
            break
        s = problem.getSuccessors(stat)
        for k in s:
            if k[0] not in traveled:
                qu.push((k[0], path + [k[1]]))
                traveled.append(k[0])

    return path


def breadthFirstSearch(problem):
    # TODO 06
    qu = Queue()
    qu.push(((problem.getStartState()), []))
    traveled = []
    while qu.isEmpty() is False:
        (stat, path) = qu.pop()
        if(problem.isGoalState(stat)):
            break
        s = problem.getSuccessors(stat)
        for k in s:
            if k[0] not in traveled:
                qu.push((k[0], path + [k[1]]))
                traveled.append(k[0])
    return path


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    PQ = util.PriorityQueue()
    PQ.push((problem.getStartState(), [], 0), 0)
    expanded = []

    while not PQ.isEmpty():
        node, actions, curCost = PQ.pop()

        if(not node in expanded):
            expanded.append(node)

            if problem.isGoalState(node):
                return actions

            for child, direction, cost in problem.getSuccessors(node):
                PQ.push(
                    (child, actions+[direction], curCost + cost), curCost + cost)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# TODO 08 + 09
'''
students propose at least two heuristic functions for A*
'''


def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 10
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0),
                heuristic(problem.getStartState(), problem))
    expanded = []

    while not fringe.isEmpty():
        node, actions, curCost = fringe.pop()

        if(not node in expanded):
            expanded.append(node)

            if problem.isGoalState(node):
                return actions

            for child, direction, cost in problem.getSuccessors(node):
                g = curCost + cost
                fringe.push(
                    (child, actions+[direction], curCost + cost), g + heuristic(child, problem))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
