import pygame

class Obstacle:
    def __init__(self, x):
        self.width = 40
        self.height = 60
        self.x = x
        self.y = 350  # 바닥
        self.color = (255, 0, 0)

        # 충돌 판정을 위한 Rect
        self.rect = pygame.Rect(self.x, self.y - self.height, self.width, self.height)

    def update(self, scroll_speed):
        self.x -= scroll_speed
        self.rect.x = self.x

    def draw(self, screen):
        # 꼭짓점 3개 좌표
        top = (self.x + self.width // 2, self.y - self.height)  # 위 꼭짓점
        left = (self.x, self.y)  # 왼쪽 아래
        right = (self.x + self.width, self.y)  # 오른쪽 아래

        pygame.draw.polygon(screen, self.color, [top, left, right])