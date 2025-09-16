import pygame

pygame.init()
WIDTH, HEIGHT = 600, 600
X = WIDTH / 2
Y = HEIGHT / 2
x_speed = 0.05
y_speed = 0.05
RADIUS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Key Movements")

def drawCircle():
    pygame.draw.circle(screen, [255, 255, 255], [X, Y], RADIUS)

def keyMovements():
    global X
    global Y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        X -= x_speed
    if keys[pygame.K_d]:
        X += x_speed
    if keys[pygame.K_w]:
        Y -= y_speed
    if keys[pygame.K_s]:
        Y += y_speed


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keyMovements()
    drawCircle()

    pygame.display.update()

    screen.fill([0, 0, 0])

pygame.quit()
