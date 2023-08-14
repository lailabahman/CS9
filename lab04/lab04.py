# Laila Bahman

from Stack import Stack


# helper function to print out state of maze
def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='',end='')
        print("|")
    return


def solveMaze(maze, startX, startY):

    stack = Stack()
    stack.push([startX, startY])
    count = 1
    maze[startX][startY] = count # the initial position

    while stack.isEmpty() == False:

        peek = stack.peek()
        x = peek[0]
        y = peek[1]

        if maze[x-1][y] == 'G': # goal north
            return True

        if maze[x-1][y] == ' ': # empty north
            stack.push([x-1, y])
            count+=1
            maze[x-1][y] = count
            continue

        if maze[x][y-1] == 'G': # goal west
            return True

        if maze[x][y-1] == ' ': # empty west
            stack.push([x, y-1])
            count+=1
            maze[x][y-1] = count
            continue
                
        if maze[x+1][y]=='G': # goal south
            return True

        if maze[x+1][y] == ' ': # empty south
            stack.push([x+1,y])
            count+=1
            maze[x+1][y] = count
            continue

        if maze[x][y+1] == 'G': # goal east
            return True

        if maze[x][y+1] == ' ': # empty east
            stack.push([x, y+1])
            count+=1
            maze[x][y+1] = count
            continue
        
        stack.pop()
        
    return False
