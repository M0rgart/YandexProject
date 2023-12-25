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


def terminate():
    pygame.quit()
    sys.exit()

#Стартовый экран, выбор персонажа или создание его
def start_screen():
    pass

#Окно создания персонажа: информация про классы
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

    pygame.display.flip()
    clock.tick(FPS)
terminate()
