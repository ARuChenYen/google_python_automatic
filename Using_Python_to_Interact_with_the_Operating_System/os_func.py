'''
一、OS Moudule可以做很多事情，像是移動刪除或者複製檔案
二、os.path可以得到很多檔案的訊息
    不用死背，但要會查文件
'''

import os

os.remove('file.txt')
#刪除檔案

os.rename('file.txt')
#重新命名

os.path.exists('file.txt')
#確認檔案是否存在。是retuen True，否return False

os.path.getsize('file.txt')
#確認檔案大小bytes

os.path.getmtime('file.txt')
#得到Unix timestamp，從1970/1/1到今天的時間
#因為不會有檔案早於這個時間，所以用daytime轉成易讀的模式

import datetime
timestamp = os.path.getmtime('file.txt')
datetime.datetime.fromtimestamp(timestamp)
#用datetime轉換成讓人較容易讀的模式

os.path.abspath('file.txt')
#取得絕對路徑

os.getcwd()
#取得現在的路徑位址

os.mkdir('new_dir')
#建立一個名為new_dir的資料夾

os.chdir('change_dir')
#改變目前指向位址

os.rmdir('dir')
#移除路徑資料夾，但只有在路徑中完全沒有檔案才能用

os.listdir('dir')
#列出路徑資料夾中的所有物件，但可能是檔案或者路徑
#因此用os.path.isdir()檢查是不是路徑

os.path.join(dir,file_name)
#列出檔案的完整路徑
#可以跨平台的列出檔案路徑而不會有問題 (os, linux用\,而window用/)
