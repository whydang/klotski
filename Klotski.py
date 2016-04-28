# Ying Dang and Derek Rhodehamel
# CSE 415 A, Spring 2016
# Homework 4

# Klotski


#<INITIAL_STATE>
GOAL_BLOCK = 'B'
CREATE_INITIAL_STATE = lambda : ["A", "B", "B", "C",
                                 "A", "B", "B", "C",
                                 "D", "E", "E", "F",
                                 "D", "G", "H", "F",
                                 "I", "_", "_", "J"]
#</INITIAL_STATE>



# class for a piece
# represented by it's id = ALPHA_CHAR
#                      x = top left starting x
#                      y = top left starting y
#                      w = how wide to the right
#                      h = how long to the bottom
# defining can move precond
class Piece:
    # constructor
    def __init__(self, id, x, y, w, h):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # precond defining whether or not this piece can move in a certain
    # direction given a current state
    def can_move(self, state, direction):
        w = self.w
        h = self.h
        x = self.x
        y = self.y
        try:
            move = 1
            if direction > 1:
                move = -move
            if direction%2 == 0:
                for i in range(h):
                    if 0 <= x + move < 4:
                        if state[4*(y+i) + x + move] != ("_" or self.id):
                            return False
                    else:
                        return False
            else:
                for i in range(w):
                    if 0 <= y + move < 5:
                        if state[4*(y+move) + (x+i)] != ("_" or self.id):
                            return False
                    else:
                        return False
            return True

        except (Exception) as e:
            print(e)




def make_library(state):
    library = {}
    for i in range(len(state)):
        if state[i] != "_":
            if state[i] not in library:
                shape = [1,1]
                if state[(i + 1)%len(state)] == state[i]:
                    shape[0] += 1
                if state[(i + 4)%len(state)] == state[i]:
                    shape[1] += 1
                library[state[i]] = Piece(state[i], i%4, i/4, shape[0], shape[1])
    return library


piece_dictionary = make_library(CREATE_INITIAL_STATE())


# returns a message when the goal is reached
def goal_message(s):
    return "Solved the Klotski puzzle, champ!"



# Performs an appropriately deep copy of a state,
# for use by operators in creating new states.
def copy_state(s):
    new_state = list(s)
    return new_state



# determines whether or not the two states are indentical by value
def DEEP_EQUALS(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# string representation of the state of the game as shown:
# A B B C
# A B B C
# D E E F
# D G H F
# I _ _ J
def DESCRIBE_STATE(state):
    result = ""
    for row in range(5):
        result = result + "   "
        for col in range (4):
            result = result + (str(state[4*row + col]) + " ")
        result = result + "\n"
    return result


# hashes the current state given such that all states
# are guaranteed to be unique
def HASHCODE(state):
    return DESCRIBE_STATE(state)



class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


## inprogress
def move(s, tile, dir):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the a tile to an available
     location'''
    new_state = copy_state(s)

    curr_index = tile.y * 4 + tile.x
    for width in range(tile.w):
        for height in range(tile.h):
            tile_index = (curr_index + width + height * 4)
            print(s[tile_index])
            if dir == 3:
                new_state[tile_index + 4] = s[tile_index]
                if height == 0:
                    new_state[tile_index] = "_"
            elif dir == 1:
                new_state[tile_index - 4] = s[tile_index]
                if height == tile.h - 1:
                    new_state[tile_index] = "_"
            elif dir == 0:
                new_state[tile_index + 1] = s[tile_index]
                if width == 0 :
                    new_state[tile_index] = "_"
            else:
                new_state[tile_index - 1] = s[tile_index]
                if width == tile.w - 1:
                    new_state[tile_index] = "_"


    return new_state

temp = ["A", "B", "B", "C",
        "A", "B", "B", "C",
        "D", "E", "E", "F",
        "D", "G", "H", "F",
        "I", "_", "_", "J"]

new_temp = move(temp, Piece("F", 3, 2, 1, 2), 1)
print(DESCRIBE_STATE(temp))
print(DESCRIBE_STATE(new_temp))

# determines whether or not the state is a goal state
# implying that 2x2 square is on the center bottom
def goal_test(state):
    return state[13] == GOAL_BLOCK and state[14] == GOAL_BLOCK and \
           state[17] == GOAL_BLOCK and state[18] == GOAL_BLOCK



# creates a list of all possible combinations of tiles to
# direction = (0, 1, 2, 3) and returns it
def combo_list():
    ls = []
    for tile in list(set(CREATE_INITIAL_STATE()) - set(['_'])):
        for i in range(4):
            ls.append((tile, i))
    return ls


# print(str(combo_list()))


# translate a numerical direction into the corresponding
# compass direction in the following format:
#    1
# 2     0
#    3
# on the condition that only 0 - 3 is passed in
def translate_dir(num):
    dir = ''
    if num == 0:
        dir = 'east'
    elif num == 1:
        dir = 'north'
    elif num == 2:
        dir = 'west'
    else:
        dir = 'south'
    return dir



# returns the can_move function of the given piece in a
# direction relative to the state
def can_move(s, piece, direction):
    piece.can_move(s, direction)


#<OPERATORS>
tile_combinations = combo_list()

OPERATORS = [Operator("Move tile " + str(tile) + str(translate_dir(direction)),
                      lambda s,p=tile,q=direction: can_move(s,piece_dictionary[p], q),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p=tile,q=direction: move(s, piece_dictionary[p], q))
             for (tile, direction) in tile_combinations]
#</OPERATORS>


#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>


#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
