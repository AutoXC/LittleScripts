import cv2
import os

#批量处理视频文件
dir_path = r"E:\BaiduNetdiskDownload\\"         #视频文件所在文件夹路径
videopath_list = os.listdir(dir_path)           #文件夹下所有视频文件名列表
n=1                                             #截图起始编号

for i in videopath_list:
	videopath = dir_path + i
	print("video path is "+ videopath)

	#videopath = r"E:\BaiduNetdiskDownload\2min.mp4"
	vc = cv2.VideoCapture(videopath)            #读入视频path
	c=1                                         #起始帧数
 
	if vc.isOpened():                           #判断是否正常打开
		rval , frame = vc.read()
	else:
		rval = False
	 
	timeF = 100                                 #视频帧计数间隔
	 
	while rval:                                 #循环读取视频帧
		rval, frame = vc.read()
		if(c%timeF == 0):                       #每隔timeF帧进行存储操作
			cv2.imwrite(r"E:\BaiduNetdiskDownload\video2pic\\" + "Scrshot" + str(n) + '.png',frame) #存储为图像
			n = n + 1
		c = c + 1
		cv2.waitKey(1)
	vc.release()                                #.release()与cv2.destroyAllWindows()只能放在循环体外
print("done!")