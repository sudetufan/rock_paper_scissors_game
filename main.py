import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock–Paper–Scissors Game with AI")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)
BLUE = (100, 149, 237)

font = pygame.font.Font(None, 36)


button_width = 170
button_height = 60
buttons = {
    "rock": pygame.Rect(50, 300, button_width, button_height),
    "paper": pygame.Rect(225, 300, button_width, button_height),
    "scissors": pygame.Rect(400, 300, button_width, button_height)
}

options = ["rock", "paper", "scissors"]
players_choice = ""
ai_choice = ""
result = ""
history = []


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

running = True
while running:
    screen.fill(WHITE)

    draw_text("Rock–Paper–Scissors AI", 150, 40, BLUE)

    for name, rect in buttons.items():
        pygame.draw.rect(screen, PINK, rect)
        draw_text(name.capitalize(), rect.x + 45, rect.y + 15)

    if players_choice:
        draw_text(f"You chose: {players_choice}", 200, 150)
        draw_text(f"AI chose: {ai_choice}", 200, 190)
        draw_text(result, 260, 230, BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    players_choice = name
                    ai_choice = ai_move()
                    history.append(players_choice)

                    if players_choice == ai_choice:
                        result = "Draw!"
                    elif (players_choice == "rock" and ai_choice == "scissors") or \
                         (players_choice == "paper" and ai_choice == "rock") or \
                         (players_choice == "scissors" and ai_choice == "paper"):
                        result = "You Win!"
                    else:
                        result = "AI Wins!"

    pygame.display.flip()

pygame.quit()
