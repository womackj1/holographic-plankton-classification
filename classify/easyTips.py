import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def normResize(img,num1,num2):
    img2 = (img - np.min(img))/(np.max(img) - np.min(img))
    img2 = cv.resize(img2, (num1, num2), interpolation=cv.INTER_CUBIC)
    return img2
#
def reSize(img2,num1,num2):
    img2 = cv.resize(img2, (num1, num2), interpolation=cv.INTER_CUBIC)
    return img2

def norm(img):
    img2 = (img - np.min(img))/(np.max(img) - np.min(img))
    return img2

def rgb2gray(img):
    try:
        if len(img.shape) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    except:
        pass
    return img

def allFileList(filePath,fileType = '.tif'):
    fileListReturn =[]
    for subMainPath, subDirs,subFile in os.walk(filePath, topdown=False):  #find data file
        for dataFile in subFile:   #read data file

            if os.path.splitext(dataFile)[1] == fileType:    #find data with specific suffix
                dataName = os.path.join(subMainPath, dataFile)  #obtain the filename
                dataName = dataName.replace('\\', '/')  #change the formate

                fileListReturn.append(dataName)
    # except:
    #     print('change the path')
    return fileListReturn

def fileList(filePath,fileType = '.tif'):
    fileListReturn =[]
    ld = os.listdir(filePath)  #find data file
    for n in np.arange(len(ld)):   #read data file

        if os.path.splitext(ld[n])[1] == fileType:    #find data with specific suffix
            dataName = os.path.join(filePath, ld[n])
            dataName = dataName.replace('\\', '/')  #change the formate

            fileListReturn.append(dataName)
    # except:
    #     print('change the path')
    return fileListReturn

def creatFolder(savePath, filePath = os.getcwd()):
    if os.path.isdir(savePath) == True:
        savePath = savePath.replace('\\', '/')
    else:
        try:
            savePath = savePath.replace('\\', '/')
        except:
            pass

        if '/' in savePath:
            os.makedirs(savePath)
        else:
            savePath = os.path.join(filePath, savePath)
            folder = os.path.exists(savePath)
            if not folder:
                os.makedirs(savePath)

    return savePath

def plotAllLine(lists): #need to box the lists into one list
    for n in np.arange(len(lists)):
        fList = lists[n]
        x = np.arange(0, len(fList))

def plotOneLine(lists):  # need to box the lists into one list
    x = np.arange(0, len(lists))
    plt.plot(x, lists)
    plt.show()

def plotImage(img, rgbOrGray = 'gray'):
    plt.imshow(img,cmap=rgbOrGray)
    plt.show()

def txtWrite(fileList,savePath = os.getcwd(), saveName = 'txtFile.txt'):
    file = open(os.path.join(savePath,saveName), 'w')
    file.write(str(fileList))
    file.close()

def outputName(path):
    temp = os.path.splitext(path)[0]
    temp = temp.split('/')[-1]
    return temp
