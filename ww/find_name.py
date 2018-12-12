# coding=utf-8
import os

# keyword为关键字，root为文件夹路径
def findfile(keyword, root):
    filelist=[]
    newfilelist=[]
    for root,dirs,files in os.walk(root):
        for name in files:
            filelist.append(os.path.join(root,name))

    for i in filelist:
        if os.path.isfile(i):
            if keyword in os.path.basename(os.path.splitext(i)[0]):
                newfilelist.append(i)
            else:
                pass
        else:
            pass
    os.system(f'cp {newfilelist}')  # 执行终端命令


findfile('.flv','/Users/momo/Desktop/lastvideo2清晰')
