import tkinter

root = tkinter.Tk()
content= tkinter.Frame(root)
newprojcont = tkinter.Frame(root)
l1 = tkinter.Label(newprojcont, text='projectname')
e1 = tkinter.Entry(newprojcont)
cancel = tkinter.Button(newprojcont, text='cancel')


def newprojOkBtnClicked():
    pass
    

def startup2newproject():
    content.grid_remove()
    newprojcont.grid(column=0, row=0)
    l1.grid(column=0, row=0)
    e1.grid(column=1, row=0)
    cancel.grid(column=1, row=3)
    ok = tkinter.Button(newprojcont, text='ok', command=newprojOkBtnClicked)
    ok.grid(column=2, row=3)
    root.geometry("500x500")
   
content.grid(column=0, row=0)
newProjBtn = tkinter.Button(content, text="new project", command=startup2newproject)
newProjBtn.grid(column=0, row=0)
openProjBtn = tkinter.Button(content, text="open project")
openProjBtn.grid(column=0, row=2)

root.mainloop()

