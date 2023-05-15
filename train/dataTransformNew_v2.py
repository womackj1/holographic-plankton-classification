from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch
import numpy as np
from PIL import Image
import cv2 as cv

# def default_loader(path):
#     return Image.open(path).convert('F')

class dataTran(Dataset):
    # 构造函数带有默认参数
    def __init__(self,outputSize, dataSet, transform=None, target_transform=None):
        self.dataSet = dataSet
        self.transform = transform
        self.padToNum = outputSize
        self.target_transform = target_transform
        # self.loader = loader

    def __getitem__(self, item):
        imgData, label = self.dataSet[item]
        padTo = self.padToNum
        # img = self.loader(imgData)
        
        if imgData.size[0]> padTo or imgData.size[1]> padTo:
            open_cv_image=np.array(imgData)
            open_cv_image=cv.resize(open_cv_image,(padTo, padTo),interpolation = cv.INTER_AREA)
            imgData = Image.fromarray(open_cv_image)
        if self.transform is not None:

            a = (padTo - imgData.size[0]) // 2
            b = (padTo - imgData.size[1]) // 2

            transform1 = transforms.Pad((a, b, padTo - a - imgData.size[0], padTo - b - imgData.size[1]), fill=0,
                                        padding_mode='constant')
            try:
                imgData = transform1(imgData)
                img = self.transform(imgData)
            except:
                print(imgData)
        return img, label

    def __len__(self):
        return len(self.dataSet)

