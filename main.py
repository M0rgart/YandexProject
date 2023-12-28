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
                           True, (255, 255, 255))
    screen.blit(game,
                (game.get_width() + 300, game.get_height() - 50))

    ngButton = small_font.render("Начать игру",
                                 True, (255, 255, 255))
    screen.blit(ngButton,
                (ngButton.get_width() + 820, 300 - ngButton.get_height()))

    achievements = small_font.render("Достижения",
                                     True, (255, 255, 255))
    screen.blit(achievements,
                (ngButton.get_width() + 805, 450 - ngButton.get_height()))

    exit_button = small_font.render("Покинуть игру",
                                     True, (255, 255, 255))
    screen.blit(exit_button,
                (exit_button.get_width() + 720,
                 600 - exit_button.get_height()))

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

    pygame.display.flip()
    clock.tick(FPS)
terminate()
