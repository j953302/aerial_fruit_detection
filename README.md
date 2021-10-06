# aerial_fruit_detection
Using few high resolution aerial pictures of melon patchs. And train yolov4 model to detect it. However, now the current train data doesn't enough so that train and valid data are same.
使用高解析空拍影像做yolov4模型訓練，因目前版本訓練資料為爬蟲，資料有限的情況下，訓練與驗證僅能使用相同照片。


1. 利用爬蟲技術先抓取可以使用的西瓜航拍，如下(資料來源：網路)：
![image](https://github.com/j953302/aerial_fruit_detection/blob/main/downloads/33322775458_e7a3373121_o.jpg)
為了增加資料與加速訓練效率，將同一張照片利用crop的python檔完成切分資料。
