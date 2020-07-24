import os


def fi(name):
    for path1, dirs, files in os.walk(name):
        # print('root_dir:', path1)# 当前目录路径
        # print('root_dirs:', dirs)# 当前路径下所有子目录
        # print('root_fils:', files) # 当前路径下所有非目录子文件
        for fs in files:
            path2 = os.path.join(path1, fs)
            with open(path2,"r",encoding="utf_8") as f :
                p = f.read()
                print(p)


name =  r"D:\UnrealEngine"
fi(name)