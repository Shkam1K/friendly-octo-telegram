import pygame
import sys
import random
from PIL import Image
# Инициализация Pygame
pygame.init()

# Установка размеров окна
WINDOW_SIZE = (800, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Игра в Дурака')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка экрана
    window.fill(WHITE)
    
    # Отображение текста и графики
    text = font.render('Игра в Дурака', True, BLACK)
    window.blit(text, (300, 50))

    # Отображение карт игрока и компьютера (заглушка)
    # Замените этот блок кода на вашу логику отображения карт
    player_hand = ['2', '3', '4', '5', '6']
    for i, card in enumerate(player_hand):
        card_text = font.render(card, True, RED)
        window.blit(card_text, (100 + i * 80, 300))

    computer_hand = ['7', '8', '9', '10', 'J']
    for i, card in enumerate(computer_hand):
        card_text = font.render(card, True, RED)
        window.blit(card_text, (100 + i * 80, 100))

    # Отображение кнопки для хода (заглушка)
    pygame.draw.rect(window, BLACK , (350, 450, 100, 50))
    button_text = font.render('Ход', True, WHITE)
    window.blit(button_text, (370, 460))

    pygame.display.update()
