import pygame
import tkinter
import random
BLUE = (135, 206 , 250)
BLACK = (0, 0, 0)
block_size = 50
left_margin = 200
upper_margin = 200
size = (left_margin + 15*block_size, upper_margin+15*block_size)
pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Морской бой")

font_size = int(block_size//1.5)
font = pygame.font.SysFont('notosans', font_size)

def draw_grid():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for y in range(11):
        for x in range(11):
            # Первое поле
            pygame.draw.line(screen, BLACK, (left_margin,upper_margin+y*block_size), (left_margin+10*block_size, upper_margin+y*block_size), 1)
            pygame.draw.line(screen, BLACK, (left_margin+x*block_size, upper_margin),(left_margin+x*block_size, upper_margin+10*block_size), 1)
        if y < 10:
            num_vert = font.render(str(y+1), True, BLACK)
            letters_hor = font.render(letters[y], True, BLACK)

            num_vert_width = num_vert.get_width()
            num_vert_height = num_vert.get_height()
            letters_hor_witdth = letters_hor.get_width()

            #Вертикальные цифры, первой сетки
            screen.blit(num_vert, (left_margin - (block_size//2+num_vert_width//2), upper_margin +y*block_size + (block_size//2 - num_vert_height//2)))
            #Буквы первой сетки
            screen.blit(letters_hor, (left_margin + y*block_size+ (block_size//2 - letters_hor_witdth//2), upper_margin + (-1*block_size)))

def main():
    game_over = False
    screen.fill(BLUE)
    while not game_over:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                game_over = True
        pygame.display.update()
        draw_grid()
main()
pygame.quit()
