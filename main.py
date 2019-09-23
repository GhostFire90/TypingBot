from PIL import ImageGrab
from pyautogui import typewrite
import numpy as np
import time
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Evan Anderson\PycharmProjects\typerbot2.0\tesseract\tesseract.exe"
box = (492,158,1452,426)
ready = False
def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def Type(img):
    global ready
    if ready != False:
        text = pytesseract.image_to_string(img)
        typewrite(text)
    else:
        yes = input("Ready? (Y/N) ")
        if yes == 'y' or yes == 'Y':
            ready = True

def main():
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=box))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        Type(new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()