import pyautogui as aut
import keyboard 
import time


def main():
    time.sleep(1)   
    while True:
        fix_tool() 
        for i in range(15):
            KeyPress()

def Click():
    aut.click()
    time.sleep(CLICK_SPEED)

def KeyPress(): #좌우 이동 동작 & 클릭
    PassSecurity()
    keyboard.press('d')
    time.sleep(0.4)
    keyboard.release('d')
    Click()

    PassSecurity()
    keyboard.press('a')
    time.sleep(0.4)
    keyboard.release('a')
    Click()

def PassSecurity(): #보안 팝업 제거
    isOn = aut.locateOnScreen('minemacro/image/target.png', region=(766, 294, 140, 60))
    if isOn: # 보안창이 떴다면?
        for i in range(4):
            for j in range(4):
                aut.click(x=830+18+36*j, y= 373+18+36*i)
                time.sleep(0.2)
        aut.click()
    else:
        pass

def fix_tool():
    keyboard.send('/')
    time.sleep(0.2)
    keyboard.write("수리")
    time.sleep(0.2)
    keyboard.send('enter')


CLICK_SPEED = 2.7
main()