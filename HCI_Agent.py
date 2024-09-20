import tkinter as tk
from ApplicationButtons import *
from win32api import GetSystemMetrics

class HCIAgent():
    '''
    HCI GUI Speller Agent
    '''
    def __init__(self, grid_Y = 5, grid_X = 11, btn_text = None, second_lang = None):
        global btn_list

        self.h_ratio = 0.5
        self.label_ratio = 0.15
        self.alpha = 1.0

        self.btn_text = btn_text
        self.second_lang = second_lang

        self.grid_Y = grid_Y
        self.grid_X = grid_X

        self.res_Y = int(GetSystemMetrics(1) * self.h_ratio)
        self.res_X = GetSystemMetrics(0)

        self.root = tk.Tk()

        self.root.overrideredirect(True)
        self.root.wm_attributes('-topmost', 1)
        self.root.wm_attributes('-alpha', self.alpha)

        self.root['bg'] = 'black'
        self.root.title(f'HCI GUI Speller Agent')
        self.root.geometry(f'{self.res_X}x{self.res_Y}+0+{self.res_Y}')

        self.grid_width = self.res_X / self.grid_X
        self.grid_height = self.res_Y * (1 - self.label_ratio) / self.grid_Y

        # self.btn_list = list()
        btn_list = list()

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

        self.text_label = tk.Label(self.root, font = ('Arial', 30), bg = 'black', fg = 'white')
        self.text_label['textvariable'] = text_var
        self.text_label.place(x = 0, y = 0, width = self.res_X, height = int(self.res_Y * self.label_ratio))

        self.reset_button = ResetButton(self.root, text = '지우기', font = ('Arial', 30), bg = 'white', fg = 'black', highlightthickness = 0, bd = 0)
        self.reset_button.place(x = (self.grid_X - 1) * self.grid_width, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
        self.reset_button.bind('<Enter>', self.reset_button.cursor_enter)
        self.reset_button.bind('<Leave>', self.reset_button.cursor_leave)

        self.exit_button = ExitButton(self.root, text = '나가기', font = ('Arial', 30), bg = 'red', fg = 'white', highlightthickness = 0, bd = 0)
        self.exit_button.place(x = 0, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
        self.exit_button.bind('<Enter>', self.exit_button.cursor_enter)
        self.exit_button.bind('<Leave>', self.exit_button.cursor_leave)

        layout = [11, 10, 9, 7, 9]
        margin_list = [(self.grid_X - val) * self.grid_width / 2 for val in layout]

        for y, margin in zip(range(len(layout)), margin_list):
            row = list()

            for x in range(layout[y]):
                if self.btn_text[sum(layout[:y]) + x] == 'Space':
                    Button = SpaceButton
                elif self.btn_text[sum(layout[:y]) + x] == '쌍자음':
                    Button = DoubleJaumButton
                elif self.btn_text[sum(layout[:y]) + x] == '<':
                    Button = BackSpaceButton
                elif self.btn_text[sum(layout[:y]) + x] == '한영':
                    Button = KorEngButton
                elif self.btn_text[sum(layout[:y]) + x] == 'TTS':
                    Button = TTSButton
                elif self.btn_text[sum(layout[:y]) + x] == 'Ent':
                    Button = EnterButton
                # elif self.btn_text[sum(layout[:y]) + x] == 'Ghost':
                #     Button = GhostButton
                elif self.btn_text[sum(layout[:y]) + x] == 'Copy':
                    Button = CopyButton
                else:
                    Button = TextButton

                btn = Button(self.root, text = f'{self.btn_text[sum(layout[:y]) + x]}', font = ('Arial', 30), bg = 'black', highlightthickness=0, bd=1, fg='white')
                btn.place(x = x * self.grid_width + margin, y = (self.res_Y * self.label_ratio) + y * self.grid_height, width = self.grid_width, height = self.grid_height)
                btn.bind('<Enter>', btn.cursor_enter)
                btn.bind('<Leave>', btn.cursor_leave)

                row.append(btn)

            btn_list.append(row)

        for y, margin in zip(range(len(layout)), margin_list):
            for x in range(layout[y]):
                if type(self.second_lang[sum(layout[:y]) + x]) == TextButton:
                    btn_list[y][x].set_second_text(self.second_lang[sum(layout[:y]) + x])

        self.root.wm_attributes('-topmost', 1)
        self.root.protocol('WM_DELETE_WINDOW', self.root.destroy)

        self.root.mainloop()

    def destroy(self):
        print(f'Gog Bay...')
        self.root.destroy()

        return

def run_hci_agent():
    global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list

    exit_flag = None
    text_var = None
    double_jaum_flag = None
    double_jaum_buffer = None
    btn_list = None

    def gui_setup():
        global speller

        btn_text = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<',
            'ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ',
            'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ',
            'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ',
            '쌍자음', '한영', 'Empty', 'Empty', 'Space', 'Empty', 'Empty', 'Empty', 'TTS'
        ]

        eng_map = [
            None, None, None, None, None, None, None, None, None, None, None,
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm',
            None, None, None, None, None, None, None, None, None
        ]

        speller = HCIAgent(btn_text=btn_text, second_lang = eng_map)
        speller.setup()

        return speller

    return gui_setup()