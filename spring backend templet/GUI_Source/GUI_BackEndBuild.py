import sys
import tkinter as tk
from tkinter import ttk
import util


class MakeFrame(tk.Frame):
    # variable
    moduleList={
        "직접입력": "",
        "회계": "financial",
        "인사": "human",
        "시스템": "system"
    }
    moduleTxt = None
    moduleDropBox = None
    menuTxt = None
    pathTxt = None
    stateLb = None

    def __init__(self, master):
        # 모듈코드, 메뉴코드, 경로, 확인버튼, 취소버튼, 설명서버튼
        moduleLb = ttk.Label(text="모듈코드", borderwidth=2, relief="ridge")
        self.moduleTxt = ttk.Entry()
        self.moduleTxt.bind("<Key>", self.moduleTxtHandler)
        self.moduleTxt.bind("<FocusOut>", self.moduleTxtHandler)
        self.moduleTxt.bind("<Return>", self.moduleTxtHandler)
        self.moduleDropBox = ttk.Combobox(value=list(self.moduleList.keys()), state="readonly")
        self.moduleDropBox.current(0)
        self.moduleDropBox.bind("<<ComboboxSelected>>", self.dropDownHendler)
        menuLb = ttk.Label(text="메뉴코드", borderwidth=2, relief="ridge")
        self.menuTxt = ttk.Entry()
        self.menuTxt.bind("<FocusOut>", self.menuTxtHandler)
        self.menuTxt.bind("<Return>", self.menuTxtHandler)
        pathLb = ttk.Label(text="경로", borderwidth=2, relief="ridge")
        self.pathTxt = ttk.Entry()
        confirmBtn = ttk.Button(text="confirm", command=self.confirmClick)
        cancelBtn = ttk.Button(text="cancel", command=self.cancelClick)

        self.stateLb = ttk.Label(border=2, relief="ridge", wraplength=330)

        # set widget position
        moduleLb.place(x=20, y=20, width=70, height=25)
        self.moduleTxt.place(x=100, y=20, width=120, height=25)
        self.moduleDropBox.place(x=230, y=20, width=120, height=25)
        menuLb.place(x=20, y=50, width=70, height=25)
        self.menuTxt.place(x=100, y=50, width=250, height=25)
        pathLb.place(x=20, y=80, width=70, height=25)
        self.pathTxt.place(x=100, y=80, width=250, height=25)
        confirmBtn.place(x=20, y=110, width=70, height=25)
        cancelBtn.place(x=100, y=110, width=70, height=25)

        self.stateLb.place(x=20, y=140, width=330, height=100)

    def confirmClick(self):
        if(tk.Entry.get(self.pathTxt)[-1] != '.'):
            self.pathTxt.insert(len(tk.Entry.get(self.pathTxt)), '.')

        fileData = {
            "moduleName": tk.Entry.get(self.moduleTxt),
            "menuCodeU": tk.Entry.get(self.menuTxt).upper(),
            "menuCodeL": tk.Entry.get(self.menuTxt).lower(),
            "path": tk.Entry.get(self.pathTxt)
        }

        try:
            # print(fileData)
            util.makeDirtory(fileData)
            util.makeFiles(fileData)
            madePath = util.folderMove(fileData)
            
            self.stateLb["text"] = f"""
SUCCESS
생성 경로 => {madePath}
"""
        except Exception as e:
            self.stateLb["text"] = f"""
FAILURE
error => {e}
"""

    def cancelClick(self):
        sys.exit()

    def dropDownHendler(self, event):
        self.moduleTxt.delete(0, "end")
        self.moduleTxt.insert(0, self.moduleList[self.moduleDropBox.get()])
        self.menuTxt.delete(0, "end")
        self.pathTxt.delete(0, "end")
        self.stateLb["text"] = ""
        
    def moduleTxtHandler(self, event):
        self.moduleDropBox.set("직접입력")
        self.menuTxt.delete(0, "end")
        self.pathTxt.delete(0, "end")
        self.stateLb["text"] = ""
        if(len(tk.Entry.get(self.moduleTxt)) > 0 and len(tk.Entry.get(self.menuTxt)) > 0):
            self.setPathTxt()

    def menuTxtHandler(self, event):
        self.pathTxt.delete(0, "end")
        self.stateLb["text"] = ""
        if(len(tk.Entry.get(self.moduleTxt)) > 0 and len(tk.Entry.get(self.menuTxt)) > 0):
            self.setPathTxt()

    def setPathTxt(self):
        self.stateLb["text"] = ""
        self.pathTxt.delete(0, "end")
        self.pathTxt.insert(0, util.makePath(tk.Entry.get(self.moduleTxt), tk.Entry.get(self.menuTxt)))

def main():
    root = tk.Tk()
    root.title("BackTemplet(ver.2)")
    root.geometry('370x400+300+300')
    root.resizable(False, False)

    frame = MakeFrame(root)

    root.mainloop()

if __name__ == "__main__":
    main()