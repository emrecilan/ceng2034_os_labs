import os
import shutil
import time
start_time = time.time()

jpgMagic = "ffd8ffe0"
mp3Magic = "49443303"
pngMagic = "89504e47"
file_list = []
for i in os.listdir(os.getcwd()):
    file_list.append(i)


os.mkdir("TxtFiles")
os.mkdir("JpegFiles")
os.mkdir("Mp3Files")
os.mkdir("PngFiles")
def func(file_list):
    for filename in file_list:
        file = open(filename, "rb")
        content = file.read(4).hex()
        if content == jpgMagic:
            shutil.move(filename, "./jpegFiles")
        elif content == pngMagic:
            shutil.move(filename, "./pngFiles")
        elif content == mp3Magic:
            shutil.move(filename, "./mp3Files")
        else:
            shutil.move(filename, "./txtFiles")

end_time = time.time()
print("Used Time: " + str(end_time - start_time) + " sec")
