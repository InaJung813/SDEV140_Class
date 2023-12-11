from breezypythongui import EasyFrame
import tkinter as tk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Label, Button, StringVar, DoubleVar, messagebox

import json
from datetime import datetime as dt


class Plan():
    def __init__(self, name, amount, start_date, end_date):
        date_format = "%Y-%m-%d"
        self.name = str(name)
        self.amount = float(amount)
        self.start_date = dt.strptime( start_date, date_format ) 
        self.end_date = dt.strptime( end_date, date_format )

        self.spendings = list()

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date
    
    def get_spendings(self):
        return self.spendings
    
    def add_spendings(self, spending):
        self.spendings.append(spending)

    def __str__(self):
        return "Plan: {}, Amount: {}, Start Date: {}, End Date: {}".format(self.name, self.amount, self.start_date, self.end_date)

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
        self.addLabel(text="Make Your Plan", row=0, column=10, font=("Arial", 30) ).place(x=300, y=10)
        # add buttons
        self.addButton(text="Create New Plan", row=1, column=10, command=self.start_add_new_plan).place(x=100, y=100)
        self.addButton(text="Change Plan", row=2, column=10, command=self.start_change_plan).place(x=100, y=200)
        self.addButton(text="Finish", row=0, column=0, command=self.finish_create_plan).place(x=0, y=0)

    def start_add_new_plan(self):
        create_new_plan_window = CreateNewPlan()
        create_new_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def start_change_plan(self):
        change_plan_window = ChangePlan()
        change_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def finish_create_plan(self):
        self.grid_forget()

def start_create_plan():
    global create_plan_window
    create_plan_window = CreatePlan()
    create_plan_window.grid(row=0, column=0, sticky ="NSEW")

class CreateNewPlan(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        
        # add TextBox in certer of the screen
        self.addLabel(text="Create New Plan", row=0, column=10, font=("Arial", 30) ).place(x=300, y=10)
        self.addLabel(text="New Plan", row=0, column=10, font=("Arial", 30) ).place(x=350, y=70)

        # add labels and textboxs
        self.addLabel(text="Plan Name", row=0, column=10, font=("Arial", 15) ).place(x=100, y=150)
        self.plan_name = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_name.place(x=300, y=150)
        self.addLabel(text="Budget Amount", row=0, column=10, font=("Arial", 15) ).place(x=100, y=200)
        self.plan_amount = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_amount.place(x=300, y=200)
        self.addLabel(text="Start Date", row=0, column=10, font=("Arial", 15) ).place(x=100, y=250)
        self.plan_start_date = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_start_date.place(x=300, y=250)
        self.addLabel(text="End Date", row=0, column=10, font=("Arial", 15) ).place(x=100, y=300)
        self.plan_end_date = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_end_date.place(x=300, y=300)

        # add Buttons
        self.addButton(text="Create", row=0, column=10, command=self.create_new_plan).place(x=300, y=350)
        self.addButton(text="Cancel", row=0, column=10, command=self.cancel_new_plan).place(x=400, y=350)
        self.addButton(text="Finish", row=0, column=0, command=self.finish_add_new_plan).place(x=0, y=0)

    def create_new_plan(self):
        # get the input
        plan_name = self.plan_name.getText()
        plan_amount = self.plan_amount.getText()
        plan_start_date = self.plan_start_date.getText()
        plan_end_date = self.plan_end_date.getText() 

        # check if the input is valid
        if plan_name == "" or plan_amount == "" or plan_start_date == "" or plan_end_date == "":
            messagebox.showinfo("Create New Plan", "Please fill in all the blanks!")
            return
        # check if the date is valid
        date_format = "%Y-%m-%d"
        try:
            dt.strptime( plan_start_date, date_format )
            dt.strptime( plan_end_date, date_format ) 
        except ValueError:
            messagebox.showinfo("Create New Plan", "Please enter date in the format YYYY-MM-DD!")
            return
        if plan_start_date > plan_end_date:
            messagebox.showinfo("Create New Plan", "Start date should be earlier than end date!")
            return
        if float(plan_amount) < 0:
            messagebox.showinfo("Create New Plan", "Amount should be positive!")
            return
        
        # create new plan
        new_plan = Plan(plan_name, plan_amount, plan_start_date, plan_end_date)
        plans.append(new_plan)
        print(str(new_plan))

        # clear the input
        self.plan_name.setText("")
        self.plan_amount.setText("")
        self.plan_start_date.setText("")
        self.plan_end_date.setText("")
        messagebox.showinfo("Create New Plan", "Create New Plan Successfully!")

    def cancel_new_plan(self):
        self.plan_name.setText("")
        self.plan_amount.setText("")
        self.plan_start_date.setText("")
        self.plan_end_date.setText("")
        messagebox.showinfo("Create New Plan", "Cancel New Plan Successfully!")

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


class Spend(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        # add finish button
        finish_btn = tk.Button(self, text="Finish", command=self.finish_spend)
        finish_btn.grid(row=0, column=0)

    def finish_spend():
        spend_window.grid_forget()

    def input_spending():
        pass

def start_spend():
    global spend_window
    spend_window = Spend()
    spend_window.grid(row=0, column=0, sticky ="NSEW")
    finish_btn = tk.Button(spend_window, text="Back to main", command=finish_spend)
    finish_btn.grid(row=0, column=0)

class CheckStatus(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        # add finish button
        finish_btn = tk.Button(self, text="Finish", command=self.finish_check_status)
        finish_btn.grid(row=0, column=0)

    def finish_check_status(self):
        self.grid_forget()

def start_check_status():
    global check_status_window
    check_status_window = CheckStatus()
    check_status_window.grid(row=0, column=0, sticky ="NSEW")
    finish_btn = tk.Button(check_status_window, text="Back to main", command=finish_check_status)
    finish_btn.grid(row=0, column=0)

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

    # Create the buttons
    plan_button = Button(main_window, image=plan_button_img, borderwidth=0, highlightthickness=0, command=start_create_plan)
    spend_button = Button(main_window, image=spend_button_img, borderwidth=0, highlightthickness=0, command=start_spend)
    status_button = Button(main_window, image=status_button_img, borderwidth=0, highlightthickness=0, command=start_check_status)

    # Place the buttons on the screen
    plan_button.place(x=83, y=13)
    spend_button.place(x=500, y=206)
    status_button.place(x=36, y=405)

    # add finish button
    finish_btn = tk.Button(main_window, text="Finish", command=root.destroy)
    finish_btn.grid(row=0, column=0)

    global plans
    plans = list()

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()  

    