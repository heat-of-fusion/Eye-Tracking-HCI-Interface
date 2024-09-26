import time
import tkinter as tk
from ApplicationButtons import *
from win32api import GetSystemMetrics

from utils import flatten, command_set

# class HCIAgent():
#     '''
#     HCI GUI Speller Agent
#     '''
#     def __init__(self, btn_text = None, second_lang = None):
#         global btn_list, root
#
#         self.h_ratio = 0.5
#         self.label_ratio = 0.15
#         self.alpha = 1.0
#
#         self.btn_text = btn_text
#         self.second_lang = second_lang
#
#         self.layout = [len(txt_list) for txt_list in self.btn_text]
#
#         self.grid_Y = len(self.layout)
#         self.grid_X = max([len(btn_list) for btn_list in self.btn_text])
#
#         self.res_Y = int(GetSystemMetrics(1) * self.h_ratio)
#         self.res_X = GetSystemMetrics(0)
#
#         root = tk.Tk()
#
#         root.overrideredirect(True)
#         root.wm_attributes('-topmost', 1)
#         root.wm_attributes('-alpha', self.alpha)
#
#         root['bg'] = 'black'
#         root.title(f'HCI GUI Speller Agent')
#         root.geometry(f'{self.res_X}x{self.res_Y}+0+{self.res_Y}')
#
#         self.grid_width = self.res_X / self.grid_X
#         self.grid_height = self.res_Y * (1 - self.label_ratio) / self.grid_Y
#
#         btn_list = list()
#
#         return
#
#     def setup(self):
#         '''
#         Write Someting
#         '''
#
#         global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list
#
#         exit_flag = False
#         text_var = tk.StringVar()
#         double_jaum_flag = False
#         double_jaum_buffer = str()
#
#         text_var.set('')
#
#         self.text_label = tk.Label(root, font = ('Arial', 30), bg = 'black', fg = 'white')
#         self.text_label['textvariable'] = text_var
#         self.text_label.place(x = 0, y = 0, width = self.res_X, height = int(self.res_Y * self.label_ratio))
#
#         self.reset_button = ResetButton(root, text = '지우기', font = ('Arial', 30), bg = 'white', fg = 'black', highlightthickness = 0, bd = 0)
#         self.reset_button.place(x = (self.grid_X - 1) * self.grid_width, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
#         self.reset_button.bind('<Enter>', self.reset_button.cursor_enter)
#         self.reset_button.bind('<Leave>', self.reset_button.cursor_leave)
#
#         self.exit_button = ExitButton(root, text = '나가기', font = ('Arial', 30), bg = 'red', fg = 'white', highlightthickness = 0, bd = 0)
#         self.exit_button.place(x = 0, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
#         self.exit_button.bind('<Enter>', self.exit_button.cursor_enter)
#         self.exit_button.bind('<Leave>', self.exit_button.cursor_leave)
#
#         # self.btn_text = [txt_list for txt_list in self.btn_text]
#         # self.second_lang = [txt_list for txt_list in self.second_lang]
#
#         self.btn_text = flatten(self.btn_text)
#         self.second_lang = flatten(self.second_lang)
#
#         margin_list = [(self.grid_X - val) * self.grid_width / 2 for val in self.layout]
#
#         for y, margin in zip(range(len(self.layout)), margin_list):
#             row = list()
#
#             for x in range(self.layout[y]):
#                 Button = text_button_map[self.btn_text[sum(self.layout[:y]) + x]] if self.btn_text[sum(self.layout[:y]) + x] in text_button_map.keys() else TextButton
#
#                 btn = Button(root, text = f'{self.btn_text[sum(self.layout[:y]) + x]}', font = ('Arial', 30), bg = 'black', highlightthickness=0, bd=1, fg='white')
#                 btn.place(x = x * self.grid_width + margin, y = (self.res_Y * self.label_ratio) + y * self.grid_height, width = self.grid_width, height = self.grid_height)
#                 btn.bind('<Enter>', btn.cursor_enter)
#                 btn.bind('<Leave>', btn.cursor_leave)
#
#                 if type(btn) == TextButton and self.second_lang[sum(self.layout[:y]) + x] is not None:
#                     btn.set_second_text(self.second_lang[sum(self.layout[:y]) + x])
#
#                 row.append(btn)
#
#             btn_list.append(row)
#
#         root.wm_attributes('-topmost', 1)
#         root.protocol('WM_DELETE_WINDOW', root.destroy)
#
#         root.mainloop()
#
#     def destroy(self):
#         print(f'Gog Bay...')
#         root.destroy()
#
#         return

class HCI_App(tk.Tk):
    def __init__(self, btn_text = None, second_lang = None):
        super().__init__()

        self.config(bg = 'black')
        self.title(f'HCI GUI Speller Agent')

        self.main_frame = MainFrame(self, btn_text, second_lang)
        self.cmd_frame = CommandFrame(self)
        self.exp_frame = ExplorerFrame(self)
        self.min_frame = MinimizedFrame(self)

        self.show_frame(self.main_frame)

        return

    def show_frame(self, frame):
        frame.set_geometry(self)
        time.sleep(0.1)
        frame.tkraise()

        return


class MainFrame(tk.Frame):
    def __init__(self, master, btn_text, second_lang):
        super().__init__(master)

        global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list

        print(btn_text)
        print(second_lang)

        self.btn_text = btn_text
        self.second_lang = second_lang

        self.h_ratio = 0.5
        self.label_ratio = 0.15
        self.alpha = 1.0

        self.res_Y = int(GetSystemMetrics(1) * self.h_ratio)
        self.res_X = GetSystemMetrics(0)

        self.place(x = 0, y = 0, width = self.res_X, height = self.res_Y)

        self.layout = [len(txt_list) for txt_list in self.btn_text]

        self.grid_Y = len(self.layout)
        self.grid_X = max([len(btn_list) for btn_list in self.btn_text])

        self.grid_width = self.res_X / self.grid_X
        self.grid_height = self.res_Y * (1 - self.label_ratio) / self.grid_Y

        btn_list = list()

        exit_flag = False
        text_var = tk.StringVar()
        double_jaum_flag = False
        double_jaum_buffer = str()

        text_var.set('')

        self.text_label = tk.Label(self, font = ('Arial', 30), bg = 'black', fg = 'white')
        self.text_label['textvariable'] = text_var
        self.text_label.place(x = 0, y = 0, width = self.res_X, height = int(self.res_Y * self.label_ratio))

        self.reset_button = ResetButton(self, text = '지우기', font = ('Arial', 30), bg = 'white', fg = 'black', highlightthickness = 0, bd = 0)
        self.reset_button.place(x = (self.grid_X - 1) * self.grid_width, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
        self.reset_button.bind('<Enter>', self.reset_button.cursor_enter)
        self.reset_button.bind('<Leave>', self.reset_button.cursor_leave)

        self.exit_button = ExitButton(self, text = '나가기', font = ('Arial', 30), bg = 'red', fg = 'white', highlightthickness = 0, bd = 0)
        self.exit_button.place(x = 0, y = 0, width = self.grid_width, height = self.res_Y * self.label_ratio)
        self.exit_button.bind('<Enter>', self.exit_button.cursor_enter)
        self.exit_button.bind('<Leave>', self.exit_button.cursor_leave)

        self.btn_text = flatten(self.btn_text)
        self.second_lang = flatten(self.second_lang)

        margin_list = [(self.grid_X - val) * self.grid_width / 2 for val in self.layout]

        for y, margin in zip(range(len(self.layout)), margin_list):
            row = list()

            for x in range(self.layout[y]):
                Button = text_button_map[self.btn_text[sum(self.layout[:y]) + x]] if self.btn_text[sum(self.layout[:y]) + x] in text_button_map.keys() else TextButton

                btn = Button(self, text = f'{self.btn_text[sum(self.layout[:y]) + x]}', font = ('Arial', 30), bg = 'black', highlightthickness=0, bd=1, fg='white')
                btn.place(x = x * self.grid_width + margin, y = (self.res_Y * self.label_ratio) + y * self.grid_height, width = self.grid_width, height = self.grid_height)
                btn.bind('<Enter>', btn.cursor_enter)
                btn.bind('<Leave>', btn.cursor_leave)

                if type(btn) == TextButton and self.second_lang[sum(self.layout[:y]) + x] is not None:
                    btn.set_second_text(self.second_lang[sum(self.layout[:y]) + x])

                row.append(btn)

            btn_list.append(row)

        self['bg'] = 'black'

        return

    def set_geometry(self, master):
        master.geometry(f'{self.res_X}x{self.res_Y}+0+{self.res_Y}')

        master.overrideredirect(True)
        master.wm_attributes('-topmost', 1)
        master.wm_attributes('-alpha', self.alpha)

        master['bg'] = 'black'
        master.title(f'HCI GUI Speller Agent')

        return

class CommandFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.h_ratio = 0.5
        self.go_back_ratio = 0.15

        self.n_btn_per_row = 7
        self.n_btn = len(command_set)

        self.res_Y = int(GetSystemMetrics(1) * self.h_ratio)
        self.res_X = int(GetSystemMetrics(0))

        self.place(x = 0, y = 0, width = self.res_X, height = self.res_Y)

        self.go_back_btn_height = int(self.res_Y * self.go_back_ratio)

        self.btn_height = (self.res_Y - self.go_back_btn_height) / (self.n_btn // self.n_btn_per_row + 1)
        self.btn_width = self.res_X / self.n_btn_per_row

        go_back_btn = MainButton(self, text = f'메인 화면으로', font = ('Arial', 30), bg = 'white', fg='black', highlightthickness=0, bd=1)
        go_back_btn.place(x = 0, y = 0, width = self.res_X, height = self.go_back_btn_height)
        go_back_btn.bind('<Enter>', go_back_btn.cursor_enter)
        go_back_btn.bind('<Leave>', go_back_btn.cursor_leave)

        print(f'btn_height: {self.btn_height}, btn_width: {self.btn_width}')

        self.cmd_btn_list = list()

        for y in range(self.n_btn // self.n_btn_per_row):
            row = list()

            for x in range(self.n_btn_per_row):
                command = command_set[y * self.n_btn_per_row + x]
                btn = CommandTextButton(command, self, text = command, font = ('Arial', 30), bg = 'black', fg='white', highlightthickness=0, bd=1)
                btn.place(x = x * self.btn_width, y = self.go_back_btn_height + y * self.btn_height, width = self.btn_width, height = self.btn_height)
                btn.bind('<Enter>', btn.cursor_enter)
                btn.bind('<Leave>', btn.cursor_leave)

                row.append(btn)

            self.cmd_btn_list.append(row)

        row = list()

        for x in range(self.n_btn % self.n_btn_per_row):
            command = command_set[(y + 1) * self.n_btn_per_row + x]
            btn = CommandTextButton(command, self, text = command, font = ('Arial', 30), bg = 'black', fg = 'white', highlightthickness = 0, bd = 1)
            btn.place(x=x * self.btn_width, y= self.go_back_btn_height + (y + 1) * self.btn_height, width=self.btn_width, height=self.btn_height)
            btn.bind('<Enter>', btn.cursor_enter)
            btn.bind('<Leave>', btn.cursor_leave)

            row.append(btn)

        self.cmd_btn_list.append(row)

        master['bg'] = 'black'

        return

    def set_geometry(self, master):
        master.geometry(f'{self.res_X}x{self.res_Y}+0+{self.res_Y}')

        return

class ExplorerFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        return

class MinimizedFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.res_Y = GetSystemMetrics(1)
        self.res_X = GetSystemMetrics(0)

        # self.btn_width = int(self.res_X * (1 / 10))
        self.btn_height = int(self.res_Y * (1 / 10))

        self.place(x = 0, y = 0, width = self.btn_height, height = self.btn_height)

        self.btn = MainButton(self, text = f'대형화', font = ('Arial', 30), bg = 'white', fg='black', highlightthickness=0, bd=1)
        self.btn.place(x = 0, y = 0, width = self.btn_height, height = self.btn_height)
        self.btn.bind('<Enter>', self.btn.cursor_enter)
        self.btn.bind('<Leave>', self.btn.cursor_leave)

        master['bg'] = 'black'

        return

    def set_geometry(self, master):
        master.geometry(f'{self.btn_height}x{self.btn_height}+{self.res_X - self.btn_height}+{(self.res_Y - self.btn_height) // 2}')

        return

# def run_hci_agent():
#     global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list, root, transparent
#
#     exit_flag = None
#     text_var = None
#     double_jaum_flag = None
#     double_jaum_buffer = None
#     btn_list = None
#     root = None
#     transparent = False
#
#     def gui_setup():
#         global speller
#
#         btn_text = [
#             ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<'],
#             ['', 'ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', ''],
#             ['', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', ''],
#             ['', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', ''],
#             ['쌍자음', '한영', '명령어', '유튜브', 'Space', '탐색', '투명도', '소형화', 'TTS']
#         ]
#         # 완성: 쌍자음, 한영, Space, 투명도, TTS, 유튜브, 탐색
#         # 미완: 명령어, 소형화
#
#         eng_map = [
#             ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', None],
#             ['', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', ''],
#             ['', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ''],
#             ['', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ''],
#             [None, None, None, None, None, None, None, None, None]
#         ]
#
#         speller = HCIAgent(btn_text=btn_text, second_lang = eng_map)
#         speller.setup()
#
#         return speller
#
#     return gui_setup()

def run_hci_app():
    global exit_flag, text_var, double_jaum_flag, double_jaum_buffer, btn_list, root, transparent, speller

    exit_flag = None
    text_var = None
    double_jaum_flag = None
    double_jaum_buffer = None
    btn_list = None
    root = None
    transparent = False
    speller = None

    # def gui_setup():

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

    speller = HCI_App(btn_text=btn_text, second_lang = eng_map)
    speller.mainloop()

    return speller