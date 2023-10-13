import pygame, sys

pygame.init()
# Screen
size = width, height = 1024, 600
screen = pygame.display.set_mode(size)

# Variable
    # Color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
    # Player dimensions
dimen_p_w = 10
dimen_p_h = 150
    # Ball dimension
radio_ball = 20
    # Position players
pos_p1_y, pos_p2_y = 100, 100
pos_ball_x, pos_ball_y = width//2, height//2
    # Speed
speed_players = 2
speed_ball_x, speed_ball_y = 1,1
    # Score
score_p1 = 0
score_p2 = 0
score_win = 5
winner = ''

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): sys.exit()

    # Logic
        # Control player1
    if (pygame.key.get_pressed()[pygame.K_w]): pos_p1_y -= speed_players
    if (pygame.key.get_pressed()[pygame.K_s]): pos_p1_y += speed_players
        # Control player2
    if (pygame.key.get_pressed()[pygame.K_UP]): pos_p2_y -= speed_players
    if (pygame.key.get_pressed()[pygame.K_DOWN]): pos_p2_y += speed_players
        # Move ball
    pos_ball_x += speed_ball_x
    pos_ball_y += speed_ball_y

        # Limit players
            # players
    if (pos_p1_y >= (height-dimen_p_h) ): pos_p1_y -= speed_players
    if (pos_p1_y < 0): pos_p1_y += speed_players
    if (pos_p2_y >= (height-dimen_p_h) ): pos_p2_y -= speed_players
    if (pos_p2_y < 0): pos_p2_y += speed_players
            # ball
    if (pos_ball_y >= height or pos_ball_y < 0 ): speed_ball_y *= -1
    if (pos_ball_x >= width or pos_ball_x < 0 ): 
        # Score
        if (pos_ball_x >= width): score_p1 += 1; print("player1: ", score_p1)
        if (pos_ball_x < 0): score_p2 += 1; print("player2: ", score_p2)
        pos_ball_x = width//2
        pos_ball_y = height//2
        speed_ball_x *= -1
        # Winner
    if(score_p1 == score_win or score_p2 == score_win):
        if(score_p1 == score_win): winner = 'Player 1 winner!!!'
        if(score_p2 == score_win): winner = 'Player 2 winner!!!'

    # Graphic
    screen.fill(BLACK)
    if(len(winner)==0):   
            # Font
        Font_score = pygame.font.SysFont('Corbel', height//8)
            # PLayer1
        text_p1 = Font_score.render(str(score_p1),True, WHITE)
        post_text_p1_x = width//4
        post_text_p1_y = height//10
        screen.blit(text_p1, (post_text_p1_x, post_text_p1_y))
            # PLayer2
        text_p2 = Font_score.render(str(score_p2),True, WHITE)
        post_text_p2_x = width - width//4
        post_text_p2_y = height//10
        screen.blit(text_p2, (post_text_p2_x, post_text_p2_y))

            # Players
        rect_player1 = pygame.draw.rect(screen,WHITE,(10,pos_p1_y,dimen_p_w,dimen_p_h))
        rect_player2 = pygame.draw.rect(screen,WHITE,(width-20,pos_p2_y,dimen_p_w,dimen_p_h))
            # Ball
        circl_ball = pygame.draw.circle(screen, RED, (pos_ball_x, pos_ball_y), radio_ball)
            # Line
        pygame.draw.rect(screen,WHITE,(width//2, 0, 2,height))
            # Collision
        if(rect_player1.colliderect(circl_ball) or rect_player2.colliderect(circl_ball)):  speed_ball_x *= -1
    else:
        Font_winner = pygame.font.SysFont('Corbel', height//5)
        text_winner = Font_winner.render(winner,True, WHITE)
        post_text_winner_x = width//2 - text_winner.get_width()//2
        post_text_winner_y = height//2 - text_winner.get_height()//2
        screen.blit(text_winner, (post_text_winner_x, post_text_winner_y))
        pos_ball_x, pos_ball_y = 0,0

    pygame.display.flip()