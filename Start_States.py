# Shapes:
# A B B C
# A B B C
# D E E F
# D G H F
# I _ _ J

CREATE_INITIAL_STATE = lambda : ["A", "B", "B", "C", "A", "B", "B", "C", "D", "E", "E", "F", "D", "G", "H", "F", "I", "_", "_", "J"]

def toString(state):
    result = ""
    for row in range(5):
        result += "   "
        for col in range (4):
            result += (state[4*row + col] + " ")
        result+="\n"
    return result

save = toString(CREATE_INITIAL_STATE())
print(save)
