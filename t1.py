import pygame as pg


def t1():
    pg.init()

    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    BG_COLOR = pg.Color('gray12')
    SIENNA = pg.Color('sienna1')
    radius = 20
    # This rect serves as the position of the circle and
    # can be used for collision detection.
    rect = pg.Rect(50, 200, radius, radius)

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        rect.x += 1  # Update the position of the rect.

        screen.fill(BG_COLOR)
        # Now draw the circle at the center of the rect.
        pg.draw.circle(screen, SIENNA, rect.center, radius)
        pg.display.flip()
        clock.tick(30)

    pg.quit()


if __name__ == '__main__':
    t1()
