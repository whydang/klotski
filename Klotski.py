# Ying Dang and Derek Rhodehamel
# CSE 415 A, Spring 2016
# Homework 4: Part I

#2. BFS COMPLETE

# returns a message when goal is reached
def goal_message(s):
    return "Solved the Klotski puzzle, champ!"


# determines whether or not the two states are indentical by value
def DEEP_EQUALS(s1,s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


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
     the new state resulting from moving the a tile to an available
     location'''
    new_state = copy_state(s)
    # in progress
    return new_state


# determines whether or not the state is a goal state
# implying that 2x2 square is on the center bottom
def goal_test(state):
    return state[13] == '_' and state[14] == '_' and \
           state[17] == '_' and state[18] == '_'



# Performs an appropriately deep copy of a state,
# for use by operators in creating new states.
def copy_state(s):
    new_state = list(s)
    return new_state



#<OPERATORS>
tile_combinations = [(a, b) for (a, b) in
                    [
                    # needs to an array with piece to 0, 1, 2, 3 direction
                    ]]

OPERATORS = [Operator("Move tile from "+ str(p)+" to "+ str(q),
                      lambda s,p=p,q=q: can_move(s,p,q),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p=p,q=q: move(s,p,q))
             for (p,q) in tile_combinations]
#</OPERATORS>

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
