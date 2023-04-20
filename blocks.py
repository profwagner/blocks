#need to finish


board = []
cols = 10
rows = 20

row = ['#']
for i in range(cols):
    row.append(' ')
row.append('#')

for r in range(rows):
    board.append(row.copy())
bot =['#' for c in range(cols+2)]
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
piece = ( ((-1,0),(0,0),(0,-1),(1,0)),((0,0),(0,-1),(0,1),(1,0)) )
# ((spots in 1st roation),(spots in 2nd rotation))
mp_piece = ( ( (0,0),(0,-1),(0,1),(1,1) ), ( (0,0),(-1,0),(1,0),(1,-1) ), ( (0,0),(0,1),(0,-1),(-1,-1) ), ( (0,0),(-1,1),(-1,0),(1,0) ) ) 

shape=piece[0]

#def check_roate (x, y, b, shape):
#    pass
def check_move (x, y, b, shape):
    #can the piece be moved to have its center at x, y?
    for spot in shape:
        nx = x + spot[0]
        ny = y + spot[1]
        if b[ny][nx] == '#': #spot is filled
            return False
    return True

def rotate(x, y, b, piece, rot):
    nrot = rot + 1
    nrot %= len(piece) #if we have reached end of list go back to first rotation
    shape = piece[nrot]
    #need to see if it fits
    if check_move (x, y, b, shape):
        print ('can rotate')
        rot = nrot
    else:
        print ("can't rotate")
    return rot
        
    
    #need to return new roation
for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            board[ny][nx]='%' #draw 1st piece
board[y][x] = '*' #mark center location
display_board(board)

    
def move_right(x, y, b, shape):
    cx = x + 1 #find new position
    cy = y
    if check_move(cx,cy, b, shape): #If space to right empty move right
        for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            b[ny][nx]=' ' #erase piece from old location
        x += 1 #actally update new position
        for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            b[ny][nx]='%' #draw piece in new location
        b[y][x] = '*' #mark center location
        
    return x #return new x value
