import pyautogui as pg
from PIL import ImageGrab, Image
import os
import natsort
import time

def pageCapture(index):
    tempImg = ImageGrab.grab((20, 84, 733, 958))
    tempImg.save(f'./capture/{index}.png')

def movePage(index):
    print(f'{index} >> {pg.position()}')
    pg.click(698, 547)

def imgsToPdf():
    imgsPath = './capture'
    pdfPath = './pdf'

    fileList = os.listdir(imgsPath)
    
    imgList = []

    cvtRgb0 = Image.open(f'{imgsPath}/0.png').convert('RGB')
    for file in natsort.natsorted(fileList):
        if(file == '0.png' or file == '.DS_Store'):
            continue
        print(file)
        cvtRgb = Image.open(f'{imgsPath}/{file}').convert('RGB')
        imgList.append(cvtRgb)

    cvtRgb0.save('./test.pdf', save_all=True, append_images=imgList)

def positionTest():
    print(pg.size())
    print(pg.position())

pg.click()
for index in range(663):
    time.sleep(2)
    pageCapture(index)
    movePage(index)

# input()
imgsToPdf()

# positionTest()
# pageCapture(0)