import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import Tkinter as tk
import ttk

LARGE_FONT = ("Verdana", 12)
style.use('fivethirtyeight')

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111) #1x1x1 meaning there is just one chart
        
#animate set to 1000miliseconds at bottom function
def animate(i):
        data_list = open("AAPL.txt","r").readlines()
        print len(data_list)
        xlist =[]
        ylist =[]
        for each_line in data_list:
                print each_line
                if len(each_line) > 1:
                        x,y = each_line.split(',')
                        xlist.append(int(x))
                        ylist.append(float(y))
        a.clear()
        a.plot(xlist,ylist)

class stock_chart(tk.Tk):
    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        #title display
        tk.Tk.wm_title(self, "Stock Graph")
        container = tk.Frame(self)

        container.pack(side="top", fill ="both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        #add new page here
        for F in (StartPage, Page_one,Page_two,Page_three):

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

        button2 = ttk.Button(self, text ="Page 2",
                command =lambda:controller.show_frame(Page_two))
        button2.pack()

        button3 = ttk.Button(self, text ="Graph",
                command =lambda:controller.show_frame(Page_three))
        button3.pack()


#home page
class Page_one(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="This Is Page One", font = LARGE_FONT)
        label.pack(pady=80,padx=80)

        button1 = ttk.Button(self, text ="Page 1",
                command =lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text ="Page 2",
                command =lambda:controller.show_frame(Page_two))
        button2.pack()

        button3 = ttk.Button(self, text ="Graph",
                command =lambda:controller.show_frame(Page_three))
        button3.pack()

#copy and paste for new page
class Page_two(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="This Is Page two", font = LARGE_FONT)
        label.pack(pady=80,padx=80)

        button1 = ttk.Button(self, text ="Lets Go Home!",
                command =lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text ="Page 1",
                command =lambda:controller.show_frame(Page_one))
        button2.pack()

        button3 = ttk.Button(self, text ="Graph",
                command =lambda:controller.show_frame(Page_three))
        button3.pack()
#graph page
class Page_three(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Graph Page", font = LARGE_FONT)
        label.pack(pady=80,padx=80)

        button1 = ttk.Button(self, text ="Lets Go Home!",
                command =lambda:controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)





app = stock_chart()
ani = animation.FuncAnimation(f,animate, interval = 1000)
app.mainloop()
