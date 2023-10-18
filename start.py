import sys
import main
import pygame

pygame.init()
WINDOW_SIZE = (1780, 720)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Дурак')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Выход из игры
            sys.exit()

    # Отрисовка объектов и графики
    window.fill((255, 255, 255))  # Заливка окна белым цветом

    # Здесь вы можете добавить код для отрисовки других объектов или графики

    pygame.display.update()  # Обновление экрана