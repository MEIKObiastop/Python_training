#手書き文字を読み取って何の数字か判定するアプリ

import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image,ImageOps
import PIL.ImageTk
from sklearn import datasets, svm
import numpy as np
import matplotlib.pyplot as plt #fromとimportを使った読み込みが理解できていない

last_x,last_y=None,None #当初は分けていたけど1文で表記可能


def start_draw(event):
    global last_x,last_y
    last_x=event.x
    last_y=event.y

def draw(event):
    global last_x,last_y
    canvas.create_line(last_x,last_y,event.x,event.y,fill="black",width=3,capstyle=tk.ROUND,smooth=True)
    last_x=event.x
    last_y=event.y

def clear_canvas():
    canvas.delete("all")

#キャンバス画像→特徴量データへ
def imageToData():
    #保存して読み込み
    canvas.postscript(file="temp.eps")
    image=Image.open("temp.eps").convert("L")
    image=ImageOps.invert(image)
    image=image.resize((8,8),Image.BICUBIC)#精度のためLANCZOS→BICUBICに変更
    
    image=np.array(image)
    
    image=255-image
    image=16-(image/255*16.0)
    image=np.clip(image,0,16)#念のため値の範囲を制限
    flat=image.flatten()
    return flat

#判定ボタン
def predictDigits():
    data=imageToData()
    n=clf.predict([data])[0]
    result_label.config(text="この画像は、「"+str(n)+"」です！")

# 学習済みモデルの準備（scikit-learn の digits データで学習）
digits = datasets.load_digits()
X, y = digits.data, digits.target
clf = svm.SVC(gamma=0.001, C=100.0)
clf.fit(X, y)


#ウィンドウを作る
root=tk.Tk()
root.title("数字を書こう")
root.geometry("300x250")

#描画エリアを作る
canvas=tk.Canvas(root,width=120,height=120,bg="white")#読み取り精度のため画面は小さめ
canvas.pack()

#ドラッグで描画
canvas.bind("<Button-1>",start_draw)
canvas.bind("<B1-Motion>",draw)

#クリアボタン
btn_clear=tk.Button(root,text="書き直す",command=clear_canvas)
btn_clear.pack()

#判定ボタン
btn_predict=tk.Button(root,text="判定！",command=predictDigits)
btn_predict.pack()

#予測結果を表示するラベル
result_label=tk.Label(text="手書きの数字を認識します！")
result_label.pack()


root.mainloop()

