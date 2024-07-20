import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))

# 设置角色初始位置和大小
character_rect = pygame.Rect(50, 50, 50, 50)  # x, y, width, height
character_speed = 5


    # 按键控制
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character_rect.move_ip(0, -character_speed)  # 向上移动
    if keys[pygame.K_s]:
        character_rect.move_ip(0, character_speed)  # 向下移动
    if keys[pygame.K_a]:
        character_rect.move_ip(-character_speed, 0)  # 向左移动
    if keys[pygame.K_d]:
        character_rect.move_ip(character_speed, 0)  # 向右移动

    # 确保角色不会移出屏幕
    if character_rect.left < 0:
        character_rect.left = 0
    if character_rect.right > 800:
        character_rect.right = 800
    if character_rect.top < 0:
        character_rect.top = 0
    if character_rect.bottom > 600:
        character_rect.bottom = 600

    # 绘制背景（在这里只是简单的清屏）
    screen.fill((255, 255, 255))

    # 绘制角色
    pygame.draw.rect(screen, (0, 0, 255), character_rect)  # 使用蓝色绘制矩形代表角色

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)
