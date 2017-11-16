import pygame



display_width = 800
display_height = 450
screen = pygame.display.set_mode((display_height, display_width))
clock = pygame.time.Clock()

def main():
	background = pygame.image.load('home_purple_small.png')
	planet_img = pygame.image.load('planet_original.png').convert()
	ring_x = 0
	ring_y = 0
	planet_img.center = (500, 375)
	direction = 'right'
	rotateBy = 10
	angle = 0
	going = True
	while going:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
				going = False
		screen.blit(background)
		angle += rotateBy
		planet_imgNew = pygame.transform.rotate(planet_img, angle)
		#ring_rectNew = ring_imgNew.get_rect()
		planet_imgNew.center = (500, 475)

		screen.blit(planet_imgNew)
		clock.tick(60)
		pygame.display.update()

main()