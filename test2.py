import pyautogui


img = pyautogui.locateOnScreen('october_treat.PNG', confidence=0.9, grayscale = True)

pyautogui.moveTo(img)