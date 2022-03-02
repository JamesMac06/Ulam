#contant starting number //DO NOT CHANGE//
NUMBER = 1
#//CONTROLES SIZE OF BOARD//
scale = 60
#variables based on "scale"
Spiralsize = (scale * 2) + 1
center = scale
#empty array
GRID = []
#used in the output of the visualization
prime = "\u2588\u2588"
not_prime = '  '


#function that finds if a given number (NUMBER) is prime
def find_prime(NUMBER):
    isPrime = True
    if NUMBER <= 1:
        isPrime = False
    for i in range(2, int(round(NUMBER / 2)) + 1):
        if NUMBER % i == 0:
            isPrime = False
    return isPrime


#creates a blank 2d array within the parameters assigned earlier
def make_grid():
    for i in range(Spiralsize):
        GRID.append([])
        for j in range(Spiralsize):
            GRID[i].append('')


#assignes the numbers to the 2d array in spiral pattern
def spiral(x):
    y = x
    NUMBER = 1
    rep = 1
    GRID[y][x] = NUMBER
    cont = True
    while cont == True:
        for i in range(rep):
            NUMBER += 1
            x += 1
            if 0 <= y <= Spiralsize - 1:
                if 0 <= x <= Spiralsize - 1:
                    GRID[y][x] = NUMBER
                else:
                    cont = False
            else:
                cont = False
        for i in range(rep):
            NUMBER += 1
            y -= 1
            if 0 <= y <= Spiralsize - 1:
                if 0 <= x <= Spiralsize - 1:
                    GRID[y][x] = NUMBER
                else:
                    cont = False
            else:
                cont = False
        rep += 1
        for i in range(rep):
            NUMBER += 1
            x -= 1
            if 0 <= y <= Spiralsize - 1:
                if 0 <= x <= Spiralsize - 1:
                    GRID[y][x] = NUMBER
                else:
                    cont = False
            else:
                cont = False
        for i in range(rep):
            NUMBER += 1
            y += 1
            if 0 <= y <= Spiralsize - 1:
                if 0 <= x <= Spiralsize - 1:
                    GRID[y][x] = NUMBER
                else:
                    cont = False
            else:
                cont = False
        rep += 1


#prints the 2d array as a readable output
def draw(grid):
    line = ''
    line += "\u2554"
    for i in range((Spiralsize * 2) + 2):
        line += "\u2550"
    line += "\u2557"
    print(line)
    for i in range(Spiralsize):
        row = ''
        row += "\u2551" + " "
        for j in range(Spiralsize):
            if find_prime(int(grid[i][j])) == True:
                row += prime
            else:
                row += not_prime
            #row += ' '
        row += " " + "\u2551"
        if i % 5 == 0: row += '  ' + str(i)
        print(row)
    line = ''
    line += "\u255A"
    for i in range((Spiralsize * 2) + 2):
        line += "\u2550"
    line += "\u255D"
    print(line)


#final code
def display():
    make_grid()
    spiral(center)
    draw(GRID)


display()
