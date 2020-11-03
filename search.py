
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv
# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    
    with open("fruits.csv") as f:
        for row in csv.reader(f):
            print(f"{row}")

    source = row

    word =input("フルーツを入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        print('見つかりません')
        source.append(word)
        print(source)

if __name__ == "__main__":
    search()