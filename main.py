import os
import sys
import pygame


running = True
FPS = 60
WIDTH = 1366
HEIGHT = 768

pygame.init()
pygame.key.set_repeat(200, 70)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_moment = "start"
big_font = pygame.font.SysFont("comicsansms", 70)
small_font = pygame.font.SysFont("kacstbook", 60)

def terminate():
    pygame.quit()
    sys.exit()

#Стартовый экран, выбор персонажа или создание его
def start_screen():
    game = big_font.render("Название игры",
                           True, (255, 165, 0))
    screen.blit(game,
                (game.get_width() + 300,
                 game.get_height() - 50))

    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class NewGameSprite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("newGame.png")
            self.rect = self.image.get_rect()
            self.rect.center = (1160, 250)

    all_sprites = pygame.sprite.Group()
    NGS = NewGameSprite()
    all_sprites.add(NGS)
    all_sprites.draw(screen)

    class Rev(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("rewards.png")
            self.rect = self.image.get_rect()
            self.rect.center = (1150, 400)

    all_sprites = pygame.sprite.Group()
    rev = Rev()
    all_sprites.add(rev)
    all_sprites.draw(screen)

    class Exit(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("exit.png")
            self.rect = self.image.get_rect()
            self.rect.center = (1130, 550)

    all_sprites = pygame.sprite.Group()
    exit = Exit()
    all_sprites.add(exit)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)



#Окно сохдания персонажа: информация про классы
def choose_class():
    pass

#Окно инвенторя, возможность сменить оружие, увидеть статистику персонажа
#распределение очков характеристик
def open_inventory():
    pass

#Повышение уровня, +очки характеристик
def lvl_up():
    pass

#Комната с сундуком, вначале рандомим редкость, затем предмет этой редкости
#Можно сделать псеводорандом на предметы класса (мечнику мечи пдают чаще луков)
def chest():
    pass

#Комната с магазином, куить предметы или улучшить старые
#сделать анимацию при выборе предметов
def shop():
    pass

#Бой, рандомный враг
def battle():
    pass

#Битв с боссом, пропаботать интелект получше чем в обычном бою
def boss_battle():
    pass

#генератор комнат, попытка перерботать этжи. комнаты более рандомные чем
#в определенном порядке
def room_generator():
    pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_moment == "start":
        start_screen()
    elif game_moment == "battle":
        battle()
    elif game_moment == "shop":
        shop()
    elif game_moment == "chest":
        chest()
    elif game_moment == "boss_battle":
        boss_battle()

    pygame.display.flip()
    clock.tick(FPS)
terminate()
