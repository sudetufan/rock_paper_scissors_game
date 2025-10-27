import pygame
import random

# Pygame başlat
pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock–Paper–Scissors AI 🎮")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)

# Font
font = pygame.font.Font(None, 36)

# Butonlar
button_width = 150
button_height = 60
buttons = {
    "rock": pygame.Rect(50, 300, button_width, button_height),
    "paper": pygame.Rect(225, 300, button_width, button_height),
    "scissors": pygame.Rect(400, 300, button_width, button_height)
}

# Oyun verileri
options = ["rock", "paper", "scissors"]
player_choice = ""
ai_choice = ""
result = ""
history = []

# Fonksiyonlar
def draw_text(text, x, y, color=BLACK):
    txt = font.render(text, True, color)
    screen.blit(txt, (x, y))

def ai_move():
    if len(history) < 3:
        return random.choice(options)
    counts = {move: history.count(move) for move in options}
    most_common = max(counts, key=counts.get)
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

# Ana döngü
running = True
while running:
    screen.fill(WHITE)

    draw_text("Rock–Paper–Scissors AI", 150, 40, BLUE)

    for name, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        draw_text(name.capitalize(), rect.x + 35, rect.y + 15)

    if player_choice:
        draw_text(f"You chose: {player_choice}", 200, 150)
        draw_text(f"AI chose: {ai_choice}", 200, 190)
        draw_text(result, 260, 230, BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    player_choice = name
                    ai_choice = ai_move()
                    history.append(player_choice)

                    if player_choice == ai_choice:
                        result = "Draw!"
                    elif (player_choice == "rock" and ai_choice == "scissors") or \
                         (player_choice == "paper" and ai_choice == "rock") or \
                         (player_choice == "scissors" and ai_choice == "paper"):
                        result = "You Win!"
                    else:
                        result = "AI Wins!"

    pygame.display.flip()

pygame.quit()
