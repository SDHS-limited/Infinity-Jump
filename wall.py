import pygame

class Wall:
    def __init__(self, x, width=40, height=150):
        self.color = (50, 50, 50)  # 어두운 회색
        self.x = x
        self.width = width
        self.height = height
        self.y = 350 - height  # 바닥 위에 세우기
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, scroll_speed):
        self.x -= scroll_speed
        self.rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)