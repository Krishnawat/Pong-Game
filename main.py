import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions and create a window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")


purple = (191, 0, 255) #paddle color
salmon = (255, 160, 122) #bg color


# Define paddle and ball dimensions
paddle_width = 15
paddle_height = 100
ball_size = 15

# Paddle positions and velocities
paddle1_y = height // 2 - paddle_height // 2
paddle2_y = height // 2 - paddle_height // 2
paddle1_velocity = 0
paddle2_velocity = 0
ball_x = width // 2
ball_y = height // 2
ball_velocity_x = random.choice([5, -5])
ball_velocity_y = random.choice([5, -5])

# Define font
font = pygame.font.SysFont(None, 55)

# Score tracking
score1 = 0
score2 = 0

# Func to display score
def display_score():
    score_text = font.render(f"{score1}  -  {score2}", True, purple)
    screen.blit(score_text, [width // 2 - score_text.get_width() // 2, 20])

# Main game loop
while True:
    screen.fill(salmon) 

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Control paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 10
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += 10
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 10
    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += 10

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y + ball_size >= height:
        ball_velocity_y *= -1

    # Ball collision with paddles
    if (ball_x <= paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height) or \
       (ball_x + ball_size >= width - paddle_width and paddle2_y <= ball_y <= paddle2_y + paddle_height):
        ball_velocity_x *= -1

    # Ball out of bounds
    if ball_x <= 0:
        score2 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_velocity_x *= -1
    if ball_x + ball_size >= width:
        score1 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_velocity_x *= -1

    # Draw paddles and ball
    pygame.draw.rect(screen, purple, (0, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, purple, (width - paddle_width, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, purple, (ball_x + ball_size // 2, ball_y + ball_size // 2), ball_size // 2)
    pygame.draw.rect(screen, purple, (ball_x, ball_y, ball_size, ball_size))

    # Display player's score
    display_score()

    #update the whole screen, including everything that's been drawn since the previous .
    pygame.display.flip()

    # Set Frame Rate
    pygame.time.Clock().tick(60)


# Quit program
pygame.quit()
quit()
