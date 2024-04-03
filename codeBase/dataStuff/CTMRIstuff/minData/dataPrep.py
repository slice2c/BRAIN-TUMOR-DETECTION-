import matplotlib.pyplot as plt
from tkinter import filedialog
import random
import tqdm
import glob
import time
import cv2
import os

t1 = time.time()
print("Select the Directory Yo!")
#imgDir = filedialog.askdirectory()
imgDir = '/Volumes/ReserveDisk/OpenSourceContribution/SynthCT/codeBase/dataStuff/CTMRIstuff/minData/mergeCTMRI'
if "\\" in imgDir:
    imgDir = imgDir + '\\'
else:
    imgDir = imgDir + '/'
print("---->", imgDir)

imgList = glob.glob(imgDir + "*.png")
for i in tqdm.tqdm(imgList, colour="red"):
    img = cv2.imread(i)
    i = i.replace(imgDir, '')
    if not os.path.isdir("CTstuff"):
        os.makedirs("CTstuff")
    if not os.path.isdir("MRIstuff"):
        os.makedirs("MRIstuff")
    imgCT = img[:, :256]
    cv2.imwrite('CTstuff//'+i, imgCT)
    imgMRI = img[:, 256:]
    cv2.imwrite('MRIstuff//'+i, imgMRI)