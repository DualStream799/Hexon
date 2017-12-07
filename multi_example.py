import os
import sys
import pygame
from textbox import TextBox


KEY_REPEAT_SETTING = (200,70)
login_page_original = pygame.image.load(r'.\Images\Background\signup_page_original.png')


class Control(object):
    def __init__(self):
        pygame.init()
        self.input = []
        pygame.display.set_caption("Multiple Input Boxes")
        self.screen = pygame.display.set_mode((450,800))
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.done = False
        useremail_input = TextBox((85,278,305,45), command=self.save_input(text_type='email'), clear_on_enter=True, inactive_on_enter=False)
        username_input = TextBox((85,364,305,45), command=self.save_input(text_type='text'), clear_on_enter=True, inactive_on_enter=False, active=False)
        password_input = TextBox((85,453,305,45), command=self.save_input(text_type='text'), clear_on_enter=True, inactive_on_enter=False, active=False)
        self.prompts = self.make_prompts()
        self.inputs = [useremail_input, username_input, password_input]
        self.color = (100, 100, 100)
        
        pygame.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompts(self, color=pygame.Color("gray")):
        rendered = []
        font = pygame.font.SysFont("01 Digitall", 20)

        message = 'EMAIL: (A-Z 0-9 Space @ - _ .)'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(15,244))))

        message = 'USERNAME: (A-Z 0-9 Space)'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(15,331))))

        message = 'PASSWORD: (A-Z 0-9 - _ .)'
        rend = font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10,420))))
        print(rendered)
        return rendered

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            for box in self.inputs:
                box.get_event(event)



    def save_input(self, id, info, text_type='text'):
        self.input_data = []
        if text_type == 'email':
            if '@' not in info:
                print("Please input a valid email")
            else:
                self.input_data.append(str(info))
        if text_type == 'text':
            self.input_data.append(str(info))



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
        self.screen.blit(login_page_original, (0, 0))

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
        print(self.input_data)


if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pygame.quit()
    sys.exit()
