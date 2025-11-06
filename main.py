import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock Paper Scissors")

white = (255, 255, 255)
navy = (0, 0, 128)
pink = (255, 182, 193)
blue = (100, 149, 237)


font = pygame.font.Font(None, 36)

rock_button = pygame.Rect(50, 300, 170, 60)
paper_button = pygame.Rect(225, 300, 170, 60)
scissors_button = pygame.Rect(400, 300, 170, 60)

choices = ["rock", "paper", "scissors"]
player_pick = ""
ai_pick = ""
result = ""
past_moves = []

def draw_text(text, x, y, color=navy):
    txt = font.render(text, True, color)
    screen.blit(txt, (x, y))

def get_ai_choice():
    if len(past_moves) < 3:
        return random.choice(choices)
    
    rock_count = 0
    paper_count = 0
    scissors_count = 0
    
    for move in past_moves:
        if move == "rock":
            rock_count += 1
        elif move == "paper":
            paper_count += 1
        elif move == "scissors":
            scissors_count += 1
    
    if rock_count >= paper_count and rock_count >= scissors_count:
        return "paper"     
    elif paper_count >= scissors_count:
        return "scissors"   
    else:
        return "rock"       


running = True
while running:
    screen.fill(white)
    
    draw_text("Rock Paper Scissors AI", 150, 40, blue)


    pygame.draw.rect(screen, pink, rock_button)
    draw_text("Rock", rock_button.x + 50, rock_button.y + 15)

    pygame.draw.rect(screen, pink, paper_button)
    draw_text("Paper", paper_button.x + 45, paper_button.y + 15)

    pygame.draw.rect(screen, pink, scissors_button)
    draw_text("Scissors", scissors_button.x + 25, scissors_button.y + 15)


    if player_pick != "":
        draw_text("You chose: " + player_pick, 200, 150)
        draw_text("AI chose: " + ai_pick, 200, 190)
        draw_text(result, 260, 230, blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos 
            if rock_button.collidepoint(mouse_x, mouse_y):
                player_pick = "rock"
            elif paper_button.collidepoint(mouse_x, mouse_y):
                player_pick = "paper"
            elif scissors_button.collidepoint(mouse_x, mouse_y):
                player_pick = "scissors"
            
            if player_pick != "":
                ai_pick = get_ai_choice()
                past_moves.append(player_pick)
                
                if player_pick == ai_pick:
                    result = "Draw!"
                elif player_pick == "rock" and ai_pick == "scissors":
                    result = "You Win!"
                elif player_pick == "paper" and ai_pick == "rock":
                    result = "You Win!"
                elif player_pick == "scissors" and ai_pick == "paper":
                    result = "You Win!"
                else:
                    result = "AI Wins!"

    pygame.display.flip()

pygame.quit()
