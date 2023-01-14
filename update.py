import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from urllib.request import urlretrieve
import zipfile
import win32api, win32con
import urllib.request


def download_and_extract():

    url = "http://download.gjjwh.cn/benti.zip"#填写下载链接，zip格式
    filename = "benti.zip"#填写压缩包名称
    # urlretrieve方法中的reporthook参数设置为update_progress函数
    urllib.request.urlretrieve(url, filename, reporthook=update_progress)
    # 解压文件
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall()

    print("下载并解压完成")
    win32api.MessageBox(0, "软件更新完成", "提醒", win32con.MB_ICONASTERISK)

    subprocess.run(["epsdl.exe"])#下载完成后需要运行的exe文件

    window.destroy()




def update_progress(count, block_size, total_size):
    # count:已经下载的块数
    # block_size:每一块的大小
    # total_size:文件总大小

    progress = count * block_size / total_size
    progress_bar['value'] = progress * 100

    window.update()


print('need download')
global window
window = tk.Tk()
window.geometry('1050x660')
window.resizable(0, 0)
window.title('EPS Launcher')
bgPath = "./img/update.png"
bgImg = ImageTk.PhotoImage(file=bgPath)
bg = tk.Label(window, width=1050, height=660, image=bgImg)
bg.pack()

progress_bar = ttk.Progressbar(window, length=500)
progress_bar.place(x=350, y=302)

download_and_extract()

window.mainloop()





