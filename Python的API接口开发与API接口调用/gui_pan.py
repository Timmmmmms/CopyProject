# -*- coding:utf-8 -*-
from tkinter import *
from tkinter.filedialog import *
import urllib

def upload():
    filename = askopenfilename()
    url = ' http://127.0.0.1:5000/upload'
    data = '''------WebKitFormBoundarye6aUDkxZAlL9VBJ8
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: application/octet-stream

[file]
------WebKitFormBoundarye6aUDkxZAlL9VBJ8--'''%filename.split('/'[-1])
    file = open(filename,'rb').read()
    data = bytes(data)
    data = data.replace(bytes('[file]'),file)
    req = urllib.Request(url)
    req.add_header('Content-Type','multipart/form-data; boundary=----WebKitFormBoundarye6aUDkxZAlL9VBJ8')
    html = urllib.urlopen(req,data=data).read()
    print(html)


root = Tk()
root.title('网盘')
ent = Entry(root,width=40) # 输入框空间
ent.grid()
btn_upload = Button(root,text=' 上 传 ',command=upload)
btn_upload.grid()
btn_download = Button(root,text=' 下 载 ')
btn_download.grid()
mainloop()
