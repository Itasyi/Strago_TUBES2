import turtle

t = turtle.Turtle()
turtle.tracer(0)
t.speed(10)
t.hideturtle()

# Fungsi untuk menggambarkan box
def box(intDim):
    t.begin_fill()
    t.forward(intDim)
    t.left(90)
    t.forward(intDim)
    t.left(90)
    t.forward(intDim)
    t.left(90)
    t.forward(intDim)
    t.end_fill()
    t.setheading(0)

# Spesifikasi Maze dalam bentuk 0,1. 1 untuk dinding, 0 untuk jalur
palette = ["#FFFFFF", "#000000", "#00ff00", "#ff00ff", "#AAAAAA"]
maze = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
maze.append([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1])
maze.append([1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1])
maze.append([1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1])
maze.append([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1])
maze.append([1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1])
maze.append([1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1])
maze.append([1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1])
maze.append([1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1])
maze.append([1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1])
maze.append([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1])
maze.append([1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1])
maze.append([1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1])
maze.append([1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1])
maze.append([1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2])
maze.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# Fungsi untuk menggambarkan Maze
def drawMaze(maze):
    boxSize = 15
    t.penup()
    t.goto(-130, 130)
    t.setheading(0)
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            t.color(palette[maze[i][j]])
            box(boxSize)
            t.penup()
            t.forward(boxSize)
            t.pendown()
        t.setheading(270)
        t.penup()
        t.forward(boxSize)
        t.setheading(180)
        t.forward(boxSize * len(maze[i]))
        t.setheading(0)
        t.pendown()

# Fungsi rekursif untuk mencari jalan keluar
# Urutan pencarian: bawah, atas, kanan, kiri, atas
def exploreMaze(maze, row, col):
    if maze[row][col] == 2: # Jika bernilai 2, maka jalan keluar ketemu
        return True
    elif maze[row][col] == 0:  # Jika bernilai 0, maka itu adalah jalur
        maze[row][col] = 3
        t.clear()
        drawMaze(maze)
        t.getscreen().update()

        # Cek ke bawah
        if row < len(maze) - 1:
            if exploreMaze(maze, row + 1, col):
                return True

        # Cek ke atas
        if row > 0:
            if exploreMaze(maze, row - 1, col):
                return True

        # Cek ke kanan
        if col < len(maze[row]) - 1:
            # Explore path to the right
            if exploreMaze(maze, row, col + 1):
                return True

        # Cek ke kiri
        if col > 0:
            # Explore path to the left
            if exploreMaze(maze, row, col - 1):
                return True

        # Backtrack
        maze[row][col] = 4
        t.clear()
        drawMaze(maze)
        t.getscreen().update()

        print("Backtrack, kembali ke: [", row, "] [", col, "]")

# Main program
drawMaze(maze)
t.getscreen().update()

solved = exploreMaze(maze, 0, 1) # Dimulai pada row 0, column 1, karena Start terlatak disana
if solved:
    print("Jalan keluar Maze ditemukan")
else:
    print("Jalan keluar Maze TIDAK ditemukan")

t.getscreen().update()
turtle.Screen().exitonclick()
