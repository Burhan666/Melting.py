from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

import time
import messagebox
from PIL import Image, ImageGrab
import random
import pygame
messagebox.showinfo("Melting", "L BOZO YOU JUST GOT YOUR PC MELTED")

time.sleep(3)
desktop_image = ImageGrab.grab()

clock = pygame.time.Clock()

pygame.init()
w, h = desktop_image.width, desktop_image.height

def pilImageToSurface(pilImage):
    i = pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
    return pygame.transform.scale(i, (1920, 1080))

def manipulate(image: Image.Image):
    random_column = random.randint(0, image.width)
    copied = image.crop((random_column, 0, random_column + random.randint(20, 40), image.height))
    image.paste(copied, (random_column, random.randint(5, 10)))

sc = pygame.display.set_mode((w, h))
pygame.mouse.set_visible(False)

image = desktop_image
t = 0
pg_mg = pilImageToSurface(image)
while 1:
    for ev in pygame.event.get():
        pass
    sc.blit(pg_mg, (0, 0))
    if t % 2:
        manipulate(image)
        pg_mg = pilImageToSurface(image)
    pygame.display.update()
    clock.tick(60)
    t += 1