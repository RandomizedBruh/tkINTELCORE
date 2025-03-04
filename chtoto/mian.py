import tkinter as tk

root = tk.Tk()
root.title = "Программс"
root.geometry("400x300")

# root.iconbitmap(default="./limonch.ico")
# metanit.com

count = 0

def handlePop():
    global count
    count = count +1
    print("HAHA U can't LEAVE")
    label["text"] = f"click {count}"
    if count > 40:
        label["background"] = "red"


iconFromPhoto = tk.PhotoImage(file="./5RUBLESFNFWHAAT.png")
root.iconphoto(False,iconFromPhoto)




root.minsize(200,200)
root.maxsize(800,800)

root.resizable(True, False) 



label = tk.Label(root,text=f"prevet {count}", font =20, foreground="green", background="yellow")
label.pack()

topFrame = tk.Frame(root, width=200 ,height=100, background="blue",padx=20, pady=30)
topFrame.pack()


button = tk.Button(topFrame, text="Close dis shhhh....", background="red", command=handlePop)
button.pack()


check = tk.Checkbutton(topFrame, text="CHECKPOINT")
check.pack()



root.mainloop()