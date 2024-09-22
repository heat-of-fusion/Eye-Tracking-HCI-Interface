import tkinter as tk
from ApplicationButtons import *
from win32api import GetSystemMetrics

from utils import flatten

class HCIAgent():
    '''
    HCI GUI Speller Agent
    '''
    def __init__(self, btn_text = None, second_lang = None):
        global btn_list, root

        self.h_ratio = 0.5
        self.label_ratio = 0.15
        self.alpha = 1.0

        self.btn_text = btn_text
        self.second_lang = second_lang

        self.layout = [len(txt_list) for txt_list in self.btn_text]

        self.grid_Y = len(self.layout)
        self.grid_X = max([len(btn_list) for btn_list in self.btn_text])

        self.res_Y = int(GetSystemMetrics(1) * self.h_ratio)
        self.res_X = GetSystemMetrics(0)

        root = tk.Tk()

        root.overrideredirect(True)
        root.wm_attributes('-topmost', 1)
        root.wm_attributes('-alpha', self.alpha)

        root['bg'] = 'black'
        root.title(f'HCI GUI Speller Agent')
        root.geometry(f'{self.res_X}x{self.res_Y}+0+{self.res_Y}')

        self.grid_width = self.res_X / self.grid_X
        self.grid_height = self.res_Y * (1 - self.label_ratio) / self.grid_Y

        btn_list = list()

        return

    def setup(self):
        '''
        Write Someting
        '''

        global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list

        exit_flag = False
        text_var = tk.StringVar()
        double_jaum_flag = False
        double_jaum_buffer = str()

        text_var.set('')

        self.text_label = tk.Label(root, font = ('Arial', 30), bg = 'black', fg = 'white')
        self.text_label['textvariable'] = text_var
        self.text_label.place(x = 0, y = 0, width = self.res_X, height = int(self.res_Y * self.label_ratio))

        self.reset_button = ResetButton(root, text = '지우기', font = ('Arial', 30), bg = 'white', fg = 'black', highlightthickness = 0, bd = 0)
        self.reset_button.place(x = (self.grid_X - 1) * self.grid_width, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
        self.reset_button.bind('<Enter>', self.reset_button.cursor_enter)
        self.reset_button.bind('<Leave>', self.reset_button.cursor_leave)

        self.exit_button = ExitButton(root, text = '나가기', font = ('Arial', 30), bg = 'red', fg = 'white', highlightthickness = 0, bd = 0)
        self.exit_button.place(x = 0, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
        self.exit_button.bind('<Enter>', self.exit_button.cursor_enter)
        self.exit_button.bind('<Leave>', self.exit_button.cursor_leave)

        # self.btn_text = [txt_list for txt_list in self.btn_text]
        # self.second_lang = [txt_list for txt_list in self.second_lang]

        self.btn_text = flatten(self.btn_text)
        self.second_lang = flatten(self.second_lang)

        margin_list = [(self.grid_X - val) * self.grid_width / 2 for val in self.layout]

        for y, margin in zip(range(len(self.layout)), margin_list):
            row = list()

            for x in range(self.layout[y]):
                Button = text_button_map[self.btn_text[sum(self.layout[:y]) + x]] if self.btn_text[sum(self.layout[:y]) + x] in text_button_map.keys() else TextButton

                btn = Button(root, text = f'{self.btn_text[sum(self.layout[:y]) + x]}', font = ('Arial', 30), bg = 'black', highlightthickness=0, bd=1, fg='white')
                btn.place(x = x * self.grid_width + margin, y = (self.res_Y * self.label_ratio) + y * self.grid_height, width = self.grid_width, height = self.grid_height)
                btn.bind('<Enter>', btn.cursor_enter)
                btn.bind('<Leave>', btn.cursor_leave)

                if type(btn) == TextButton and self.second_lang[sum(self.layout[:y]) + x] is not None:
                    btn.set_second_text(self.second_lang[sum(self.layout[:y]) + x])

                row.append(btn)

            btn_list.append(row)

        root.wm_attributes('-topmost', 1)
        root.protocol('WM_DELETE_WINDOW', root.destroy)

        root.mainloop()

    def destroy(self):
        print(f'Gog Bay...')
        root.destroy()

        return

def run_hci_agent():
    global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list, root, transparent

    exit_flag = None
    text_var = None
    double_jaum_flag = None
    double_jaum_buffer = None
    btn_list = None
    root = None
    transparent = False

    def gui_setup():
        global speller

        btn_text = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<'],
            ['', 'ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', ''],
            ['', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', ''],
            ['', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', ''],
            ['쌍자음', '한영', '명령어', '유튜브', 'Space', '탐색', '투명도', '소형화', 'TTS']
        ]
        # 완성: 쌍자음, 한영, Space, 투명도, TTS, 유튜브, 탐색
        # 미완: 명령어, 소형화

        eng_map = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', None],
            ['', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', ''],
            ['', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ''],
            ['', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ''],
            [None, None, None, None, None, None, None, None, None]
        ]

        speller = HCIAgent(btn_text=btn_text, second_lang = eng_map)
        speller.setup()

        return speller

    return gui_setup()