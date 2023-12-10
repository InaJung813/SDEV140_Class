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

        # add CreatePlan button
        create_plan_button = self.addButton(text="Create Plan", row=1, column=1, command=self.start_create_plan)
        # add Spend button
        spend_button = self.addButton(text="Spend", row=1, column=2, command=self.start_spend)
        # add CheckStatus button
        check_status_button = self.addButton(text="Check Status", row=1, column=3, command=self.start_check_status)

    def start_create_plan(self):
        create_plan_window = CreatePlan()
        create_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def start_spend(self):
        spend_window = Spend()
        spend_window.grid(row=0, column=0, sticky ="NSEW")

    def start_check_status(self):
        check_status_window = CheckStatus()
        check_status_window.grid(row=0, column=0, sticky ="NSEW")


class CreatePlan(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        # add TextBox in certer of the screen
        self.addLabel(text="Make Your Plan", row=0, column=10, font=("Arial", 30) )
        # add CreateNewPlan button
        create_new_plan_button = self.addButton(text="Create New Plan", row=1, column=10, command=self.start_add_new_plan)
        # add ChangePlan button
        change_plan_button = self.addButton(text="Change Plan", row=2, column=10, command=self.start_change_plan)
        # add finish button
        finish_btn = tk.Button(self, text="Back to main", command=self.finish_create_plan)
        finish_btn.grid(row=0, column=0)

    def start_add_new_plan(self):
        create_new_plan_window = CreateNewPlan()
        create_new_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def start_change_plan(self):
        change_plan_window = ChangePlan()
        change_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def finish_create_plan(self):
        self.grid_forget()

class CreateNewPlan(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        # add finish button
        finish_btn = tk.Button(self, text="Finish", command=self.finish_add_new_plan)
        finish_btn.grid(row=0, column=0)

    def finish_add_new_plan(self):
        self.grid_forget()

class ChangePlan(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        # add finish button
        finish_btn = tk.Button(self, text="Finish", command=self.finish_change_plan)
        finish_btn.grid(row=0, column=0)

    def finish_change_plan(self):
        self.grid_forget()


def start_create_plan():
    global create_plan_window
    create_plan_window = CreatePlan()
    create_plan_window.grid(row=0, column=0, sticky ="NSEW")

    
def finish_create_plan():
    create_plan_window.grid_forget()

class Spend(EasyFrame):
     def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0

def start_spend():
    global spend_window
    spend_window = Spend()
    spend_window.grid(row=0, column=0, sticky ="NSEW")
    finish_btn = tk.Button(spend_window, text="Back to main", command=finish_spend)
    finish_btn.grid(row=0, column=0)

def finish_spend():
    spend_window.grid_forget()

class CheckStatus(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0

def start_check_status():
    global check_status_window
    check_status_window = CheckStatus()
    check_status_window.grid(row=0, column=0, sticky ="NSEW")
    finish_btn = tk.Button(check_status_window, text="Back to main", command=finish_check_status)
    finish_btn.grid(row=0, column=0)

def finish_check_status():
    check_status_window.grid_forget()



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
    spend_button = Button(main_window, image=spend_button_img, borderwidth=0, highlightthickness=0, command=start_spend)
    status_button = Button(main_window, image=status_button_img, borderwidth=0, highlightthickness=0, command=start_check_status)


    # Place the buttons on the screen
    plan_button.place(x=83, y=13)
    spend_button.place(x=500, y=206)
    status_button.place(x=36, y=405)

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()  

    