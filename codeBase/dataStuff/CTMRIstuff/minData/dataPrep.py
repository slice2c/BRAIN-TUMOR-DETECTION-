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
imgDir = filedialog.askdirectory() + '//'
print("---->", imgDir)
cDir = os.getcwd()
os.chdir(imgDir)

imgList = glob.glob("*.png")
os.chdir(cDir)
for i in tqdm.tqdm(imgList, colour="red"):
    img = cv2.imread(i)
    if not os.path.isdir("CTstuff"):
        os.makedirs("CTstuff")
    imgCT = img[:, :255]
    cv2.imwrite('CTstuff//'+i, imgCT)
    if not os.path.isdir("MRIstuff"):
        os.makedirs("MRIstuff")
    imgMRI = img[:, 256:]
    cv2.imwrite('MRIstuff//'+i, imgCT)