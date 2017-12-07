import os
import sys
import pygame
from textbox import TextBox


KEY_REPEAT_SETTING = (200,70)
login_page_original = pygame.image.load(r'.\Images\Background\login_page_original.png')


class Control(object):
    def __init__(self, screen=(450, 800)):
        pygame.init()
        pygame.display.set_caption("Hexon Acess")
        self.screen = pygame.display.set_mode(screen)
        self.screen.blit(login_page_original, screen)
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.done = False
        self.input = TextBox((100,100,150,30),command=self.change_color,
                              clear_on_enter=True,inactive_on_enter=False)
        self.color = (100,100,100)
        self.prompt = self.make_prompt()
        pygame.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompt(self):
        font = pygame.font.SysFont("arial", 20)
        message = 'Username (A-Z  0-9):'
        rend = font.render(message, True, pygame.Color("gray"))
        print((rend, rend.get_rect(topleft=(10,35))))
        return (rend, rend.get_rect(topleft=(10,35)))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.input.get_event(event)

    def change_color(self,id,color):
        try:
            self.color = pygame.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.input.update()
            self.screen.fill(self.color)
            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pygame.quit()
    sys.exit()
