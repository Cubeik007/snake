import pygame
import time
from pygame.locals import *
from random import randint

SIZE = 30
TIME = 0.2
START_X = 250
START_Y = 250
LENGTH = 3

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((85, 235, 52))
        self.snake = Snake(self.surface, LENGTH)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.apple.draw()

    def next_move(self):
        self.snake.draw()
        self.apple.draw()

    def check_colision(self):
        if abs(self.snake.x[0] -  self.apple.x) < SIZE and abs(self.snake.y[0] -  self.apple.y) < SIZE:
            self.apple.change_apple()
            self.snake.append_block()

    def pause(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN and event.key == K_p:
                    return 

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RIGHT:
                        #self.snake.move_right()
                        self.snake.direction = "right"
                    if event.key == K_LEFT:
                        #self.snake.move_left()
                        self.snake.direction = "left"
                    if event.key == K_UP:
                        #self.snake.move_up()
                        self.snake.direction = "up"
                    if event.key == K_DOWN:
                        #self.snake.move_down()
                        self.snake.direction = "down"
                    if event.key == K_p:
                            self.pause()
                elif event.type == QUIT:
                    running = False
            #print(self.snake.direction)
            time.sleep(TIME)
            self.check_colision() 
            self.snake.set_direction()  
            self.next_move()
            

        
            

class Snake():
    def __init__(self, parent_screen, length) -> None:
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("images/block.png").convert_alpha()
        self.block = pygame.transform.scale(self.block, (SIZE, SIZE))
        self.x = [START_X-30*k for k in range(length)]
        self.y = [START_Y]*length
        self.direction = None
        self.all_directions = ["right"]*length
        self.speed = SIZE

    def draw(self):
        self.parent_screen.fill((85, 235, 52))
        for k in range(self.length):
            self.parent_screen.blit(self.block, (self.x[k], self.y[k]))
        pygame.display.update()
    
    def move_right(self, block_id):
        self.x[block_id] += self.speed

    def move_left(self, block_id):
        self.x[block_id] -= self.speed

    def move_up(self, block_id):
        self.y[block_id] -= self.speed

    def move_down(self, block_id):
        self.y[block_id] += self.speed

    def set_direction(self):
        print(self.x)
        print(range(self.length))
        for block_id in reversed(range(self.length)):
            print(block_id)
            if block_id == 0:
                self.all_directions[0] = self.direction
            else:
                if block_id == 3:
                    print(self.all_directions[block_id-1])
                self.all_directions[block_id] = self.all_directions[block_id-1]
            if self.all_directions[block_id] == "right":
                self.move_right(block_id)
            if self.all_directions[block_id] == "left":
                self.move_left(block_id)
            if self.all_directions[block_id] == "up":
                self.move_up(block_id)
            if self.all_directions[block_id] == "down":
                self.move_down(block_id)
        print(self.x)

    def append_block(self):
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])
        self.all_directions.append(self.all_directions[-1])

class Apple():
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("images/apple-removebg-preview.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (SIZE, SIZE))
        self.x = 0
        self.y = 0
        
    def change_apple(self):
        #self.parent_screen.fill((85, 235, 52))
        self.x = randint(0, 8)*30
        self.y = randint(0, 8)*30

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.update()



if __name__ == "__main__":
    game = Game()
    game.run()

    

    