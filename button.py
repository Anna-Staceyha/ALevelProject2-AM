import pygame 

#button class
class Button():
	def __init__(self,x, y, image, scale, pos, text_input, font, base_color, hovering_color):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self,base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.tect.get_rect(center=(self.x_pos, self.y_pos))
		self.rect.topleft = (x, y)
		self.clicked = False
		self.text = self.font.render(self.text_input, True, self.base_colour)
		if self.image is None:
			self.image = self.text
		

	def draw(self, surface):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
	
	def update(self,screen):
		if self.image is not None:
				screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput
	############################################################################