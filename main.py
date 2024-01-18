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
               "Mag_dmg": False, "LVL": False, "max_hp": False, "money": 5}
enemyInformation = {"Enemy_hp": 0, "Enemy_atc": 0, "Type": 0}
room_num = 0
location = 1
inventory = []
items = [
        "sword1", "sword2", "sword3",
        "staff1", "staff2",
        "silver", "broom", "stone",
        "gold_pile", "gold_coins", "wallet",
        "helmet", "armor", "boots",
        "strength_potion"
    ]


def terminate():
    pygame.quit()
    sys.exit()


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
    ngs = NewGameSprite()
    all_sprites.add(ngs)
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
    all_sprites.add(Exit())
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


def choose():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.draw(screen)
    choose_class = big_font.render("выберете класс",
                                   True, (255, 0, 0))
    screen.blit(choose_class,
                ((screen.get_width() - choose_class.get_width()) // 2,
                 10))

    class Shadow(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(
                pygame.image.load("shadow.png"), (350, 450))
            self.rect = self.image.get_rect()
            self.rect.center = (500, 550)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Shadow())
    all_sprites.draw(screen)

    class Shadow(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(
                pygame.image.load("shadow.png"), (375, 375))
            self.rect = self.image.get_rect()
            self.rect.center = (975, 560)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Shadow())
    all_sprites.draw(screen)

    class ArturPirozhkov(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(
                pygame.image.load("Knight.png"), (275, 390))
            self.rect = self.image.get_rect()
            self.rect.center = (500, 475)

    all_sprites = pygame.sprite.Group()
    pineapple = ArturPirozhkov()
    all_sprites.add(pineapple)
    all_sprites.draw(screen)

    class Wizard(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(
                pygame.image.load("mag.png"), (275, 390))
            self.rect = self.image.get_rect()
            self.rect.center = (975, 480)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Wizard())
    all_sprites.draw(screen)

    class Front(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('frontground.png')
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Front())
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


def open_inventory():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()
    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


def lvl_up():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


def chest():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(f'chest{location}.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.draw(screen)

    pygame.draw.rect(screen, (150, 150, 150),
                     (100, 100, WIDTH - 200, HEIGHT - 200))

    pygame.draw.rect(screen, (50, 50, 50),
                     (150, 150, 508, 468))
    pygame.draw.rect(screen, (50, 50, 50),
                     (708, 150, 508, 468))

    exit_button = small_font.render("Выход", True, (255, 0, 0))
    screen.blit(exit_button, (1150, 700))

    pygame.display.flip()
    clock.tick(FPS)


def shop():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    all_sprites = pygame.sprite.Group()
    x = Tree()
    all_sprites.add(x)
    all_sprites.draw(screen)

    money_icon = pygame.transform.scale(
        pygame.image.load('money.png'), (50, 50))
    money_icon.set_colorkey((255, 255, 255))
    screen.blit(money_icon, (25, 15))
    money_text = small_font.render(str(information["money"]),
                                   True, (255, 255, 0))
    screen.blit(money_text, (80, 20))

    if "shop_items" not in information:
        information["shop_items"] = generate_shop_items()

    item_images, item_prices, item_bought = information["shop_items"]

    for i, item_image in enumerate(item_images):
        if not item_bought[i]:
            price_text = small_font.render(f"{item_prices[i]} монет", True, (255, 255, 0))
            screen.blit(price_text, (200 + i * 300, 300))
            screen.blit(item_image, (200 + i * 300, 150))

            buy_button = small_font.render("Купить", True, (255, 0, 0))
            button_rect = buy_button.get_rect(center=(300 + i * 300, 500))
            screen.blit(buy_button, button_rect.topleft)

            mouse = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if information["money"] >= item_prices[i]:
                        information["money"] -= item_prices[i]

                        inventory.append(f'item{i + 1}.png')
                        print(f"Ты купил предмет {i + 1} за {item_prices[i]} монет.")

                        item_bought[i] = True

    exit_button = small_font.render("Выход", True, (255, 0, 0))
    screen.blit(exit_button, (1150, 700))

    pygame.display.flip()
    clock.tick(FPS)


def generate_shop_items():
    num_items = 3
    item_images = []
    item_prices = []
    item_bought = [False] * num_items

    for _ in range(num_items):
        item_name = f'{random.choice(items)}.png'
        item_image = pygame.image.load(item_name)
        item_price = random.randint(10, 30)

        item_images.append(item_image)
        item_prices.append(item_price)

    return item_images, item_prices, item_bought


def battle():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    if enemyInformation["Type"] == 0:
        enemyInformation["Type"] = random.randint(1, 4)
        if enemyInformation["Type"] == 1:
            enemyInformation["Enemy_hp"] = 100
            enemyInformation["Enemy_atc"] = 2

        elif enemyInformation["Type"] == 2:
            enemyInformation["Enemy_hp"] = 25
            enemyInformation["Enemy_atc"] = 10

        elif enemyInformation["Type"] == 3:
            enemyInformation["Enemy_hp"] = 50
            enemyInformation["Enemy_atc"] = 5

        elif enemyInformation["Type"] == 4:
            enemyInformation["Enemy_hp"] = 50
            enemyInformation["Enemy_atc"] = 5

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            mob = enemyInformation["Type"]
            self.image = pygame.image.load(f'enemy{mob}.png')
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 2, 600)

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    class Shadow(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(
                pygame.image.load("shadow.png"), (375, 375))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 2 + 10, 575)

    class Money(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(
                pygame.image.load('money.png'), (50, 50))
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.center = (1325, 35)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.add(Shadow())
    all_sprites.add(Enemy())
    all_sprites.add(Money())
    all_sprites.draw(screen)

    mon = small_font.render(str(information["money"]),
                            True, (255, 255, 0))
    screen.blit(mon, (1250, 20))

    hp = small_font.render(str(information["hp"]), True,
                         (0, 255, 0))
    screen.blit(hp, (25, 15))

    enemy_hp = big_font.render(str(enemyInformation["Enemy_hp"]),
                               True, (150, 0, 0))
    screen.blit(enemy_hp, (WIDTH // 2 - 50, 450))

    atc_btn = big_font.render("Атаковать", True, (255, 0, 0))
    screen.blit(atc_btn, ((WIDTH - atc_btn.get_width()) // 2, 10))

    pygame.display.flip()
    clock.tick(FPS)


def boss_battle():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    if enemyInformation["Type"] == 0:
        enemyInformation["Type"] ="god"
        enemyInformation["Enemy_hp"] = 300
        enemyInformation["Enemy_atc"] = 20

    class Boss(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(
                pygame.image.load('dragon.png'), (300, 300))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 2, 550)

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background1.png')
            self.rect = self.image.get_rect()

    class Shadow(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50, 50))
            self.image = pygame.transform.scale(
                pygame.image.load("shadow.png"), (375, 375))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 2 + 10, 575)

    class Money(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(
                pygame.image.load('money.png'), (50, 50))
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.center = (1325, 35)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.add(Shadow())
    all_sprites.add(Money())
    all_sprites.add(Boss())
    all_sprites.draw(screen)

    mon = small_font.render(str(information["money"]),
                            True, (255, 255, 0))
    screen.blit(mon, (1250, 20))

    hp = small_font.render(str(information["hp"]), True,
                           (0, 255, 0))
    screen.blit(hp, (25, 15))

    enemy_hp = big_font.render(str(enemyInformation["Enemy_hp"]),
                               True, (150, 0, 0))
    screen.blit(enemy_hp, (WIDTH // 2 - 50, 300))

    atc_btn = big_font.render("Атаковать", True, (255, 0, 0))
    screen.blit(atc_btn, ((WIDTH - atc_btn.get_width()) // 2, 10))

    pygame.display.flip()
    clock.tick(FPS)


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


def rewards():
    information["LVL"] += 1
    information["max_hp"] += 5
    information["hp"] += 2
    information["Fiz_dmg"] += 1
    information["Mag_dmg"] += 1

    give_random_item()


def the_end():
    all_sprites = pygame.sprite.Group()
    all_sprites.update()

    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('background2.png')
            self.rect = self.image.get_rect()

    class Slime1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('enemy1.png')
            self.rect = self.image.get_rect()
            self.rect.center = (200, 625)

    class Slime2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('enemy2.png')
            self.rect = self.image.get_rect()
            self.rect.center = (700, 625)

    class Slime3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('enemy4.png')
            self.rect = self.image.get_rect()
            self.rect.center = (1200, 625)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Tree())
    all_sprites.add(Slime1())
    all_sprites.add(Slime2())
    all_sprites.add(Slime3())
    all_sprites.draw(screen)

    end = big_font.render("You Win", True, (255, 0, 0))
    screen.blit(end, ((WIDTH - end.get_width()) // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)


def give_random_item():

    random_item = random.choice(items)

    if random_item.startswith("sword"):
        information["Fiz_dmg"] += int(random_item[-1])
        print(f"Ты получил {random_item} - Physical damage + "
              f"{int(random_item[-1])}!")

    elif random_item.startswith("staff"):
        information["Mag_dmg"] += int(random_item[-1])
        print(f"Ты получил {random_item} - Magical damage + "
              f"{int(random_item[-1])}!")

    elif random_item == "silver":
        information["max_hp"] += 25
        print(f"Ты получил {random_item} - Max HP +25!")

    elif random_item == "broom":
        information["max_hp"] += 15
        print(f"Ты получил {random_item} - Max HP +15!")

    elif random_item == "stone":
        information["max_hp"] += 30
        information["defence"] += 5
        print(f"Ты получил {random_item} - Max HP +30, Defense +5!")

    elif random_item == "gold_pile":
        information["money"] += 30
        print(f"Ты получил {random_item} - Money +30!")

    elif random_item == "gold_coins":
        information["money"] += 15
        print(f"Ты получил {random_item} - Money +15!")

    elif random_item == "wallet":
        information["money"] += 50
        print(f"Ты получил {random_item} - Money +50!")

    elif random_item == "helmet":
        information["defence"] += 3
        print(f"Ты получил {random_item} - Defense +3!")

    elif random_item == "armor":
        information["defence"] += 7
        print(f"Ты получил {random_item} - Defense +7!")

    elif random_item == "boots":
        information["defence"] += 5
        print(f"Ты получил {random_item} - Defense +5!")

    elif random_item == "strength_potion":
        information["max_hp"] += 25
        information["defence"] += 10
        information["Fiz_dmg"] += 10
        information["Mag_dmg"] += 10
        print(f"Ты получил {random_item} - Max HP +25, Defense +10, "
              f"Physical/Magical damage +10!")

    inventory.append(random_item)


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
                if 0 <= mouse[0] <= (WIDTH // 2) and 200 <= mouse[1]:
                    information['class'] = "knight"
                    information["Fiz_dmg"] = 10
                    information["Mag_dmg"] = 0
                    information["hp"] = 150
                    information["defence"] = 5
                    information["LVL"] = 1
                    information["max_hp"] = 150
                    information["defence"] = 3
                    game_moment = room_generator()
                elif WIDTH // 2 <= mouse[0] <= WIDTH and 200 <= mouse[1]:
                    information['class'] = "mage"
                    information["Fiz_dmg"] = 0
                    information["Mag_dmg"] = 20
                    information["hp"] = 100
                    information["defence"] = 0
                    information["LVL"] = 1
                    information["max_hp"] = 100
                    game_moment = room_generator()
                else:
                    pass
                room_num += 1
            elif game_moment == "battle" or game_moment == "boss_battle":
                if WIDTH // 2 - 125 <= mouse[0] <= WIDTH // 2 + 125 \
                 and 25 <= mouse[1] <= 100:
                    if information["Fiz_dmg"] > information["Mag_dmg"]:
                        enemyInformation["Enemy_hp"] -= information["Fiz_dmg"]
                    else:
                        enemyInformation["Enemy_hp"] -= information["Mag_dmg"]
                    if enemyInformation["Enemy_hp"] <= 0:
                        if game_moment == "battle":
                            enemyInformation = {"Enemy_hp": 0, "Enemy_atc": 0,
                                                "Type": 0}
                            information["money"] += random.randint(1, 5)
                            rewards()
                            game_moment = room_generator()
                            room_num += 1
                        else:
                            game_moment = "end"
                    else:
                        dmg = enemyInformation["Enemy_atc"] - \
                              information["defence"]
                        if dmg > 0:
                            information["hp"] -= dmg
            elif game_moment == "shop":
                if 1150 <= mouse[0] <= WIDTH and 700 <= mouse[1] <= 750:
                    game_moment = room_generator()
                    room_num += 1
            elif game_moment == "chest":
                if 1150 <= mouse[0] <= WIDTH and 700 <= mouse[1] <= 750:
                    game_moment = room_generator()
                    room_num += 1

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
    elif game_moment == "end":
        the_end()

    pygame.display.flip()
    clock.tick(FPS)

terminate()