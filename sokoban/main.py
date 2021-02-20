import pygame

pygame.init()

# N & M :number of x and y tiles on board

N = 11
M = 7

# screen creation

screen = pygame.display.set_mode((N * 64, M * 64))

# Title and icon/ icon nie wiem czemu nie dziala

pygame.display.set_caption("Gra Macieja")
icon = pygame.image.load("32bitbox.png")
pygame.display.set_icon(icon)

# Clock

clock = pygame.time.Clock()

# Player

playerImg = pygame.image.load("64bitplayer.png").convert()
playerX = 64
playerY = 64
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Objects

wall = pygame.image.load("64bitwall.png").convert()
box = pygame.image.load("64bitbox.png").convert()
exit_image = pygame.image.load("64bitexit.png").convert()

# Level

def level_to_matrix(file_path: str):
    with open(file_path, 'r') as lvl:
        level_matrix = []
        for line in lvl:
            level_line = []
            for char in line:
                level_line.append(char)
            level_matrix.append(level_line)
    return level_matrix

def open_level(matrix):
    non_moveable = []
    moveable = []
    exit_cord = []
    for idx_y, line in enumerate(matrix):
        for idx_x, char in enumerate(line):
            if char == '#':
                screen.blit(wall, (idx_x * 64, idx_y * 64))
                non_moveable.append((idx_x * 64, idx_y * 64))
            if char == 'X':
                screen.blit(box, (idx_x * 64, idx_y * 64))
                moveable.append((idx_x * 64, idx_y * 64))
            if char == '*':
                screen.blit(exit_image, (idx_x * 64, idx_y * 64))
                non_moveable.append((idx_x * 64, idx_y * 64))
                exit_cord.append((idx_x * 64, idx_y * 64))
    return moveable, non_moveable, exit_cord
            
lvl_matrix = level_to_matrix("/home/maciek/Desktop/projects/python game/level2.txt")

# Game Over

font = pygame.font.SysFont("comicsansms", 72)

def Game_Over():
    screen.fill((0, 0, 0))
    victory = font.render('DUPA', True, (255, 255, 255))
    screen.blit(victory, ((N - 2.5) / 2 * 64, M / 2 * 64))
    return (((N + 1) * 64), ((M + 1) * 64))

# Game loop

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -64
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerY_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 64
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerY_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -64
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 64
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= (N - 1) * 64:
        playerX = (N - 1) * 64

    if playerY <= 0:
        playerY = 0
    elif playerY >= (M - 1) * 64:
        playerY = (M - 1) * 64

    move, non_move, ex_cord = open_level(lvl_matrix)

    if (playerX, playerY) in ex_cord:
        (playerX, playerY) = Game_Over()
        running = False
    
    if (playerX, playerY) in non_move:
        playerX -= playerX_change
        playerY -= playerY_change

    if (playerX, playerY) in move:
        behind_box_X = playerX + playerX_change
        behind_box_Y = playerY + playerY_change
        if (behind_box_X, behind_box_Y) in non_move or (behind_box_X, behind_box_Y) in move:
            playerX -= playerX_change
            playerY -= playerY_change
        else:
            playerX_ind = int(playerX / 64)
            playerY_ind = int(playerY / 64)
            if playerX_change > 0:
                lvl_matrix[playerY_ind][playerX_ind], lvl_matrix[playerY_ind][playerX_ind + 1] = lvl_matrix[playerY_ind][playerX_ind + 1], lvl_matrix[playerY_ind][playerX_ind]
            if playerX_change < 0:
                lvl_matrix[playerY_ind][playerX_ind], lvl_matrix[playerY_ind][playerX_ind -1] = lvl_matrix[playerY_ind][playerX_ind - 1], lvl_matrix[playerY_ind][playerX_ind]
            if playerY_change > 0:
                lvl_matrix[playerY_ind][playerX_ind], lvl_matrix[playerY_ind + 1][playerX_ind] = lvl_matrix[playerY_ind + 1][playerX_ind], lvl_matrix[playerY_ind][playerX_ind]
            if playerY_change < 0:
                lvl_matrix[playerY_ind][playerX_ind], lvl_matrix[playerY_ind - 1][playerX_ind] = lvl_matrix[playerY_ind - 1][playerX_ind], lvl_matrix[playerY_ind][playerX_ind]
    
    player(playerX, playerY)
    pygame.display.update()
    clock.tick(5)
