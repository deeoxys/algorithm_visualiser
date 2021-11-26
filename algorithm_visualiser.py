# sorting algorithm visualiser, like the ones you see on youtube
# TODO add sound effects
# TODO highlight blocks at indexes being read/written to
# TODO add lots of different algorithms

import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time

from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_r,
    K_q,
    K_ESCAPE,
)

name = "Algorithm Visualiser"
screen_width = 1200
screen_height = 600
running = True
operations = 0

pygame.init()
pygame.font.init()
pygame.display.set_caption(name)

font = pygame.font.SysFont("Verdana", 16)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

debug = False
block_width = 10
# block_height = 30 # TODO implement block height variable
delay = 0
fps = 30

# get command line arguments
for i in range(1, len(sys.argv)):
    if sys.argv[i] == "--debug":
        debug = True
        print("Debug mode enabled")
    elif sys.argv[i].__contains__("-w"):
        try:
            block_width = int(sys.argv[i].strip("-w"))
            if (debug):
                print("Block width: " + str(block_width))
        except:
            pass
    elif sys.argv[i].__contains__("-fps"):
        try:
            fps = int(sys.argv[i].strip("-fps"))
            if (debug):
                print("FPS: " + str(fps))
        except:
            pass

class Block(pygame.sprite.Sprite):  # block object used for rendering
    def __init__(self, pos, size):
        super(Block, self).__init__()
        self.pos = pos
        self.size = size
        
        self.surf = pygame.Surface((block_width, size * 30))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = ((pos + 1) * block_width, (screen_height) - (size * 10)))

def render(list):
    screen.fill((30, 30, 30))   # background
    positions = [0] # positions to render blocks at (so they dont overlap)
    
    for i in range(1, len(list)):
        positions.append(i * (block_width + 5)) # blocks are 30px wide and we want a 5px gap between each of them
    
    k = 1
    for item in list:
        block = Block(k, item)
        r = pygame.Rect.copy(block.rect)
        r.update(positions[k - 1], block.rect.top, 30, block.rect.height)
        screen.blit(block.surf, r)  # actual render
        k += 1
    
    text = font.render("Operations: " + str(operations), False, (255, 255, 255))
    screen.blit(text, (1, 0))   # render operations counter
    
    pygame.display.flip()   # show frame on screen

def randomise():
    global operations   # access and set global operations variable to 0
    operations = 0
    
    temp = []
    for i in range(screen_width // (block_width + 5)):
        temp.append(random.randint(1, screen_height / 30))
    return temp

def bubbleSort(list):
    for i in range(len(list)- 1):
        swapped = False
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:   # sleep so that we get a nice slow animation, rather than all at once
                temp = list[j]
                # render, increment operations, print if debug
                render(list)
                time.sleep(delay)
                global operations
                operations += 1
                if (debug): print(list)
                #
                list[j] = list[j + 1]
                list[j + 1] = temp
                swapped = True
        if (swapped == False):
            break
    return list

list = randomise()
while running:
    clock = pygame.time.Clock()
    clock.tick(fps)
    render(list)
    
    input = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                pygame.quit()
            elif event.key == K_SPACE:
                list = bubbleSort(list)
            elif event.key == K_r:
                list = randomise()
pygame.quit()
