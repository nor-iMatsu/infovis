# infovis

## Description
* 2016年アメリカ大統領選挙の開票速報ライブ中継を，同時刻にTwitter上でつぶやかれた単語のトレンドとともに視聴できるシステム
* 選挙の趨勢とつぶやきのトレンドが対応づけて一目で見られる
  
  * ex) ある州の結果が出た直後にその州名が一斉につぶやかれる，両候補者の名前がつぶやかれた数から選挙の趨勢が予想できる，など

### Program Description
* Gather_tweet, Gather_tweet2, Gather_tweet3にはそれぞれ序盤・中盤・終盤のデータファイルを作成するためのプログラムが入っている。
* % (Name of input/output file) -> Name of program file -> ...

  * (twitter_stream.sqlite) -> separate_Database.py -> (output*.json) -> analyze.py -> (hist_per_minute*.json)
  * (twitter_stream.sqlite) -> twitter_db_hist.py -> (hist*.csv)

## Demo
![demo](infovis.gif)
