import pygame
from settings import *
from random import choice, randint


class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):  # Орг Загрузка и масштабирование background
        # Создание бесшовного фона путем дублирования изображения
        # Плавное перемещение фона влево

        super().__init__(groups)
        bg_image = pygame.image.load('../graphics/environment/background.png').convert()

        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor
        full_sized_image = pygame.transform.scale(bg_image, (full_width, full_height))

        self.image = pygame.Surface((full_width * 2, full_height))
        self.image.blit(full_sized_image, (0, 0))
        self.image.blit(full_sized_image, (full_width, 0))

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):  # Тут будет движение фона с постоянной скоростью
        self.pos.x -= 300 * dt
        if self.rect.centerx <= 0: #возврат в начальное положение при достижении края
            self.pos.x = 0
        self.rect.x = round(self.pos.x)


class Ground(pygame.sprite.Sprite):


    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        self.sprite_type = 'ground'

        # (Почти как с BG) Загрузка и масштабирование земли
        ground_surf = pygame.image.load('../graphics/environment/ground.png').convert_alpha()
        self.image = pygame.transform.scale(ground_surf, pygame.math.Vector2(ground_surf.get_size()) * scale_factor)

        # Установка позиции внизу экрана
        self.rect = self.image.get_rect(bottomleft=(0, WINDOW_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # Создание маски для коллизий
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):  # Движение земли с постоянной скоростью
        self.pos.x -= 360 * dt
        if self.rect.centerx <= 0: # Возврат в начальное положение при достижении края
            self.pos.x = 0

        self.rect.x = round(self.pos.x)


class Plane(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)


        # Загрузка анимационных кадров
        self.import_frames(scale_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # Настройка начальной позиции
        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # движение и физика гравитации
        self.gravity = 600
        self.direction = 0

        # маска коллизий
        self.mask = pygame.mask.from_surface(self.image)

        # настройки звука  и звук прыжка
        self.jump_sound = pygame.mixer.Sound('../sounds/jump.wav')
        self.jump_sound.set_volume(0.3)

    def import_frames(self, scale_factor):  # масштабирование кадров анимации
        self.frames = []
        for i in range(3):
            surf = pygame.image.load(f'../graphics/plane/red{i}.png').convert_alpha()
            scaled_surface = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            self.frames.append(scaled_surface)

    def apply_gravity(self, dt):  #  гравитация (постепенное увеличение скорости падения)
        self.direction += self.gravity * dt # Увеличивает скорость падения
        self.pos.y += self.direction * dt
        self.pos.y += self.direction * dt  # Применяет скорость к позиции
        self.rect.y = round(self.pos.y)

    def jump(self):  # физика прыжка (резкое движение вверх)

        self.jump_sound.play()
        self.direction = -350

    def animate(self, dt):  # анимация крыльев самолета
        self.frame_index += 15 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def rotate(self):  # наклон самолета в зависимости от направления движения
        rotated_plane = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
        self.image = rotated_plane
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):  # обновление всех функций самолета (гравитация,анимация,наклон в направлении)
        self.apply_gravity(dt)
        self.animate(dt)
        self.rotate()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):



        super().__init__(groups)
        self.sprite_type = 'obstacle'

        orientation = choice(('up', 'down')) # случайный выбор типа препятствия (верхнее/нижнее)
        surf = pygame.image.load(f'../graphics/obstacles/{choice((0, 1))}.png').convert_alpha() # загрузка и масштабирование изображения
        self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)

        x = WINDOW_WIDTH + randint(40, 100)

        if orientation == 'up': # Случайное позиционирование за пределами экрана
            y = WINDOW_HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            y = randint(-50, -10)
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midtop=(x, y))

        self.pos = pygame.math.Vector2(self.rect.topleft)

        # Создание маски для коллизий
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 400 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()
        # Движение препятствия влево
        # Удаление при выходе за пределы экрана