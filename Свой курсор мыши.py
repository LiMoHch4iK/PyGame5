import os
import sys

import pygame


def load_image(name, colorkey=None):
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


class Arrow(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("arrow.png")
        self.rect = self.image.get_rect()

    def update(self, *args):
        if args:
            self.rect = args[0]


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Kypcop')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    arrow = Arrow()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(arrow)
    all_sprites.draw(screen)
    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                all_sprites.update(event.pos)

        screen.fill('black')
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()
