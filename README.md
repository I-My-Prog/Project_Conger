# Project_Conger
株式情報のスクレイピング
## ファイル一覧
|ファイル名|内容|状態|
|:---|:---|:---:|
|a.py|Tkinterのサンプル|削除予定|
|AD_List.csv|ADのカラム一覧、コピペ要員|編集禁止|
|Alchemy_Setting.py|SQLAlchemyの設定情報|開発完了|
|Alchemy.py|SQLの操作、データモデルの定義|開発中|
|Command.py|Edit_Windowのボタンに関連付けたコマンドの処理|開発中|
|DB.sqlite|データベースファイル|編集禁止|
|Edit_Window.py|登録画面制御、メインモジュール|開発停止|
|Msgbox.py|メッセージモジュール|開発停止|
|README.md||編集継続|
|Scrape.py|スクレイピングモジュール|開発中|

## スクレイプロジック
|Order|使用モジュール|実行内容|引数|返り値|
|:---:|:---|:---|:---|:---|
|1|Commamd.run()|Alchemy.BL_sel()を実行する|-|-|
|2|Alchemy.BL_sel()|指定されたnumberのデータをBLから読み出す|int(number)|-|
|3|Scrape.main()|引数のリストデータに基づいてHTMLを取得、分析|list()|-|
|4|Scrape.main()|分析結果をリストデータで渡す|-|list()|
|5|Alchemy.BL_sel()|分析結果リスト(4の返り値)をAD_insに渡す|-|-|
|6|Alchemy.AD_ins()|ADにデータを書き込む|list()|-|
|7|Alchemy.BL_sel()|終了|-|-|
|8|Commamd.run()|Alchemy.export()を実行する|-|-|
|9|Alchemy.export()|ADを読み取ってCSVに出力する|-|-|
