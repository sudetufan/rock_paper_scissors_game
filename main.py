import pygame
import random

# Start pygame
pygame.init()

# Make the window
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Game variables
player_wins = 0
ai_wins = 0
total_games = 0
message = ""

# AI memory (list to remember player choices)
ai_memory = []

def get_ai_choice():
    # If we don't have enough data, pick random
    if len(ai_memory) < 3:
        return random.randint(0, 2)
    
    # Count how many times player picked each choice
    rock_count = ai_memory.count(0)
    paper_count = ai_memory.count(1) 
    scissors_count = ai_memory.count(2)
    
    # Find what player picks most
    if rock_count >= paper_count and rock_count >= scissors_count:
        most_picked = 0  # Rock
    elif paper_count >= scissors_count:
        most_picked = 1  # Paper
    else:
        most_picked = 2  # Scissors
    
    # Pick the choice that beats what player picks most
    if most_picked == 0:  # Player picks rock most
        return 1  # AI picks paper (paper beats rock)
    elif most_picked == 1:  # Player picks paper most
        return 2  # AI picks scissors (scissors beats paper)
    else:  # Player picks scissors most
        return 0  # AI picks rock (rock beats scissors)

def play_game(player_choice):
    global player_wins, ai_wins, total_games, message
    
    # Get AI choice
    ai_choice = get_ai_choice()
    
    # Remember player's choice
    ai_memory.append(player_choice)
    
    # Check who wins
    if player_choice == ai_choice:
        message = "Tie! Both picked the same thing"
    elif (player_choice == 0 and ai_choice == 2) or \
         (player_choice == 1 and ai_choice == 0) or \
         (player_choice == 2 and ai_choice == 1):
        player_wins = player_wins + 1
        message = "You win!"
    else:
        ai_wins = ai_wins + 1
        message = "AI wins!"
    
    total_games = total_games + 1

def draw_screen():
    # Clear screen
    window.fill(white)
    
    # Draw title
    font = pygame.font.Font(None, 30)
    title = font.render("Rock Paper Scissors", True, black)
    window.blit(title, (100, 20))
    
    # Draw scores
    score_text = "You: " + str(player_wins) + "  AI: " + str(ai_wins) + "  Games: " + str(total_games)
    score = font.render(score_text, True, black)
    window.blit(score, (50, 60))
    
    # Draw message
    if message != "":
        msg = font.render(message, True, black)
        window.blit(msg, (100, 100))
    
    # Draw buttons
    pygame.draw.rect(window, gray, (50, 150, 80, 50))
    pygame.draw.rect(window, gray, (150, 150, 80, 50))
    pygame.draw.rect(window, gray, (250, 150, 80, 50))
    
    # Draw button text
    rock_text = font.render("Rock", True, black)
    paper_text = font.render("Paper", True, black)
    scissors_text = font.render("Scissors", True, black)
    
    window.blit(rock_text, (65, 165))
    window.blit(paper_text, (165, 165))
    window.blit(scissors_text, (255, 165))
    
    # Draw instructions
    if total_games == 0:
        instructions = font.render("Click a button to play!", True, black)
        window.blit(instructions, (100, 220))
    
    # Show the screen
    pygame.display.flip()

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Check if clicked on Rock button
            if 50 <= mouse_x <= 130 and 150 <= mouse_y <= 200:
                play_game(0)  # 0 = Rock
            
            # Check if clicked on Paper button  
            elif 150 <= mouse_x <= 230 and 150 <= mouse_y <= 200:
                play_game(1)  # 1 = Paper
            
            # Check if clicked on Scissors button
            elif 250 <= mouse_x <= 330 and 150 <= mouse_y <= 200:
                play_game(2)  # 2 = Scissors
    
    # Draw everything
    draw_screen()
    
    # Wait a bit
    pygame.time.wait(30)

# End pygame
pygame.quit()
print("Game over! Thanks for playing!")