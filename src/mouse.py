
import pyautogui
import sys

# print(sys.argv)
# print(sys.argv[1])
# print(sys.argv[2])
# print(pyautogui.size())
# print(pyautogui.position())

res_x, res_y = pyautogui.size()
x, y = res_x * float(sys.argv[1]), res_y * float(sys.argv[2])
# print(res_x * x, res_y * y)
# x, y = 1810, 1062

pyautogui.moveTo(x, y, duration = 0.3)
pyautogui.click(x, y)
# print(pyautogui.position())
