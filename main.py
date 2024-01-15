import os
import sys
import pygame
import random


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
information = {"class": False, "Fiz_dmg": False, "hp": False, "defence": False,
               "Mag_dmg": False, "LVL": False, "max_hp": False}
enemyInformation = {"Enemy_hp": 0, "Enemy_atc": 0, "Type": 0}
money = 10
room_num = 0
location = 1

def terminate():
    pygame.quit()
    sys.exit()


#Стартовый экран, выбор персонажа или создание его
def start_screen():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    game = big_font.render("Название игры",
                           True, (255, 165, 0))
    screen.blit(game,
                (game.get_width() + 300,
                 game.get_height() - 50))

    class NewGameSprite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("newGame.png")
            self.image.set_colorkey((0, 0, 0))
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
            self.image.set_colorkey((0, 0, 0))
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
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (1130, 550)

    all_sprites = pygame.sprite.Group()
    exit = Exit()
    all_sprites.add(exit)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#выбор класса персонажа
def choose():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    choose_class = big_font.render("выберете класс",
                           True, (255, 0, 0))
    screen.blit(choose_class,
                ((screen.get_width() - choose_class.get_width()) // 2,
                 10))

    class knight(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("knight.png")
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width() // 6, 300)

    all_sprites = pygame.sprite.Group()
    kng = knight()
    all_sprites.add(kng)
    all_sprites.draw(screen)

    class hunter(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("hunter.png")
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width() // 6 * 3, 300)

    all_sprites = pygame.sprite.Group()
    hnt = hunter()
    all_sprites.add(hnt)
    all_sprites.draw(screen)

    class wizard(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.image.load("magic.png")
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width() // 6 * 5, 300)

    all_sprites = pygame.sprite.Group()
    wiz = wizard()
    all_sprites.add(wiz)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#Окно инвенторя, возможность сменить оружие, увидеть статистику персонажа
#распределение очков характеристик
def open_inventory():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#Повышение уровня, +очки характеристик
def lvl_up():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#Комната с сундуком, вначале рандомим редкость, затем предмет этой редкости
#Можно сделать псеводорандом на предметы класса (мечнику мечи пдают чаще луков)
def chest():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(f'chest{location}.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#Комната с магазином, куить предметы или улучшить старые
#сделать анимацию при выборе предметов
def shop():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#Бой, рандомный враг
def battle():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    if enemyInformation["Type"] == 0:
        enemyInformation["Type"] = random.randint(1, 2)
        if enemyInformation["Type"] == 1:
            enemyInformation["Enemy_hp"] = 25
            enemyInformation["Enemy_atc"] = 3

        elif enemyInformation["Type"] == 2:
            enemyInformation["Enemy_hp"] = 50
            enemyInformation["Enemy_atc"] = 1

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            mob = enemyInformation["Type"]
            self.image = pygame.image.load(f'enemy{mob}.png')
            self.rect = self.image.get_rect()
            self.rect.center = (900, 600)

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()
#todo

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    all_sprites = pygame.sprite.Group()
    enemy = Enemy()
    all_sprites.add(enemy)
    all_sprites.draw(screen)

    Hp = big_font.render(str(information["hp"]), True,
                               (150, 0, 0))
    screen.blit(Hp, (300, 450))

    enemy_hp = big_font.render(str(enemyInformation["Enemy_hp"]),
                               True, (150, 0, 0))
    screen.blit(enemy_hp, (1000, 450))

    atc_btn = big_font.render("Атаковать", True, (255, 0, 0))
    screen.blit(atc_btn, ((WIDTH - atc_btn.get_width()) // 2, 600))

    pygame.display.flip()
    clock.tick(FPS)


#Битв с боссом, пропаботать интелект получше чем в обычном бою
def boss_battle():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = (1000, 500)

    all_sprites = pygame.sprite.Group()
    bcg = Tree()
    all_sprites.add(bcg)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


#генератор комнат, попытка перерботать этжи. комнаты более рандомные чем
#в определенном порядке
def room_generator():
    if room_num == 10:
        return "boss_battle"
    else:
        rand = random.randint(1, 6)
        if rand == 6:
            return "shop"
        elif rand == 5:
            return "chest"
        else:
            return "battle"


#Достижения
def rewards():
    information["LVL"] += 1
    information["hp"] += 5
    information["Fiz_dmg"] += 1
    information["Mag_dmg"] += 1



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if game_moment == "start":
                if 1000 <= mouse[0] <= 1400 and 225 <= mouse[1] <= 275:
                    game_moment = "choose"
                elif 1000 <= mouse[0] <= 1400 and 375 <= mouse[1] <= 425:
                    game_moment = "rewards"
            elif game_moment == "choose":
                if 0 <= mouse[0] <= (WIDTH // 3) and 200 <= mouse[1]:
                    information['class'] = "knight"
                    information["Fiz_dmg"] = 10
                    information["Mag_dmg"] = 0
                    information["hp"] = 150
                    information["defence"] = 5
                    information["LVL"] = 1
                    game_moment = room_generator()
                elif ((WIDTH // 3) <= mouse[0] <= (WIDTH // 3) * 2
                      and 200 <= mouse[1]):
                    information['class'] = "hunter"
                    information["Fiz_dmg"] = 15
                    information["Mag_dmg"] = 5
                    information["hp"] = 120
                    information["defence"] = 0
                    information["LVL"] = 1
                    game_moment = room_generator()
                elif (WIDTH // 3) * 2 <= mouse[0] <= WIDTH and 200 <= mouse[1]:
                    information['class'] = "mage"
                    information["Fiz_dmg"] = 0
                    information["Mag_dmg"] = 20
                    information["hp"] = 100
                    information["defence"] = 0
                    information["LVL"] = 1
                    game_moment = room_generator()
                else:
                    pass
            elif game_moment == "battle":
                if WIDTH // 2 - 125 <= mouse[0] <= WIDTH // 2 + 125 \
                 and 625 <= mouse[1] <= 675:
                    enemyInformation["Enemy_hp"] -= information["Fiz_dmg"]
                    if enemyInformation["Enemy_hp"] <= 0:
                        enemyInformation = {"Enemy_hp": 0, "Enemy_atc": 0,
                                            "Type": 0}
                        rewards()
                        game_moment = room_generator()
                    else:
                        information["hp"] -= enemyInformation["Enemy_atc"]

                    print(information)
                    print(enemyInformation)

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
    elif game_moment == "choose":
        choose()
    elif game_moment == "rewards":
        rewards()

    pygame.display.flip()
    clock.tick(FPS)
terminate()
