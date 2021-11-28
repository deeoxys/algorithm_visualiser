# r333mo's Sorting algorithm visualiser, like the ones you see on youtube
# TODO add sound effects
# TODO highlight blocks at indexes being read/written to
# TODO add lots of different algorithms

import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
# import random
from numpy import random
import time

from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_b,
    K_i,
    K_r,
    K_q,
    K_ESCAPE,
)

name = "Algorithm Visualiser"
screen_width = 1200
screen_height = 600
running = True
operations = 0
status = "Idle"
arr_size = 30

automate = False
gap = 5

pygame.init()
pygame.font.init()
pygame.display.set_caption(name)

# font = pygame.font.SysFont("Monospace", 16)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

list = []
blocks = []

debug = False
block_width = 10
block_height = 1
# delay = 0
fps = 30

for i in range(1, len(sys.argv)):
    if sys.argv[i] == "--debug":
        debug = True
        print("Debug mode enabled")
    elif sys.argv[i] == "--automate":
        automate = True
        print("Automate mode enabled")
    elif sys.argv[i].__contains__("-w"):
        try:
            block_width = int(sys.argv[i].strip("-w")) + 1  # we dont want to set to zero
            if (debug):
                print("Block width: " + str(block_width))
        except:
            pass
    elif sys.argv[i].__contains__("-h"):
        try:
            block_height = int(sys.argv[i].strip("-h")) + 1
            if (debug):
                print("Block height: " + str(block_height))
        except:
            pass
    elif sys.argv[i].__contains__("-fps"):
        try:
            fps = int(sys.argv[i].strip("-fps"))
            if (debug):
                print("FPS: " + str(fps))
        except:
            pass
    elif sys.argv[i].__contains__("-g"):
        try:
            gap = int(sys.argv[i].strip("-g"))
            if (debug):
                print("Gap: " + str(gap))
        except:
            pass

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super(Block, self).__init__()
        self.pos = pos
        self.size = size
        self.surf = pygame.Surface((block_width, size * block_height))
        self.surf.fill((220, 220, 220))
        self.rect = self.surf.get_rect(center = ((pos + 1) * block_width, (screen_height) - (size * block_height)))

def render(list):
    screen.fill((30, 30, 30))   # background
    
    for i in range(1, len(list)):
        block = Block(i, list[i])   # this line is FAR TOO inefficient.. FIND A SOLUTION!!!!
        screen.blit(block.surf, pygame.Rect(i * (block_width + gap), screen_height - block.rect.height, block_height * list[i], block.rect.height))
    
    # self.rect = self.surf.get_rect(center = ((pos + 1) * block_width, (screen_height) - (size * block_height)))
    # for i in range(len(blocks)):
    #             screen.blit(blocks[i].surf, pygame.Rect(i * (block_width + gap), screen_height - blocks[i].rect.height, block_height * list[i], blocks[i].rect.height))
    
    # text = font.render("Operations: " + str(operations), False, (255, 255, 255))
    # screen.blit(text, (1, 0))   # render operations counter
    # text = font.render("Status: " + status, False, (255, 255, 255))
    # screen.blit(text, (1, text.get_height()))   # render status
    
    pygame.display.set_caption(name + " - " + status + " - " + str(arr_size) + " items - " + str(operations) + " Operations")
    pygame.display.flip()   # show frame on screen

def randomise():
    global status
    status = "Randomising"
    if (automate and debug): print(status)
    global operations   # access and set global operations variable to 0
    operations = 0
    
    temp = []
    # blocks_temp = []
    for i in range(screen_width // (block_width + gap)):
        temp.append(random.randint(1, screen_height // block_height))
        # block = Block(i, temp[i])
        # blocks_temp.append(block)
        render(temp)
    
    # temp = random.randint(low=(1), high=(screen_height // block_height), size=(screen_width // (block_width + gap)))
    
    # for i in range(screen_width // (block_width + gap), 0, -1):
    #     render(temp)
    #     temp.append(i)
    
    global arr_size
    arr_size = len(temp)
    
    status = "Idle"
    return temp#, blocks_temp

def bubbleSort(list):
    if (debug): print(list)
    global status
    status = "Bubble Sort"
    if (automate and debug): print(status)
    for i in range(len(list)- 1):
        swapped = False
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                # render, increment operations, print if debug
                render(list)
                # time.sleep(delay)
                global operations
                operations += 1
                #
                list[j] = list[j + 1]
                list[j + 1] = temp
                swapped = True
        if (swapped == False):
            break
    if (debug): print(list)
    return list

def insertionSort(list):
    if (debug): print(list)
    global status
    status = "Insertion Sort"
    if (automate and debug): print(status)
    pos = 0
    valueToInsert = 0
    for i in range(len(list)):
        valueToInsert = list[i]
        pos = i
        while pos > 0 and list[pos - 1] > valueToInsert:
            # render, increment operations, print if debug
            render(list)
            # time.sleep(delay)
            global operations
            operations += 1
            #
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = valueToInsert
    if (debug): print(list)
    return list

list = randomise()
# list, blocks = randomise()
while running:
    clock = pygame.time.Clock()
    clock.tick(fps)
    screen_width, screen_height = pygame.display.get_surface().get_size()
    
    # print("hello world")
    render(list)
    
    if (automate):
        time.sleep(1)
        list = bubbleSort(list)
        time.sleep(1)
        list = randomise()
        time.sleep(1)
        list = insertionSort(list)
        time.sleep(1)
        list = randomise()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                pygame.quit()
            elif event.key == K_b and not automate:
                list = bubbleSort(list)
            elif event.key == K_i and not automate:
                list = insertionSort(list)
            elif event.key == K_r and not automate:
                list = randomise()
pygame.quit()
