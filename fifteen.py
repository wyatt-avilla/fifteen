#Name: Wyatt Avilla
#Date: 11-26-22
#Functionality: impliments game of fifteen using list indexes as board cells
import numpy as np
import random

class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.win_condition = np.array([i for i in range(1,size**2)] + [0])
        self.adjacent_spaces = {0:[1,4],1:[0,2,5],2:[1,3,6],3:[2,7],4:[0,5,8],5:[1,4,6,9],6:[2,5,7,10],7:[3,6,11],8:[4,9,12],9:[5,8,10,13],10:[6,9,11,14],11:[7,10,15],12:[8,13],13:[9,12,14],14:[10,13,15],15:[11,14]}
        #^ has form {index:adjacent spaces} ^

    def draw(self):
        formatted_tiles = []  #tiles displayed as " x " or "xx " depending on number of digits present
        for x in range(16): 
            if self.tiles[x] == 0:
                formatted_tiles.append("   ")
            else:
                if len(str(self.tiles[x])) == 1:
                    formatted_tiles.append(f" {self.tiles[x]} ")
                else:
                    formatted_tiles.append(f"{self.tiles[x]} ")
        print(" +---+---+---+---+")
        print(f" |{formatted_tiles[0]}|{formatted_tiles[1]}|{formatted_tiles[2]}|{formatted_tiles[3]}|")
        print(" +---+---+---+---+")
        print(f" |{formatted_tiles[4]}|{formatted_tiles[5]}|{formatted_tiles[6]}|{formatted_tiles[7]}|")
        print(" +---+---+---+---+")
        print(f" |{formatted_tiles[8]}|{formatted_tiles[9]}|{formatted_tiles[10]}|{formatted_tiles[11]}|")
        print(" +---+---+---+---+")
        print(f" |{formatted_tiles[12]}|{formatted_tiles[13]}|{formatted_tiles[14]}|{formatted_tiles[15]}|")
        print(" +---+---+---+---+")

    def __str__(self):
        size = 4
        n = 0
        string = ""
        for x in range(size): #" x " or "xx " depending on number of digits present
            for y in range(size):
                if self.tiles[y+n] == 0:
                    string += "   "
                else:
                    if len(str(self.tiles[y+n])) == 1:
                        string += f" {self.tiles[y+n]} "
                    else:
                        string += f"{self.tiles[y+n]} "
            string += "\n"
            n += size 
        return string
    

    # exchange i-tile with j-tile, tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done (not required) using a dot product of the vector of tiles and the matrix of 
    # the corresponding transformation (vector by matrix multiplication)
    # can (not required) return the dot product
    def transpose(self, i, j): #exchanges two tiles (based on tile vales) without checking for move legality
        i_index = np.where(self.tiles == i)[0][0]
        j_index = np.where(self.tiles == j)[0][0]
        self.tiles[i_index], self.tiles[j_index] = self.tiles[j_index], self.tiles[i_index]

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):  
        tile_index = (np.where(self.tiles == move))[0][0]
        for cell in self.adjacent_spaces.get(tile_index):
            if self.tiles[cell] == 0:
                return True
        else: return False

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move):
        if self.is_valid_move(move):  #swaps 0 and chosen tile
            tile_index = (np.where(self.tiles == move))[0][0]
            zero_index = (np.where(self.tiles == 0))[0][0]
            self.tiles[tile_index] = 0
            self.tiles[zero_index] = move
    
    # shuffle tiles
    def shuffle(self, moves = 100): #randomly choose between valid moves x times
        for x in range(moves):
            zero_index = (np.where(self.tiles == 0))[0][0]
            adj = self.adjacent_spaces.get(zero_index)
            choice = random.randint(0, len(adj)-1)
            self.update(self.tiles[adj[choice]])
    
    # verify if the puzzle is solved
    def is_solved(self): #checks if current board state is equal to win condition specified in __init__
        return np.array_equal(self.tiles, self.win_condition)

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle
    def solve(self):  #set board to win condition
        self.tiles = self.win_condition
        

    '''uncomment this to play the game without the gui'''
    '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''