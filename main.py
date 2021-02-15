import pyautogui
import time



#딜레이 0.5초
def sl():
    time.sleep(0.5)
    return
#초기화 함수
def init():
    time.sleep(2)
    pyautogui.moveTo(742, 969)
    pyautogui.click()
    sl()
    pyautogui.press('right')
    sl()
    pyautogui.press('space')
    return

init()
sl()
pyautogui.typewrite('4')
time.sleep(0.3)
print("참깨빵")
pyautogui.typewrite('442',interval=0.25)
print("위에")
pyautogui.typewrite('2', interval=0.2)
print("순쇠고기")
pyautogui.typewrite('5', interval=0.2)
pyautogui.typewrite('555', interval=0.2)
print("패티두장")
pyautogui.typewrite('1111', interval=0.15)

print("특별한소스")
pyautogui.typewrite('4')
time.sleep(0.3)
pyautogui.typewrite('442',interval=0.25)
pyautogui.typewrite('2', interval=0.2)
print("양상추")
pyautogui.typewrite('55',interval=0.4)
pyautogui.typewrite('4',interval=0.2)

sl()
print("치즈 피클 양파")
pyautogui.typewrite('44',interval=0.4)
pyautogui.typewrite('225',interval=0.3)
pyautogui.typewrite('5',interval=0.4)
print("까아지4")
pyautogui.typewrite('654',interval=0.4)
time.sleep(1)
pyautogui.typewrite('45',interval=0.2)
pyautogui.typewrite('6',interval=0.2)
pyautogui.typewrite('9',interval=0.2)
pyautogui.typewrite('8',interval=0.2)
time.sleep(0.5)
pyautogui.press('right')
pyautogui.press('space')
