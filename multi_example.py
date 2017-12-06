import os
import sys
import pygame

from textbox import TextBox


KEY_REPEAT_SETTING = (200,70)


class Control(object):
    def __init__(self):
        pygame.init()
        self.input = []
        pygame.display.set_caption("Multiple Input Boxes")
        self.screen = pygame.display.set_mode((450,800))
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.done = False
        email_color = TextBox((100,100,250,30), command=self.change_color, clear_on_enter=True, inactive_on_enter=False)
        username_color = TextBox((100,150,250,30), command=self.change_text_color, clear_on_enter=True, inactive_on_enter=False, active=False)
        password_color = TextBox((100,370,250,30), command=self.change_text_color, clear_on_enter=True, inactive_on_enter=False, active=False)
        self.prompts = self.make_prompts()
        self.inputs = [email_color, username_color, password_color]
        self.color = (100,100,100)
        pygame.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompts(self, color=pygame.Color("white")):
        rendered = []
        font = pygame.font.SysFont("arial", 20)

        message = 'Username: (A-Z 0-9 Space)'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10,35))))

        message = 'Email: (A-Z 0-9 Space @ - _ .)'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10,215))))

        message = 'Password: (A-Z 0-9 - _ .)'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10,315))))

        return rendered

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            for box in self.inputs:
                box.get_event(event)

    def change_color(self, id, color):
        try:
            self.color = pygame.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")

    def change_text_color(self, id, color):
        try:
            color = pygame.Color(str(color))
            for box in self.inputs:
                box.font_color = color
            self.prompts = self.make_prompts(color)
        except ValueError:
            print("Please input a valid color name.")

    def render(self):
        self.screen.fill(self.color)

        for box in self.inputs:
            box.draw(self.screen)

        for prompt in self.prompts:
            self.screen.blit(*prompt)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            for box in self.inputs:
                box.update()
            self.render()
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pygame.quit()
    sys.exit()
