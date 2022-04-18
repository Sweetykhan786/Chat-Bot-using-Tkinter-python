from tkinter import*
r=Tk()
r.configure(background="pink")

# print(r)

def send():
    send = "you->"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=='hii' or e.get()=='Hello' or e.get()=="Hi"):
        txt.insert(END,'\n'+'\t'+"Bot-> Hello!, How can we help you?")
    elif (e.get()=='I want to know about Navgurukul?'):
        txt.insert(END,"\n"+'\t'+"Bot-> Sure! Navgurukul is a free Software Development course")
    elif (e.get()=='How many year is this course?'):
        txt.insert(END,"\n"+'\t'+"Bot-> One year course")
    elif (e.get()=='What are the languages you are learning?'):
        txt.insert(END,"\n"+'\t'+"PYTHON, JAVASCRIPT,HTML and CSS")
    elif (e.get()=='Thank you'):
        txt.insert(END,"\n"+'\t'+"Bot-> Do Visit Again")
    else:
        txt.insert(END,"\n"+'\t'"Bot-> Sorry I didn't get you?")
    e.delete(0,END)
txt = Text(r)
txt.grid(row=0,column=0)
e=Entry(r,width=80,bg="purple",fg="white")
send=Button(r,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
r.title("CHATBOT")
r.mainloop()
