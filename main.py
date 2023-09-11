import time

import cv2
import pyautogui
import numpy as np
import multiprocessing



x, y = pyautogui.size()

def primu():
   print('Bafta la peste, pune-te intr-o zona unde culoarea apei are o culoare mai inchisa:')
   while True:
    if pyautogui.locateOnScreen('1.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('1')
    if pyautogui.locateOnScreen('2.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('2')
    if pyautogui.locateOnScreen('3.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('3')
    if pyautogui.locateOnScreen('4.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('4')
    if pyautogui.locateOnScreen('5.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('5')
    if pyautogui.locateOnScreen('6.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('6')
    if pyautogui.locateOnScreen('7.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('7')
    if pyautogui.locateOnScreen('8.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('8')
    if pyautogui.locateOnScreen('9.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('9')
    if pyautogui.locateOnScreen('a.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('a')
    if pyautogui.locateOnScreen('b.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('b')
    if pyautogui.locateOnScreen('c.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('c')




def loop2():
   while True:
     if pyautogui.locateOnScreen('d.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('d')
     if pyautogui.locateOnScreen('e.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('e')
     if pyautogui.locateOnScreen('f.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('f')
     if pyautogui.locateOnScreen('g.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('g')
     if pyautogui.locateOnScreen('h.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('h')
     if pyautogui.locateOnScreen('j.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('j')
     if pyautogui.locateOnScreen('k.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('k')
     if pyautogui.locateOnScreen('l.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('l')
     if pyautogui.locateOnScreen('m.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('m')
     if pyautogui.locateOnScreen('n.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('n')

def loop3():
  while True:
   if pyautogui.locateOnScreen('p.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('p')
   if pyautogui.locateOnScreen('q.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('q')
   if pyautogui.locateOnScreen('r.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('r')
   if pyautogui.locateOnScreen('s.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('s')
   if pyautogui.locateOnScreen('t.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('t')
   if pyautogui.locateOnScreen('u.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('u')
   if pyautogui.locateOnScreen('v.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('v')
   if pyautogui.locateOnScreen('w.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('w')
   if pyautogui.locateOnScreen('y.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('y')
   if pyautogui.locateOnScreen('z.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('z')




if __name__ == '__main__':
  p1 = multiprocessing.Process(target =primu)
  p2 = multiprocessing.Process(target=loop2)
  p3 = multiprocessing.Process(target=loop3)
  p1.start()
  p2.start()
  p3.start()
  p1.join()
  p2.join()
  p3.join()