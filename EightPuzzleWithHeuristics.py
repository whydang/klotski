# Ying Dang
# CSE 415 A, Spring 2016
# Homework 3: Part II

#4. EightPuzzleWithHeuristics CMPLETE

#<METADATA>
QUIET_VERSION = "0.1"
PROBLEM_NAME = "Basic Eight Puzzle"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Y. Dang']
PROBLEM_CREATION_DATE = "19-APR-2016"
PROBLEM_DESC=\
'''This formulation of the Basic Eight Puzzle problem uses generic
Python 3 constructs and has been tested with Python 3.4.
It is designed to work according to the QUIET tools interface.
'''
#</METADATA>


GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def DEEP_EQUALS(s1,s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def DESCRIBE_STATE(state):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    txt = "\n"
    for index in range(len(state)):
        txt += str(state[index]) + " "
        if index % 3 == 2:
            txt += "\n"
    return txt

def HASHCODE(s):
    '''The result should be an immutable object such as a string
    that is unique for the state s.'''
    return DESCRIBE_STATE(s)


def copy_state(s):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = list(s)
    return news



def can_move(s,From,To):
    '''Tests whether it's legal to move a tile in state s
     from the From index to the To index.'''

    try:
        from_tile = s[From] # tile goes from index
        to_tile =s[To]   # tile goes to index

        if from_tile != 0 and to_tile == 0:
            return True
        return False
    except (Exception) as e:
        print(str(e))



class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)



def move(s, From, To):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the topmost disk
     from the From tile to the To tile.'''
    news = copy_state(s) # start with a deep copy.
    from_tile = s[From] # tile goes from.
    to_tile = s[To] # tile goes to
    news[From] = to_tile
    news[To] = from_tile
    return news # return new state



def goal_test(s):
    '''If the the tiles are in reverse order from left to right and top to bottom,
    it is in its goal state'''
    return DEEP_EQUALS(s, GOAL_STATE)


def goal_message(s):
    return "Reversed the Basic 8 Puzzle!"


#<INITIAL_STATE>
INITIAL_STATE = [1, 4, 2, 3, 7, 0, 6, 8, 5]

CREATE_INITIAL_STATE = lambda: INITIAL_STATE
DUMMY_STATE =  []
#</INITIAL_STATE>



#<OPERATORS>
tile_combinations = [(a, b) for (a, b) in
                    [(0, 1), (0, 3),
                     (1, 0), (1, 2), (1, 4),
                     (2, 1), (2, 5),
                     (3, 0), (3, 4), (3, 6),
                     (4, 1), (4, 3), (4, 5), (4, 7),
                     (5, 2), (5, 4), (5, 8),
                     (6, 3), (6, 7),
                     (7, 4), (7, 6), (7, 8),
                     (8, 5), (8, 7)]]

OPERATORS = [Operator("Move tile from "+ str(p)+" to "+ str(q),
                      lambda s,p=p,q=q: can_move(s,p,q),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p=p,q=q: move(s,p,q))
             for (p,q) in tile_combinations]
#</OPERATORS>


#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

# computes the hypotenuse between the current tile and where it should be
# for all tiles, and returns that total hypotenuse value
def h_euclidean(s):
    total = 0

    for index in range(len(s)):
        curr = s[index]
        curr_row = int(index / 3)
        curr_col = index % 3

        expect_row = int(curr / 3)
        expect_col = curr % 3

        diff_row = abs(curr_row - expect_row)
        diff_col = abs(curr_col - expect_col)

        total = total + ((diff_col ** 2) + (diff_row ** 2)) ** (0.5)
    return total

# computes the total number of misplacement of tiles and returns it
def h_hamming(s):
    total = 0
    for index in range(len(s)):
        if s[index] != GOAL_STATE[index]:
            total = total + 1
    return total

# computes the total number of x + y offset from goal in each tile for all tiles
# and returns that value
def h_manhattan(s):
    total = 0

    for index in range(len(s)):
        curr = s[index]
        curr_row = int(index / 3)
        curr_col = index % 3

        expect_row = int(curr / 3)
        expect_col = curr % 3

        diff_row = abs(curr_row - expect_row)
        diff_col = abs(curr_col - expect_col)

        total = total + diff_row + diff_col
    return total

# computes the total number of x + y + distance from zero tile placement
# of all tilse and returns that value
def h_custom(s):
    index_zero = s.index(0)
    total = 0
    for index in range(len(s)):
        curr = s[index]
        curr_row = int(index / 3)
        curr_col = index % 3

        expect_row = int(curr / 3)
        expect_col = curr % 3

        zero_row = int(index_zero / 3)
        zero_col = index_zero % 3

        diff_row = abs(curr_row - expect_row)
        diff_col = abs(curr_col - expect_col)
        diff_zero_row = abs(zero_row - curr_row)
        diff_zero_col = abs(zero_col - curr_col)

        total = total + diff_zero_row + diff_zero_col + diff_row + diff_col
    return total



#<HEURISTICS>
HEURISTICS = {'h_euclidean': h_euclidean, 'h_hamming':h_hamming,
    'h_manhattan':h_manhattan, 'h_custom':h_custom}
#</HEURISTICS>

  