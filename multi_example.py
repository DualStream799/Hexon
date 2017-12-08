import os
import sys
import pygame
from textbox import TextBox


KEY_REPEAT_SETTING = (200, 70)
login_page_original = pygame.image.load(r'.\Images\Background\signup_page_original.png')


class Control(object):
    def __init__(self):
        pygame.init()
        self.input = []
        pygame.display.set_caption("Hexon Sign Up")
        self.screen = pygame.display.set_mode((450, 800))
        self.clock = pygame.time.Clock()
        # Font Selection (Any_installed_font_on_PC, font_size)
        self.font = pygame.font.SysFont("01 Digitall", 35)
        self.fps = 60.0
        self.done = False

        useremail_input = TextBox((85, 278, 305, 45), font=self.font, command=self.save_username, clear_on_enter=False, inactive_on_enter=True)
        username_input = TextBox((85, 364, 305, 45), font=self.font, command=self.save_email, clear_on_enter=False, inactive_on_enter=True, active=False)
        password_input = TextBox((85, 453, 305, 45), font=self.font, command=self.save_password, clear_on_enter=False, inactive_on_enter=True, active=False)

        self.prompts = self.make_labels()
        self.inputs = [useremail_input, username_input, password_input]
        self.input_data = {'Email': "",
                           'Username': "",
                           'Password': ""}
        self.color = (100, 100, 100)
        pygame.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_labels(self, color=pygame.Color("gray")):
        rendered = []
        # Label 01:
        message = 'USERNAME:'
        rend = self.font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(15, 244))))
        # Label 02:
        message = 'EMAIL:'
        rend = self.font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(15, 331))))
        # Label 03:
        message = 'PASSWORD:'
        rend = self.font.render(message, True, color)
        rendered.append((rend, rend.get_rect(topleft=(10, 420))))
        return rendered

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            for box in self.inputs:
                box.get_event(event)



    def save_input(self, id, info, text_type='text'):
        
        for box in self.inputs:
            if text_type == 'email':
                if '@' not in info:
                    print("Please input a valid email")
                else:
                    self.input_data.append(str(info))
            if text_type == 'text':
                self.input_data.append(str(info))



    def save_username(self, id, username_message):
        if len(username_message) > 10:
            self.input_data['Username'] = username_message
        else:
            print("Username too short")

    def save_email(self, id, email_message):
        if '@' in email_message:
            self.input_datainput_data['Email'] = email_message
        else:
            print("Invalid email")

    def save_password(self, id, password_message):
        if ' ' not in email_message:
            self.input_datainput_data['Password'] = password_message
        else:
            print("Invalid password")


    def change_text_color(self, id, color):
        try:
            color = pygame.Color(str(color))
            for box in self.inputs:
                box.font_color = color
            self.prompts = self.make_prompts(color)
        except ValueError:
            print("Please input a valid color name.")


    def render(self):
        # Showing Screen Background:
        self.screen.blit(login_page_original, (0, 0))
        # Showing each one of the TextBoxes:
        for box in self.inputs:
            box.draw(self.screen)
        # Showing each one of the Labels:
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
