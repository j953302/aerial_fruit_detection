from glob import glob
from PIL import Image

img_data = glob(".\\downloads\\西瓜\\*.jpg")
k = 0

max_num = 300

for img in img_data:
    im = Image.open(img)
    for j in range(0,im.height//max_num+1):
        if (j+1)*max_num > im.height:
            for i in range(0,im.width//max_num):
                if (i+1)*max_num > im.width:
                    test = im.crop((im.width-max_num,im.height-max_num,im.width,im.height))
                else:
                    test = im.crop((i*max_num,im.height-max_num,(i+1)*max_num,im.height))
                test.save("./downloads/crop_img/"+str(k)+"_crop.jpg")
                k +=1
        
        else:
            for i in range(0,im.width//max_num):
                if (i+1)*max_num > im.width:
                    test = im.crop((im.width-max_num,j*max_num,im.width,(j+1)*max_num))
                else:
                    test = im.crop((i*max_num,j*max_num,(i+1)*max_num,(j+1)*max_num))
                test.save("./downloads/crop_img/"+str(k)+"_crop.jpg")
                k +=1
# In[]:
    
jpglist = glob("./downloads/crop_img/*.jpg" )
file = open('apple_train.txt', 'wt')
for jpg in jpglist:
    file.write('apple_data/obj'+jpg[jpg.find('\\'):]+'\n')
file.close()   # 關閉檔案

# In[]:
jpglist = glob( "./valid//*.jpg" )
file = open('Taichung_valid.txt', 'wt')
for jpg in jpglist:
    file.write('data/valid/'+jpg[8:]+'\n')
file.close()   # 關閉檔案    