import itchat
import math
import PIL.Image as Image
import os

# 获取到当前文件的目录，并检查是否有saveImg文件夹，如果不存在则自动新建saveImg文件
File_Path = os.getcwd()
result = os.listdir(File_Path)
if "saveImg" in result:
    print('Directory already exists')
else:
    print('Directory not exists')
    os.makedirs('./saveImg')

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
user = friends[0]["UserName"]

num = 0
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open('./saveImg' + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

ls = os.listdir('./saveImg')
each_size = int(math.sqrt(float(640*640)/len(ls)))
lines = int(640/each_size)
image = Image.new('RGB', (640, 640))
x = 0
y = 0
for i in range(0,len(ls)+1):
    try:
        img = Image.open('./saveImg' + "/" + str(i) + ".jpg")
        if img.mode != "RGB":
            img = img.convert("RGB")
    except IOError:
        print(i)
        print("Error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save('./saveImg/' + 'all.jpg')
itchat.send_image('./saveImg/'+ 'all.jpg', 'filehelper')