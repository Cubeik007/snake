import pygame
import time
from pygame.locals import *
from random import randint

SIZE = 30
TIME = 0.3
START_X = 250
START_Y = 250
LENGTH = 3
FIELD_SIZE = 30*20

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((FIELD_SIZE, FIELD_SIZE))
        self.pause_image = pygame.image.load("images/Pause_image-removebg-preview.png").convert_alpha()
        self.gameover_image = pygame.image.load("images/Game_over-removebg-preview.png").convert_alpha()
        self.surface.fill((85, 235, 52))
        self.snake = Snake(self.surface, LENGTH)
        self.apple = Apple(self.surface)
        self.snake.draw()
        self.apple.draw()
        self.time = TIME

    def next_move(self):
        self.snake.draw()
        self.apple.draw()

    def check_colision(self):
        print(self.snake.x[0], self.apple.x, self.snake.y[0], self.apple.y)
        if self.snake.x[0] == self.apple.x and self.snake.y[0] ==  self.apple.y:
            self.apple.change_apple()
            self.snake.append_block()
            self.time *= 0.9
            # print(self.check_if_apple_valid_position())
            while not self.check_if_apple_valid_position():
                self.apple.change_apple()

    def pause(self):
        self.surface.blit(self.pause_image, (20, 20))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN and event.key == K_p:
                    self.surface.fill((85, 235, 52))
                    return True
    
    def check_if_apple_valid_position(self):
        for i in range(self.snake.length):
            print(self.snake.x[i],self.apple.x,self.snake.y[i],self.apple.y)
            if self.snake.x[i] == self.apple.x and self.snake.y[i] == self.apple.y:
                return False
        return True

    def game_over(self):
        self.surface.blit(self.gameover_image, (20, 20))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN and event.key == K_r:
                    self.surface.fill((85, 235, 52))
                    return True


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
            """if self.snake.check_illegal_move:
                self.game_over()"""
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
        self.direction = "right"
        self.speed = SIZE

    def draw(self):
        self.parent_screen.fill((85, 235, 52))
        for k in range(self.length):
            self.parent_screen.blit(self.block, (self.x[k], self.y[k]))
        pygame.display.update()
    
    def move_right(self):
        self.x[0] += self.speed 
        self.x[0] %= FIELD_SIZE

    def move_left(self):
        self.x[0] -= self.speed 
        self.x[0] %= FIELD_SIZE

    def move_up(self):
        self.y[0] -= self.speed 
        self.y[0] %= FIELD_SIZE

    def move_down(self):
        self.y[0] += self.speed
        self.y[0] %= FIELD_SIZE

    def set_direction(self):
        for block_id in reversed(range(self.length)):
            if block_id == 0:
                if self.direction == "right":
                    self.move_right()
                if self.direction == "left":
                    self.move_left()
                if self.direction == "up":
                    self.move_up()
                if self.direction == "down":
                    self.move_down()
            else:
                self.x[block_id]=self.x[block_id-1]
                self.y[block_id]=self.y[block_id-1]

    def append_block(self):
        self.length += 1
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

    def check_illegal_move(self):
        for i in range(1, self.length):
            return self.x[0] == self.x[i] and self.y[0] == self.y[i]

class Apple():
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("images/apple-removebg-preview.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (SIZE, SIZE))
        self.x = 10
        self.y = 10
        
    def change_apple(self):
        #self.parent_screen.fill((85, 235, 52))
        self.x = randint(0, 8)*30+10
        self.y = randint(0, 8)*30+10

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.update()



if __name__ == "__main__":
    game = Game()
    game.run()

    

    