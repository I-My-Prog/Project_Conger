from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Command
import Alchemy    #for Debug
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from Alchemy_Setting import Base,ENGINE,Session
import multiprocessing as mp
import time

def show_selection():
   for i in lb.curselection():
      print(lb.get(i))

# fontStyle_H1 = tkFont.Font("System",20)
def LB():   # Listbox
   time.sleep(0.1)
   v1 = StringVar()
   lb = Listbox(frame, listvariable=v1, height=30)
   i = 0
   for data in Alchemy.BL_sel():
      BD_zero = str(data.number).zfill(4)
      brand_data = BD_zero +" | "+ data.name
      lb.insert(i,brand_data)
      i+=1
   lb.grid(row=1, column=3,rowspan=40)
   lb.after(1000,LB)


if __name__ == '__main__':
   mp.freeze_support()
   root = Tk()
   root.title('銘柄登録ウィンドウ')
   root.resizable(False, True)
   root.columnconfigure(0, weight=1)
   root.rowconfigure(0, weight=1)

   # Frame
   frame = ttk.Frame(root, padding=5)
   frame.grid()
   
   frame.columnconfigure(0, weight=1);
   frame.rowconfigure(0, weight=1);
   # Lavel_0
   label0 = ttk.Label(frame,text="銘柄リストの編集", font=("Yu Gothic",12),anchor="w", justify='left',width =20)
   label0.grid(row=0, column=0, columnspan=2)

   # Brand_Label
   label1 = ttk.Label(frame,text="銘柄入力")
   label1.grid(row=1, column=0, columnspan=1)

   # Bland_Input
   entry = StringVar()
   B_input = ttk.Entry(
      frame,
      textvariable = entry,
      width =20,
   )
   B_input.grid(row=1, column=1, columnspan=1)

   # Add_Button
   add_button = ttk.Button(frame,text="追加　=>",command=lambda: Command.add(entry.get()))
   add_button.grid(row=1, column=2, columnspan=1)

   # Remove_Button
   remove_button = ttk.Button(frame,text="削除　<=",command=lambda: Command.remove(entry.get()))
   remove_button.grid(row=2, column=2, columnspan=1)
   
   # Run_Button
   run_button = ttk.Button(frame,text="スクレイプ実行",command=lambda: Command.run(entry.get()))
   run_button.grid(pady=6,row=4, column=0, columnspan=3,sticky="nsew")

   # Exit_Button
   exit_button = ttk.Button(frame,text="プログラムを終了",command=lambda: Command.ext(entry.get()))  #extはわざと。exitは予約語のため。
   exit_button.grid(pady=0,row=5, column=0, columnspan=3,sticky="nsew")

   # ClsAD_Button(Debug)
   clsad_button = ttk.Button(frame,text="ADクリア(DB)",command=lambda: Alchemy.AD_cls())
   clsad_button.grid(pady=0,row=6, column=0, columnspan=1,sticky="nsew")

   # CntBL_Button(Debug)
   cntbl_button = ttk.Button(frame,text="BLカウント(DB)",command=lambda: Alchemy.BL_cnt())
   cntbl_button.grid(pady=0,row=6, column=1, columnspan=1,sticky="nsew")
   LB()
   
   #Export CSV
   csv_button = ttk.Button(frame,text="CSV出力(DB)",command=lambda: Command.convert())
   csv_button.grid(pady=0,row=6, column=2, columnspan=1,sticky="nsew")
   
   root.mainloop()