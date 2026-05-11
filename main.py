# -*- coding: utf-8 -*-
import pygame
import sys
import random
import time
import base64
import io

# CONSTANTS
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5

# NOTE: If code is not working, make sure this constant is valid base64 or add your own!

FALLBACK_IMAGE_BASE64 = "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"

FALLBACK_IMAGE_BYTES = base64.b64decode(FALLBACK_IMAGE_BASE64)

def get_fallback_image():
    return io.BytesIO(FALLBACK_IMAGE_BYTES)

# VARIABLES
global gauge_increase
gauge_increase = 1
global gauge_fill
gauge_fill = 50
player_size = [random.randint(50,150), random.randint(50,150)]
player_speed = 5
global difficulty
difficulty = 0
global coins_collected
coins_collected = 0
paused = False
global coin_gain
coin_gain = 1

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trash Catcher by Bradley Hu")
clock = pygame.time.Clock()
global bg_image
try:
    bg_image = pygame.image.load("assets\\background.png").convert_alpha()
except FileNotFoundError:
        bg_image = pygame.image.load(get_fallback_image()).convert_alpha()
# CLASSES
class FallingObject(pygame.sprite.Sprite):
    def __init__(self, image_path=None, y_speed = random.uniform(1, 3)):
        super().__init__()
        try:
            if image_path is None:
                image_path = get_fallback_image()
            self.image = pygame.image.load(image_path).convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load(get_fallback_image()).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.vel_y = y_speed

    def update(self):
        global difficulty
        self.rect.y += (self.vel_y + min(round(clock.get_time() / 10000, 2), 50))*GRAVITY
        if self.rect.top > HEIGHT:
            global gauge_fill
            if self in garbage:
                gauge_fill = max(0, gauge_fill - 10)
            elif self in coins:
                gauge_fill = min(100, gauge_fill - 5)
            self.kill()

garbage = pygame.sprite.Group()
coins = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("assets\\player1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, player_size)
        except FileNotFoundError:
            self.image = pygame.image.load(get_fallback_image()).convert_alpha()
            self.image = pygame.transform.scale(self.image, player_size)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.vel_y = 0
        self.cheatmode = False

    def update(self):
        global coins_collected
        global gauge_fill
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += player_speed
        if keys[pygame.K_SPACE]:
            global paused
            if paused:
                paused = False
            else:                
                paused = True
        if keys[pygame.K_ESCAPE] and keys[pygame.K_c] and keys[pygame.K_LCTRL]:
            self.cheatmode = True
            print("Cheat code activated. Remember, with great power comes... ah nevermind, go have fun")
            coins_collected = 9999999999999999999999999999999999999999999999999999999999999999999999967
        if keys[pygame.K_i] and self.cheatmode:
            try:
                coins_collected = int(input("enter something fun>>>"))
            except ValueError:
                print("nice try")
        if pygame.sprite.spritecollide(self, garbage, True):
            gauge_fill = min(100, gauge_fill + gauge_increase)
        if pygame.sprite.spritecollide(self, coins, True):
            global coin_gain
            coins_collected += coin_gain
            gauge_fill = min(100, gauge_fill + gauge_increase*5)

class gauge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("assets\\gauge.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 120))
        except FileNotFoundError:
            self.image = pygame.image.load(get_fallback_image()).convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 120))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 50
        self.rect.y = HEIGHT / 2

class gauge_filler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = 50
        self.image = pygame.Surface((20,self.height))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 45
        self.rect.y = HEIGHT / 2 + 10
    def update(self):
        global gauge_fill
        global coins_collected
        global coin_gain
        self.height = gauge_fill
        self.image = pygame.Surface((20,max(self.height,1)))
        if gauge_fill > 33 and gauge_fill <= 66:
            self.image.fill((255,127,127))
        elif gauge_fill > 66 and gauge_fill < 100:
            self.image.fill((127,255,127))
        elif gauge_fill <= 33:
            self.image.fill((255,0,0))
        elif gauge_fill >= 100:
            self.image.fill((0,255,0))
            time.sleep(1)
            coins_collected += coin_gain * 10
            gauge_fill = 50
        if gauge_fill == 1:
            self.image.fill((255,0,0))
            time.sleep(1)
            coins_collected = max(0, coins_collected - 10)
            gauge_fill = 50

class button(pygame.sprite.Sprite):
    def __init__(self, text, pos, cost, var_changed, change_amount, price_incr, size=(100, 25)):
        super().__init__()
        self.font = pygame.font.SysFont(None, 36)
        self.text = text
        self.image = self.font.render(self.text, True, (255, 255, 255))
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.cost = cost
        self.var_changed = var_changed
        self.change_amount = change_amount
        self.price_incr = price_incr
        self.click_cd = 0
    def update(self):
        global gauge_fill
        global coins_collected
        if self.click_cd > 0:
            self.click_cd -= 1
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.handle_click()

    def handle_click(self):
        global coins_collected
        if pygame.mouse.get_pressed()[0] and coins_collected >= self.cost and self.click_cd == 0:
            self.click_cd = 10 
            coins_collected -= self.cost
            current = getattr(sys.modules[__name__], self.var_changed)
            if isinstance(current, list):
                new_value = [x + self.change_amount for x in current]
            else:
                new_value = current + self.change_amount
            setattr(sys.modules[__name__], self.var_changed, new_value)
            if self.var_changed == "player_size":
                self.update_player_size()
            self.cost += self.price_incr
            self.text = f"{self.text.split(':')[0]}: {self.cost}"
            self.image = self.font.render(self.text, True, (255, 255, 255))
            self.image = pygame.transform.scale(self.image, (100, 25))

    def update_player_size(self):
        try:
            player.image = pygame.image.load("assets\\player1.png").convert_alpha()
        except FileNotFoundError:
            player.image = pygame.image.load(get_fallback_image()).convert_alpha()
        player.image = pygame.transform.scale(player.image, player_size)
        player.rect = player.image.get_rect(center=player.rect.center)
        
# OBJECTS
player = Player()
gauge = gauge()
gauge_filler = gauge_filler()
store_buttons = pygame.sprite.Group()
store_buttons.add(button("Player Size", (WIDTH - 100, HEIGHT // 2), 1, "player_size", 10, 2))
store_buttons.add(button("Player Speed", (WIDTH - 100, HEIGHT // 2 + 30), 1, "player_speed", 3, 2))
store_buttons.add(button("Coin Gain", (WIDTH - 100, HEIGHT // 2 + 60), 5, "coin_gain", 1, 2))
store_buttons.add(button("Gauge Increase", (WIDTH - 100, HEIGHT // 2 + 90), 10, "gauge_increase", 1, 10))
label_upgrade = pygame.font.SysFont(None, 42).render("Upgrades", True, (255, 255, 255))
# MAIN GAME LOOP
running = True
while running:
    try:
        clock.tick(FPS)
    except KeyboardInterrupt:
        print("Please close the window to end the program.")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not paused:
        # Update
        if random.random() < 0.01:
           garbage.add(FallingObject(f"assets\\garbage{random.randint(1, 2)}.png", random.uniform(1, 2)))
        if random.random() < 0.001:
           coins.add(FallingObject("assets\\money.png", random.uniform(3, 4)))
        gauge_filler.update()
        garbage.update()
        coins.update()
        if gauge_fill > 0 and gauge_fill < 100:
            text = pygame.font.SysFont(None, 36).render(f"Gauge: {gauge_fill}%, Coins: {coins_collected}, Time: {pygame.time.get_ticks() // 1000}", True, (255, 255, 255))
        store_buttons.update()
    player.update()
    # Draw
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0,0))
    screen.blit(text, (10, 10))
    screen.blit(gauge_filler.image, gauge_filler.rect)
    screen.blit(gauge.image, gauge.rect)
    screen.blit(player.image, player.rect)
    garbage.draw(screen)
    coins.draw(screen)
    store_buttons.draw(screen)
    screen.blit(label_upgrade, (WIDTH - 150, HEIGHT // 2 - 50))
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit(0) # Exit with success status code