import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
WINDOW_SIZE = (800, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Выбор карты с Pygame')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Рука игрока (просто пример, можно изменить на свои карты)
player_hand = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Функция выбора карты
def choose_card():
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Если нажата клавиша, проверяем, является ли она числовой (от 1 до 9)
                if event.unicode.isdigit() and 1 <= int(event.unicode) <= len(player_hand):
                    # Возвращаем выбранную карту
                    return player_hand[int(event.unicode) - 1]

        # Отрисовка экрана
        window.fill(WHITE)
        text = font.render('Выберите карту (1-{}):'.format(len(player_hand)), True, BLACK)
        window.blit(text, (200, 250))

        # Отрисовка карт в руке игрока
        for i, card in enumerate(player_hand):
            card_text = font.render(card, True, RED)
            window.blit(card_text, (200 + i * 50, 300))

        pygame.display.update()

# Основной цикл игры
while True:
    selected_card = choose_card()
    print('Игрок выбрал карту:', selected_card)
