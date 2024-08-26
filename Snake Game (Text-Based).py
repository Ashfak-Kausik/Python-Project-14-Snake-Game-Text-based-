import random

def snake_game():
    grid_size = 5
    snake = [(2, 2)]  # Initial snake position
    food = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    
    while True:
        print(f"Snake: {snake}")
        print(f"Food: {food}")
        move = input("Move (w/a/s/d): ").lower()
        
        if move not in directions:
            print("Invalid move. Game over.")
            break
        
        # Calculate new head position
        new_head = (snake[0][0] + directions[move][0], snake[0][1] + directions[move][1])
        
        if new_head == food:
            snake.insert(0, new_head)  # Grow snake
            food = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))  # New food position
        elif 0 <= new_head[0] < grid_size and 0 <= new_head[1] < grid_size and new_head not in snake:
            snake.insert(0, new_head)  # Move snake
            snake.pop()  # Remove tail
        else:
            print("You ran into the wall or yourself. Game over.")
            break

# Run the game
snake_game()
