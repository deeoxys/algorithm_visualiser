# r333mo's Sorting algorithm visualiser, like the ones you see on youtube
# TODO add sound effects
# TODO highlight blocks at indexes being read/written to
# TODO add lots of different algorithms

import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from numpy import random
import time

from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_b,
    K_g,
    K_i,
    K_r,
    K_s,
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
gap = 5
automate = False
debug = False
block_width = 10
block_height = 1
fps = 60

pygame.init()
pygame.font.init()
pygame.display.set_caption(name)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

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

def render(list):
    screen.fill((30, 30, 30))   # background
    
    for i in range(1, len(list)):
        pygame.draw.rect(screen, (255, 255, 255), (i * (block_width + gap), screen_height - (list[i] * block_height), (block_width), (list[i] * block_height)))
    
    pygame.display.set_caption(name + " - " + status + " - " + str(arr_size) + " items - " + str(operations) + " Operations")
    pygame.display.update()   # show frame on screen

def randomise():
    global status
    status = "Randomising"
    if (automate and debug): print(status)
    global operations   # access and set global operations variable to 0
    operations = 0
    
    temp = []
    for i in range(screen_width // (block_width + gap)):
        temp.append(random.randint(1, screen_height // block_height))
        render(temp)
    
    global arr_size
    arr_size = len(temp)
    
    status = "Idle"
    return temp#, blocks_temp

def head(status_):
    if (debug): print(list)
    global status
    status = status_
    if (debug): print(status)
    
def core():
    # render, increment operations, print if debug
    render(list)
    global operations
    operations += 1
    #
    

def tail():
    if (debug): print(list)

def bubbleSort(list):
    ######
    head("Bubble Sort")
    ######
    for i in range(len(list)- 1):
        swapped = False
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
                swapped = True
                ######
                core()
                ######
        if (swapped == False):
            break
    ######
    tail()
    ######
    return list

def insertionSort(list):
    ######
    head("Insertion Sort")
    ######
    pos = 0
    valueToInsert = 0
    for i in range(len(list)):
        valueToInsert = list[i]
        pos = i
        while pos > 0 and list[pos - 1] > valueToInsert:
            list[pos] = list[pos - 1]
            pos = pos - 1
            ######
            core()
            ######
        list[pos] = valueToInsert
    ######
    tail()
    ######
    return list

def selectionSort(list):
    ######
    head("Selection Sort")
    ######
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
                ######
                core()
                ######
        list[i], list[min] = list[min], list[i]
    ######
    tail()
    ######
    return list

def gnomeSort(list):
    ######
    head("Gnome Sort")
    ######
    index = 0
    n = len(list)
    while index < n:
        if index == 0:
            index = index + 1
        if list[index] >= list[index - 1]:
            index = index + 1
        else:
            list[index], list[index-1] = list[index-1], list[index]
            index = index - 1
        #######
        core()
        ######
    #####
    tail()
    ######
    return list

list = randomise()
while running:
    clock = pygame.time.Clock()
    clock.tick(fps)
    screen_width, screen_height = pygame.display.get_surface().get_size()
    render(list)
    
    if (automate):
        time.sleep(1)
        list = selectionSort(list)
        time.sleep(1)
        list = randomise()
        time.sleep(1)
        list = gnomeSort(list)
        time.sleep(1)
        list = randomise()
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
            
            if not automate:
                if event.key == K_b and not automate:
                    list = bubbleSort(list)
                elif event.key == K_i and not automate:
                    list = insertionSort(list)
                elif event.key == K_g and not automate:
                    list = gnomeSort(list)
                elif event.key == K_s and not automate:
                    list = selectionSort(list)
                elif event.key == K_r and not automate:
                    list = randomise()
pygame.quit()
