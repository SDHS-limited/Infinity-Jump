import pygame

class Player:
    def __init__(self):
        self.width, self.height = 40, 40
        self.color = (255, 255, 0)

        # 원본 이미지 저장
        self.original_image = pygame.Surface((self.width, self.height))
        self.original_image.fill(self.color)
        self.image = self.original_image.copy()

        self.rect = self.image.get_rect(midbottom=(100, 350))

        self.gravity = 0.8
        self.velocity = 0
        self.jump_strength = -15
        self.on_ground = True

        self.is_sliding = False
        self.slide_timer = 0

        self.is_flipped = False  # 회전 상태 저장

    def update(self):
        keys = pygame.key.get_pressed()

        # 점프
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity = self.jump_strength
            self.on_ground = False
            self.flip_image()  # 점프할 때 회전 

        # 슬라이드
        if keys[pygame.K_PRINTSCREEN] or keys[pygame.K_HOME]:
            if self.on_ground and not self.is_sliding:
                self.start_slide()

        if self.is_sliding:
            self.slide_timer -= 1
            if self.slide_timer <= 0:
                self.end_slide()

        # 중력 적용
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # 바닥 체크
        if self.rect.bottom >= 350:
            self.rect.bottom = 350
            self.velocity = 0
            self.on_ground = True

    def flip_image(self):
        self.is_flipped = not self.is_flipped
        angle = 180 if self.is_flipped else 0
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def start_slide(self):
        self.is_sliding = True
        self.slide_timer = 20
        self.rect.height = 20

        slide_image = pygame.Surface((self.width, 20))
        slide_image.fill((0, 200, 255))
        self.original_image = slide_image
        self.image = pygame.transform.rotate(self.original_image, 180 if self.is_flipped else 0)
        self.rect = self.image.get_rect(midbottom=(self.rect.centerx, 350))

    def end_slide(self):
        self.is_sliding = False
        self.rect.height = self.height

        self.original_image = pygame.Surface((self.width, self.height))
        self.original_image.fill(self.color)
        self.image = pygame.transform.rotate(self.original_image, 180 if self.is_flipped else 0)
        self.rect = self.image.get_rect(midbottom=(self.rect.centerx, 350))

    def draw(self, screen):
        screen.blit(self.image, self.rect)