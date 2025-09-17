import pygame # import dependencies

HEIGHT = 600 # declare constants to set the HEIGHT and WIDTH of the screen
WIDTH = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # create the screen
pygame.display.set_caption("Basic Movements - Object Oriented") # set title of the screen

# declare variables to keep track of the speed in the x and y directions
x_speed = 0.1
y_speed = 0.1


class BallObject:
    # create a ball object

    def __init__(self, SCREEN, x, y, radius):
        """
        :param SCREEN: takes the surface to place the ball
        :param x: takes the x-coordinate of the surface to place the ball
        :param y: takes the y-coordinate of the surface to place the ball
        :param radius: takes the radius of the ball

        """
        self.x = x # initialize the data members
        self.y = y
        self.radius = radius
        self.SCREEN = SCREEN

    def drawMyself(self):
        """
        :return: draws a circle on the specified x- and y-coordinates, of the specified radius, on the specified surface
        """
        pygame.draw.circle(self.SCREEN, [255, 255, 255], [self.x, self.y], self.radius)

    def addKeyMovements(self, x_speed, y_speed):
        """
        :param x_speed: defines the speed in x-direction
        :param y_speed:  defines the speed in y-direction
        :return: changes the x- and y-coordinates according to basic WASD commands
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # if key is a, then move forward
            self.x -= x_speed
        if keys[pygame.K_d]:  # if key is d, then move backward
            self.x += x_speed
        if keys[pygame.K_w]:  # if key is w, then move up
            self.y -= y_speed
        if keys[pygame.K_s]:  # if key is s, then move down
            self.y += y_speed


pygame.init() # initialize pygame

b = BallObject(SCREEN, WIDTH/2, HEIGHT/2, 20) # create a ball object in the center of the screen, of radius = 20 units

# create the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # call the functions within the ball object
    b.addKeyMovements(x_speed, y_speed)
    b.drawMyself()
    pygame.display.update() # update the screen with each iteration

    SCREEN.fill((0,0,0)) # fill the screen after each update (performs double buffered animation)


pygame.quit() # quit from pygame
