#This is drowing clover program.　これはクローバーを描画するプログラムです
#「Pyhon1年生」の、P.54-P.60を参考にしています

from turtle import*
shape("turtle")
color("green")#単色指示の場合は"="は付けない
for i in range(4):
    forward(100)
    circle(50,180)#半円を描画する
    right(90)#向きを変える/本の表現上、右向きに進行かと思い迷った
    circle(50,180)
    forward(100)
right(90)#ここから茎
forward(100)
circle(120,130)
left(90)
forward(5)
left(90)
circle(-115,110)#茎が線だけでは味気なかったので追加
done()
#位置を揃えようと"#"の前にスペースを入れるとエラーになる＞＜
