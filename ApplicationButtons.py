import os
import HCI_Agent
import threading
import playsound
import pyautogui
import clipboard
from gtts import gTTS
from jamo import h2j, j2hcj
from unicode import join_jamos
from Hover2ClickButton import Hover2ClickButton, TextButton

from utils import *

class ResetButton(Hover2ClickButton):
    '''
    Button to reset the tk.Stringvar in the application.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        HCI_Agent.text_var.set('')

        return

class ExitButton(Hover2ClickButton):
    '''
    Close every session and exit progam.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        HCI_Agent.exit_flag = True
        HCI_Agent.speller.destroy()

        return

class SpaceButton(TextButton):
    '''
    Function as a SpaceBar Button.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        prev_text = HCI_Agent.text_var.get()

        prev_text = j2hcj(h2j(prev_text))
        prev_text = self.double_moum_decomp(prev_text)

        new_text = prev_text + ' '
        new_text = self.double_moum_merge(new_text)
        new_text = join_jamos(new_text)

        HCI_Agent.text_var.set(new_text)

        return

class BackSpaceButton(TextButton):
    '''
    Function as a BackSpace Button.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        prev_text = HCI_Agent.text_var.get()
        prev_text = j2hcj(h2j(prev_text))
        prev_text = self.double_moum_decomp(prev_text)

        new_text = self.double_moum_merge(prev_text[:-1])
        new_text = join_jamos(new_text)

        HCI_Agent.text_var.set(new_text)

        return

class TTSButton(Hover2ClickButton):
    '''
    Convert the given string to .mp3 file and play.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        text = HCI_Agent.text_var.get()

        if 'tts.mp3' in os.listdir(f'./src/'):
            os.remove(f'./src/tts.mp3')

        tts = gTTS(text = text, lang = 'ko')
        tts.save(f'./src/tts.mp3')

        threading.Thread(target = lambda: playsound.playsound(f'./src/tts.mp3')).start()

        return

class EnterButton(Hover2ClickButton):
    '''
    Type the given string.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        pyautogui.write(HCI_Agent.text_var.get(), interval = 0.01)

        print(f'Writing {HCI_Agent.text_var.get()} ...')

        return

class CopyButton(Hover2ClickButton):
    '''
    Copy the given string to the clipboard.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    @blinkdecorator
    def click_function(self):
        clipboard.copy(HCI_Agent.text_var.get())

        return

class DoubleJaumButton(Hover2ClickButton):
    '''
    Activate Double-Jaum function.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return

    def activate_double_jaum(self):
         HCI_Agent.double_jaum_flag = True
         HCI_Agent.double_jaum_buffer = str()

         self.config(fg = self['bg'], bg = self['fg'])

         return

    def deactivate_double_jaum(self):
        HCI_Agent.double_jaum_flag = False
        HCI_Agent.double_jaum_buffer = str()

        self.config(fg = self['bg'], bg = self['fg'])

        return

    @blinkdecorator
    def click_function(self):
        if HCI_Agent.double_jaum_flag:
            self.deactivate_double_jaum()

        else:
            self.activate_double_jaum()

        return

class KorEngButton(Hover2ClickButton):
    '''
    Toggle Korean/English keyboards.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.korean = True

        return

    @blinkdecorator
    def click_function(self):
        for row in range(len(HCI_Agent.btn_list)):
            for column in range(len(HCI_Agent.btn_list[row])):
                if type(HCI_Agent.btn_list[row][column]) == TextButton:
                    HCI_Agent.btn_list[row][column].switch_lang()

        self.korean = False if self.korean else True

        return