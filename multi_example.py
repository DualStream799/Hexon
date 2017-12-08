import os
import sys
import pygame
import json
from textbox import TextBox


KEY_REPEAT_SETTING = (200, 70)
signup_page_original = pygame.image.load(r'.\Images\Background\signup_page_original.png')
but_signup_no = pygame.image.load(r'.\Images\Buttons\Small\hex_but_signup_yes.png')
but_signup_yes = pygame.image.load(r'.\Images\Buttons\Small\hex_but_signup_no.png')

but_signup_yes_pos = [[149, 515], [149 + 57, 515 + 65]]
but_signup_no_pos = [[260, 514], [260 + 59, 514 + 67]]

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
        # TextBoxes configurations:
        self.useremail_input = TextBox((85, 278, 305, 45), font=self.font, command=self.save_username, clear_on_enter=False, inactive_on_enter=True)
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
        # Returning list for render:
        return rendered

    def event_loop(self):

        for event in pygame.event.get():
            # Quit Command (Calls 'GameEnd' function):
            if event.type == pygame.QUIT:
                self.done = True
            # Detection of box command:
            for box in self.inputs:
                box.get_event(event)
            # Keyboard Click Detection (and cosequential actions, depending where/what is clicked):
            if event.type == pygame.KEYDOWN:
                # Quit Command:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
            # Mouse Click Detection (and consequential actions, depending where/what is clicked):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse Position (axis x and -y coordinates):
                mouse_pos_x, mouse_pos_y = event.pos
                # Mouse Tracking:
                print(mouse_pos_x, mouse_pos_y)
                # NO BUTTON Clicked:
                if (mouse_pos_x in range(but_signup_yes_pos[0][0], but_signup_yes_pos[1][0])) and (mouse_pos_y in range(but_signup_yes_pos[0][1], but_signup_yes_pos[1][1])):
                    #screen.blit(but_pressed, (but_signup_yes_pos[0][0], but_signup_yes_pos[0][1]))
                    print("Delete Clicked")
                    # GameEnd()
                # YES BUTTON Clicked:
                if (mouse_pos_x in range(but_signup_no_pos[0][0], but_signup_no_pos[1][0])) and (mouse_pos_y in range(but_signup_no_pos[0][1], but_signup_no_pos[1][1])):
                    #screen.blit(but_pressed, (but_signup_yes_pos[0][0], but_signup_yes_pos[0][1]))
                    print("Confirm Clicked")
                    # GameEnd()
    # Save Username Function:
    def save_username(self, id, username_message):
        """Check username input and, if it's valid, save it in a dictionary"""
        if len(username_message) > 10:
            self.input_data['Username'] = username_message
        else:
            print("Username too short")
    # Save Email Function:
    def save_email(self, id, email_message):
        """Check email input and, if it's valid, save it in a dictionary"""
        if '@' in email_message:
            self.input_data['Email'] = email_message
        else:
            print("Invalid email")
    # Save Password Function:
    def save_password(self, id, password_message):
        """Check password input and, if it's valid, save it in a dictionary"""
        if ' ' not in email_message:
            self.input_data['Password'] = password_message
        else:
            print("Invalid password")


    def change_text_color(self, id, color):
        if self.input_data['Username'] != '' and self.input_data['Email'] != '' and self.input_data['Password']:
            pass

    def render(self):
        # Showing Screen Background:
        self.screen.blit(signup_page_original, (0, 0))
        # Showing Screen Buttons:
        self.screen.blit(but_signup_yes, (but_signup_yes_pos[0][0], but_signup_yes_pos[0][1]))
        self.screen.blit(but_signup_no, (but_signup_no_pos[0][0], but_signup_no_pos[0][1]))

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
