import pygame,sys

def draw_floor():
    screen.blit(floor, (floor_x_pos,550))
    screen.blit(floor, (floor_x_pos+432,550))    

pygame.init()
#set fps
clock = pygame.time.Clock()

#hien thi screen x = 432, y= 768
screen = pygame.display.set_mode((432,638))

#set gravity
gravity = 0.25
bird_movement = 0

#load background
bg = pygame.image.load('assets/background-night.png')
#scale full man hinh background
bg = pygame.transform.scale2x(bg)

#tạo sàn, floor
floor = pygame.image.load('assets/floor.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#tạo chim
bird = pygame.image.load('assets/yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100, 319)) #tạo hình chữ nhật cho chim,cách bên trái chiều ngang 100, dọc 1 nửa 639



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            sys.exit()
        if event.type == pygame.KEYDOWN: #event co phim nhan xuong
            if event.key == pygame.K_SPACE:
                bird_movement = 0 #set Y về 0
                bird_movement = -7 #muốn đi lên thì trừ y
    """add nhung thu can thiet len man hinh blit"""       
    screen.blit(bg, (0,0))
    """chay san lien tuc"""
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    """chim trên màn hình"""
    screen.blit(bird, bird_rect)
    bird_movement += gravity #chim càng di chuyển, Y tăng, trọng lực tăng, chim cắm đầu xuống
    bird_rect.centery += bird_movement 

    pygame.display.update()
    #fps 120
    clock.tick(120)