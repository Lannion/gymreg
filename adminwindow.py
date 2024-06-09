import tkinter as tk
from tkinter import ttk, messagebox

class AdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration System")
        self.root.geometry("1200x650")
        self.root.configure(background='cornsilk2')
        

        self.dash_frame = tk.Frame(root, bg='grey')
        self.dash_frame.pack(side=tk.LEFT, fill=tk.Y)  # Fill vertically
        self.dash_frame.propagate(False)  # Prevent frame from resizing to fit its contents
        self.dash_frame.configure(width=250, height=400)

        
        self.main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)  # Fill vertically
        self.main_frame.propagate(False)  # Prevent frame from resizing to fit its contents
        self.main_frame.configure(width=1150, height=700)


        self.Reg_btn = tk.Button(self.dash_frame, text='Registration', font=('Bold', 20), fg= "#158aff", bd=0, bg = "grey", padx=10, command=lambda: self.change_indicator_color(self.Reg_ind, self.Reg_page))
        self.Reg_btn.place(x = 22, y= 50)
        self.Reg_ind = tk.Label(self.dash_frame, text = "", bg= "grey")
        self.Reg_ind.place(x=3,y=50, width=8, height=50)

        self.Menu_btn = tk.Button(self.dash_frame, text='MENU', font=('Bold', 20), fg= "#158aff", bd=0, bg = "grey", padx=10, command=lambda: self.change_indicator_color(self.Menu_ind, self.Menu_page))
        self.Menu_btn.place(x = 22, y= 100)
        self.Menu_ind = tk.Label(self.dash_frame, text = "", bg= "grey")
        self.Menu_ind.place(x=3,y=100, width=8, height=50)
        
        self.Exit_btn = tk.Button(self.dash_frame, text='Exit', font=('Bold', 20), fg= "#158aff", bd=0, bg = "grey", padx=10, command=lambda: self.change_indicator_color(self.Exit_ind, self.Exit_page))
        self.Exit_btn.place(x = 22, y= 600)
        self.Exit_ind = tk.Label(self.dash_frame, text = "", bg= "grey")
        self.Exit_ind.place(x=3,y=600, width=8, height=50)

    


    def change_indicator_color(self, label, page):
        self.hide_indicator()
        label.config(bg="#158aff")
        self.delete_page()
        page()

    def hide_indicator(self):
        self.Reg_ind.config(bg="grey")  
        self.Menu_ind.config(bg="grey")
        self.Exit_ind.config(bg="grey")          

    def Reg_page(self):
        Reg_frame = tk.Frame(self.main_frame)



        lb= tk.Label(Reg_frame, text="Gym Registration", padx= 10 ,font= ("times new roman", 15))
        lb.pack()



        Reg_frame.pack(pady=20)

    def Menu_page(self):
        Menu_frame = tk.Frame(self.main_frame)



        lb= tk.Label(Menu_frame, text="Menu\n\nPage: 1", font= ("times new roman", 20))
        lb.pack()



        Menu_frame.pack(pady=20)  

    def Exit_page(self):
        Exit_frame = tk.Frame(self.main_frame)



        lb= tk.Label(Exit_frame, text="Exit", font= ("times new roman", 20))
        lb.pack()



        Exit_frame.pack(pady=20)     

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()            

if __name__ == "__main__":
    root = tk.Tk()
    obj = AdminWindow(root)
    root.mainloop()
