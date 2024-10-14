# Pong Arcade Game

This is a classic Pong arcade game built using Python and the Turtle graphics library. Players can move paddles up and down to prevent the ball from passing them. The game includes object-oriented programming principles with classes for the ball, paddles, and scoreboard.

## Features
1. **Turtle Graphics**: The game uses the Turtle library to create graphical elements for paddles, ball, and the game screen.
2. **Ball Class**: Implements the logic for the movement of the ball and bouncing mechanics when it hits walls or paddles.
3. **Scoreboard Class**: Keeps track of the score for each player and updates the score display during the game.
4. **Paddle Class**: Implements the logic for controlling the paddles on each side of the screen.

## Game Controls
- **Right Paddle**: Use the "Up" and "Down" arrow keys to move the right paddle.
- **Left Paddle**: Use the "W" and "S" keys to move the left paddle.
  
The game ends when one player reaches a certain score, or the game can run indefinitely.

## Classes Used

### 1. Ball Class (`ball.py`)
The `Ball` class handles:
- Moving the ball in different directions.
- Bouncing the ball off the walls and paddles.
- Resetting the ball position when a player misses the ball.

### 2. Paddle Class (`paddle.py`)
The `Paddl` class handles:
- Creating paddles at specified positions.
- Moving the paddles up and down when the user presses the keys.
- Stopping the paddle's movement when the key is released.

### 3. Scoreboard Class (`score.py`)
The `Score` class handles:
- Keeping track of the score for both players.
- Updating the scoreboard after each point.
