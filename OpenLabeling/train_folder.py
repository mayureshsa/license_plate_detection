import os

path='data/obj/'



imgList=os.listdir(r'D:\UiT\Semester 2\AI\project\training_data\OpenLabeling\main\input')

print(imgList)

textFile=open('train.txt','w')


for img in imgList:
    imgPath=path+ img +'\n'
    textFile.write(imgPath)
