import os
path = r"E:\project\Python\research\hat_faster_rcnn\images\\"
filepath = os.listdir(path)

for filename in filepath:
	oldname = os.path.splitext(filename)
	newname = oldname[0] + '.jpg'
	os.rename(path + filename,path + newname)