from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('ImageViewer')

my_img1=ImageTk.PhotoImage(Image.open("images/pro1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("images/pro2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("images/pro3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("images/pro4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("images/pro5.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label=Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(imgno):
                global my_label
                global button_prev
                global button_next

                my_label.grid_forget()
                my_label=Label(image=image_list[imgno-1])
                button_next=Button(root,text="next", command= lambda:forward(imgno+1))
                button_prev=Button(root,text="prev", command= lambda:back(imgno-1))

                if imgno==5:
                                button_next=Button(root,text="next", state=DISABLED)
                
                my_label.grid(row=0, column=0, columnspan=3)
                button_prev.grid(row=1,column=0)
                button_next.grid(row=1,column=2)
                
def back(imgno):
                global my_label
                global button_prev
                global button_next

                my_label.grid_forget()
                my_label=Label(image=image_list[imgno-1])
                button_next=Button(root,text="next", command= lambda:forward(imgno+1))
                button_prev=Button(root,text="prev", command= lambda:back(imgno-1))

                if imgno==1:
                                button_prev=Button(root,text="prev", state=DISABLED)
                

                my_label.grid(row=0, column=0, columnspan=3)
                button_prev.grid(row=1,column=0)
                button_next.grid(row=1,column=2)



button_prev=Button(root, text="prev",command=back, state=DISABLED)
button_exit=Button(root, text="exit", command=root.quit)
button_next=Button(root, text="next",command=lambda:forward(2))

button_prev.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_next.grid(row=1,column=2)



root.mainloop()
