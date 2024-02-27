import pygame, random, os
PATH = os.path.abspath('.')+'/'
pygame.init()
screen = pygame.display.set_mode((400, 400))
ball_size = (200, 200)
ball = pygame.transform.scale(pygame.image.load(PATH+'ball.png').convert_alpha(), ball_size)
current_color = (255, 0, 0)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_color = random.sample(range(0, 256), 3)
    screen.fill(current_color)
    screen.blit(ball, (screen.get_width()//2-ball_size[0]//2, screen.get_height()//2-ball_size[1]//2))
    pygame.display.flip()
pygame.quit()
