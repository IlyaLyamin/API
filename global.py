import pygame
import sys
import os
import requests

                            
def print_window():
    coord = input().split()
    scale = int(input())
    pygame.init()
    screen = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Maps API")
    create_file(coord, scale, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEDOWN:
                    scale -= 1
                    if scale <= 2:
                        scale = 2
                    create_file(coord, scale, screen)
                elif event.key == pygame.K_PAGEUP:
                    scale += 1
                    if scale >= 17:
                        scale = 17
                    create_file(coord, scale, screen)
                elif event.key == pygame.K_RIGHT:
                    print("ridht")
                    coord = up_coord_x(coord, scale)
                    create_file(coord, scale, screen)
        pygame.display.flip()


def create_file(coord, scale, screen):
    server = "http://static-maps.yandex.ru/1.x/?"
    print(scale)

    params = {"ll": ",".join(coord),
              "z": scale,
              "l": "map"}

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
    elif scale == 
    print(f"{str(x)},{coord[1]}")
    return f"{str(x)} {coord[1]}".split()



print_window()

#55.705758, 37.528071