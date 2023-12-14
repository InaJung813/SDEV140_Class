from typing import Any
from breezypythongui import EasyFrame
import tkinter as tk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Label, Button, StringVar, DoubleVar, messagebox
from datetime import datetime as dt

# Main frame of the application, setting up the UI elements
class MainFrame(EasyFrame):
    # Initializing the main frame
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        
        # Setting up the main label
        money_clip_label = self.addLabel("Money Clip", row=0, column=1,columnspan = 2)
        money_clip_label["font"] = ("Arial", 45)
        money_clip_label["foreground"] = "#385492"
        money_clip_label["background"] = "#7FE7FE"
        money_clip_label.place(x=350, y=10)
        self.round_w = 0
        self.round_1 = 0
        
        # Setting the background image
        self.background_image = PhotoImage(file="image/main_background_re.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window
        money_clip_label = Label(self, text="Money Clip", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        money_clip_label.place(x=350, y=10)
        
     # Creating buttons for each functionality and linking them to their respective functions
     # Define functions for each button to open corresponding windows
    def start_create_plan(self):
        create_plan_window = CreatePlan()
        create_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def start_spend(self):
        spend_window = Spend()
        spend_window.grid(row=0, column=0, sticky ="NSEW")

    def start_check_status(self):
        check_status_window = CheckStatus()
        check_status_window.grid(row=0, column=0, sticky ="NSEW")
        
# Main function to initiate the application
def main() :
    global root
    global save_file_name

    # Filename for saving and loading data
    save_file_name = "plans.txt"
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
    spend_button.place(x=492, y=219)
    status_button.place(x=52, y=413)

    # add finish button
    finish_btn = tk.Button(main_window, text="Finish", height= 3, width= 5 , command=finish_main_window, fg="#385492", bg="#7FE7FE")
    finish_btn.place(x=750, y=0)

    global plans
    plans = list()

    # load data from file
    load_from_file()

    # Start the GUI
    root.mainloop()

# Class definition for the 'Create Plan' window in the application
class CreatePlan(EasyFrame):
    def __init__(self):
        # Initializing the frame with a specific size and title
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        # add TextBox in certer of the screen
        self.addLabel(text="Make Your Plan", row=0, column=10, font=("Arial", 45), background = "#F7F5F7" ).place(x=300, y=10)
        # Adding buttons for creating a new plan, changing an existing plan, and going back to the main menu
        self.addButton(text="Create New Plan", row=1, column=10,height= 12, width= 25, command=self.start_add_new_plan).place(x=120, y=150)
        self.addButton(text="Change Plan", row=2, column=10, height= 12, width= 25, command=self.start_change_plan).place(x=500, y=150)
        self.addButton(text="Back \nto Main", row=0, column=0, height=3, width=5, command=self.finish_create_plan).place(x=30, y=0)
        
    # Functions to handle button clicks: to open windows for adding a new plan, changing an existing plan, and closing this window    
    def start_add_new_plan(self):
        create_new_plan_window = CreateNewPlan()
        create_new_plan_window.grid(row=0, column=0, sticky ="NSEW")

    def start_change_plan(self):
        change_plan_window = ChangePlan()
        change_plan_window.grid(row=0, column=0, sticky ="NSEW")    

    def finish_create_plan(self):
        self.grid_forget()
        
# Global function to create and display the 'Create Plan' window
def start_create_plan():
    global create_plan_window
    create_plan_window = CreatePlan()
    create_plan_window.grid(row=0, column=0, sticky ="NSEW")
 
# Plan class to represent a financial plan with name, amount, start and end dates, and spendings    
class Plan():
    def __init__(self, name, amount, start_date, end_date):
        self.name = str(name)
        self.amount = float(amount)
        self.start_date = start_date
        self.end_date = end_date

        self.spendings = list()

    # Getter methods for retrieving plan details
    def get_name(self):
        return self.name

    def get_amount(self):
        return float(self.amount)

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date
    
    def get_spendings(self):
        return self.spendings
    
    # Method to add spending records to the plan
    def add_spendings(self, spending):
        self.spendings.append(spending)

    # String representation of the plan
    def __str__(self):
        # return "Plan: {}, Amount: {}, Start Date: {}, End Date: {}".format(self.name, self.amount, self.start_date, self.end_date) as YYYY-MM-DD
        return "Plan: {}, Amount: {}, Start Date: {}, End Date: {}".format(self.name, self.amount, self.start_date.strftime("%Y-%m-%d"), self.end_date.strftime("%Y-%m-%d"))
    
    # Setter method with validation for amount and dates
    def __setattr__(self, name, value):
        date_format = "%Y-%m-%d"
        if name == "amount":
            try:
                value = float(value)
            except ValueError:
                raise ValueError("Amount must be a float")
        elif name in ["start_date", "end_date"] and type(value) == str:  
            try:
                value = dt.strptime(value, date_format)
            except ValueError:
                raise ValueError("Date must be in format: " + date_format)
        super().__setattr__(name, value)

# Class to handle the creation of a new financial plan
class CreateNewPlan(EasyFrame):
    def __init__(self):
        # Setting up the frame with a specific size and title
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        
        # Adding title label and input fields for plan creation
        self.addLabel(text="Create New Plan", row=0, column=10, font=("Arial", 45), background = "#F7F5F7" ).place(x=300, y=10)

        # add labels and textboxs(and set the bind events)
        self.addLabel(text="Plan Name", row=0, column=10, font=("Arial", 15), background = "#F7F5F7" ).place(x=100, y=150)
        self.plan_name = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_name.place(x=300, y=150)
        self.plan_name.setText("Enter your plan name")
        self.plan_name.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="Budget Amount", row=0, column=10, font=("Arial", 15), background = "#F7F5F7" ).place(x=100, y=200)
        self.plan_amount = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_amount.place(x=300, y=200)
        self.plan_amount.setText("Enter the plan budget amount")
        self.plan_amount.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="Start Date", row=0, column=10, font=("Arial", 15), background = "#F7F5F7" ).place(x=100, y=250)
        self.plan_start_date = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_start_date.place(x=300, y=250)
        self.plan_start_date.setText("YYYY-MM-DD")
        self.plan_start_date.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="End Date", row=0, column=10, font=("Arial", 15), background = "#F7F5F7" ).place(x=100, y=300)
        self.plan_end_date = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_end_date.place(x=300, y=300)
        self.plan_end_date.setText("YYYY-MM-DD")
        self.plan_end_date.bind("<FocusIn>", self.on_entry_click)

        # Adding buttons to create, cancel a plan, and return to the main menu
        self.addButton(text="Create", row=0, column=10, height= 3, width= 5 ,command=self.create_new_plan).place(x=300, y=350)
        self.addButton(text="Cancel", row=0, column=10, height= 3, width= 5 ,command=self.cancel_new_plan).place(x=500, y=350)
        self.addButton(text="Back \nto Main", row=0, column=0, height=3, width=5, command=self.finish_add_new_plan).place(x=30, y=0)

        self.plan_name.bind("<FocusOut>", self.on_focusout)
        self.plan_amount.bind("<FocusOut>", self.on_focusout)
        self.plan_start_date.bind("<FocusOut>", self.on_focusout)
        self.plan_end_date.bind("<FocusOut>", self.on_focusout)
        
    def on_entry_click(self, event):
        #Event handler: executed when the user clicks on a text field.
        current_text = event.widget.getText()
        if current_text == "YYYY-MM-DD" or current_text == "Enter your plan name" or current_text == "Enter the plan budget amount":
            event.widget.setText("")
            event.widget["foreground"] = "black"


    def on_focusout(self, event):
        #Event handler: executed when a text field loses focus.
        if event.widget == self.plan_name and event.widget.getText() == "":
            event.widget.setText("Enter your plan name")
            event.widget["foreground"] = "grey"
        elif event.widget == self.plan_amount and event.widget.getText() == "":
            event.widget.setText("Enter the plan budget amount")
            event.widget["foreground"] = "grey"
        elif (event.widget == self.plan_start_date or event.widget == self.plan_end_date) and event.widget.getText() == "":
            event.widget.setText("YYYY-MM-DD")
            event.widget["foreground"] = "grey"
    
    # New financial plan based on user input        
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

        # clear the input
        self.plan_name.setText("Enter your plan name")
        self.plan_amount.setText("Enter the plan budget amount")
        self.plan_start_date.setText("YYYY-MM-DD")
        self.plan_end_date.setText("YYYY-MM-DD")
        messagebox.showinfo("Create New Plan", "Create New Plan Successfully!")

    # Cancellation of new plan creation
    def cancel_new_plan(self):
        self.plan_name.setText("Enter your plan name")
        self.plan_amount.setText("Enter the plan budget amount")
        self.plan_start_date.setText("YYYY-MM-DD")
        self.plan_end_date.setText("YYYY-MM-DD")
        messagebox.showinfo("Create New Plan", "Cancel New Plan Successfully!")

    def finish_add_new_plan(self):
        self.grid_forget()
        

# Class to handle the changing of a new financial plan information
class ChangePlan(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        # Set the background image for this frame
        self.background_image = PhotoImage(file="image/budget_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0

        # Adding a label for the frame's main functionality
        self.addLabel(text="Change Plan", row=0, column=10, font=("Arial", 30), background = "#F7F5F7").place(x=300, y=10)

        # Adding a Plans list drop down list
        self.addLabel(text="Plan List", row=0, column=10, font=("Arial", 15), background = "#F7F5F7").place(x=100, y=100)
        self.addLabel(text="Select a Plan \nfor change information", row=0, column=10, font=("Arial", 12), background = "#F7F5F7", foreground = "gray").place(x=100, y=120)
        self.listbox = tk.Listbox(self, width=50, height=5, selectmode=tk.SINGLE)
        self.listbox.place(x=300, y=100)
        # Inserting plans list into the listbox
        for i in range(len(plans)):
            plan = plans[i]
            self.listbox.insert(i, plan.get_name())

        # Adding labels and textboxs(and set the bind events)
        self.addLabel(text="Plan Name", row=0, column=10, font=("Arial", 15), background = "#F7F5F7").place(x=100, y=200)
        self.plan_name = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_name.place(x=300, y=200)
        self.plan_name.setText("Enter your plan name")
        self.plan_name.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="Budget Amount", row=0, column=10, font=("Arial", 15), background = "#F7F5F7").place(x=100, y=250)
        self.plan_amount = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_amount.place(x=300, y=250)
        self.plan_amount.setText("Enter the plan budget amount")
        self.plan_amount.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="Start Date", row=0, column=10, font=("Arial", 15), background = "#F7F5F7").place(x=100, y=300)
        self.plan_start_date = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_start_date.place(x=300, y=300)
        self.plan_start_date.setText("YYYY-MM-DD")
        self.plan_start_date.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="End Date", row=0, column=10, font=("Arial", 15), background = "#F7F5F7").place(x=100, y=350)
        self.plan_end_date = self.addTextField(text="", row=0, column=10, width=40)
        self.plan_end_date.place(x=300, y=350)
        self.plan_end_date.setText("YYYY-MM-DD")
        self.plan_end_date.bind("<FocusIn>", self.on_entry_click)

        # Add buttons for changing plan details, canceling changes, and returning to the main menu
        self.addButton(text="Change", row=0, column=10, height=3, width= 5, command=self.change_plan).place(x=600, y=400)
        self.addButton(text="Cancel", row=0, column=10, height=3, width= 5, command=self.cancel_change_plan).place(x=600, y=500)
        self.addButton(text="Back \nto Main", row=0, column=0, height=3, width=5, command=self.finish_change_plan).place(x=30, y=0)
        

        self.plan_name.bind("<FocusOut>", self.on_focusout)
        self.plan_amount.bind("<FocusOut>", self.on_focusout)
        self.plan_start_date.bind("<FocusOut>", self.on_focusout)
        self.plan_end_date.bind("<FocusOut>", self.on_focusout)

    
    def on_entry_click(self, event):
        #Event handler: executed when the user clicks on a text field.
        default_taxt= {
            self.plan_name : "Enter your plan name",
            self.plan_amount: "Enter the plan budget amount",
            self.plan_start_date: "YYYY-MM-DD",
            self.plan_end_date: "YYYY-MM-DD"
        }
        current_text = event.widget.getText()
        if current_text == "YYYY-MM-DD" or current_text == "Enter your plan name" or current_text == "Enter the plan budget amount":
            event.widget.setText("")
            event.widget["foreground"] = "gray"

    def on_focusout(self, event):
        #Event handler: executed when a text field loses focus.
        if event.widget == self.plan_name and event.widget.getText() == "":
            event.widget.setText("Enter your plan name")
            event.widget["foreground"] = "grey"
        elif event.widget == self.plan_amount and event.widget.getText() == "":
            event.widget.setText("Enter the plan budget amount")
            event.widget["foreground"] = "grey"
        elif (event.widget == self.plan_start_date or event.widget == self.plan_end_date) and event.widget.getText() == "":
            event.widget.setText("YYYY-MM-DD")
            event.widget["foreground"] = "grey"

    #Updating the selected plan's details based on user input
    def change_plan(self):
        # get the input
        plan_name = self.plan_name.getText()
        plan_amount = self.plan_amount.getText()
        plan_start_date = self.plan_start_date.getText()
        plan_end_date = self.plan_end_date.getText()

        # check if the input is valid
        if plan_name == "" or plan_amount == "" or plan_start_date == "" or plan_end_date == "":
            messagebox.showinfo("Change Plan", "Please fill in all the blanks!")
            return
        # check if the date is valid
        date_format = "%Y-%m-%d"
        try:
            dt.strptime( plan_start_date, date_format )
            dt.strptime( plan_end_date, date_format )
        except ValueError:
            messagebox.showinfo("Change Plan", "Please enter date in the format YYYY-MM-DD!")
            return
        if plan_start_date > plan_end_date:
            messagebox.showinfo("Change Plan", "Start date should be earlier than end date!")
            return
        if float(plan_amount) < 0:
            messagebox.showinfo("Change Plan", "Amount should be positive!")
            return
        
        # get the selected plan
        selected_plan_index = self.listbox.curselection()
        if len(selected_plan_index) == 0:
            messagebox.showinfo("Change Plan", "Please select a plan!")
            return
        selected_plan_index = selected_plan_index[0]
        selected_plan = plans[selected_plan_index]

        # change the plan
        selected_plan.name = plan_name
        selected_plan.amount = plan_amount
        selected_plan.start_date = plan_start_date
        selected_plan.end_date = plan_end_date

        # clear the input
        self.plan_name.setText("Enter your plan name")
        self.plan_amount.setText("Enter the plan budget amount")
        self.plan_start_date.setText("YYYY-MM-DD")
        self.plan_end_date.setText("YYYY-MM-DD")
        messagebox.showinfo("Change Plan", "Change Plan Successfully!")

    def cancel_change_plan(self):
        self.plan_name.setText("Enter your plan name")
        self.plan_amount.setText("Enter the plan budget amount")
        self.plan_start_date.setText("YYYY-MM-DD")
        self.plan_end_date.setText("YYYY-MM-DD")
        messagebox.showinfo("Change Plan", "Cancel Change Plan Successfully!")
    
    def finish_change_plan(self):
        self.grid_forget()
        
class Spend(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image_spend = PhotoImage(file="image/spend_back.png")
        background_label = Label(self, image=self.background_image_spend)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0

        # add TextBox in certer of the screen
        self.addLabel(text="New Spending", row=0, column=10, font=("Arial", 30), background = "#FFF2CC" ).place(x=350, y=10)
        
        # add Plans drop down list
        self.addLabel(text="Plans", row=0, column=10, font=("Arial", 15), background = "#FFF2CC" ).place(x=100, y=100)
        self.addLabel(text="Select a Plan \nto enter spending", row=0, column=10, font=("Arial", 12), background = "#FFF2CC", foreground = "gray").place(x=100, y=120)
        self.listbox = tk.Listbox(self, width=50, height=5, selectmode=tk.SINGLE)
        self.listbox.place(x=300, y=100)
        # insert plans into the listbox
        for i in range(len(plans)):
            plan = plans[i]
            self.listbox.insert(i, plan.get_name())
            
        # add labels and textboxs
        self.addLabel(text="Spending Name", row=0, column=10, font=("Arial", 15), background = "#FFF2CC" ).place(x=100, y=200)
        self.spending_name = self.addTextField(text="", row=0, column=10, width=40)
        self.spending_name.place(x=300, y=200)
        self.spending_name.setText("Enter the spending details")
        self.spending_name.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="Spending Amount", row=0, column=10, font=("Arial", 15), background = "#FFF2CC" ).place(x=100, y=250)
        self.spending_amount = self.addTextField(text="", row=0, column=10, width=40)
        self.spending_amount.place(x=300, y=250)
        self.spending_amount.setText("Enter the spending amount")
        self.spending_amount.bind("<FocusIn>", self.on_entry_click)
        
        self.addLabel(text="Spending Date", row=0, column=10, font=("Arial", 15), background = "#FFF2CC" ).place(x=100, y=300)
        self.spending_date = self.addTextField(text="", row=0, column=10, width=40)
        self.spending_date.place(x=300, y=300)
        self.spending_date.setText("YYYY-MM-DD")
        self.spending_date.bind("<FocusIn>", self.on_entry_click)
        
        self.spending_name.bind("<FocusOut>", self.on_focusout)
        self.spending_amount.bind("<FocusOut>", self.on_focusout)
        self.spending_date.bind("<FocusOut>", self.on_focusout)
    
     
        # add Buttons
        self.addButton(text="Save\nSpend", row=0, column=10, height=3, width= 5, command=self.spend).place(x=550, y=350)
        self.addButton(text="Cancel", row=0, column=10, height=3, width= 5, command=self.cancel_spend).place(x=550, y=430)
        
        # add finish button
        self.addButton(text="Back \nto Main", row=0, column=0, height=3, width=5, command=self.finish_spend).place(x=30, y=0)
      
    def on_entry_click(self, event):
        #Event handler: executed when the user clicks on a text field.
        default_taxt= {
            self.spending_name : "Enter your plan name",
            self.spending_amount: "Enter the spending amount",
            self.spending_date: "YYYY-MM-DD",
        }
        current_text = event.widget.getText()
        if current_text == "YYYY-MM-DD" or current_text == "Enter the spending details" or current_text == "Enter the spending amount":
            event.widget.setText("")
            event.widget["foreground"] = "gray"


    def on_focusout(self, event):
        #Event handler: executed when a text field loses focus.
        if event.widget == self.spending_name and event.widget.getText() == "":
            event.widget.setText("Enter the spending details")
            event.widget["foreground"] = "grey"
        elif event.widget == self.spending_amount and event.widget.getText() == "":
            event.widget.setText("Enter the spending amount")
            event.widget["foreground"] = "grey"
        elif event.widget == self.spending_date and event.widget.getText() == "":
            event.widget.setText("YYYY-MM-DD")
            event.widget["foreground"] = "grey"
    
    def spend(self):
        # get the input
        spending_name = self.spending_name.getText()
        spending_amount = self.spending_amount.getText()
        spending_date = self.spending_date.getText()

        # check if the input is valid
        if spending_name == "" or spending_amount == "" or spending_date == "":
            messagebox.showinfo("Spend", "Please fill in all the blanks!")
            return
        
        # check if the spending amount is a valid float
        try:
            spending_amount_float = float(spending_amount)
        except ValueError:
            messagebox.showinfo("Spend", "Please enter a valid number for the spending amount!")
            return
        
        # check if the date is valid
        date_format = "%Y-%m-%d"
        try:
            spending_date_check = dt.strptime( spending_date, date_format )
        except ValueError:
            messagebox.showinfo("Spend", "Please enter date in the format YYYY-MM-DD!")
            return
        if float(spending_amount) < 0:
            messagebox.showinfo("Spend", "Amount should be positive!")
            return
        
        # get the selected plan
        selected_plan_index = self.listbox.curselection()
        if len(selected_plan_index) == 0:
            messagebox.showinfo("Spend", "Please select a plan!")
            return
        selected_plan_index = selected_plan_index[0]
        selected_plan = plans[selected_plan_index]
        
        # get the selected plan
        selected_plan_index = self.listbox.curselection()
        if len(selected_plan_index) == 0:
            messagebox.showinfo("Spend", "Please select a plan!")
            return
        selected_plan_index = selected_plan_index[0]
        selected_plan = plans[selected_plan_index]

        # check if the spending date is in the plan
        if not selected_plan.get_start_date() <= spending_date_check <= selected_plan.get_end_date():
            messagebox.showinfo("Spend", "Spending date should be in the plan!")
            return
                
        # create new spending
        new_spending = Spending(spending_name, spending_amount, spending_date)
        selected_plan.add_spendings(new_spending)
        
        # clear the input
        self.spending_name.setText("Enter the spending details")
        self.spending_amount.setText("Enter the spending amount")
        self.spending_date.setText("YYYY-MM-DD")
        messagebox.showinfo("Spend", "Spend Successfully!")


    def cancel_spend(self):
        self.spending_name.setText("Enter the spending details")
        self.spending_amount.setText("Enter the spending amount")
        self.spending_date.setText("YYYY-MM-DD")
        messagebox.showinfo("Spend", "Cancel Successfully!")

    def finish_spend(self):
        self.grid_forget()    

# Constructor for the Spending class        
class Spending():
    def __init__(self, name, amount, date):
        self.name = str(name)
        self.amount = float(amount)
        self.date = date
        
    # Getters for spending attributes    
    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_date(self):
        return self.date

    def __str__(self):
        # return "Spending: {}, Amount: {}, Date: {}".format(self.name, self.amount, self.date) as YYYY-MM-DD 
        return "Spending: {}, Amount: {}, Date: {}".format(self.name, self.amount, self.date.strftime("%Y-%m-%d"))
    
    # Setter with validation for attributes
    def __setattr__(self, __name, __value):
        date_format = "%Y-%m-%d"

        if __name == "amount":
            __value = float(__value)
        elif __name == "date" and type(__value) == str :
            __value = dt.strptime(__value, date_format)
        super().__setattr__(__name, __value) 

# Global function to initiate the Spend frame
def start_spend():
    global spend_window
    spend_window = Spend()
    spend_window.grid(row=0, column=0, sticky ="NSEW")
    
    
# Class definition for the 'Budget Status' window in the application
class CheckStatus(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Money Clip", height=800, width=880)
        self.background_image = PhotoImage(file="image/report_back.png")
        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.round_w = 0
        self.round_1 = 0
        
        self.addLabel(text="Report", row=0, column=10, font=("Arial", 30), background= "#FBE5D6" ).place(x=350, y=10)

        # add Plans drop down list
        self.addLabel(text="Select Plan", row=3, column=10, font=("Arial", 20) , background="#FBE5D6" ).place(x=150, y=100)
        self.listbox = tk.Listbox(self, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.place(x=300, y=100)
        # insert plans into the listbox
        for i in range(len(plans)):
            plan = plans[i]
            self.listbox.insert(i, plan.get_name())

        # add Summary report button
        self.addButton(text="Summary Report", row=0, column=10, height=3, width= 10,command=self.summary_report).place(x=300, y=300)
        # add Spending report button
        self.addButton(text="Spending Report", row=0, column=10, height=3, width= 10, command=self.spending_report).place(x=600, y=300)

        # add finish button
        finish_btn = tk.Button(self, text="Back \nto Main", height=3, width=5, command=self.finish_check_status).place(x=30, y=0)


    def summary_report(self):
        # get the selected plan
        selected_plan_index = self.listbox.curselection()
        if len(selected_plan_index) == 0:
            messagebox.showinfo("Summary Report", "Please select a plan!")
            return
        selected_plan_index = selected_plan_index[0]
        selected_plan = plans[selected_plan_index]

        # get the budget amount
        budget_amount = selected_plan.get_amount()

        # get the total amount of spending
        total_spending = 0
        for spending in selected_plan.get_spendings():
            total_spending += spending.get_amount()

        # get the remaining amount
        remaining_amount = selected_plan.get_amount() - total_spending

        # show the summary report
        messagebox.showinfo("Summary Report", "Budget Amount: {}\nTotal Spending: {}\nRemaining Amount: {}".format(budget_amount, total_spending, remaining_amount))

    def spending_report(self):
        # get the selected plan
        selected_plan_index = self.listbox.curselection()
        if len(selected_plan_index) == 0:
            messagebox.showinfo("Spending Report", "Please select a plan!")
            return
        selected_plan_index = selected_plan_index[0]
        selected_plan = plans[selected_plan_index]
        
        # get the total amount of spending
        total_spending = 0
        for spending in selected_plan.get_spendings():
            total_spending += spending.get_amount()

        # show the spending details
        spending_details = ""
        for spending in selected_plan.get_spendings():
            spending_details += "{}: {}\n".format(spending.get_name(), spending.get_amount())
        spending_details += "Total Spending: {}".format(total_spending)
        messagebox.showinfo("Spending Report", spending_details)

    def finish_check_status(self):
        self.grid_forget()

def start_check_status():
    global check_status_window
    check_status_window = CheckStatus()
    check_status_window.grid(row=0, column=0, sticky ="NSEW")

 # Function to finish and exit the main window
def finish_main_window():
    # Save data and close the application
    save_to_file()
    root.destroy()

def save_to_file():
    with open(save_file_name, "w") as f:
        for plan in plans:
            f.write(str(plan) + "\n")
            for spending in plan.get_spendings():
                f.write(str(spending) + "\n")
            f.write("\n")

def load_from_file():
    with open(save_file_name, "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("Plan"):
                plan_name = line.split(",")[0].split(":")[1].strip()
                plan_amount = line.split(",")[1].split(":")[1].strip()
                plan_start_date = line.split(",")[2].split(":")[1].strip()
                plan_end_date = line.split(",")[3].split(":")[1].strip()
                print( f"plan_name: {plan_name}, plan_amount: {plan_amount}, plan_start_date: {plan_start_date}, plan_end_date: {plan_end_date}")
                new_plan = Plan(plan_name, plan_amount, plan_start_date, plan_end_date)
                plans.append(new_plan)
                i += 1
                line = lines[i]
                while line.startswith("Spending"):
                    spending_name = line.split(",")[0].split(":")[1].strip()
                    spending_amount = line.split(",")[1].split(":")[1].strip()
                    spending_date = line.split(",")[2].split(":")[1].strip()
                    new_spending = Spending(spending_name, spending_amount, spending_date)
                    new_plan.add_spendings(new_spending)
                    i += 1
                    line = lines[i]
                i -= 1
            i += 1

# test data
def add_test_data():
    plan1 = Plan("plan1", 100, "2023-01-01", "2023-01-31")

    # add test data
    spending1 = Spending("spending1", 10, "2023-01-01")
    spending2 = Spending("spending2", 20, "2023-01-02")
    spending3 = Spending("spending3", 30, "2023-01-03")
    plan1.add_spendings(spending1)
    plan1.add_spendings(spending2)
    plan1.add_spendings(spending3)

    plan2 = Plan("plan2", 200, "2023-02-01", "2023-02-28")

    # add test data
    spending4 = Spending("spending4", 40, "2023-02-01")
    spending5 = Spending("spending5", 50, "2023-02-02")
    spending6 = Spending("spending6", 60, "2023-02-03")
    plan2.add_spendings(spending4)
    plan2.add_spendings(spending5)
    plan2.add_spendings(spending6)

    plan3 = Plan("plan3", 300, "2023-03-01", "2023-03-31")

    # add test data
    spending7 = Spending("spending7", 70, "2023-03-01")
    spending8 = Spending("spending8", 80, "2023-03-02")
    spending9 = Spending("spending9", 90, "2023-03-03")
    plan3.add_spendings(spending7)
    plan3.add_spendings(spending8)
    plan3.add_spendings(spending9)

    plans.append(plan1)
    plans.append(plan2)
    plans.append(plan3)

if __name__ == "__main__":
    main()