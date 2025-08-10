import pygame
import numpy as np
import random

pygame.init()

# 基礎設置
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("多樣化煙火效果")
clock = pygame.time.Clock()

# 粒子基類


class FireworkParticle:
    def __init__(self, pos, color, velocity=None, lifetime=None, size=None):
        self.pos = pos.copy()  # 粒子位置
        self.color = color
        self.velocity = velocity if velocity else [
            random.uniform(-3, 3), random.uniform(-3, 3)]
        self.lifetime = lifetime if lifetime else random.randint(30, 60)
        self.size = size if size else random.randint(2, 5)

    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.velocity[1] += 0.05  # 重力效果
        self.lifetime -= 1
        self.size = max(self.size - 0.1, 1)

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(
                self.pos[0]), int(self.pos[1])), int(self.size))

# 煙火基類


class Firework:
    def __init__(self):
        self.color = random.choice([
            (255, 0, 0), (255, 100, 100), (255, 200, 200),
            (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)
        ])
        self.pos = [random.randint(200, SCREEN_WIDTH - 200), SCREEN_HEIGHT]
        self.velocity = random.uniform(-8, -15)
        self.particles = []
        self.exploded = False

    def update(self):
        if not self.exploded:
            self.pos[1] += self.velocity
            self.velocity += 0.2  # 重力加速度
            if self.velocity >= 0:
                self.exploded = True
                self.create_particles()
        else:
            for particle in self.particles:
                particle.update()
            self.particles = [p for p in self.particles if p.lifetime > 0]

    def create_particles(self):
        pass  # 由子類別實現

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, self.color,
                               (int(self.pos[0]), int(self.pos[1])), 5)
        else:
            for particle in self.particles:
                particle.draw(screen)

# 愛心煙火類別


class HeartFirework(Firework):
    def __init__(self):
        super().__init__()
        # 愛心公式
        self.t = np.linspace(0, 2 * np.pi, 1000)
        self.x = 16 * np.sin(self.t) ** 3 * 30  # 調整愛心大小
        self.y = (13 * np.cos(self.t) - 5 * np.cos(2 * self.t) -
                  2 * np.cos(3 * self.t) - np.cos(4 * self.t)) * 30

    def create_particles(self):
        for xi, yi in zip(self.x, self.y):
            px = self.pos[0] + xi
            py = self.pos[1] - yi
            self.particles.append(FireworkParticle([px, py], self.color))

# 星形煙火類別（示例，可擴展更多）


class StarFirework(Firework):
    def __init__(self):
        super().__init__()
        # 星形公式
        self.t = np.linspace(0, 2 * np.pi, 1000)
        self.x = 50 * np.cos(self.t)
        self.y = 50 * np.sin(self.t)

    def create_particles(self):
        for angle in range(0, 360, 5):
            rad = np.radians(angle)
            px = self.pos[0] + 100 * np.cos(rad)
            py = self.pos[1] + 100 * np.sin(rad)
            velocity = [random.uniform(-3, 3), random.uniform(-3, 3)]
            self.particles.append(FireworkParticle(
                [px, py], self.color, velocity=velocity, lifetime=60, size=3))


class RectangleFirework(Firework):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 50

    def create_particles(self):
        for i in range(-self.width, self.width, 10):
            for j in range(-self.height, self.height, 10):
                px = self.pos[0] + i
                py = self.pos[1] + j
                velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]
                self.particles.append(FireworkParticle(
                    [px, py], self.color, velocity=velocity, lifetime=60, size=3))


# 煙火工廠


class FireworkFactory:
    @staticmethod
    def create_firework():
        types = [HeartFirework, StarFirework, RectangleFirework]  # 添加新的類別
        firework_class = random.choice(types)
        return firework_class()

# 主循環


MAX_FPS = 30  # 控制更新頻率的最大幀率


def main():
    running = True
    fireworks = []
    text_alpha = 0
    alpha_increment = 1
    show_text = False
    text_display_time = 180
    frames = 0

    while running:
        screen.fill((0, 0, 0))  # 背景黑色

        # 隨機生成煙火
        if random.randint(1, 15) == 1:
            fireworks.append(FireworkFactory.create_firework())
            show_text = True
        if frames % (60 // MAX_FPS) == 0:
            # 更新並繪製煙火
            for firework in fireworks:
                firework.update()
                firework.draw(screen)

            # 控制文字顯示
            if show_text:
                text_alpha = min(255, text_alpha + alpha_increment)
                frames += 1
                if frames > text_display_time:
                    show_text = False
                    frames = 0
                    text_alpha = 0

            # 繪製文字
            font = pygame.font.Font(None, 200)
            text = font.render("I love you", True, (255, 0, 0))
            text.set_alpha(text_alpha)
            text_rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

            # 刷新畫面
            pygame.display.flip()
            clock.tick(60)

            # 移除已消失的煙火
            fireworks = [fw for fw in fireworks if not (
                fw.exploded and len(fw.particles) == 0)]

            # 事件處理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        # 控制幀率
        clock.tick(60)
        frames += 1
    pygame.quit()


if __name__ == "__main__":
    main()

# refernce : https://github.com/pinyou123/Love-Firework/blob/main/love%20firework.py
