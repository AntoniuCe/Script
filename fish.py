import sys
import pyautogui
import multiprocessing
script_dir = sys.path[0]
photo = script_dir + "\\images\\"

########################
x, y = pyautogui.size()

def primu():
   print('Bafta la peste, pune-te intr-o zona unde culoarea apei are o culoare mai inchisa:')
   while True:
    if pyautogui.locateOnScreen(photo + '1.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('1')
    if pyautogui.locateOnScreen(photo + '2.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('2')
    if pyautogui.locateOnScreen(photo + '3.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('3')
    if pyautogui.locateOnScreen(photo + '4.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('4')
    if pyautogui.locateOnScreen(photo + '5.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('5')
    if pyautogui.locateOnScreen(photo + '6.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('6')
    if pyautogui.locateOnScreen(photo + '7.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('7')
    if pyautogui.locateOnScreen(photo + '8.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('8')
    if pyautogui.locateOnScreen(photo + '9.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('9')
    if pyautogui.locateOnScreen(photo + 'a.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('a')
    if pyautogui.locateOnScreen(photo + 'b.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('b')
    if pyautogui.locateOnScreen(photo + 'c.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('c')




def loop2():
   while True:
     if pyautogui.locateOnScreen(photo + 'd.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('d')
     if pyautogui.locateOnScreen(photo + 'e.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('e')
     if pyautogui.locateOnScreen(photo + 'f.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('f')
     if pyautogui.locateOnScreen(photo + 'g.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('g')
     if pyautogui.locateOnScreen(photo + 'h.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('h')
     if pyautogui.locateOnScreen(photo + 'j.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('j')
     if pyautogui.locateOnScreen(photo + 'k.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('k')
     if pyautogui.locateOnScreen(photo + 'l.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('l')
     if pyautogui.locateOnScreen(photo + 'm.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('m')
     if pyautogui.locateOnScreen(photo + 'n.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('n')

def loop3():
  while True:
   if pyautogui.locateOnScreen(photo + 'p.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('p')
   if pyautogui.locateOnScreen(photo + 'q.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('q')
   if pyautogui.locateOnScreen(photo + 'r.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('r')
   if pyautogui.locateOnScreen(photo + 's.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('s')
   if pyautogui.locateOnScreen(photo + 't.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('t')
   if pyautogui.locateOnScreen(photo + 'u.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('u')
   if pyautogui.locateOnScreen(photo + 'v.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('v')
   if pyautogui.locateOnScreen(photo + 'w.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('w')
   if pyautogui.locateOnScreen(photo + 'y.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('y')
   if pyautogui.locateOnScreen(photo + 'z.png', confidence = 0.95, region = (0, 0, x, y), grayscale=True):
       pyautogui.press('z')




if __name__ == '__main__':
  p1 = multiprocessing.Process(target =primu)
  p2 = multiprocessing.Process(target=loop2)
  p3 = multiprocessing.Process(target=loop3)
  p1.start()
  p2.start()
  p3.start()
  try:
      p1.join()
      p2.join()
      p3.join()
  except KeyboardInterrupt:
      print("KeyboardInterrupt: Stopping the script.")