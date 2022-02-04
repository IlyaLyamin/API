import pygame
import sys
import os
import requests

# s - спутник
# g - гибрид
# m - карта

                            
def print_window():
    coord = input().split()
    scale = int(input())
    if scale >= 17:
        scale = 17
    elif scale <= 3:
        scale = 3
    pygame.init()
    screen = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Maps API")
    type = "map"
    create_file(coord, scale, screen, type)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEDOWN:
                    scale -= 1
                    if scale <= 3:
                        scale = 3
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_PAGEUP:
                    scale += 1
                    if scale >= 17:
                        scale = 17
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_RIGHT:
                    coord = up_coord_x(coord, scale)
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_LEFT:
                    coord = down_coord_x(coord, scale)
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_UP:
                    coord = up_coord_y(coord, scale)
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_DOWN:
                    coord = down_coord_y(coord, scale)
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_m:
                    type = "map"
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_s:
                    type = "sat"
                    create_file(coord, scale, screen, type)
                elif event.key == pygame.K_g:
                    type = "sat,skl"
                    create_file(coord, scale, screen, type)
        pygame.display.flip()


def create_file(coord, scale, screen, type):
    server = "http://static-maps.yandex.ru/1.x/?"

    params = {"ll": ",".join(coord),
              "z": scale,
              "l": type}

    response = requests.get(server, params=params)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    fon = pygame.image.load(map_file)
    draw_cart(screen, fon)

    os.remove(map_file)


def draw_cart(screen, fon):
    screen.blit(fon, (0, 0))


def up_coord_x(coord, scale):
    x = float(coord[0])
    if scale == 17:
        print("ok")
        x += 0.0043
        if x >= 180.0:
            x = 180.0
    elif scale == 16:
        x += 0.009
        if x >= 180.0:
            x = 180.0
    elif scale == 15:
        x += 0.015
        if x >= 180.0:
            x = 180.0
    elif scale == 14:
        x += 0.025
        if x >= 180.0:
            x = 180.0
    elif scale == 13:
        x += 0.06
        if x >= 180.0:
            x = 180.0
    elif scale == 12:
        x += 0.12
        if x >= 180:
            x = 180
    elif scale == 11:
        x += 0.27
        if x >= 180.0:
            x = 180.0
    elif scale == 10:
        x += 0.5
        if x >= 180.0:
            x = 180.0
    elif scale == 9:
        x += 1.0
        if x >= 180.0:
            x = 180.0
    elif scale == 8:
        x += 1.9
        if x >= 180.0:
            x = 180.0
    elif scale == 7:
        x += 4.5
        if x >= 180.0:
            x = 180.0
    elif scale == 6:
        x += 9.0
        if x >= 180.0:
            x = 180.0
    elif scale == 5:
        x += 18.0
        if x >= 180.0:
            x = 180.0
    elif scale == 4:
        x += 30.0
        if x >= 180.0:
            x = 180.0
    elif scale == 3:
        x += 70.0
        if x >= 180.0:
            x = 180.0
    return f"{str(x)} {coord[1]}".split()


def down_coord_x(coord, scale):
    x = float(coord[0])
    if scale == 17:
        print("ok")
        x -= 0.0043
        if x <= -180.0:
            x = -180.0
    elif scale == 16:
        x -= 0.009
        if x <= -180.0:
            x = -180.0
    elif scale == 15:
        x -= 0.015
        if x <= -180.0:
            x = -180.0
    elif scale == 14:
        x -= 0.025
        if x <= -180.0:
            x = -180.0
    elif scale == 13:
        x -= 0.06
        if x <= -180.0:
            x = -180.0
    elif scale == 12:
        x -= 0.12
        if x <= -180:
            x = -180
    elif scale == 11:
        x -= 0.27
        if x <= -180.0:
            x = -180.0
    elif scale == 10:
        x -= 0.5
        if x <= -180.0:
            x = -180.0
    elif scale == 9:
        x -= 1.0
        if x <= -180.0:
            x = -180.0
    elif scale == 8:
        x -= 1.9
        if x <= -180.0:
            x = -180.0
    elif scale == 7:
        x -= 4.5
        if x <= -180.0:
            x = -180.0
    elif scale == 6:
        x -= 9.0
        if x <= -180.0:
            x = -180.0
    elif scale == 5:
        x -= 18.0
        if x <= -180.0:
            x = -180.0
    elif scale == 4:
        x -= 30.0
        if x <= -180.0:
            x = -180.0
    elif scale == 3:
        x -= 70.0
        if x <= -180.0:
            x = -180.0
    return f"{str(x)} {coord[1]}".split()


def up_coord_y(coord, scale):
    y = float(coord[1])
    if scale == 17:
        print("ok")
        y += 0.0043
        if y >= 80.0:
            y = 80.0
    elif scale == 16:
        y += 0.009
        if y >= 80.0:
            y = 80.0
    elif scale == 15:
        y += 0.015
        if y >= 80.0:
            y = 80.0
    elif scale == 14:
        y += 0.025
        if y >= 80.0:
            y = 80.0
    elif scale == 13:
        y += 0.06
        if y >= 80.0:
            y = 80.0
    elif scale == 12:
        y += 0.12
        if y >= 80:
            y = 80
    elif scale == 11:
        y += 0.27
        if y >= 80.0:
            y = 80.0
    elif scale == 10:
        y += 0.5
        if y >= 80.0:
            y = 80.0
    elif scale == 9:
        y += 1.0
        if y >= 80.0:
            y = 80.0
    elif scale == 8:
        y += 1.9
        if y >= 80.0:
            y = 80.0
    elif scale == 7:
        y += 4.5
        if y >= 80.0:
            y = 80.0
    elif scale == 6:
        y += 9.0
        if y >= 80.0:
            y = 80.0
    elif scale == 5:
        y += 18.0
        if y >= 80.0:
            y = 80.0
    elif scale == 4:
        y += 30.0
        if y >= 80.0:
            y = 80.0
    elif scale == 3:
        y += 70.0
        if y >= 80.0:
            y = 80.0
    return f"{coord[0]} {y}".split()


def down_coord_y(coord, scale):
    y = float(coord[1])
    if scale == 17:
        y -= 0.0043
        if y <= -80.0:
            y = -80.0
    elif scale == 16:
        y -= 0.009
        if y <= -80.0:
            y = -80.0
    elif scale == 15:
        y -= 0.015
        if y <= -80.0:
            y = -80.0
    elif scale == 14:
        y -= 0.025
        if y <= -80.0:
            y = -80.0
    elif scale == 13:
        y -= 0.06
        if y <= -80.0:
            y = -80.0
    elif scale == 12:
        y -= 0.12
        if y <= -80:
            y = -80
    elif scale == 11:
        y -= 0.27
        if y <= -80.0:
            y = -80.0
    elif scale == 10:
        y -= 0.5
        if y <= -80.0:
            y = -80.0
    elif scale == 9:
        y -= 1.0
        if y <= -80.0:
            y = -80.0
    elif scale == 8:
        y -= 1.9
        if y <= -80.0:
            y = -80.0
    elif scale == 7:
        y -= 4.5
        if y <= -80.0:
            y = -80.0
    elif scale == 6:
        y -= 9.0
        if y <= -80.0:
            y = -80.0
    elif scale == 5:
        y -= 18.0
        if y <= -80.0:
            y = -80.0
    elif scale == 4:
        y -= 30.0
        if y <= -80.0:
            y = -80.0
    elif scale == 3:
        y -= 70.0
        if y <= -80.0:
            y = -80.0
    return f"{coord[0]} {y}".split()


print_window()

#55.705758, 150.528071