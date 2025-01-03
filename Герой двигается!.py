import os
import sys

import pygame


# from pygame.examples.moveit import load_image


def Load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением'{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Creature(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = Load_image("creature.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if args:
            self.rect.x += args[0][0]
            self.rect.y += args[0][1]


if __name__ == '__main__':
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    creature = Creature(all_sprites)
    FPS = 40
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        screen.fill('white')
        if keys[pygame.K_LEFT]:
            all_sprites.update((-10, 0))
        elif keys[pygame.K_RIGHT]:
            all_sprites.update((10, 0))
        elif keys[pygame.K_UP]:
            all_sprites.update((0, -10))
        elif keys[pygame.K_DOWN]:
            all_sprites.update((0, 10))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
