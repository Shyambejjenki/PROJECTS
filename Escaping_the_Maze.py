import tkinter as tk
import time

# Maze Config: 'S' = Start, 'E' = End, '#' = Wall, ' ' = Path
maze = [
    ["S", " ", "#", " ", " ", " "],
    ["#", " ", "#", " ", "#", " "],
    ["#", " ", " ", " ", "#", " "],
    ["#", "#", "#", " ", "#", " "],
    ["#", " ", " ", " ", " ", "E"]
]

CELL_SIZE = 60
ROWS = len(maze)
COLS = len(maze[0])

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Escape")
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()
        self.draw_maze()
        self.root.after(500, self.solve_maze)  # Delay before starting DFS

    def draw_maze(self, path=[]):
        self.canvas.delete("all")
        for i in range(ROWS):
            for j in range(COLS):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

                cell = maze[i][j]
                if (i, j) in path:
                    color = "lightgreen"
                elif cell == "#":
                    color = "black"
                elif cell == "S":
                    color = "blue"
                elif cell == "E":
                    color = "red"
                else:
                    color = "white"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
        self.root.update()

    def solve_maze(self):
        start = self.find_pos("S")
        end = self.find_pos("E")
        path = self.dfs(start, end)
        if path:
            for step in path:
                self.draw_maze(path[:path.index(step)+1])
                time.sleep(0.3)
            print("Maze escaped successfully!")
        else:
            print("No path found.")

    def find_pos(self, symbol):
        for i in range(ROWS):
            for j in range(COLS):
                if maze[i][j] == symbol:
                    return (i, j)
        return None

    def dfs(self, start, end):
        stack = [(start, [start])]
        while stack:
            (x, y), path = stack.pop()
            if (x, y) == end:
                return path
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] != "#" and (nx, ny) not in path:
                    stack.append(((nx, ny), path + [(nx, ny)]))
        return None

# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
