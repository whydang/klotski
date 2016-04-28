# Shapes:
# A B B C
# A B B C
# D E E F
# D G H F
# I _ _ J

state = ["A", "B", "B", "C", "A", "B", "B", "C", "D", "E", "E", "F", "D", "G", "H", "F", "I", "_", "_", "J"]

# Shapes:
# A B B C
# A B B C
# D E E F
# D G H F
# I _ _ J
def toString(state):
    result = ""
    for row in range(5):
        result += "   "
        for col in range(4):
            result += (state[4*row + col] + " ")
        result += "\n"
    return result

# class for a piece
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
            if direction == 1 or 2:
                move = -move
            if direction%2 == 0:
                for i in range(h):
                    for j in range(w):
                        if 0 <= (x+j) + move < 4:
                            if state[4*(y+i) + (x+j) + move] != ("_" or self.id):
                                return False
                        else:
                            return False
            else:
                for i in range(h):
                    for j in range(w):
                        if 0 <= (y+i) + move < 5:
                            if state[4*(y+i+move) + (x+j)] != ("_" or self.id):
                                return False
                        else:
                            return False
            return True

        except (Exception) as e:
            print(e)

    def move(self, state, direction):
        x = self.x
        y = self.y
        nu_state = copy_state(state)
        index = state.index(self.id)
        move = 1
        if direction == 1 or 2:
            move = -move
        if direction%2 == 0:
            for i in range(self.w + 1):
                for j in range(self.h):
                    pos = 4*(y + j) + x + i + (-1 + move)/2
                    nu_state[pos] = index
                    if i == 0 and move > 0:
                        nu_state[pos] = "_"
                    if i == self.w - 1 and move < 0:
                        nu_state[pos + self.w] = "_"
        else :
            for i in range(self.w):
                for j in range(self.h + 1):
                    pos = 4 * (y + j + (-1 + move)/2) + x + i
                    nu_state[pos] = index
                    if j == 0 and move > 0:
                        nu_state[pos] = "_"
                    if j == self.h - 1 and move < 0:
                        nu_state[pos + self.w] = "_"




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
                    
