# Ying Dang and Derek Rhodehamel
# CSE 415 A, Spring 2016
# Homework 4: Part I

#2. BFS COMPLETE

# determines whether or not the state is a goal state
def goal_state(state):
    return state[13] == '_' and state[14] == '_' and \
           state[17] == '_' and state[18] == '_'


# determines whether or not the two states are indentical by value
def DEEP_EQUALS(s1,s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# Performs an appropriately deep copy of a state,
# for use by operators in creating new states.
def copy_state(s):
    new_state = list(s)
    return new_state


