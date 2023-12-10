"""
Budget Management Program

This is a simple project designed to help you manage budgets, expenses, and balances for various purposes such as travel, daily life, or specific funds. 
The program allows you to manage budgets by subcategories.

It can be used for basic financial planning among family members, monthly budget tracking, 
or even for managing savings goals by keeping track of your progress towards a specific savings target.

"""

import tkinter as tk
from tkinter import PhotoImage
from breezypythongui import EasyFrame



class MoneyClipApp():
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
        pass

    def save_plan(self):
        pass
        
    def delete_plan(self):
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
    

    
def main():
    app = MoneyClipApp()
    app.mainpage()

if __name__ == "__main__":
    main()
