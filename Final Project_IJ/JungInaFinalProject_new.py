import tkinter as tk
from breezypythongui import EasyFrame
from tkinter import PhotoImage, Label, Button

# Create_plan 윈도우를 정의하는 클래스
class Create_plan(EasyFrame):
    def __init__(self):
        super().__init__(title="Create Plan", width=800, height=880)
        # Background 설정
        background_image = PhotoImage(file='image/budget_back.png')
        background_label = Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        self.background_image = background_image  # 이미지 참조 유지

        # Label과 Button 추가
        create_plan_label = Label(self, text="Make Your Plan", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        create_plan_label.place(x=350, y=10)

        # New Plan Button
        new_plan_button = self.addButton(text="Create New Plan", row=1, column=0, command=self.new_plan)
        # Change Plan Button
        change_plan_button = self.addButton(text="Change Plan", row=1, column=1, command=self.change_plan)

    def new_plan(self):
        # 새 계획을 생성하는 로직
        pass
    
    def change_plan(self):
        # 계획을 변경하는 로직
        pass

# Input Spending 윈도우를 정의하는 클래스
class InputSpendingWindow(EasyFrame):
    def __init__(self, master):
        super().__init__(master, title="Input Spending", width=800, height=880)
        # 여기에 Input Spending 관련 요소 추가
        pass

# Check Status 윈도우를 정의하는 클래스
class CheckStatusWindow(EasyFrame):
    def __init__(self, master):
        super().__init__(master, title="Check Status", width=800, height=880)
        # 여기에 Check Status 관련 요소 추가
        pass

# 메인 애플리케이션 클래스
class MoneyClipApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Money Clip")
        self.geometry("800x880")
        self.project = []
        self.mainpage()

    def mainpage(self):
        # Background 이미지 설정
        self.background_image = PhotoImage(file='image/main_background_re.png')
        background_label = Label(self, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        # 메인 레이블
        money_clip_label = Label(self, text="Money Clip", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        money_clip_label.place(x=350, y=10)
        
        # 버튼 이미지 로딩
        plan_button_img = PhotoImage(file='image/Button1.png')
        spend_button_img = PhotoImage(file='image/Button2.png')
        status_button_img = PhotoImage(file='image/Button3.png')
        self.plan_button_img = plan_button_img  # Keep a reference

        # 버튼 설정 및 위치 지정
        plan_button = Button(self, image=plan_button_img, borderwidth=0, highlightthickness=0, command=self.create_plan)
        spend_button = Button(self, image=spend_button_img, borderwidth=0, highlightthickness=0, command=self.create_input_spending_window)
        status_button = Button(self, image=status_button_img, borderwidth=0, highlightthickness=0, command=self.create_check_status_window)

        # 버튼 배치
        plan_button.place(x=47, y=56)
        spend_button.place(x=456, y=266)
        status_button.place(x=16, y=455)

    # Create Plan 윈도우를 여는 메소드
    def create_plan(self):
        create_plan_window = Create_plan()
        create_plan_window.mainloop()

    # Input Spending 윈도우를 여는 메소드
    def create_input_spending_window(self):
        input_spending_window = InputSpendingWindow(self)
        input_spending_window.grab_set()  # 다른 윈도우로의 입력을 막음

    # Check Status 윈도우를 여는 메소드
    def create_check_status_window(self):
        check_status_window = CheckStatusWindow(self)
        check_status_window.grab_set()  # 다른 윈도우로의 입력을 막음

# 애플리케이션을 시작하는 메인 함수
def main():
    app = MoneyClipApp()
    app.mainloop()

if __name__ == "__main__":
    main()
