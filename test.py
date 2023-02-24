import pygame

x1 = 0;
x2 = 0
y1 = 0;
y2 = 30
black = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((500, 500))

grasslist = pygame.sprite.Group()
go = True
clock = pygame.time.Clock()


def create(what, x, y):
    global grasslist
    if what == 'grass':
        block = grass.Grass()
        grasslist.add(block)
        block.rect.x = x
        block.rect.y = y


while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        x1 += 3

    create('grass', x1, y1)
    create('grass', x2, y2)
    screen.fill((255, 255, 255))
    grasslist.draw(screen)
    clock.tick(60)
    pygame.display.flip()
