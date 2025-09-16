import pygame # import dependencies

# initialize pygame
pygame.init()

# declare constants
WIDTH, HEIGHT = 600, 600
X = WIDTH / 2
Y = HEIGHT / 2

# define x and y speed
x_speed = 0.05
y_speed = 0.05
RADIUS = 20

# create pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Key Movements") # set the title of the window

# draws a circle on the screen
def drawCircle():
    pygame.draw.circle(screen, [255, 255, 255], [X, Y], RADIUS)

def keyMovements():
    # a function which performs key movements
    global X
    global Y
    
    # get the keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: # if key is a, then move forward
        X -= x_speed
    if keys[pygame.K_d]: # if key is d, then move backward
        X += x_speed
    if keys[pygame.K_w]: # if key is w, then move up
        Y -= y_speed
    if keys[pygame.K_s]: # if key is s, then move down
        Y += y_speed

# create game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keyMovements() # call the function to perform key movements
    drawCircle() # draw the circle

    pygame.display.update() # update the screen

    screen.fill([0, 0, 0]) # fill the screen

pygame.quit() # close the game, after completion of program
