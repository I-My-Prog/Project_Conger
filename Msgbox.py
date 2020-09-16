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
    elif code == 200:
        messagebox.showerror('エラー code:'+str(code),'Unknown')
    elif code == 201:
        messagebox.showerror('エラー code:'+str(code),'無効な入力：'+str(option))
    elif code == 202:
        messagebox.showerror('エラー code:'+str(code),'銘柄リストに存在しない銘柄が指定：'+str(option))