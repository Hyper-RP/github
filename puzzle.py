from queue import PriorityQueue

class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def __eq__(self, other):
        return self.puzzle == other.puzzle
    
    def __lt__(self, other):
        return False
    
    def __hash__(self):
        return hash(str(self.puzzle))
    
    def is_goal(self):
        return self.puzzle == self.goal
    
    def possible_moves(self):
        moves = []
        row, col = self.find_zero()
        
        if row > 0:
            moves.append((-1, 0))  # Move blank space up
        if row < self.size - 1:
            moves.append((1, 0))  # Move blank space down
        if col > 0:
            moves.append((0, -1))  # Move blank space left
        if col < self.size - 1:
            moves.append((0, 1))  # Move blank space right
        
        return moves
    
    def find_zero(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    return i, j
    
    def swap(self, direction):
        puzzle_copy = [row[:] for row in self.puzzle]
        row, col = self.find_zero()
        new_row = row + direction[0]
        new_col = col + direction[1]
        puzzle_copy[row][col], puzzle_copy[new_row][new_col] = \
            puzzle_copy[new_row][new_col], puzzle_copy[row][col]
        return puzzle_copy

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    explored = set()
    
    frontier.put((0, initial_state))
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state.is_goal():
            return current_state
        
        explored.add(current_state)
        
        for move in current_state.possible_moves():
            new_puzzle = current_state.swap(move)
            new_state = PuzzleState(new_puzzle)
            
            if new_state not in explored:
                frontier.put((new_state.size, new_state))
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Solution found:")
        for row in solution.puzzle:
            print(row)

def main():
    initial_puzzle = []
    print("Enter the initial configuration of the puzzle (use 0 to represent the blank space):")
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_puzzle.append(row)
    
    initial_state = PuzzleState(initial_puzzle)
    solution = solve_puzzle(initial_state)
    print_solution(solution)

if __name__ == "__main__":
    main()
