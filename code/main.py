import pygame, sys, time
from settings import *
from sprites import BG, Ground, Plane, Obstacle


class Game:
    def __init__(self):

        # Инициализация pygame и игрового окна
        pygame.init()  # Инициализация pygame
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Plane')
        self.clock = pygame.time.Clock()
        self.active = True

        # Настройка групп спрайтов
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # scale factor (коэффицент масштабирования)
        bg_height = pygame.image.load('../graphics/environment/background.png').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height

        # установка спрайтов (самолета,бг,земли)
        BG(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites, self.collision_sprites], self.scale_factor)
        self.plane = Plane(self.all_sprites, self.scale_factor / 1.8)

        # таймер для генерации препятствий
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        # настройка шрифта и счета
        self.font = pygame.font.Font('../graphics/font/BD_Cartoon_Shout.ttf', 30)
        self.score = 0
        self.start_offset = 0

        # загрузка меню
        self.menu_surf = pygame.image.load('../graphics/ui/menu.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # загрузка музыки
        self.music = pygame.mixer.Sound('../sounds/music.wav')
        self.music.play(loops=-1)

    def collisions(self):
        # проверка столкновений самолета с землей или препятствиями
        # остановка игры при столкновении
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False, pygame.sprite.collide_mask) \
                or self.plane.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.active = False
            self.plane.kill()

    def display_score(self):
        # отображение текущего счета во время игры
        # отображение финального счета
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1400
            y = WINDOW_HEIGHT / 10
        else:
            y = WINDOW_HEIGHT / 2 + (self.menu_rect.height / 1.5)

        score_surf = self.font.render(str(self.score), True, 'black')
        score_rect = score_surf.get_rect(midtop=(WINDOW_WIDTH / 2, y))
        self.display_surface.blit(score_surf, score_rect)

    def run(self):
        # основной игровой цикл
        last_time = time.time()
        while True:
            # delta time (dt)
            dt = time.time() - last_time
            last_time = time.time()

            # цикл обработка событий (нажатий, закрытия окна)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # прыжок на ЛКМ или пробел
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or \
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane = Plane(self.all_sprites, self.scale_factor / 1.7)
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()

                if event.type == self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.1)

            # логика игры
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.active:
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf, self.menu_rect)

            pygame.display.update()
# проверка на main
if __name__ == '__main__':
    game = Game()
    game.run()
