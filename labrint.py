import random

# Maze size
WIDTH = 10
HEIGHT = 10

# Maze cell states
WALL = "#"
PATH = " "
START = "S"
END = "E"

# Directions
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Initialize the maze
maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]


def generate_maze():
    stack = [(0, 0)]
    visited = set([(0, 0)])

    while stack:
        x, y = stack[-1]
        neighbors = []

        # Find unvisited neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            dx, dy = nx - x, ny - y

            # Remove wall between current cell and chosen neighbor
            maze[x + dx // 2][y + dy // 2] = PATH
            maze[nx][ny] = PATH

            stack.append((nx, ny))
            visited.add((nx, ny))
        else:
            stack.pop()


def solve_maze():
    stack = [(0, 0)]
    visited = set([(0, 0)])

    while stack:
        x, y = stack[-1]

        if maze[x][y] == END:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < WIDTH
                and 0 <= ny < HEIGHT
                and (nx, ny) not in visited
                and maze[nx][ny] != WALL
            ):
                stack.append((nx, ny))
                visited.add((nx, ny))
                break
        else:
            stack.pop()


def print_maze():
    for row in maze:
        print(" ".join(row))


# Set start and end positions
maze[0][0] = START
maze[WIDTH - 1][HEIGHT - 1] = END

# Generate and solve the maze
generate_maze()
solve_maze()

# Print the maze
print("Generated Maze:")
print_maze()
print("\nSolved Maze:")
print_maze()
