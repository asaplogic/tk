import Tkinter as tk
import ttk

LARGE_FONT = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):
    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        #title display
        tk.Tk.wm_title(self, "Sea of BTC client")
        container = tk.Frame(self)

        container.pack(side="top", fill ="both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        #add new page here
        for F in (StartPage, Page_one,Page_two):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0,column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print param

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text ="Start Page", font = LARGE_FONT)
        label.pack(pady=80,padx=80)

        button1 = ttk.Button(self, text ="Page 1",
                command =lambda:controller.show_frame(Page_one))
        button1.pack()

        button2 = ttk.Button(self, text ="Visit Page 2",
                command =lambda:controller.show_frame(Page_two))
        button2.pack()



class Page_one(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="This Is Page One", font = LARGE_FONT)
        label.pack(pady=80,padx=80)

        button1 = ttk.Button(self, text ="Lets Go Home!",
                command =lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text ="Visit Page 2",
                command =lambda:controller.show_frame(Page_two))
        button2.pack()
#copy and paste for new pageç 
class Page_two(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="This Is Page two", font = LARGE_FONT)
        label.pack(pady=80,padx=80)

        button1 = ttk.Button(self, text ="Lets Go Home!",
                command =lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text ="Visit Page 1",
                command =lambda:controller.show_frame(Page_one))
        button2.pack()





app = SeaofBTCapp()
app.mainloop()
