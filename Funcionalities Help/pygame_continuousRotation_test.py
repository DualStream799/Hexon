import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))

class Planet(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # Image we want to tranform
        self.imageMaster = pygame.image.load('planet_originalaa.png')
        self.imageMaster = self.imageMaster.convert()
        # setting the Sprot image attribute to our transformation image
        self.image = self.imageMaster
        # get the rect of the image
        self.rect = self.image.get_rect()
        # pu it in the center of the screen no matter what resolution is
        self.rect.center = ((screen.get_width()/2), (screen.get_height()/2))
        # sprites direction based on mathematical rotation of degrees
        self.dir = 0

    def update(self):
        """To rotate properly, rather than continuing to rotate an blit our image (which will be 
           distort it beyond belief after a few transformations), we need to keep loading/rotating our imageMaster to the proper degree"""
        # get original center because new Rect will change with image transformation
        old_center = self.rect.center
        # use pygame.transform.rotate(<image_to_rotate>, <turn degrees>)
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        # get new Rect
        self.rect = self.image.get_rect()
        # set new center to original center
        self.rect.center = old_center

    def turn_left(self):
        self += 15
        if self.dir > 360:
            self.dir = 15

    def turn_right(self):
        self -= 15
        if self.dir > 360:
            self.dir = 15


def main(screen):
    pygame.display.set_caption("Planet Rotation")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 75, 200))
    screen.blit(background, (0, 0))
    planet = Planet(screen)
    allSprites = pygame.sprite.OrderedUpdates(planet)
    # ticker is used to delay our animation
    ticker = 0
    clock = pygame.time.Clock()
    keep_playing = True

    while keep_playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                keep_playing = False
        # Continuous Input (command repited )
        keys = pygame.key.get_pressed()
        if ticker >= 3:
            if keys[pygame.K_d]:
                planet.turn_right()
            if keys[pygame.K_a]:
                planet.turn_left()
        # CUD blitting
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
        if ticker >= 3:
            ticker = 0
        else:
            ticker += 1

main(screen)
pygame.quit()