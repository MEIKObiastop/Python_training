#nameが筋トレすることでマッチョになる物語プログラム

import random

#トレーニング辞書を作成
traning_menu = {"バーピー":7,"スクワット":5,"ベンチプレス":3,"ジョギング":1}

#trainyのクラスを作る
class Trany:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.strength = 0
    
    def training(self): #トレーニングする関数を作る(ランダム)
        exersise = random.choice(list(self.menu.keys()))
        streng = self.menu[exersise]
        self.strength += streng
        print(f"{self.name}は{exersise}をした！")
    
    def muscle(self): #筋トレの進捗
        if 7 < self.strength < 10:
            print(f"{self.name}はまだまだひょろひょろだ！")
        elif 13 < self.strength < 17:
            print(f"{self.name}はそこそこマッチョになってきた！")
        elif self.strength == 20:
            print(f"{self.name}は少し疲れてきた・・・")

traning_menu["腕立て伏せ"] = 2

thin = Trany("ひょろっぴ", traning_menu)

while thin.strength <= 25: #筋トレをする/25でマッチョだ！
    thin.training()
    thin.muscle() #trainingとmuscleを順番に呼び出す

print(f"{thin.name}はマッチョになった！！むきむき！！")
#筋トレをして最終的にマッチョになる