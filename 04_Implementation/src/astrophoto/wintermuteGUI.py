import tkinter
from tkinter import ttk
import workflow

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
camerainterfacelist = 'a' 
inames = tkinter.StringVar(value=camerainterfacelist)
interfacelist = tkinter.Listbox(addDevFrame, listvariable=inames, height=5)
session = workflow.Session()

def addDeviceOkBtnClicked():
    selectionlist = interfacelist.curselection()
    strindex = selectionlist[0]
    index = int(strindex)
    selectedInterface = camerainterfacelist[index]
    session.createCameraConfiguration()

def addDevice():
    plancont.grid_forget()
    namelist = workflow.getInterfaceNames()
    camerainterfacelist = tuple(namelist)
    inames = tkinter.StringVar(value=camerainterfacelist)
    addDevFrame.grid(column=0, row=0)
    okbtn = tkinter.Button(addDevFrame, text='ok', command=addDeviceOkBtnClicked)
    okbtn.grid(column=0, row=1, sticky=tkinter.W)
    interfacelist.grid(column=0, row=2, rowspan=6, sticky=(tkinter.N,tkinter.S,tkinter.E,tkinter.W))

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

