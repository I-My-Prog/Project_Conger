from tkinter import messagebox
'''
    メッセージボックス定義
    警告=3xx　エラー=2xx　注意=1xx　情報=0xx (x=[0-9])
    
    エラー
        200 > 未知のエラー(標準)
    情報
        001 > 
'''
def msgbox(code=200,option=0):
    if code == 0:
        messagebox.showerror('エラー', 'エラーが発生しました')
    elif code == 2:
        messagebox.showinfo('情報 code:'+str(code),'出力：'+str(option))
    elif code == 5:
        messagebox.showinfo('情報 code:'+str(code),'スクレイピングの実行が完了しました')
    elif code == 6:
        messagebox.showinfo('情報 code:'+str(code),'CSVの出力が完了しました')
    elif code == 11:
        messagebox.showinfo('情報 code:'+str(code),'銘柄'+str(option)+'を登録しました')
    elif code == 200:
        messagebox.showerror('エラー code:'+str(code),'Unknown')
    elif code == 201:
        messagebox.showerror('エラー code:'+str(code),'無効な入力：'+str(option))
    elif code == 202:
        messagebox.showerror('エラー code:'+str(code),'銘柄リストに存在しない銘柄が指定：'+str(option))
    elif code == 206:
        messagebox.showerror('エラー code:'+str(code),'銘柄'+str(option)+'のページが存在しません')
    elif code == 207:
        messagebox.showerror('エラー code:'+str(code),'銘柄'+str(option)+'のページを解析できません\n上場廃止銘柄の可能性があります')