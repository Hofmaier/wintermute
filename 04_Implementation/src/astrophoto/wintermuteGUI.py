import tkinter
from tkinter import ttk
import apw

root = tkinter.Tk()
content= tkinter.Frame(root)
newprojcont = tkinter.Frame(root)
l1 = tkinter.Label(newprojcont, text='projectname')
projectname = tkinter.StringVar()
e1 = tkinter.Entry(newprojcont, textvariable=projectname)
cancel = tkinter.Button(newprojcont, text='cancel')
plancont = tkinter.Frame(root)
cameracb = ttk.Combobox(plancont)
cameralbl = tkinter.Label(plancont, text='camera')
addDevFrame = tkinter.Frame(root)
camerainterfacelist = 'a', 
inames = tkinter.StringVar(value=camerainterfacelist)

def addDevice():
    plancont.grid_forget()
    interfacelist = apw.getInterfaceNames()
    camerainterfacelist = tuple(interfacelist)
    inames = tkinter.StringVar(value=camerainterfacelist)
    addDevFrame.grid(column=0, row=0)
    interfacelist = tkinter.Listbox(addDevFrame, listvariable=inames, width=300)
    interfacelist.grid(column=0, row=0)
    okbtn = tkinter.Button(addDevFrame, text='ok', command=addDeviceOkBtnClicked)
    okbtn.grid(column=0, row=1)

def newprojOkBtnClicked():
    newprojcont.grid_forget()
    plancont.grid(column=0, row=0)
    cameracb.grid(column=1, row=0)
    cameralbl.grid(column=0, row=0)
    addConfbtn = tkinter.Button(plancont,text='add camera', command=addDevice)
    addConfbtn.grid(column=2, row=0)

def startup2newproject():
    content.grid_forget()    
    newprojcont.grid(column=0, row=0)
    l1.grid(column=0, row=0)
    e1.grid(column=1, row=0)
    cancel.grid(column=1, row=3)
    ok = tkinter.Button(newprojcont, text='ok', command=newprojOkBtnClicked)
    ok.grid(column=2, row=3)
   
content.grid(column=0, row=0)
newProjBtn = tkinter.Button(content, text="new project", command=startup2newproject)
newProjBtn.grid(column=0, row=0)
openProjBtn = tkinter.Button(content, text="open project")
openProjBtn.grid(column=0, row=2)
root.geometry("500x500")

root.mainloop()

