"""
Budget Management Program

This is a simple project designed to help you manage budgets, expenses, and balances for various purposes such as travel, daily life, or specific funds. 
The program allows you to manage budgets by subcategories.

It can be used for basic financial planning among family members, monthly budget tracking, 
or even for managing savings goals by keeping track of your progress towards a specific savings target.

"""

import tkinter as tk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Label, Button, StringVar, DoubleVar, messagebox


class MoneyClipApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Money Clip")
        self.geometry("800x880")
        self.project = []
        self.mainpage()

    def mainpage(self):
        self.background_image = PhotoImage(file='image/main_background_re.png')
        background_label = Label(self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window

        money_clip_label = Label(self, text="Money Clip", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        money_clip_label.place(x=350, y=10)
        

        # Setting the position of buttons on the screen
        plan_button_img = PhotoImage(file='image/Botton1.png')
        spend_button_img = PhotoImage(file='image/Botton2.png')
        status_button_img = PhotoImage(file='image/Botton3.png')
        self.plan_button_img = plan_button_img  # Keep a reference

        plan_button = Button(self, image=plan_button_img, borderwidth=0, highlightthickness=0, command=self.create_plan)
        spend_button = Button(self, image=spend_button_img, borderwidth=0, highlightthickness=0, command=self.input_spending)
        status_button = Button(self, image=status_button_img, borderwidth=0, highlightthickness=0, command=self.check_status)


        plan_button.place(x=47, y=56)
        spend_button.place(x=456, y=266)
        status_button.place(x=16, y=455)

    def create_plan(self):
        create_plan_window = Create_plan()
        create_plan_window.mainloop()
        
    
class Create_plan(EasyFrame):
          
    def __init__(self):
        super().__init__(title="Money Clip", width=800, height=880)
        background_image = PhotoImage(file='image/budget_back.jpg')
        background_label = Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window
        self.background_image = background_image  # Keep a reference

        create_plan_label = Label(self, text="Make Your Plan", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        create_plan_label.place(x=350, y=10)
        
        new_plan_button = self.addButton(text="Create New Plan", row=1, column=0, command=self.new_plan)
        change_plan_button = self.addButton(text="Change Plan", row=1, column=1, command=self.change_plan)
        
    def new_plan(self):
        # Implementation for creating a new plan
        pass
    
    def change_plan(self):
        # Implementation for changing an existing plan
        pass
        
class input_spending():        
    def input_spending_show(self):
        pass
    # Spending Input (refund can also be entered)
    # Project Name (rolldown - selection only)
    # Automatically import project subcategories
    # Spending date (select from calendar or enter only in mm/dd/YY format)
    # Input person (name input_text)
    # spending amount
    # description (text box can accommodate about 2~3 sentences)
    # After entering, the total budget, amount spent, and remaining amount % will appear in a pop-up window.

class check_status():        
    def check_status_show(self):
        pass
    #Report printing
    # Project name, total budget, amount spent so far, by subcategory (total line appears at the top), remaining amount and % expression
    # Three buttons for simple report, sub-stage, and save as file
    # Output data to file (csv file)

        
        
        
        
        
        
        
        
        
        
        
        
                
"""   
# Setting the background for the main page
    def mainpage(self):
        root = tk.Tk()
        root.title("Money Clip")
        root.geometry("800x880") 

        # Configuring menu buttons and setting their background
        background_image = PhotoImage(file='image/main_background_re.png')
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window

        money_clip_label = tk.Label(root, text="Money Clip", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        money_clip_label.place(x= 350, y=10)  

        # Setting the position of buttons on the screen
        plan_button_img = tk.PhotoImage(file='image/Botton1.png')
        spend_button_img = tk.PhotoImage(file='image/Botton2.png')
        status_button_img = tk.PhotoImage(file='image/Botton3.png')

        plan_button = tk.Button(root, image=plan_button_img, borderwidth=0,highlightthickness=0)
        spend_button = tk.Button(root, image=spend_button_img, borderwidth=0,highlightthickness=0)
        status_button = tk.Button(root, image=status_button_img, borderwidth=0,highlightthickness=0)

        plan_button.place(x=47, y=56)
        spend_button.place(x=456, y=266)
        status_button.place(x=16, y=455)
        
        # Linking each button to its respective function/module
        plan_button.config(command=self.create_plan)
        spend_button.config(command=self.input_spending)
        status_button.config(command=self.check_status)
        
        root.mainloop()      
        
    def create_plan(self):
        # Make your plan: Project & Budget creating
        # Budget amount, dates, and subcategories can be modified midway. 
        # However, subcategories can only be added (subcategories that already have spanning cannot be deleted).
        
        # Project Name
            # If the name is the same as an existing project, a warning message notifying that the same name exists is displayed in red on the bottom line and requires re-entry.
            # When re-entering, the previously entered information remains in the input window, making it easy to edit
     
        # Sub Budget Category
            # Category selection possible with scroll bar
            # Monthly living expenses, travel budget, saving money, etc.
        
        #BudgetAmount
            # There may be no subcategories. (yes, no button.)
            # When you press the yes button, a window is created where you can enter up to 5 subcategories.
            # If the amount of the subcategory is different from the total budget, a warning message is displayed in the bottom line.
        
        # Project starting date & Ending date
            # So that you can input it in MM/DD/YY format. If the format is incorrect, a warning message is displayed in red at the bottom line and you can re-enter it.
    
        #Creatingbutton
       pass
        
    
    def return_to_main(self):
        pass

    def input_spending(self):
        # Spending Input (refund can also be entered)
        # Project Name (rolldown - selection only)
        # Automatically import project subcategories
        # Spending date (select from calendar or enter only in mm/dd/YY format)
        # Input person (name input_text)
        # spending amount
        # description (text box can accommodate about 2~3 sentences)
        # After entering, the total budget, amount spent, and remaining amount % will appear in a pop-up window.
        pass

    def check_status(self):
        #Report printing
        # Project name, total budget, amount spent so far, by subcategory (total line appears at the top), remaining amount and % expression
        # Three buttons for simple report, sub-stage, and save as file
        # Output data to file (csv file)
        pass
        
        """
        
        
# Main function to start the application
def main():
    app = MoneyClipApp()
    app.mainpage()

if __name__ == "__main__":
    main()

