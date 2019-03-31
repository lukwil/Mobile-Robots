from random import randint

import pygame

WHITE = (255, 255, 255)  # background color
BLUE = (0, 0, 253)  # obstacle color
# GREEN =     (  0, 255,   0)
RED = (255, 0, 0)  # robot color
# TEXTCOLOR = (  0,   0,  0)
(width, height) = (600, 600)  # screen dimensions

running = True

obstacles = []


def main():
    global running, screen, surface, robot

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((width, height))
    surface.fill(WHITE)

    pygame.display.set_caption("Mobile Roboter: Übung 1")

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()

    robot = draw_Robot()
    draw_Obstacles()
    print(obstacles)
    obstacle = obstacles[0]
    print(obstacle)
    pygame.draw.rect(surface, BLUE, pygame.Rect(0, 0, 20, 20))
    pygame.display.flip()
    a = surface.get_at((1, 1))
    screen.blit(surface, (0, 0))
    print(a)

    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30)

        # robot.move_ip(10, 10)
        robot.x += 1
        # screen.blit(surface, (0, 0))
        # move_robot()

        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False

        # Inhalt von screen anzeigen.
        # pygame.display.flip()
        pygame.display.update()


def draw_Robot():
    position = (int(width / 2), int(height / 2))  # place in the center
    return pygame.draw.circle(surface, RED, position, 20)


def move_robot():
    # r = robot.move(10, 0)
    # robot = r
    pass


def draw_Obstacles():
    # draw ten obstacles

    for i in range(10):
        x = randint(0, 580)
        y = randint(0, 580)
        print(x, y)
        obstacles.append((x, y))
        pygame.draw.rect(surface, BLUE, pygame.Rect(x, y, 20, 20))


if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
