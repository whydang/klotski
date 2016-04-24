# Ying Dang
# CSE 415 A, Spring 2016
# Homework 3: Part II

#2. BFS COMPLETE

import sys

if sys.argv==[''] or len(sys.argv) < 2:
  import BasicEightPuzzle as Problem
else:
  import importlib
  Problem = importlib.import_module(sys.argv[1])


print("\nWelcome to ItrBFS")
COUNT = None
BACKLINKS = {}



def runBFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(Problem.DESCRIBE_STATE(initial_state))
  global COUNT, BACKLINKS
  COUNT = 0
  BACKLINKS = {}
  IterativeBFS(initial_state) # issue here
  print(str(COUNT)+" states examined.")


# iterates BFS on given puzzle state until a goal is reached
def IterativeBFS(initial_state):
  global COUNT, BACKLINKS

  OPEN = [initial_state]
  CLOSED = []
  BACKLINKS[Problem.HASHCODE(initial_state)] = -1

  while OPEN != []:
    S = OPEN[0]
    del OPEN[0]
    CLOSED.append(S)

    # prints start of solution given pegs 1 & 2 are empty
    if Problem.GOAL_TEST(S):
      print(Problem.GOAL_MESSAGE_FUNCTION(S))
      backtrace(S)
      return

    COUNT += 1
    if (COUNT % 32)==0:
       print(".", end="")
       if (COUNT % 128)==0:
         print("COUNT = "+str(COUNT))
         print("len(OPEN)="+str(len(OPEN)))
         print("len(CLOSED)="+str(len(CLOSED)))

    L = []
    for op in Problem.OPERATORS:
      if op.precond(S):
        new_state = op.state_transf(S)
        if not occurs_in(new_state, CLOSED) and OPEN.count(new_state) == 0:
          L.append(new_state)
          BACKLINKS[Problem.HASHCODE(new_state)] = S


    for s2 in L:
      for i in range(len(OPEN)):
        if Problem.DEEP_EQUALS(s2, OPEN[i]):
          del OPEN[i]; break

    OPEN = OPEN + L


# backtrace the goal and prints it out
def backtrace(S):
  global BACKLINKS

  path = []
  while not S == -1:
    path.append(S)
    S = BACKLINKS[Problem.HASHCODE(S)]
  path.reverse()
  print("Solution path: ")
  for s in path:
    print(Problem.DESCRIBE_STATE(s))
  return path    
  

# determines if the state is deep equal to any state in the list
def occurs_in(s1, lst):
  for s2 in lst:
    if Problem.DEEP_EQUALS(s1, s2): return True
  return False

if __name__=='__main__':
  runBFS()
