import os
import sys
import pygame
import requests

plus = pygame.image.load('plus.png')
plus.set_colorkey((255, 255, 255))

minus = pygame.image.load('minus.png')
minus.set_colorkey((255, 255, 255))

z = 4
nx, ny = '', ''
f = open('coordinates.txt')
for n, i in enumerate(f):
    if n == 0:
        nx = i.strip('\n')
    else:
        ny = i.strip('\n')
f.close()
type_obj = ['map', 'sat', 'skl']
type_ind = 0
map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                z += 1
                if z > 17:
                    z = 17
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
            elif event.key == pygame.K_PAGEDOWN:
                z -= 1
                if z < 0:
                    z = 0
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
            if event.key == pygame.K_LEFT:
                nnx = float(nx)
                if nnx > -180:
                    nnx -= 0.1
                nx = str(nnx)
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
            if event.key == pygame.K_RIGHT:
                nnx = float(nx)
                if nnx < 180:
                    nnx += 0.1
                nx = str(nnx)
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
            if event.key == pygame.K_DOWN:
                nny = float(ny)
                if nny > -180:
                    nny -= 0.1
                ny = str(nny)
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
            if event.key == pygame.K_UP:
                nny = float(ny)
                if nny < 180:
                    nny += 0.1
                ny = str(nny)
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if x > 550:
                if y > 400:
                    z -= 1
                    if z < 0:
                        z = 0
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
            elif x < 50 and y > 400:
                type_ind += 1
                if type_ind == 3:
                    type_ind = 0
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={nx}%2C{ny}&z={z}&l={type_obj[type_ind]}"
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
        pygame.draw.circle(screen, (255, 0, 0),(25, 25), 25)
        pygame.draw.circle(screen, (0, 255, 0),(25, 425), 25)
        pygame.display.flip()

