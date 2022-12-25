inputx = open("input.txt", "r" )
#outputx = open("outoput.txt", "a" )
import pyautogui
import time
lic = 0
ord = 0

for x in inputx:
    x = x.split(" ")
    for y in x:
        try:
            y = int(y)
            length = len(str(y))
            length = int(length)
            if length == 9:
                lic = y
                pyautogui.click(x=327, y=224)
                time.sleep(0.3)
                pyautogui.typewrite(str(y))
                pyautogui.press('enter')
                time.sleep(0.3)
                pyautogui.typewrite("SKD282955")
                pyautogui.press('enter')
                time.sleep(0.1)
                #outputx.write(y+'\n')
            elif length == 8:
                ord = y
                #print(lic,',',ord)
                print(lic)
                #outputx.write()
            else:
                print(p)
        except:
            continue
