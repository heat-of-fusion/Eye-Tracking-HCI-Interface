import time
import threading
from abc import *
from utils import *
import tkinter as tk
from jamo import h2j, j2hcj
from unicode import join_jamos

import HCI_Agent
from utils import double_jaum_dict, double_moum_dict

class Hover2ClickButton(tk.Button):
    '''
    This class successes tk.Button and make it clickable with mouse hovering.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(command = self.click_function)

        self.stay_time = 0.75 # Default staying time. You can change this time with self.set_stay_time() function.
        self.blink_time = 0.05 # Blinking time when the button is clicked.

        # Flags
        self.click_flag = False
        self.exit_flag = True

        self.running_thread = False

        return

    def set_stay_time(self, stay_time):
        '''
        Change the hoverting time to click.
        :param stay_time: When you hover your cursor for this time, the button would be clicked.
        :return: None
        '''
        self.stay_time = stay_time

        return

    @blinkdecorator
    def click_function(self):
        '''
        This function is called automatically when the cursor is hovering on the button for "self.stay_time".
        :return: None
        '''

        return

    def blink(self):
        '''
        This function helps you recognize the button click visually.
        :return: None
        '''

        def _blink():
            bg_color = self['bg']
            font_color = self['fg']

            self.config(bg = font_color, fg = bg_color)

            time.sleep(self.blink_time)

            self.config(bg = bg_color, fg = font_color)

        blink_thread = threading.Thread(target = _blink)
        blink_thread.start()

        return

    def delayed_click(self):
        '''
        Call self.click_function if the mouse is still on the button even after "self.stay_time".
        :return: None
        '''
        time.sleep(self.stay_time)

        if self.click_flag:
            self.click_function()

        self.running_thread = False

        if self.exit_flag == False:
            self.cursor_enter(None)

        return

    def cursor_enter(self, e):
        '''
        This function is called when the mouse enter the button.
        :return: None
        '''

        # print(f'Cursor Entered!')

        self.exit_flag = False

        if self.running_thread:
            return

        self.running_thread = True

        self.click_thread = threading.Thread(target = self.delayed_click)
        self.click_thread.start()

        self.click_flag = True

        return

    def cursor_leave(self, e):
        '''
        This function is called when the mouse leave button.
        :return: None
        '''

        # print(f'Cursor Left!')

        self.click_flag = False
        self.exit_flag = True

        return

class TextButton(Hover2ClickButton):
    '''
    This class success Hover2ClickButton and function as a Korean keyboard engine.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moum_decomp_dict = dict(zip(list(double_moum_dict.values()), list(double_moum_dict.keys())))
        self.first_lang = True

        self.first_text = self['text']
        self.second_text = None

        return

    def set_second_text(self, second_text):
        '''
        Set the second-language text.
        :param second_text: String to use as a second-language text.
        :return: None
        '''
        self.second_text = second_text

        return

    def switch_lang(self):
        '''
        Toggle the first/second-language text.
        :return: None
        '''
        self.first_lang = False if self.first_lang else True

        self.config(text = self.first_text if self.first_lang else self.second_text)

        return

    def double_moum_merge(self, text):
        '''
        This function analyzes the input String and merge double-moums.
        :param text: String to apply double-moum-merging.
        :return: String with the function applied.
        '''

        # print(f'Double Moum Merge Call! Input: {text}')

        new_string = str()
        skip_flag = False

        for idx in range(len(text)):
            if skip_flag:
                skip_flag = False

                continue

            if text[idx : idx + 2] in list(double_moum_dict.keys()):
                # print(f'Double Moum Detected! {text[idx : idx + 2]}')

                new_string += double_moum_dict[text[idx : idx + 2]]
                skip_flag = True

                continue

            new_string += text[idx]

        return new_string

    def double_moum_decomp(self, text):
        '''
        This function analyzes the input tring and decompose double-moums.
        :param text: String to apply double-moum-decomposition.
        :return: String with the function applied.
        '''
        new_string = str()

        for idx in range(len(text)):
            if text[idx] in self.moum_decomp_dict.keys():
                new_string += self.moum_decomp_dict[text[idx]]

                continue

            new_string += text[idx]

        return new_string

    @blinkdecorator
    def click_function(self):
        # print(f'Double Jaum Flag: {HCI_Agent.double_jaum_flag}, Buffer: {HCI_Agent.double_jaum_buffer}')

        prev_text = HCI_Agent.text_var.get()
        prev_text = j2hcj(h2j(prev_text))
        prev_text = self.double_moum_decomp(prev_text)

        if HCI_Agent.double_jaum_flag:
            if HCI_Agent.double_jaum_buffer == '':
                HCI_Agent.double_jaum_buffer += self.first_text
                new_text = prev_text

            else:
                try:
                    new_text = prev_text + double_jaum_dict[HCI_Agent.double_jaum_buffer + self.first_text]

                except:
                    new_text = prev_text

                HCI_Agent.btn_list[-1][0].deactivate_double_jaum()

        elif self.first_lang:
            new_text = prev_text + self.first_text

        else:
            new_text = prev_text + self.second_text

        new_text = self.double_moum_merge(new_text)
        new_text = join_jamos(new_text)

        HCI_Agent.text_var.set(new_text)

        # self.blink()

        return