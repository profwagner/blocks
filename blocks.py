#8 wide 10 tall
row = ['#',' ',' ',' ',' ',' ',' ','#']
bot = ['#','#','#','#','#','#','#','#']

board = []
for r in range(9):
    board.append(row.copy())
board.append(bot)

def display_board(b):
    for r in b:
        s = ''
        for c in r:
            s += c
        print (s)
        
x = 3
y = 4
rotation = 0
piece = (((-1,0),(0,0),(0,-1),(1,0)),((0,0),(0,-1),(0,1),(1,0)))

shape=piece[0]
def rotate(x, y, b, piece, rot):
    pass
    rot += 1
    rot %= len(piece)
    #need to see if it fits
    #need to return new roation
for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            board[ny][nx]='%' #draw 1st piece
board[y][x] = '*' #mark center location
display_board(board)

def check_move (x, y, b, shape):
    #can the piece be moved to have its center at x, y?
    for spot in shape:
        nx = x + spot[0]
        ny = y + spot[1]
        if b[ny][nx] == '#': #spot is filled
            return False
    return True
    
def move_right(x, y, b, shape):
    cx = x + 1
    cy = y
    if check_move(cx,cy, b, shape): #If space to right empty move right
        for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            b[ny][nx]=' ' #erase piece from old location
        x += 1
        for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            b[ny][nx]='%' #draw piece in new location
        b[y][x] = '*' #mark center location
        
    return x



        