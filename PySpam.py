import keyboard
import time
import pyautogui
import webview


class Api:
    def main(self, Message, SpamAmount,Speed):
        time.sleep(5)
        for x in range(1 , SpamAmount+1):
            if keyboard.is_pressed('esc'):
                quit()
            pyautogui.typewrite(Message)
            time.sleep(Speed / 10)
            pyautogui.press('enter')
            time.sleep(Speed / 10)


if __name__ == "__main__":
    api = Api()
    webview.create_window('PySpam v0.0.1' , 'src/index.html', width=450, height=650 ,js_api=api)
    webview.start()