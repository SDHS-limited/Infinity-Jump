import pygame
import sys
from player import Player
from obstacle import Obstacle
from wall import Wall
import random

pygame.init()
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
width = pygame.display.set_caption("Infinite jump")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 60)
FPS = 60


player = Player()
obstacles = []
wall = []
SCROLL_SPEED = 5     
SPEED_INCREMENT = 1
speed_level = 0
SPAWN_TIMER = 0
SPAWN_INTERVAL = 60  # 프레임마다 장애물 생성
score = 0
Bestscore = 0
font = pygame.font.SysFont(None, 36)

game_over = False

# 게임 초기화 함수
def reset_game():
    global player, obstacles, game_over, SPAWN_TIMER, score
    player = Player()
    obstacles = []
    SPAWN_TIMER = 0
    game_over = False
    score = 0
    Bestscore = 0

while True:
    screen.fill((0, 150, 255))  # 파란색 배경

    pygame.draw.rect(screen, (100, 100, 100), (0, 350, 800, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        player.update()

        # 장애물 생성
        SPAWN_TIMER += 1
        if SPAWN_TIMER >= SPAWN_INTERVAL:
            SPAWN_TIMER = 0
            new_obs = Obstacle(WIDTH + random.randint(0, 200))
            obstacles.append(new_obs)

        for obs in obstacles[:]:
            obs.update(SCROLL_SPEED)
            if obs.rect.right < 0:
                obstacles.remove(obs)

            # 점수 조건: 플레이어가 장애물 완전히 넘었을 때
            if not hasattr(obs, 'scored'):
                obs.scored = False

            if not obs.scored and obs.rect.right < player.rect.left:
                score += 100
                obs.scored = True                

            if score >= Bestscore:
                Bestscore = score
            
            if score >= (speed_level + 1) * 1000:
                speed_level += 1
                SCROLL_SPEED += speed_level
                if SCROLL_SPEED >= 8:
                    SCROLL_SPEED = 8

            if player.rect.colliderect(obs.rect):
                game_over = True
                #파티클 추가
    else:
        if keys[pygame.K_r]:
            SCROLL_SPEED = 5
            reset_game()

    # 그리기
    player.draw(screen)
    for obs in obstacles:
        obs.draw(screen)

    if game_over:
        text = FONT.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - 310, HEIGHT//2 - 60))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    Bestscore_text = font.render(f"Best Score: {Bestscore}", True, (255, 255, 255))
    screen.blit(Bestscore_text, (10, 50))

    pygame.display.update()
    clock.tick(60)