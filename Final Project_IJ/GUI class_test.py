from breezypythongui import EasyFrame
import tkinter as tk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Label, Button, StringVar, DoubleVar, messagebox
        
class MainFrame(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        
        money_clip_label = self.addLabel("Money Clip", row=0, column=1,columnspan = 2)
        
        money_clip_label["font"] = ("Arial", 40)
        money_clip_label["foreground"] = "#385492"
        money_clip_label["background"] = "#7FE7FE"
        money_clip_label.place(x=350, y=10)

        self.round_w = 0
        self.round_1 = 0
        

        self.background_image = PhotoImage(file="image/main_background_re.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window

        money_clip_label = Label(self, text="Money Clip", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        money_clip_label.place(x=350, y=10)
        
        
    def round_won(self):
        pass
    def round_lost(self):
        pass

class CreatePlan(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
            
def start_create_plan():
    global create_plan_window
    create_plan_window = Create_plan()
    create_plan_window.grid(row=0, column=0, sticky ="NSEW")
    finish_btn = tk.Button(create_plan_window, text="Back to main", command=finish_create_plan)
    finish_btn.grid(row=0, column=0)
    
def finish_create_plan():
    create_plan_window.grid_forget()

def input_spending():
        pass
    
def check_status():
        pass    


def main() :
    # Create the main window
    root = tk.Tk()
    main_window = MainFrame()
    main_window.grid(row=0, column=0)

    # Setting the position of buttons on the screen
    plan_button_img = PhotoImage(file="image/Botton1.png")
    spend_button_img = PhotoImage(file="image/Botton2.png")
    status_button_img = PhotoImage(file="image/Botton3.png")
    plan_button_img = plan_button_img  # Keep a reference

    # Create the match window
    match_window = None
    create_plan_window = None

    # Create the buttons
    plan_button = Button(main_window, image=plan_button_img, borderwidth=0, highlightthickness=0, command=start_create_plan)
    spend_button = Button(main_window, image=spend_button_img, borderwidth=0, highlightthickness=0, command=input_spending)
    status_button = Button(main_window, image=status_button_img, borderwidth=0, highlightthickness=0, command=check_status)

    # Associate the start_btn with the main window    
    start_btn = tk.Button(main_window, text="Start Match", command=start_match)
    start_btn.grid(row=0, column=0)


    # Place the buttons on the screen
    plan_button.place(x=83, y=13)
    spend_button.place(x=500, y=206)
    status_button.place(x=36, y=405)

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()  

    