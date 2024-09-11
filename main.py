"""import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("dark blue")

        PLAY_TEXT = get_font(45).render("Levels", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_LEVEL1 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="Level 1", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        PLAY_LEVEL1.changeColor(PLAY_MOUSE_POS)
        PLAY_LEVEL1.update(SCREEN)
    

        PLAY_LEVEL2 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="Level 2", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        PLAY_LEVEL2.changeColor(PLAY_MOUSE_POS)
        PLAY_LEVEL2.update(SCREEN)


        PLAY_LEVEL3 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="Level 3", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        
        PLAY_LEVEL3.changeColor(PLAY_MOUSE_POS)
        PLAY_LEVEL3.update(SCREEN)

        for button in [PLAY_LEVEL1, PLAY_LEVEL2, PLAY_LEVEL3]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_LEVEL1.checkForInput(PLAY_MOUSE_POS):
                        play()
                if PLAY_LEVEL2.checkForInput(PLAY_MOUSE_POS):
                    options()
                if PLAY_LEVEL3.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Earthly Duo", True, "#89cff0")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()





main_menu()

def play_level1():
    while True:
        play_level1_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        play_level1_TEXT = get_font(45).render("This is the LEVEL 1 screen.", True, "Black")
        play_level1_RECT = play_level1_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(play_level1_TEXT, play_level1_RECT)

        play_level1_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        play_level1_BACK.changeColor(play_level1_MOUSE_POS)
        play_level1_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           

        pygame.display.update()

def play_level2():
    while True:
        play_level2_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        play_level2_TEXT = get_font(45).render("This is the LEVEL 2 screen.", True, "Black")
        play_level2_RECT = play_level2_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(play_level2_TEXT, play_level2_RECT)

        play_level2_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        play_level2_BACK.changeColor(play_level2_MOUSE_POS)
        play_level2_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           

        pygame.display.update()

def play_level3():
    while True:
        play_level3_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        play_level3_TEXT = get_font(45).render("This is the LEVEL 3 screen.", True, "Black")
        play_level3_RECT = play_level3_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(play_level3_TEXT, play_level3_RECT)

        play_level3_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        play_level3_BACK.changeColor(play_level3_MOUSE_POS)
        play_level3_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           

        pygame.display.update()



def level_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        LEVEL_MENU_MOUSE_POS = pygame.mouse.get_pos()

        LEVEL_MENU_TEXT = get_font(80).render("Levels", True, "#89cff0")
        LEVEL_MENU_RECT = LEVEL_MENU_TEXT.get_rect(center=(640, 100))

        LEVEL1_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="LEVEL 1", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        LEVEL2_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="LEVEL 2", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        LEVEL3_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="LEVEL 3", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(LEVEL_MENU_TEXT, LEVEL_MENU_RECT)

        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON]:
            button.changeColor(LEVEL_MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(LEVEL_MENU_MOUSE_POS):
                    play_level1()
                if LEVEL2_BUTTON.checkForInput(LEVEL_MENU_MOUSE_POS):
                    play_level2()
                if LEVEL3_BUTTON.checkForInput(LEVEL_MENU_MOUSE_POS):
                    play_level3()

        pygame.display.update()"""

import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
screen_height = 720
screen_width = 1280

BG = pygame.image.load("assets/Background.png")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# Function to display the selected level screen
def play_level(level_num):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        # Display the current level dynamically
        LEVEL_TEXT = get_font(45).render(f"This is LEVEL {level_num}", True, "Black")
        LEVEL_RECT = LEVEL_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVEL_TEXT, LEVEL_RECT)

        # Back button
        BACK_BUTTON = Button(image=None, pos=(640, 460),
                             text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        BACK_BUTTON.changeColor(MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    play()  # Return to level selection screen

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()  # Return to the main menu

        pygame.display.update()


# Level selection screen
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("dark blue")

        PLAY_TEXT = get_font(45).render("Levels", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Back button
        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Level buttons
        PLAY_LEVEL1 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                             text_input="Level 1", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        PLAY_LEVEL2 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                             text_input="Level 2", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        PLAY_LEVEL3 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                             text_input="Level 3", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        # Render buttons
        for button in [PLAY_LEVEL1, PLAY_LEVEL2, PLAY_LEVEL3]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()  # Return to main menu
                if PLAY_LEVEL1.checkForInput(PLAY_MOUSE_POS):
                    play_level(1)  # Go to level 1
                if PLAY_LEVEL2.checkForInput(PLAY_MOUSE_POS):
                    play_level(2)  # Go to level 2
                if PLAY_LEVEL3.checkForInput(PLAY_MOUSE_POS):
                    play_level(3)  # Go to level 3

        pygame.display.update()

# Main menu function
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Earthly Duo", True, "#89cff0")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                             text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                             text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()  # Navigate to level selection screen
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()  # Show options screen
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Start the game with the main menu
main_menu()

title_size = 50

def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(SCREEN, (225, 225, 225), (0, line * title_size), (screen_width, line * title_size))
        pygame.draw.line(SCREEN, (255, 255, 255), (line * title_size, 0), (line * title_size, screen_height))



class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])



world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]




world = World(world_data)

run = True
while run:

	screen.blit(bg_img, (0, 0))
	screen.blit(sun_img, (100, 100))

	world.draw()

	draw_grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()