import os
import socket
import threading
import HCI_Agent
import pyautogui
import mss, mss.tools
from win32api import GetSystemMetrics

def main():
    speller_thread = threading.Thread(target = HCI_Agent.run_hci_app)
    eyetracker_thread = threading.Thread(target = lambda: os.system(f'eye_tracking.exe'))

    speller_thread.start()
    eyetracker_thread.start()

    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

    res_Y, res_X = GetSystemMetrics(1), GetSystemMetrics(0)

    sock = socket.socket(socket.AF_INET, type = socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 1235))

    while True:
        if HCI_Agent.exit_flag:
            print(f'Exit Flag Called!')
            os.system(f'taskkill /im eye_tracking.exe /t /f')
            break

        try:
            message, client_addr = sock.recvfrom(4096)

            row = message.decode(encoding='utf-8').split(',')

            timestep, (x, y) = int(row[0]), list(map(float, row[1:]))

            coordX = min(max(0, res_X * x), res_X)
            coordY = min(max(0, res_Y * y), res_Y)

            # print(f'cX: {coordX}, cY: {coordY}')

            pyautogui.moveTo(coordX, coordY, 0)

        except KeyboardInterrupt:
            sock.close()
            break

    return

if __name__ == '__main__':
    main()