import os
import sys
import pygame
import requests

plus = pygame.image.load('plus.png')
plus.set_colorkey((255, 255, 255))

minus = pygame.image.load('minus.png')
minus.set_colorkey((255, 255, 255))

z = 4

nx = '133.795384'
ny = '-25.694768'

f = open('coordinates.txt')
for n, i in enumerate(f):
    if n == 0:
        nx = i.strip('\n')
    else:
        ny = i.strip('\n')
map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l=sat"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
g_l_r = plus.get_rect(
        topleft=(550, 0))
screen.blit(plus, g_l_r)
g_l_r = minus.get_rect(
        topleft=(550, 400))
screen.blit(minus, g_l_r)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if x > 550:
                if y > 400:
                    z -= 1
                    if z < 0:
                        z = 0
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l=sat"
                    response = requests.get(map_request)
                    if not response:
                        print("Ошибка выполнения запроса:")
                        print(map_request)
                        print("Http статус:", response.status_code, "(", response.reason, ")")
                        sys.exit(1)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    g_l_r = plus.get_rect(
                            topleft=(550, 0))
                    screen.blit(plus, g_l_r)
                    g_l_r = minus.get_rect(
                            topleft=(550, 400))
                    screen.blit(minus, g_l_r)
                    pygame.display.flip()
                if y < 50:
                    z += 1
                    if z > 17:
                        z = 17
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l=sat"
                    response = requests.get(map_request)
                    if not response:
                        print("Ошибка выполнения запроса:")
                        print(map_request)
                        print("Http статус:", response.status_code, "(", response.reason, ")")
                        sys.exit(1)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    g_l_r = plus.get_rect(
                            topleft=(550, 0))
                    screen.blit(plus, g_l_r)
                    g_l_r = minus.get_rect(
                            topleft=(550, 400))
                    screen.blit(minus, g_l_r)
                    pygame.display.flip()
            elif x < 50 and y < 50:
                running = False
                import coords
        pygame.display.flip()

pygame.quit()
os.remove(map_file)
